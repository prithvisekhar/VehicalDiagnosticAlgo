cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run --source=.  Test*.py
coverage html 
cd ..
cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run --source=.  Test*.py
coverage html 
cd ..
