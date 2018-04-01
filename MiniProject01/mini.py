##Mini Project
import threading
import time
import notify as Notify # Send Notification(Email)
import airinfo as Air # Get Air Data
import led as LED
##################################################
import RPi.GPIO as GPIO
import time
##################################################


def sendNotification():
  Notify.send('imjoshua9316dev@gmail.com', 'imjoshua9316@gmail.com')
  print("success to send Notification")    
  
def getAirData():
  global air_data
  while True:
    air_data = Air.getAir()
    #print(air_data)
    time.sleep(1800) # execute with interval 30min

def controlUltraSensor():
  global sts_mode
  global air_data
  US_TRIG=18
  US_ECHO=21
  GPIO.setwarnings(False)
  distance_now = 0.0
  distance_prev = 0.0
  time_now = 0.0
  time_prev = 0.0
  detect_count = 0
  GPIO.setup(US_TRIG, GPIO.OUT)
  GPIO.setup(US_ECHO, GPIO.IN)
  GPIO.output(US_TRIG, GPIO.LOW)
  time.sleep(0.3)
  
  time_prev = time.time()
  while True:
    time_now = time.time()
    GPIO.output(US_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(US_TRIG, False)
    
    while GPIO.input(US_ECHO)==0:
      pulse_start = time.time()
    
    while GPIO.input(US_ECHO)==1:
      pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance_now = pulse_duration*17150
    distance_now = round(distance_now, 2)
    
    if(distance_prev == 0.0 and distance_now > 0.0):
      distance_prev = distance_now
    
    elif(distance_prev > 0.0 and distance_now > 0.0):
      if(abs(distance_now - distance_prev) > 100.0):
        detect_count += 1
        distance_prev = distance_now
    
    if(abs(time_now - time_prev) > 3.0):
        detect_count = 0
        time_prev = time_now
    elif(sts_mode == 0 and detect_count >= 5):
      print("normal mode(val: "+str(distance_now)+")")
      #turn on led - air condition info
      detect_count = 0
      
      if(air_data['khai_grade'] == '1'):
        controlLED(0,0,70)
      elif(air_data['khai_grade'] == '2'):
        controlLED(0,70,0)
      elif(air_data['khai_grade'] == '3'):
        controlLED(70,70,0)
      elif(air_data['khai_grade'] == '4'):
        cotrolLED(70,0,0)
    elif(sts_mode == 1 and detect_count >= 5):
      print("detect mode(val: "+str(distance_now)+")")
      #turn on led and send notification
      detect_count = 0
    
def controlButton():
  global sts_mode
  global sts_button
  BTN_PIN = 23
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  button_value = GPIO.input(BTN_PIN)
  push_start = 0.0
  push_end = 0.0
  
  while True:
    button_value = GPIO.input(BTN_PIN)
    if(button_value == True and push_start == 0.0):
      push_start = time.time()
    
    elif(button_value == True and push_start > 0.0):
      push_end = time.time()
      push_time = (push_end-push_start)
      
      if(push_time > 2.0):
        sts_button = (sts_button^1) #reverse value
        push_start = 0.0
        push_time = 0.0
        if(sts_mode != sts_button): 
            sts_mode = sts_button
            if(sts_mode == 0): #normal mode
                print("change to normal mode")
            elif(sts_mode == 1): #detect mode
                print("change to detect mode")


def controlLED(r, g, b):
    LED_POWER=14
    RED = 4
    GREEN = 3
    BLUE = 2
    FREQ = 100
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_POWER, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    
    LED_R = GPIO.PWM(RED, FREQ)
    LED_G = GPIO.PWM(GREEN, FREQ)
    LED_B = GPIO.PWM(BLUE, FREQ)
    LED_R.start(0)
    LED_G.start(0)
    LED_B.start(0)

    LED_R.ChangeDutyCycle(r)
    LED_G.ChangeDutyCycle(g)
    LED_B.ChangeDutyCycle(b)
    time.sleep(5)

  

if __name__ == '__main__': #start main procedure
  global sts_button
  global sts_ultra_sensor
  global sts_mode
  #set GPIO mode
  GPIO.setmode(GPIO.BCM)
  sts_button = 0
  sts_ultra_sensor = 0
  sts_mode = 0 # 0: home mode / 1: detect mode
  
  #init air_data value
  global air_data
  air_data = {
    'khai_value': '', #통합대기환경수치 0-50:좋음 51-100:보통 101-250:나쁨 251-:매우나쁨
    'khai_grade': ''  #통합대기환경등급 1:좋음 2:보통 3:나쁨 4:매우나쁨
  }
  
  #set threads
  t_notify = threading.Thread(target=sendNotification)
  t_getAirData = threading.Thread(target=getAirData)
  t_ultra_sensor = threading.Thread(target=controlUltraSensor)
  t_button = threading.Thread(target=controlButton)
  t_notify.daemon = True # when Main Thread exited, is exited
  t_getAirData.daemon = True
  t_ultra_sensor.daemon = True
  t_button.daemon = True
  
  
  #t_notify.start()
  print("getAirData thread starting...")
  t_getAirData.start()
  print("Ultra Sensor thread starting...")
  t_ultra_sensor.start()
  print("Button thread starting...")
  t_button.start()
  
  count = 1
  while True:
    print("main Thread Running...("+str(count)+")")
    print("통합대기환경수치 : "+str(air_data['khai_value']))
    print("통합대기환경등급 : "+str(air_data['khai_grade']))
    #print(threading.activeCount())
    count += 1
    time.sleep(10)
  
