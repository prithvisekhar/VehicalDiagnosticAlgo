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
coverage run  --include='pwd'/* DIAFuelMixture/Test*.py
coverage report 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
pwd
coverage run  --include='pwd'/* DistAvg/Test*.py
coverage report 
coverage html 
cd ..
