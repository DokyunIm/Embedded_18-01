##Mini Project
import threading
import time
import notify as Notify # Send Notification(Email)
import airinfo as Air # Get Air Data
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
  US_TRIG=23
  US_ECHO=24
  GPIO.setup(US_TRIG, GPIO.OUT)
  GPIO.setip(US_ECHO, GPIO.IN)
  distance_now = 0.0
  distance_prev = 0.0
  time.sleep(0.3)
  
  while True:
    GPIO.output(US_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(US_TRIG, False)
    
    while GPIO.input(US_ECHO)==0:
      pulse_start = time.time()
    
    while GPIO.input(US_ECHO)==1:
      pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance_now = pulse_duration*17150
    distance_now = round(US_distance, 2)
    
    if(sts_mode == 0):
      print("normal mode")
    elif(sts_mode == 1):
      print("detect mode")
    
def controlButton():
  global sts_mode
  global sts_button
  BTN_PIN = 24
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  button_value = GPIO.input(BTN_PIN)
  push_start = 0.0
  push_end = 0.0
  
  while True:
    if(button_value == True and push_start == 0.0):
      push_start = time.time()
    
    elif(button_value == False and push_start > 0.0):
      push_end = time.time()
      push_time = int(round(push_end-push_start, 0))
      push_start = 0.0
      
      if(push_time > 3.0):
        sts_button = (sts_button^1) #reverse value
        
    if(sts_mode != sts_button): 
      sts_mode = sts_button
      if(sts_mode == 0): #normal mode
        print("change to normal mode")
      elif(sts_mode == 1): #detect mode
        print("change to detect mode")
    
    
  

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
  
  t_notify.start()
  t_getAirData.start()
  t_ultra_sensor.start()
  t_button()
  
  print("getAirData starting...")
  t_getAirData.start()
  
  count = 1
  while True:
    print("main Thread Running...("+str(count)+")")
    print("통합대기환경수치 : "+str(air_data['khai_value']))
    print("통합대기환경등급 : "+str(air_data['khai_grade']))
    print(threading.activeCount())
    count += 1
    time.sleep(5)
  
