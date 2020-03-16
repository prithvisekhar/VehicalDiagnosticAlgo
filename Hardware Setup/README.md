# OBD- Hardware Setup

Aim: To use OBD adapter to record and share necessary data.

## Prerequisites

1.OBD Adapter
2.Torque Pro Android Application

## Procedure

### OBD Adapter-

-Make sure your car is OBD2 compatible. You can check our list of OBD2 compatible cars here.
-Ensure that the car supports the latest OBD2 protocol. (Older versions might not work on new OBD2 modules).
-Locate your car&#39;s OBD II diagnostic port and plug in your scanner. It&#39;s usually found under the driver&#39;s side dashboard, under the steering wheel.
-Turn on your ignition by turning your key to the 2nd turn. The engine will be off, but this provides power to your dash lights, radio and also the OBD II diagnostic port.
-From your Android Smartphone or tablet, go to your SETTINGS, then WIRELESS &amp; NETWORKS, then BLUETOOTH SETTINGS. Turn on Bluetooth, scan for the nearby devices and pair your phone with the scanner. The name of the scanner will vary depending on the model.

### Bluetooth Pairing Issues

-Unpair any existing Bluetooth devices such as, smartwatch, headset or speaker
-Make sure the App is not running in the background. Close the app before pairing
-If the password 1234 doesn&#39;t work, try 12345 or 0000
-Turn off Bluetooth, turn it back on and rescan for the device

### Android Application

