##Mini Project
import threading
import time
import notify as Notify # Send Notification(Email)
import airinfo as Air # Get Air Data

def sendNotification():
  Notify.send('imjoshua9316dev@gmail.com', 'imjoshua9316@gmail.com')
  print("success to send Notification")    
  
def getAirData():
  global air_data
  while True:
    air_data = Air.getAir()
    #print(air_data)
    time.sleep(1800) # execute with interval 30min


if __name__ == '__main__':
  global air_data
  air_data = {
    'khai_value': '', #통합대기환경수치 0-50:좋음 51-100:보통 101-250:나쁨 251-:매우나쁨
    'khai_grade': ''  #통합대기환경등급 1:좋음 2:보통 3:나쁨 4:매우나쁨
  }
  
  t_notify = threading.Thread(target=sendNotification)
  t_getAirData = threading.Thread(target=getAirData)
  t_notify.daemon = True # when Main Thread exited, is exited
  t_getAirData.daemon = True # when Main Thread exited, is exited
  
  #print("notify starting...")
  #t_notify.start()
  
  print("getAirData starting...")
  t_getAirData.start()
  
  count = 1
  while True:
    print("main Thread Running...("+str(count)+")")
    print("통합대기환경수치 : "+str(air_data['khai_value']))
    print("통합대기환경등급 : "+str(air_data['khai_grade']))
    count += 1
    time.sleep(5)
  
