cd DIASpeedVoilation_SpeedVoilation
python Test*.py
pwd
coverage run --source=. Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
pwd
coverage run  --source=.,DIAFuelMixture/Test*.py DIAFuelMixture/Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
pwd
coverage run  --source=.,DistAvg/Test*.py DistAvg/Test*.py
coverage report 
coverage html 
cd ..
