cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run --source=. Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run  --source=. DIAFuelMixture/Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run  --source=. DistAvg/Test*.py
coverage report 
coverage html 
cd ..
