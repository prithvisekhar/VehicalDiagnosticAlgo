cd DIASpeedVoilation_SpeedVoilation
python Test*.py
coverage run --source=.  Test*.py
coverage report 
coverage html 
cd ..
