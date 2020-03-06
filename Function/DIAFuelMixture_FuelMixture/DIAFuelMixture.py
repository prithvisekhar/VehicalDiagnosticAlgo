""" This function checks the ratio of air-fuel mixture and classify them as the Lean or Rich mixture.
1. When the oxygen value in the sensor is less than 0.1, it is classified as the Lean mixture.
2. When the O2 value is between 0.9 to 1.0, it is classified as the Rich mixture.
"""

import pandas as pd

def FuelMixture(O2_Volts):
	Lean = []
	Rich = []
	Nrml = []

	for i in range(0, len(O2_Volts)):
		if O2_Volts[i]== '-' :
			O2_Volts[i]= '0';
		O2_Volts[i] = float(O2_Volts[i])		
		if O2_Volts[i] >= 0.0 and O2_Volts[i] <= 0.1:
			Lean.append([O2_Volts[i], i])
		elif O2_Volts[i] >= 0.9 and O2_Volts[i] <= 1.0:
			Rich.append([O2_Volts[i], i])
		else:
			Nrml.append([O2_Volts[i], i])
	LEAN = pd.DataFrame(data=Lean, columns=['O2_Volts','Index'])
	RICH = pd.DataFrame(data=Rich, columns=['O2_Volts','Index'])
	NRML = pd.DataFrame(data=Nrml, columns=['O2_Volts','Index'])
	
	return LEAN, RICH, NRML
		
  

