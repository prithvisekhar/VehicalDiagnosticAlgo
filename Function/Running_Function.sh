cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run   Test*.py
coverage html 
cd ..
cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run   Test*.py
coverage html 
cd ..
