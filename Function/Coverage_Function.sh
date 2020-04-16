#!/bin/sh -e 
coverage combine    DIAEngineAnalysis/DIAEngineAnalysis_Coolant/.coverage  DIAEngineAnalysis/DIAEngineAnalysis_LoadAnalysis/.coverage  DIAFuelMixture_FuelMixture/DIAFuelMixture/.coverage  DIAO2Sensor/.coverage  DIASpeedVoilation_SpeedVoilation/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
