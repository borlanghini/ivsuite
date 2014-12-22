#!/usr/bin/env python3
# Copyright (c) 2014 Julio C. Rimada. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for scientific purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.


import os
import platform
import sys
import codecs
from datetime import datetime
import time
   
import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import pyqtgraph as pg

import Keithley
import ui_acquiredlg3 
from ui_gpibconfig import Ui_GpibConfigDialog
import calculate 
import qrc_resources3


class IVMeas(QMainWindow, ui_acquiredlg3.Ui_IVMainWindow):

	def __init__(self, parent=None):
		super(IVMeas, self).__init__(parent)
		self.setWindowTitle("IV-Suite")
		self.setWindowIcon(QIcon('sun256.png'))
		
		settings = QSettings()
		self.recentDirs = settings.value("RecentDirectories") or []
		self.setupUi(self)
		
		self.directoriescomboBox.clear()
		self.directoriescomboBox.addItems(self.recentDirs)
		self.IVtabWidget.setCurrentIndex(0)
		
		## Window to change the gpib address of the Keithley 2400
		self.configgpib = Ui_GpibConfigDialog

		
		## Switch to using white background and black foreground in the plot window
		## maybe could include in a preferences window to be selected by user
		
		#~ pg.setConfigOption('background', 'w')
		#~ pg.setConfigOption('foreground', 'k')
		
		self.plot = pg.PlotWidget(title="Solar Cell Characterization")
		self.p1 = self.plot.plotItem
		self.p1.setLabels(left='Current (A)', bottom='Voltage (V)')
		self.p1.viewRect()
		self.ivplot.addWidget(self.plot)
		
		
		self.calcparameters = [0, 0,  0,  0, 0, 0,  0] # [isc,  voc,  fillfactor,  maxscpower,  effic, rshunt,  rseries]
		self.meastype = 0 # 0 -> dark i-v, 1 -> illuminated i-v
		self.sweeptype=0  # 0 -> standard simple sweep, 1 -> i-v hysteresis sweep
		self.datalist =[] # measured data initialized to zero
		
		self.updateUi()

	@pyqtSignature("QString")
	def on_nameLineEdit_textEdited(self, text):
		self.__index = 0
		self.updateUi()

	@pyqtSignature("")
	def on_browseButton_clicked(self):
		currentdir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		self.directoriescomboBox.addItem(currentdir)
		self.addRecentDir(currentdir)
	
	@pyqtSignature("")
	def on_measureButton_clicked(self):

		class SavingDirError(Exception): pass

		try:
			if self.directoriescomboBox.currentIndex() ==-1:
				raise SavingDirError("you haven't selected any saving directory")
		
			self.measure()
			basename = self.samplename()
			self.saveresults(basename)
			self.plotresults(basename)
        
		except SavingDirError as e:
			QMessageBox.warning(self, "Saving Directory Error", str(e))
		except (IOError, OSError) as e:
			error = "Failed to save: {0}".format(e)


	def updateUi(self):
		if self.nameLineEdit.text() =="":
			enable = False
		else:
			enable = True
		self.measureButton.setEnabled(enable)
        
	def meastypeControl(self):
		self.meastype = self.MeasTypelistWidget.currentRow()
		if self.meastype == 0:
			print("measurement type = Dark I-V")
		elif self.meastype == 1:
			print("measurement type = Illuminated I-V")
		elif self.meastype == 2:
			print("measurement type = Voc photodecay")
		elif self.meastype == 3:
			print("measurement type = Jsc stability")
                
	def sweeptypeControl(self):
		self.sweeptype = self.SweepTypelistWidget.currentRow()
		if self.sweeptype == 0:
			print("Sweep type = Simple sweep")
		elif self.sweeptype == 1:
			print("Sweep type = Hysteresis sweep") 
            
	def measure(self):
		self.meastypeControl()
		self.sweeptypeControl()
		## Instantiate Keithley class to control instrument
		self.k2400 = Keithley.K2400Series(24)
		
		## Check type of measurement 
		
		if self.MeasTypelistWidget.currentRow() == 0:
			if self.SweepTypelistWidget.currentRow() == 0:
				sleepingtime = self.k2400SimpleSweep()
			elif self.SweepTypelistWidget.currentRow() == 1:
				sleepingtime = self.k2400HysteresisSweep()
		elif self.MeasTypelistWidget.currentRow() == 1:
			sleepingtime = self.k2400SimpleSweep()
		elif self.MeasTypelistWidget.currentRow() == 2:
			sleepingtime = self.k2400VocDecay()
		elif self.MeasTypelistWidget.currentRow() == 3:
			sleepingtime = self.Iscstability()
		
		self.k2400.outputon()   #Turn on instrument output
		
		self.k2400.write(":INIT; *OPC")     #Intialize and begin measurement
		print("Measuring...waiting for results in about {0:d} seconds".format(sleepingtime))
		time.sleep(sleepingtime)
		print("...Done!!!")
		datalist=self.k2400WaitRead()  # getting measurement results
		
		self.k2400.outputoff()   #Turn OFF instrument output
		
		# converting the 1D datalist into a 2 columns numpy array
		k2400datalist = np.array([datalist[i:i+2] for i in range(0, len(datalist),2)])
		if self.MeasTypelistWidget.currentRow() == 2:
			self.datalist = np.fliplr(k2400datalist)
		elif self.MeasTypelistWidget.currentRow() == 3:
			self.datalist = np.fliplr(k2400datalist)
			self.datalist[:,1]*=-1
		else:
			self.datalist = k2400datalist
		print("Printing data measured")
		print(self.datalist)

 
	def k2400SimpleSweep(self):
		self.k2400.write(":syst:pres; *RST; *CLS") # reset equipment
		self.k2400.write(":sens:func:conc off")  # Turn off concurrent functions
		self.k2400.write(":trace:feed:cont never")
		self.k2400.write("*ESE 1; *SRE 32")
		self.k2400.write(":source:func volt")
		self.k2400.write(":source:sweep:spacing lin")
		
		self.k2400.write(":source:sweep:direction down")
		self.k2400.write(":source:voltage:protection default")
		self.k2400.write(":source:voltage:start %.2f" %  self.VminSpinBox.value())
		self.k2400.write(":source:voltage:stop %.2f" % self.VmaxSpinBox.value())
		self.k2400.write(":source:voltage:step %.2f" %  self.sweepStepSpinBox.value())
		self.k2400.write(":source:volt:mode swe")
		self.k2400.write(":source:del %.4f" % self.sweepDelSpinBox.value())
		self.k2400.write(":source:sweep:poin?")
		number_of_points= self.k2400.read()
		
		compliance_list=["1.05e-6",  "1.05e-5",  "1.05e-4",  "1.05e-3",  "2.1e-2",  "1.05e-1",  "1.05"]
		self.k2400.write(":current:protection %s" % compliance_list[self.currentLimitcomboBox.currentIndex()])
		print("Compliance current = "+ compliance_list[self.currentLimitcomboBox.currentIndex()])
		self.k2400.write(":current:nplc 0.01")
		self.k2400.write(":current:range 0.01")
		self.k2400.write(":func 'curr:dc'")
		self.k2400.write(":abort")
		self.k2400.write(":arm:source imm")
		self.k2400.write(":arm:coun 1")
		self.k2400.write(":trigger:source imm")
		self.k2400.write(":trigger:del 0")
		self.k2400.write(":trigger:coun %s" % number_of_points)
		#buffer
		self.k2400.write(":form ascii")
		self.k2400.write(":form:elem volt,curr")
		self.k2400.write(":trace:poin %s" % number_of_points)
		self.k2400.write(":trace:clear")
		self.k2400.write(":trace:feed sense")    #Store readings in buffer
		self.k2400.write(":trace:feed:cont next")   #Enable buffer storage
		return 0

	def k2400HysteresisSweep(self):
		vstart = self.VminSpinBox.value()   # Initial value
		vstop = self.VmaxSpinBox.value()    # Final value
		vstep = self.sweepStepSpinBox.value()   # voltage increment
		pasosforward = (vstart-vstop)/vstep + 1     # number of steps in the forward direction
		volt_array = np.arange(vstart, vstop+vstep, vstep)   # array of voltages to apply in the forward direction
		
		if self.ZerocheckBox.isChecked():
			volt_array_from_zero = np.arange(0, vstart+vstep, vstep)   #  array of voltages from zero to start value 
			volt_array_tot = np.concatenate((volt_array_from_zero, volt_array, np.delete(volt_array[::-1],0)))   # array of voltages to apply starting from zero
		else:
			volt_array_tot = np.concatenate((volt_array, np.delete(volt_array[::-1],0)))     # array of voltages to apply not starting from zero
			
		self.number_of_points = len(volt_array_tot)    # length of voltages array
        
        # programming the Keithley 2400 for a memory sweep
		self.k2400.write("*RST")   #Reset instrument
		self.k2400.write("*CLS")     #Clear instrument status
		self.k2400.write(":OUTP:SMODE HIMP") #Use high impedance output off-state (IMPORTANT! refer to page 3-20 in 2400 Series User's Manual)
		self.k2400.write("*SRE 1")   #Enable service request generation
		self.k2400.write(":STAT:MEAS:ENAB 512")  #SRQ on buffer full
		self.k2400.write(":FORM:ELEM VOLT,CURR") #Format return data string as a list of voltage, current    

		count = 0
        # Begin configuration on each memory location
		for x in volt_array_tot:
			self.k2400.write(":SOUR:FUNC VOLT")  #Configure instrument to source voltages
			self.k2400.write(":SENS:FUNC 'CURR:DC'") # Configure instrument to measure DC current
			self.k2400.write(":SOUR:VOLT %f" %x)     # set source to corresponding voltage in the array of voltages 
			self.k2400.write(":SENS:CURR:NPLC 0.01")     #Set integration rate on current measurement = 0.01 PLC
			
			if count > 0:       # if not the first voltage on list 
				if cmp(volt_array_tot[count], volt_array_tot[count-1]>0):
					self.k2400.write(":SOUR:DEL %f" %self.ForwardsweepDelSpinBox.value())    #Set source delay in the forward direction of the sweep to the value defined by user 
				else:
					self.k2400.write(":SOUR:DEL %f" %self.BackwardsweepDelSpinBox.value())        #Set source delay in the backward direction of the sweep to the value defined by user 
			else:
				self.k2400.write(":SOUR:DEL %f" %self.ForwardsweepDelSpinBox.value())     #Set source delay for the first point to the value defined by user 

			self.k2400.write(":SOUR:MEM:SAVE %d"% (count+1))    #Save present SourceMeter configuration in source memory location n 
			count +=1

		self.k2400.write(":ARM:SOUR IMM")   #Set arm source = immediate (default)
		self.k2400.write(":ARM:COUN 1")   #Set arm count = 5 (This is the number of times you would like to make complete sweep cycles)
		self.k2400.write(":TRIG:SOUR IMM")   #Set trigger layer source = immediate (default)
		self.k2400.write(":TRIG:COUN %d" %self.number_of_points)    #Set trigger count = MUST equal number of points in source memory sweep
		self.k2400.write(":TRAC:POIN %d" %self.number_of_points)   #Configure buffer size = trigger count * arm count
		self.k2400.write(":TRAC:FEED SENS")   #Store readings in buffer
		self.k2400.write(":TRAC:FEED:CONT NEXT")   #Enable buffer storage
		self.k2400.write(":SOUR:FUNC MEM")    #Source function mode = source memory sweep
		self.k2400.write(":SOUR:MEM:POIN %d" %self.number_of_points)   # points in source memory sweep (MUST equal trigger count)
		self.k2400.write(":SOUR:MEM:STAR 1")    #Start at source memory location 1
		
		return 0
		
	def k2400VocDecay(self):
		#reset
		self.k2400.reset()
		#~ QMessageBox.information(self,  "Ok", "Reset")
		#set SRQ
		self.k2400.write("*ESE 1;*SRE 1")
		self.k2400.write("STAT:MEAS:ENAB 512")
		#~ QMessageBox.information(self,  "Ok", "SRQ")
		#set source
		self.k2400.write(":source:func curr")
		self.k2400.write(":source:current:mode FIX")
		self.k2400.write(":source:current default")
		self.k2400.write(":source:del 0")
		#~ QMessageBox.information(self,  "Ok", "Source")
		#sense
		compliance_list=["1.05e-6",  "1.05e-5",  "1.05e-4",  "1.05e-3",  "2.1e-2",  "1.05e-1",  "1.05"]
		self.k2400.write(":current:protection {0:s}".format(compliance_list[self.currentLimitcomboBox.currentIndex()]))
		#~ QMessageBox.information(self,  "Ok", "Current protection")
		self.k2400.write(":voltage:nplc 0.1")
		#~ QMessageBox.information(self,  "Ok", "nplc")
		self.k2400.write(":current:range:auto 1")
		#~ QMessageBox.information(self,  "Ok", "current range")
		self.k2400.write(":SENS:FUNC 'VOLT:DC'")
		#~ QMessageBox.information(self,  "Ok", "sense function volt")
		#~ QMessageBox.information(self,  "Ok", "Sense")
		#layer
		self.k2400.write(":abort")
		self.k2400.write(":arm:source imm")
		self.k2400.write(":arm:coun 1")
		self.k2400.write(":trigger:source imm")
		self.k2400.write(":trigger:del {0:.2f}".format(self.sweepDelSpinBox.value()))
		self.k2400.write(":trigger:coun {0:d}".format(self.VocNPointsspinBox.value()))
		#~ QMessageBox.information(self,  "Ok", "Layer")
		#buffer
		self.k2400.write(":form ascii")
		self.k2400.write(":form:elem volt, time")
		self.k2400.write(":trace:poin {0:d}".format(self.VocNPointsspinBox.value()))
		self.k2400.write(":trace:clear")
		self.k2400.write(":trace:feed sense")    #Store readings in buffer
		self.k2400.write(":trace:feed:cont next")  #Enable buffer storage
		#~ QMessageBox.information(self,  "Ok", "Buffer")
		meas_duration = self.sweepDelSpinBox.value()*self.VocNPointsspinBox.value()
		return int(meas_duration)
	
	def Iscstability(self):
		#number of points and delay time calculaiton
		#based on the measurement time selected by user
		meas_duration = self.minutesSpinBox.value()*60 #duration of measurement in seconds
		meas_interval = meas_duration/2500
		
		#reset
		self.k2400.reset()
		
		#set SRQ
		self.k2400.write("*ESE 1;*SRE 1")
		self.k2400.write("STAT:MEAS:ENAB 512")
		#~ QMessageBox.information(self,  "SRQ Ok", "Continue")
		#set source
		self.k2400.write(":source:func volt")
		self.k2400.write(":source:voltage:mode fixed")
		self.k2400.write(":source:voltage default")
		self.k2400.write(":source:del 0")
		#~ QMessageBox.information(self,  "Source Ok", "Continue")
		#sense
		compliance_list=["1.05e-6",  "1.05e-5",  "1.05e-4",  "1.05e-3",  "2.1e-2",  "1.05e-1",  "1.05"]
		self.k2400.write(":current:protection {0:s}".format(compliance_list[self.currentLimitcomboBox.currentIndex()]))
		self.k2400.write(":current:nplc 0.1")
		self.k2400.write(":current:range:auto on")
		self.k2400.write(":SENS:FUNC 'CURRENT'")
		#~ QMessageBox.information(self,  "Ok", "Sense")
		#layer
		self.k2400.write(":abort")
		self.k2400.write(":arm:source imm")
		self.k2400.write(":arm:coun 1")
		self.k2400.write(":trigger:source imm")
		self.k2400.write(":trigger:del {0:.3f}".format(meas_interval))
		self.k2400.write(":trigger:coun 2500")
		#~ QMessageBox.information(self,  "Ok", "layer")
		#buffer
		self.k2400.write(":form ascii")
		self.k2400.write(":form:elem current, time")
		self.k2400.write(":trace:tstamp:format abs")
		self.k2400.write(":trace:poin 2500")
		self.k2400.write(":trace:clear")
		self.k2400.write(":trace:feed sense")    #Store raw readings in buffer
		self.k2400.write(":trace:feed:cont next")   #Enable buffer storage
		#~ QMessageBox.information(self,  "Ok", "Buffer")
		return meas_duration
		
	def saveresults(self, basename):
		
		filename = self.directoriescomboBox.currentText()+'/'+basename+'.ivk'
		print("Sample filename: " + filename)
		np.savetxt(filename, self.datalist, fmt='%10.4e', delimiter='\t')
		
	def plotresults(self, basename):
		
		if self.MeasTypelistWidget.currentRow() == 0:
			if self.SweepTypelistWidget.currentRow() == 0:
				meas = "Dark I-V"
				y_axe = 'Current (A)'
				x_axe = 'Voltage (V)'
			elif self.SweepTypelistWidget.currentRow() == 1:
				meas = "Dark I-V Hysteresis"
				y_axe = 'Current (A)'
				x_axe = 'Voltage (V)'
		elif self.MeasTypelistWidget.currentRow() == 1:
			meas = "Solar Cell Illuminated I-V"
			y_axe = 'Current (A)'
			x_axe = 'Voltage (V)'
		elif self.MeasTypelistWidget.currentRow() == 2:
			meas = "Voc Photodecay curve"
			x_axe = 'Time (s)'
			y_axe = 'Voltage (V)'
		elif self.MeasTypelistWidget.currentRow() == 3:
			meas = "Jsc stability curve"
			x_axe = 'Time (s)'
			y_axe = 'Jsc (A)'
		
		self.plot.clear()
		self.p1.setLabels(left=y_axe, bottom=x_axe)
		self.p1.plot(self.datalist, symbol='o', clickable=True, width=6, name=basename)
		self.IVtabWidget.setCurrentIndex(1)
		
		if self.MeasTypelistWidget.currentRow() == 0:
			texto = 'Sample name: '+ basename
			print("Dark I-V measured, no solar cells parameters will be calculated..... for now")
		elif self.MeasTypelistWidget.currentRow() == 1:
			self.calcparameters = calculate.findscparam(self.datalist, self.IrradspinBox.value(), self.areaSpinBox.value())
			print("Iluminated I-V")
			print(self.calcparameters[3])
			isc = " %.2f " % (self.calcparameters[0]*1000)
			jsc = " %.2f " % (self.calcparameters[0]*1000/ self.areaSpinBox.value())
			voc = " %.2f " % (self.calcparameters[1]*1000)
			maxpower = " %.2f " %(self.calcparameters[3]*1000)
			fillfactor = " %.3f "%(self.calcparameters[2])
			effic = " %.2f "%(self.calcparameters[4]*100)
			rshunt = " %.2e "%(self.calcparameters[5])
			rseries = " %.2e "%(self.calcparameters[6])
			texto = 'Sample name: '+ basename+ '<br>I<sub>SC</sub> = '+ isc + ' mA <br> V<sub>OC</sub> = ' + voc + ' mV <br> P<sub>MAX</sub> = ' + maxpower +'mW <br> FF = ' + fillfactor + '<br> Efficiency = ' +effic+ ' % <br> R<sub>||</sub> = ' + rshunt + ' &#8486; <br> R<sub>series</sub> = ' + rseries + ' &#8486;'
		elif self.MeasTypelistWidget.currentRow() == 2:
			texto = texto = 'Sample name: '+ basename
			print("Voc photodecay measured")
		elif self.MeasTypelistWidget.currentRow() == 3:
			texto = texto = 'Sample name: '+ basename
			print("Voc photodecay measured")
		
		## Create text object, use HTML tags to specify color/size
		text = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF; font-size: 12pt;">Results of: <b>{0:s}</b></span><br><span style="color: #FF0; font-size: 12pt;">{1:s}</span></div>'.format(meas, texto), anchor=(-0.2,0), border='w', fill=(0, 0, 255, 100))	
		self.p1.addItem(text)
		text.setPos(self.datalist[:,0].min(), self.datalist[:,1].max())


	def k2400WaitRead(self):
		#wait until measurement is done through serial polling
		self.k2400.wait_for_srq()    
		#and read data, it will receive a long long list with all values separated by a comma            
		return self.k2400.gpib_ask()    

	def rolling(self,  a, window):
        #algorithm taken from http://stackoverflow.com/a/4924433
		shape = (a.size/2 , window)
		strides = (a.itemsize, a.itemsize)
		return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
		
	def samplename(self):
		if self.meastype == 0:
			meas_type = '-dark'
		elif self.meastype == 1:
			meas_type = '-light'
		elif self.meastype == 2:
			meas_type = '-VocDecay'
		elif self.meastype == 3:
			meas_type = '-JscStability'
		
		if self.sweeptype == 1:
			sweep_type = '-hysteresis'
		else:
			sweep_type = ''
		
		if self.addDatecheckBox.isChecked():
			now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
			return self.nameLineEdit.text() + meas_type + sweep_type +'-'+str(now)
		else:
			return self.nameLineEdit.text() + meas_type + sweep_type
			
	def addRecentDir(self, namedir):
		if namedir is None:
			return
		if namedir not in self.recentDirs:
			self.recentDirs = [namedir] + self.recentDirs[:8]
			
	def closeEvent(self, event):
		settings = QSettings()
		settings.setValue("RecentDirectories", self.recentDirs or [])

	def updateResults(self, textresults):
		#~ self.statusBar().showMessage(message, 5000)
		self.resultstextEdit.insertPlainText(textresults)
        #~ self.setWindowModified(self.dirty)
		


if __name__ == "__main__":

	app = QApplication(sys.argv)
	myapp = IVMeas()
	myapp.show()
	sys.exit(app.exec_())

