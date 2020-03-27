# Fuel Mixture
Function checks the ratio of air-fuel mixture and classify them as the Lean or Rich mixture.
1. When the oxygen value in the sensor is less than 0.1, it is classified as the Lean mixture.
2. When the O2 value is between 0.9 to 1.0, it is classified as the Rich mixture.


## Input
 
-   O2 Volts Bank 1 sensor 2(V)

## Output
 
-   Count of instances when NOx emissions happened

-   Count of instances when CO and HC emissions happened

# DistAvg
Logic: Total Fuel is taken at the starting then the mileage is taken till that point. Using the mileage on the remaining Fuel the expected Distance is calculated and plotted.
