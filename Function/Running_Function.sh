cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run --source=.  Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture/DIAFuelMixture
python Test*.py
coverage run --source=.  Test*.py
coverage report 
coverage html 
cd ..
cd ..
cd DIAFuelMixture_FuelMixture/DistAvg
python Test*.py
coverage run --source=.  Test*.py
coverage report 
coverage html 
cd ..
cd ..
