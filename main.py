from machine import Pin, ADC, PWM
import time

# configure digital pins for multiplexer
pinS0 = Pin(2, Pin.OUT)
pinS1 = Pin(0, Pin.OUT)
pinS2 = Pin(4, Pin.OUT)

# configure analog pins for LDRs
pin0 = ADC(0)

# Define wait time between the readjustment of the solar panel (multiplied by 4)
wait = 0.02

# Define limit (analog) to detect wether the LDR is in the sun or in the shadow
limit_LDR = 300

# define servos
servo_rotation = PWM(Pin(12), freq=50)  # Pin2
servo_tilt = PWM(Pin(14), freq=50)  # Pin4

# define the working limits for the servos
lim_servo_low = 25
lim_servo_top = 130
lim_servo_top_2 = 99

# calculate the mean for the initial position
mean_servo_bot = int(((lim_servo_top + lim_servo_low) / 2))
mean_servo_top = int((lim_servo_top + lim_servo_top_2) / 2)

# run servos to initial position
servo_rotation.duty(mean_servo_bot)
servo_tilt.duty(mean_servo_top)

# set working values for the LDR logic
working_value_down = mean_servo_bot
working_value_up = mean_servo_top
# set the step width for the servos movement
delta = 1

#function for reading of the LDR values
def read_value(s0, s1, s2):
    time.sleep(wait)
    pinS0.value(s0)
    pinS1.value(s1)
    pinS2.value(s2)
    value = pin0.read()  # Analogen Wert lesen
    position = value < limit_LDR
    print(value)
    return value, position

while True:
  
    # read LDR value top left // Multiplexer A0
    [value_top_left, top_left] = read_value(0, 0, 0)

    # read LDR value top right // Multiplexer A1
    [value_top_right, top_right] = read_value(1, 0, 0)

    # read LDR value bottom left // Multiplexer A2
    [value_bot_left, bot_left] = read_value(0, 1, 0)

    # read LDR value bottom right // Multiplexer A3
    [value_bot_right, bot_right] = read_value(1, 1, 0)
    
    if top_right == True and top_left == True and bot_right == True and bot_left == True:
        print("cloud")
        # time.sleep("600") # all values are measuring shadow, wait time is set to 10 minutes till the next readjustment

    else:
        if top_right == True and top_left == True and working_value_up >= lim_servo_low: # define the conditions for the case
            working_value_up = working_value_up - delta # define the new working value for the servo
            servo_tilt.duty(working_value_up) # tilt the servo by 1°
        #   servo_neigung.duty(mittelstellung-1)# servo Neigung um 1° gegen Uhrzeigersinn

        # Fall2: shadow tlA0 + blA2
        elif top_left == True and bot_left == True and working_value_up <= lim_servo_top: # define the conditions for the case
            working_value_down = working_value_down + delta # define the new working value for the servo
            servo_rotation.duty(working_value_down) # tilt the servo by 1°

        # Fall 3: shadow trA1 +brA3
        elif top_right == True and bot_right == True and working_value_down <= lim_servo_top: # define the conditions for the case
            working_value_down = working_value_down - delta # define the new working value for the servo
            servo_rotation.duty(working_value_down) # tilt the servo by 1°

        # Fall 4: shadow brA3 + blA2
        elif bot_right == True and bot_left == True and working_value_up >= lim_servo_low: # define the conditions for the case
            working_value_up = working_value_up + delta # define the new working value for the servo
            servo_tilt.duty(working_value_up) # tilt the servo by 1°

        else:
            print("Currently no adjustment necessary")
            time.sleep(1200)
            # set the wating time to the calculatet value (20 min) till the next readjustment starts
            
