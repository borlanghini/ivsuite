ivsuite
=======

Measure I-V characteristic and more of solar cells using a Keithley 2400 series

The Keithley 2400 must be at GPIB addres 24, later I will implement the manual setting of the GPIB address of the Keithley

The solar simulator is operated manually so far, next version will include the operation of the shutter of the solar simulator from this program using Arduino UNO

This program has benn tested with python 3.2 in Windows XP and Linux and the modules needed are:
- Numpy 1.8
- PyQt4 ver. >= 4.11
- pyqtgraph (http://www.pyqtgraph.org/ )
- pyVisa 1.6

If using Linux, and using linux-gpib python binding, it should be installed pyvisa-py from https://github.com/hgrecco/pyvisa-py
More info about pyvisa-py at http://python-in-the-lab.blogspot.it/2014/10/communicating-with-instruments-using.html

Any question or suggestion email me at jcrimada@gmail.com
