import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from shapely.geometry import Point

def combustion_mixture(O2_Volts):
	lean = []
	rich = []
	nrml = []
	LEAN = pd.DataFrame(data=lean, columns=['O2_Volts','Index'])				#"Engine is in safe state")
	RICH = pd.DataFrame(data=rich, columns=['O2_Volts','Index'])				#"Engine is in safe state")
	NRML = pd.DataFrame(data=nrml, columns=['O2_Volts','Index'])				#"Engine is in safe state")

	for i in range(0, len(O2_Volts)):
		if O2_Volts[i]== '-' :
			O2_Volts[i]= '0';
		O2_Volts[i] = float(O2_Volts[i])		
		if O2_Volts[i] >= 0.0 and O2_Volts[i] <= 0.1:
			lean.append([O2_Volts[i], i])
			LEAN = pd.DataFrame(data=lean, columns=['O2_Volts','Index'])
		elif O2_Volts[i] >= 0.9 and O2_Volts[i] <= 1.0:
			rich.append([O2_Volts[i], i])
			RICH = pd.DataFrame(data=rich, columns=['O2_Volts','Index'])
		else:
			nrml.append([O2_Volts[i], i])
			NRML = pd.DataFrame(data=nrml, columns=['O2_Volts','Index'])
	
	return LEAN, RICH, NRML
		
  

