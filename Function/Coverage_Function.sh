#!/bin/sh -e 
coverage combine .coverage   DIARoadProfile/.coverage  
codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  
