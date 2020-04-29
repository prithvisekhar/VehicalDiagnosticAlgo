#!/bin/sh -e 
coverage combine .coverage  DIAFuelMixture_FuelMixture/DistAvg/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
