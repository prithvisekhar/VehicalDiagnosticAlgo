## OBD- Hardware Setup:

Aim: To use OBD adapter to record and share necessary data.
Prerequisites: 
1.	OBD Adapter
2.	Torque Pro Android Application
Procedure:
OBD Adapter- 
 
•	Make sure your car is OBD2 compatible. You can check our list of OBD2 compatible cars here
•	Locate your car’s OBD II diagnostic port and plug in your scanner. It’s usually found under the driver’s side dashboard, under the steering wheel.
 

•	Turn on your ignition by turning your key to the 2nd turn. The engine will be off, but this provides power to your dash lights, radio and also the OBD II diagnostic port.
•	From your Android Smartphone or tablet, go to your SETTINGS, then WIRELESS & NETWORKS, then BLUETOOTH SETTINGS. Turn on Bluetooth, scan for the nearby devices and pair your phone with the scanner. The name of the scanner will vary depending on the model.
 

Bluetooth Pairing Issues:

•	Unpair any existing Bluetooth devices such as, smartwatch, headset or speaker
•	Make sure the App is not running in the background. Close the app before pairing
•	If the password 1234 doesn’t work, try 12345 or 0000
•	Turn off Bluetooth, turn it back on and rescan for the device
 
Android Application 

•	Torque Pro ( https://play.google.com/store/apps/d...l.torque&hl=en ) is one of the most popular apps for reading the OBDII data. 
•	It has both diagnosis capabilities (reading the error codes, system checkup, resetting error codes etc.) as well as real-time dashboard and graphing capabilities. 
•	It has a pretty useful - although a bit cumbersome and non-intuitive - GUI and allows the user to setup various dashboards as per their liking. 
•	It also offers various "themes" (for colors, fonts and appearances etc.) to choose from. 
•	Home Screen of the App: 
 
•	The top left hand corner you have 4 blue icons. The left one is GPS it will flash until you get GPS lock on. The next icon across is just to show that the app is running. 
•	The next is an icon to show status of connection to the ELM327 OBD device. Flashing = Not connected and Solid Blue = Connected. 
•	The right hand icon is connection to the car’s ECU, for this the ignition needs to be on and then same as before. Flashing = Not connected and Solid Blue = Connected.
•	Although not necessary, you need to set up a profile for Torque to correctly calculate fuel cost, MPG, HP, Fuel remaining and more.
•	Before you set up a profile, I recommend setting up which unit measurements you want to use first. To do this press the settings button on the bottom left of the screen – Select Settings – Then Units – Then tick or un-tick the boxes as necessary. 
 		 

•	Now you are ready to set up a profile. Go back to the first screen and again press the settings button on the bottom left – Select Vehicle Profile – Create New Profile- Then fill in the boxes with details about your car.
•	Now let’s select the sensor data we need to capture. For that go to Settings and select ‘Data Logging and Upload’ and in that ‘Select What to Log’. You can select the sensor data to be recorded from the three dots menu on the top right corner. 
 	 	 
•	Here is the list of sensors that needs to be selected
 
o	GPS Time
o	Device Time	
o	Longitude	
o	Latitude	
o	GPS Speed (Meters/second)	 
o	Altitude	 
o	G(x)	 
o	G(y)	 
o	G(z)	 
o	G(calibrated)	 
o	Absolute Throttle Position B(%)	
o	Acceleration Sensor(Total)(g)	
o	Acceleration Sensor(X axis)(g)	
o	Acceleration Sensor(Y axis)(g)	
o	Acceleration Sensor(Z axis)(g)	
o	Accelerator PedalPosition D(%)	
o	Accelerator PedalPosition E(%)	
o	Accelerator PedalPosition F(%)	
o	Actual engine % torque(%)	
o	Air Fuel Ratio(Commanded)(:1)	
o	Ambient air temp(Â°C)	
o	Average trip speed(whilst moving only)(km/h)	
o	Average trip speed(whilst stopped or moving)(km/h)	
o	Barometric pressure (from vehicle)(psi)	
o	COâ‚‚ in g/km (Average)(g/km)	
o	DPF Pressure(psi)	
o	DPF Temperature(Â°C)	
o	Engine Coolant Temperature(Â°C)	
o	Engine kW (At the wheels)(kW)	
o	Engine Load(%)	
o	Engine Load(Absolute)(%)	
o	Engine Oil Temperature(Â°C)	
o	Engine reference torque(Nm)	
o	Engine RPM(rpm)	
o	Fuel flow rate/hour(gal/hr)	
o	Fuel flow rate/minute(gal/min)	
o	Fuel Remaining (Calculated from vehicle profile)(%)	
o	GPS Accuracy(m)	
o	GPS Altitude(m)	
o	GPS Bearing(Â°)	
o	GPS Latitude(Â°)	
o	GPS Longitude(Â°)	
o	GPS Satellites	GPS vs OBD Speed difference(km/h)	
o	Horsepower (At the wheels)(hp)	
o	Intake Air Temperature(Â°C)	
o	Intake Manifold Pressure(psi)	
o	O2 Volts Bank 1 sensor 1(V)	
o	O2 Volts Bank 1 sensor 2(V)	
o	Relative Throttle Position(%)	
o	Run time since engine start(s)	
o	Speed (GPS)(km/h)	
o	Speed (OBD)(km/h)	
o	Throttle Position(Manifold)(%)	
o	Timing Advance(Â°)	
o	Torque(Nm)	
o	Trip average KPL(kpl)	
o	Trip average Litres/100 KM(l/100km)	
o	Trip average MPG(mpg)	
o	Trip Distance(km)	
o	Trip Time(Since journey start)(s)	
o	Trip time(whilst moving)(s)	
o	Trip time(whilst stationary)(s)	
o	Turbo Boost & Vacuum Gauge(psi)	
o	Turbo Pressure Control(psi)	
o	Voltage (Control Module)(V)	
o	Voltage (OBD Adapter)(V)	
o	Volumetric Efficiency (Calculated)(%)
 

•	Most of them are by default selected. This is a one-time operation.
•	Next comes the sharing of the recorded data. For this, we have to go back to the ‘Data logging and Upload’. Select ‘User Email Address’. This email address will be used to send the logged data every time we command it to.
•	The rest of the settings can be explored but mostly they are left by default.

•	Right, let’s go back to the first screen and this time we go into ‘Real-time Information’. This brings up a set of six gauges, but if you swipe left, right, up or down, depending on which way you’re holding the screen it reveals more gauges. 
•	These are fully customizable. Anything from style and size, to what data they display can be changed. 
•	Press and hold a blank area of screen and you will have the option to ‘Add a Display’ Here you select the type of gauge you want, then what data you want it to show, then the size. 
•	Press and hold a gauge that’s already on the screen and it brings up, the customization menu.
•	When everything is setup and ready to log data, click the gear icon on the bottom left corner and start logging the data. 
•	After the trip ends, stop the logging and email logs. Reset the trip counters so that the next trip starts from zero.
  	 
•	OK that about sums up what you should do to get started with Torque for Android.
•	Back at the first screen if all 4 icons are blue and have stopped flashing you’re ready to begin.

Important Tips:
1.	Start Logging data after the ignition.
2.	Reset trip Counters for every log. (End of current trip or start of the next trip)
3.	Email the datasets as soon as the trip ends.

Additional Resources:
o	Torque Pro Application Setup https://www.youtube.com/watch?v=Es5sDrVRyuI 
o	Video Plugin https://www.youtube.com/watch?v=w4yvA9gZON8 
