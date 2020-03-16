# 1) Coolant Temperature
It compares the value of coolant temperature with that of the predefined
values of coolant temperature to check whether the system is running in the safe state or not.

## Input
- Engine Coolant Temperature(Â°C)
- Engine Load(%)
- Trip Time(Since journey start)(s)

## Output
-Prints whether the system is running in safe state or not along with the plot of engine
coolant temperature.

# 2) Load Analysis
Analyzing whether the engine is working under the rated load level or exceeding
the recommended values.

## Input
-Engine Load(%)
-Engine RPM(rpm)
-Speed (GPS)(km/h)

## Output
-Engine is overloaded or not with respect to Engine Load, engine RPM, and Speed.

# 3)Fuel Mixture
The number of instances when the combustion is lean (More air and
less fuel) or rich (More fuel and less air)

## Input
-O2 Volts Bank 1 sensor 2(V)

## Output
-Count of instances when NOx emissions happened.
-Count of instances when CO and HC emissions happened.

# 4)Speed Violation
It checks the speed of the system and returns the location at which the speed
of the system exceeded the permissible value.

 ## Input
-Latitude
-Longitude
-GPS Time
-Speed (GPS)(km/h)

 ## Output
-Speed
-Index




