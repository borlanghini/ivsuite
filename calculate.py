import numpy as np
from scipy import interpolate,  stats


def findscparam(ivdata, irrad, area):
	if ivdata[:, 0][0]>ivdata[:, 0][1]:
		volt = np.flipud(ivdata[:, 0])
		curr = np.flipud(ivdata[:, 1])
	else:
		volt = ivdata[:, 0]
		curr = ivdata[:, 1]
	
	#        finding last data position before zero crossing
	zero_crossing=np.where(np.diff(np.sign(curr)))[0][0]
	
	#        creating function for data interpolation
	data_interpld = interpolate.interp1d(volt, curr,  kind='cubic')
	
	#        approximate Voc value by linear interpolation
	slope = (curr[zero_crossing +1] - curr[zero_crossing])/(volt[zero_crossing + 1]-volt[zero_crossing])
	intercept = curr[zero_crossing] - slope*volt[zero_crossing]
	
	#        slope,  intercept,  r_value,  p_value,  std_err = stats.linregress(volt[zero_crossing:zero_crossing+1],  curr[zero_crossing:zero_crossing+1])
	voc = - intercept/slope
	isc = data_interpld(0)
	
	#        finding max power point
	voltnew = np.arange(0, volt[zero_crossing+1],  0.001)
	maxscpower = max(np.abs(np.multiply(voltnew,  data_interpld(voltnew))))
	print('Pmax = ', maxscpower)
	maxscpower_voltposition = np.argmax(np.abs(np.multiply(voltnew, data_interpld(voltnew))))
	print('Vmp = ',voltnew[maxscpower_voltposition])
	print('Imp = ',data_interpld(voltnew[maxscpower_voltposition]))
	pmax = np.abs(voltnew[maxscpower_voltposition]*data_interpld(voltnew[maxscpower_voltposition]))
	print('Pmax = ', pmax)
	fillfactor = np.abs(pmax/(voc*isc))
	print('FF = ', fillfactor)
	effic = np.abs(pmax*1000/(irrad*area))
	print('Efficiency = ', effic)
	
	#        finding r_s and r_shunt graphically --- approximate method
	rsh_slope,  intercept,  r_value,  p_value,  std_err = stats.linregress(voltnew[0:int(maxscpower_voltposition*0.8)], data_interpld(voltnew[0:int(maxscpower_voltposition*0.8)]))
	rshunt = np.abs(1/rsh_slope)
	rs_slope,  intercept,  r_value,  p_value,  std_err = stats.linregress(voltnew[-50:-1], data_interpld(voltnew[-50:-1]))
	rseries = np.abs(1/rs_slope)
	
	return [isc,  voc,  fillfactor,  pmax,  effic, rshunt,  rseries]
