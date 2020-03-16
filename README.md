## Status

[![Build Status Travis](https://travis-ci.org/prithvisekhar/VehicalDiagnosticAlgo.svg?branch=master)](https://travis-ci.org/prithvisekhar/VehicalDiagnosticAlgo) 

![CI_GITHUB_Internal](https://github.com/prithvisekhar/VehicalDiagnosticAlgo/workflows/CI/badge.svg)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/850d420d714c4c5a899b0de26e00b09d)](https://www.codacy.com/manual/prithvisekhar/VehicalDiagnosticAlgo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prithvisekhar/VehicalDiagnosticAlgo&amp;utm_campaign=Badge_Grade)

[![codecov](https://codecov.io/gh/prithvisekhar/VehicalDiagnosticAlgo/branch/master/graph/badge.svg)](https://codecov.io/gh/prithvisekhar/VehicalDiagnosticAlgo)

[![Maintainability](https://api.codeclimate.com/v1/badges/4fa4a36a9eaf145944ac/maintainability)](https://codeclimate.com/github/prithvisekhar/VehicalDiagnosticAlgo/maintainability)

Some of the common road problems today include traffic, accidents and uneconomical driving styles.

In India, it is observed that more than 50% of the accidents occur due to bad road conditions. Road anomalies such as potholes and roughness also add up to traffic congestion in major cities. To solve such issues, it is important to monitor the condition of roads and vehicles regularly.

We can sort these issues into two categories:

-   Road anomalies
-   Driver and Vehicle behavior

Road anomalies can include potholes, speed-breakers or just any other abnormality on roads.

An efficient method to detect such anomalies can be through an accelerometer. An accelerometer is a device used to measure acceleration forces in the x y and z directions. Most of the smartphones today have an accelerometer in-built. This makes our approach cost efficient as we do not require any additional hardware.

The idea is to measure acceleration in x y and z directions and recognize peaks in order to detect harsh movement of the vehicle. But how do we measure the acceleration forces? How do we visualize them?

Smartphones have applications that can be installed onto the devices that measure and display acceleration forces on a 3D plane.

But is measuring acceleration enough? What can we do with that information?

Accelerometer data combined with driving style analysis or drive cycles can be of great benefit. OBD (On board diagnostics) is a simple port attachable device that records real time data from cars such as RPM, Fuel data, Pedal positions, location coordinates and much more. This data can be correlated with the accelerometer data to render amazing analytic models. The huge collection of data acquired can help us understand how the anomalies affect automobiles and how drivers react to such anomalies.

The idea not only serves the purpose of detection of, but has several other possible applications:

-  Driver applications

  -   Fuel efficiency
  -   Proximity of routes (point A to B)
  -   Drive cycles
-  Government applications

  -   Traffic violations
  -   Road health
  -   Road emergencies
-  Vehicle applications

  -   Fleet management
  -   Vehicle wear and tear
-  Allied services

  -   Insurance services (Based on drive cycles)
  -   Access to SOS – (Emergency and Breakdown)
