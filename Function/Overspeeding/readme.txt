
For this feature we are collecting the speed, engine rpm, Power at wheels, torque values from OBD data. 
From this data we calculate the angular velocity with value of engine rpm, 
and find ratio of Power in W to torque value. 
If the ratio is higher than 1.2, it indicates at current gear driver is speeding more than 
he should and he need to upshift the gear. 
This indicates that driver is exceeding the 
This conclusion is verified from observation, 
during the recording driving data gear status is manually recorded.

Input 
1) Engine RPM
2) Trip Time
3) Power at wheels
4) Torque

Output
Detecting the ratio if it is more than 1.2 
Counting the number of times this overspeeding condition occurs,
to determine driving skill based on his optimum gear shifting. 