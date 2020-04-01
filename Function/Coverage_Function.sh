git add DIAFuelMixture_FuelMixture/.coverage  
coverage combine  DIAFuelMixture_FuelMixture/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
