cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run --source=.  Test*.py
git add .coverage 
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run --source=.  Test*.py
git add .coverage 
coverage html 
cd ..
