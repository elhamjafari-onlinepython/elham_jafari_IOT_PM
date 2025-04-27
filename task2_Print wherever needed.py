'''
APM:


 daryaft shod 
'''


class Device:
    def __init__(self, topic):
        self.topic = topic
        print(f"Creating device with topic: {topic}")
        self.topic_list = self.topic.split("/")
        print(f"Topic list: {self.topic_list}")
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.device_name = self.topic_list[3]
        self.status = "OFF"
        print(f"Device initialized: Location={self.location}, Group={self.group}, Type={self.device_type}, Name={self.device_name}, Status={self.status}")
  
    def turn_on(self):
        self.status = "ON"
        print(f"Device {self.device_name} turned ON")
        
    def turn_off(self):
        self.status = "OFF"
        print(f"Device {self.device_name} turned OFF")
        
    def get_status(self):
        print(f"Current status of {self.device_name}: {self.status}")
        

class Sensor:
    def __init__(self, topic):
        self.topic = topic
        print(f"Creating sensor with topic: {topic}")
        self.topic_list = self.topic.split("/")
        print(f"Topic list: {self.topic_list}")
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.sensor_type = self.topic_list[2]
        self.sensor_name = self.topic_list[3]
        print(f"Sensor initialized: Location={self.location}, Group={self.group}, Type={self.sensor_type}, Name={self.sensor_name}")
        
    def read_sensor(self):
        value = 25
        print(f"Sensor {self.sensor_name} reading: {value}")
        return value
        

class Admin_panel:
    def __init__(self):
        self.groups = {}
        print("Admin panel initialized")
        
    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f"Group '{group_name}' created successfully")
        else:
            print(f"Group '{group_name}' already exists")
        
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f"Device '{device.device_name}' added to group '{group_name}'")
        else:
            print(f"Group '{group_name}' does not exist")

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f"home/{group_name}/{device_type}/{name}"
            print(f"Creating new device with topic: {topic}")
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f"New device '{name}' of type '{device_type}' created in group '{group_name}'")
        else:
            print(f"Cannot create device - group '{group_name}' does not exist")
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
            
                print(f"Device '{device_name}' successfully created and added to group '{group_name}'")
            
        else:
            pass
