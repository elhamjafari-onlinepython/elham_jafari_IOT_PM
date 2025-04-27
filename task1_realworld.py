'''


APM:


Salam daryaft shod 

'''

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
class Device:
    def __init__(self,topic,mqtt_broker="localhost",port=1883):
        self.topic=topic
        self.topic_list=self.topic.split("/")
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        self.mqtt_broker=mqtt_broker
        self.port=port
        self.connect_mqtt()
        self.setup.gpio()
        
    def connect_mqtt(self):
        
        self.mqtt_client=mqtt.client()
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
      
    def setup_gpio(self):
        if self.device_type=="lamps":
            GPIO.setup(17,GPIO.out)
        if self.device_type=="doors":
            GPIO.setup(27,GPIO.out)
        if self.device_type=="fans":
            GPIO.setup(22,GPIO.out)
        if self.device_type=="camera":
            GPIO.setup(100,GPIO.out)

    def turn_on(self):
        self.send_commands("TURN_ON")
        print("Turn_on,Done")
        
    def turn_off(self):
        self.send_commands("TURN_OFF")

        print("Turn_off,Done")

    def send_commands(self,command):
        self.mqtt_client.publish(self.topic,command)
        print("Done!")
        
        
a2=Device("home/group/device_type/device_name")
#a=Device("home/parking/lamps/lamps138",mqtt_broker="455.65.43.11",port=112)
#چون دیوایس واقعی نداریم میتونیم شماره پورت و ادرس آی پی رو ننویسیم 
a=Device("home/parking/lamps/lamps138")
a2=Device("home/kitchen/lamps/lamps134")
mylist=a.topic_list
a2.location
a.group
a.topic
a2.turn_off()
a2.turn_on()
