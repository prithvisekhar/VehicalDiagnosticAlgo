git add -f DIAFuelMixture_FuelMixture/.coverage  
git add -f DIASpeedVoilation_SpeedVoilation/.coverage  
coverage combine  DIAFuelMixture_FuelMixture/.coverage  DIASpeedVoilation_SpeedVoilation/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
