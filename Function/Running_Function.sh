cd DIAEngineAnalysis/DIAEngineAnalysis_Coolant
python Test*.py
pwd
coverage run   --source=.,../  Test*.py
coverage report 
coverage html 
cd ..
cd ..
cd DIAEngineAnalysis/DIAEngineAnalysis_LoadAnalysis
python Test*.py
pwd
coverage run   --source=.,../  Test*.py
coverage report 
coverage html 
cd ..
cd ..
cd DIAFuelMixture_FuelMixture/DIAFuelMixture
python Test*.py
pwd
coverage run   --source=.,../  Test*.py
coverage report 
coverage html 
cd ..
cd ..
cd DIAO2Sensor
python Test*.py
pwd
coverage run   --source=.  Test*.py
coverage report 
coverage html 
cd ..
cd DIASpeedVoilation_SpeedVoilation
python Test*.py
pwd
coverage run   --source=.  Test*.py
coverage report 
coverage html 
cd ..