-Torque Pro ( [https://play.google.com/store/apps/d...l.torque&amp;hl=en](https://play.google.com/store/apps/d...l.torque&amp;hl=en) ) is one of the most popular apps for reading the OBDII data.
-It has both diagnosis capabilities (reading the error codes, system checkup, resetting error codes etc.) as well as real-time dashboard and graphing capabilities.
-It has a pretty useful - although a bit cumbersome and non-intuitive - GUI and allows the user to setup various dashboards as per their liking.
-It also offers various &quot;themes&quot; (for colors, fonts and appearances etc.) to choose from.
-Home Screen of the App

-The top left-hand corner you have 4 blue icons. The left one is GPS it will flash until you get GPS lock on. The next icon across is just to show that the app is running.
-The next is an icon to show status of connection to the ELM327 OBD device. Flashing = Not connected and Solid Blue = Connected.
-The right-hand icon is connection to the car&#39;s ECU, for this the ignition needs to be on and then same as before. Flashing = Not connected and Solid Blue = Connected.
-Although not necessary, you need to set up a profile for Torque to correctly calculate fuel cost, MPG, HP, Fuel remaining and more.
-Before you set up a profile, I recommend setting up which unit measurements you want to use first. To do this press the settings button on the bottom left of the screen – Select Settings – Then Units – Then tick or un-tick the boxes as necessary.

-Now you are ready to set up a profile. Go back to the first screen and again press the settings button on the bottom left – Select Vehicle Profile – Create New Profile- Then fill in the boxes with details about your car.
-Now let&#39;s select the sensor data we need to capture. For that go to Settings and select &#39;Data Logging and Upload&#39; and in that &#39;Select What to Log&#39;. You can select the sensor data to be recorded from the three dots menu on the top right corner.
-Here is the list of sensors that needs to be selected

-GPS Time
-Device Time
-Longitude
- Latitude
- GPS Speed (Meters/second)
- Altitude
- G(x)
- G(y)
- G(z)
- G(calibrated)
- Absolute Throttle Position B (%)
- Acceleration Sensor (Total)(g)
- Acceleration Sensor (X axis) (g)
- Acceleration Sensor (Y axis) (g)
- Acceleration Sensor (Z axis) (g)
- Accelerator Pedal Position D (%)
- Accelerator Pedal Position E(%)
- Accelerator PedalPosition F(%)
- Actual engine % torque(%)
- Air Fuel Ratio(Commanded)(:1)
- Ambient air temp(Â°C)
- Average trip speed(whilst moving only)(km/h)
- Average trip speed(whilst stopped or moving)(km/h)
- Barometric pressure (from vehicle)(psi)
- COâ‚‚ in g/km (Average)(g/km)
- DPF Pressure(psi)
- DPF Temperature(Â°C)
- Engine Coolant Temperature(Â°C)
- Engine kW (At the wheels)(kW)
- Engine Load(%)
- Engine Load(Absolute)(%)
- Engine Oil Temperature(Â°C)
- Engine reference torque(Nm)
- Engine RPM(rpm)
- Fuel flow rate/hour(gal/hr)
- Fuel flow rate/minute(gal/min)
- Fuel Remaining (Calculated from vehicle profile)(%)
- GPS Accuracy(m)
- GPS Altitude(m)
- GPS Bearing(Â°)
- GPS Latitude(Â°)
- GPS Longitude(Â°)
- GPS Satellites        
- GPS vs OBD Speed difference(km/h)
- Horsepower (At the wheels)(hp)
- Intake Air Temperature(Â°C)
- Intake Manifold Pressure(psi)
- O2 Volts Bank 1 sensor 1(V)
- O2 Volts Bank 1 sensor 2(V)
- Relative Throttle Position(%)
- Run time since engine start(s)
- Speed (GPS)(km/h)
- Speed (OBD)(km/h)
- Throttle Position(Manifold)(%)
- Timing Advance(Â°)
- Torque(Nm)
- Trip average KPL(kpl)
- Trip average Litres/100 KM(l/100km)
- Trip average MPG(mpg)
- Trip Distance(km)
- Trip Time(Since journey start)(s)
- Trip time(whilst moving)(s)
- Trip time(whilst stationary)(s)
- Turbo Boost &amp; Vacuum Gauge(psi)
- Turbo Pressure Control(psi)
- Voltage (Control Module)(V)
- Voltage (OBD Adapter)(V)
- Volumetric Efficiency (Calculated)(%)

- Most of them are by default selected. This is a one-time operation.
- Next comes the sharing of the recorded data. For this, we have to go back to the &#39;Data logging and Upload&#39;. Select &#39;User Email Address&#39;. This email address will be used to send the logged data every time we command it to.
- The rest of the settings can be explored but mostly they are left by default.

- Right, let&#39;s go back to the first screen and this time we go into &#39;Real-time Information&#39;. This brings up a set of six gauges, but if you swipe left, right, up or down, depending on which way you&#39;re holding the screen it reveals more gauges.
- These are fully customizable. Anything from style and size, to what data they display can be changed.
- Press and hold a blank area of screen and you will have the option to &#39;Add a Display&#39; Here you select the type of gauge you want, then what data you want it to show, then the size.
- Press and hold a gauge that&#39;s already on the screen and it bring up, the customization menu.
- When everything is setup and ready to log data, click the gear icon on the bottom left corner and start logging the data.
- After the trip ends, stop the logging and email logs. Reset the trip counters so that the next trip starts from zero.
- OK that about sums up what you should do to get started with Torque for Android.
- Back at the first screen if all 4 icons are blue and have stopped flashing, you&#39;re ready to begin.

## Important Tips:

1. Start Logging data after the ignition.
2. Make sure the phone stays connected to the internet at all time when logging data. If not, it can tamper the accuracy of data (most importantly GPS data).
3. Make sure not to keep the phone on low power mode while logging data. The reason is the same as the above, it can capture inaccurate data.
4. Reset trip Counters for every log. (End of current trip or start of the next trip)
5. Email the datasets as soon as the trip ends.

## Additional Resources:

- Torque Pro Application Setup [https://www.youtube.com/watch?v=Es5sDrVRyuI](https://www.youtube.com/watch?v=Es5sDrVRyuI)
- Video Plugin [https://www.youtube.com/watch?v=w4yvA9gZON8](https://www.youtube.com/watch?v=w4yvA9gZON8)
