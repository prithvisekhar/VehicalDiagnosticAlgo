#!/bin/sh -e 
coverage combine .coverage  DIAO2Sensor/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
