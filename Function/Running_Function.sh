python Test*.py
pwd
coverage run --source=DIASpeedVoilation_SpeedVoilation DIASpeedVoilation_SpeedVoilation/Test*.py
coverage report 
coverage html 
python Test*.py
pwd
coverage run  --source=DIAFuelMixture_FuelMixture DIAFuelMixture_FuelMixture/DIAFuelMixture/Test*.py
coverage report 
coverage html 
python Test*.py
pwd
coverage run  --source=DIAFuelMixture_FuelMixture DIAFuelMixture_FuelMixture/DistAvg/Test*.py
coverage report 
coverage html 
