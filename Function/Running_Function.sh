cd DIARoadProfile
python Test*.py
pwd
coverage run   --source=.  Test*.py
coverage report 
coverage html 
cd ..
