# Dynamic-solar-panel
Github repository for a dynamic solar panel by Lennart Heinemann and Tobias T____ fot the IOT course at the university of applied science in Aachen.
The proect is about a solar panel that follows the sun to get the maximum power output and sends the data via Mqtt to aws. To compare the results and conclude wether the dynamic is more efficient than an static solar panel, we measure the power output with a dynamic panel and a statical.
The used microcontrollers are one ESP8266 and two ESP32.
The logic to follow the sun is flashed on the ESP866. Four LDR-sensors and a various 3D-Printed design part from fbuenonet/ are used for the logic.
For the power reading we measure the current and the voltage with an INA219 sensor. With these two values we can calculate the power outcome of the solar panels. Due to the size of the libary for the INA219 sensors it's not possible to use ESP8266 fot the measuring, therefore we switched over to the ESP32.
The used language is micropython.


There are various libaries:
- Main 
  Contains the Power meter reading and the MQTT connection
- ina219 // chrisb2 - https://github.com/chrisb2/pyb_ina219/blob/master/ina219.py <br />
  Contains the libary for the current/voltage sensors INA219
- logging.py // chrisb2 -https://github.com/chrisb2/pyb_ina219/blob/master/logging.py <br />
  Contains parts of the libary for the current/voltage sensors INA219
- mqtt.py // ceedee666 - https://github.com/ceedee666/iot_introduction/blob/master/src/project_template/mqtt.py <br />
  Contains the mqtt connection
- wifi.py // ceedee666 - https://github.com/ceedee666/iot_introduction/blob/master/src/project_template/wifi.py <br />
  Contains the wifi connection
