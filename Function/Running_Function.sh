cd DIAFuelMixture_FuelMixture
python Test*.py
coverage run --source=.  Test*.py
coverage report 
coverage html 
cd ..
