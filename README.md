# Dynamic-solar-panel
Github repository for a dynamic solar panel by Lennart Heinemann and Tobias Tournay for the IOT course at the University of Applied Science in Aachen.
The project is about a solar panel that follows the sun to get the maximum power output and sends the data via MQTT to amazon web services. To compare the results and conclude whether the dynamic is more efficient than a static solar panel, we measure the power output with a dynamic panel and a statical.
The used microcontrollers are one ESP8266 and two ESP32.
The logic to follow the sun is flashed on the ESP866. Four LDR-sensors and various 3D-printed designs from fbuenonet (thingiverse) are used for the logic.
For the power reading we measure the current and the voltage with an INA219 sensor. With these two values we can calculate the power output of the solar panels. Due to the size of the library for the INA219 sensors it is not possible to use ESP8266 for the measuring. Therefore, we switched over to the ESP32.
The used language for the microcontroller is MicroPython. The analysis of the measurements were done in a Jupyter Notebook. 
The following picture shows the wiring of the project.


![Wiring](https://user-images.githubusercontent.com/107534143/174503322-31b13158-e065-44cd-bc27-50133b7c3a6f.png)

There are various libraries:
- main.py <br />
  Contains the power meter reading and the MQTT connection
- ina219 // chrisb2 - https://github.com/chrisb2/pyb_ina219/blob/master/ina219.py <br />
  Contains the library for the current/voltage sensors INA219
- logging.py // chrisb2 -https://github.com/chrisb2/pyb_ina219/blob/master/logging.py <br />
  Contains parts of the library for the current/voltage sensors INA219
- mqtt.py // ceedee666 - https://github.com/ceedee666/iot_introduction/blob/master/src/project_template/mqtt.py <br />
  Contains the MQTT connection
- wifi.py // ceedee666 - https://github.com/ceedee666/iot_introduction/blob/master/src/project_template/wifi.py <br />
  Contains the wifi connection
 - solar_panel_evaluation.ipynb <br />
   Contains the Jupyter Notebook, used for the processing and evaluation of the data



