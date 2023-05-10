import random
import time
import msvcrt

class controller():
    
    def __init__(self,tv_situation = "Off",tv_volume = 0,channel_list = ["BBC"],current_chanel = "BBC"):       
        self.tv_situation = tv_situation
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.current_channel = current_chanel
                
    def tv_on(self):       
        if (self.tv_situation == "On"):
            print("The tv is already open..")
        else:
            print("The tv is openning..")
            self.tv_situation = "On"
                        
    def tv_off(self):        
        if (self.tv_situation == "Off"):
            print("The tv is already Off..")
        else:
            print("The tv is shutting down..")
            self.tv_situation = "Off"
                       
    def volume_settings(self):        
        while True:
            process = input("Volume Down: '<'\nVolume Up: '>'\nTo Exit: exit")
            if (process == "<"):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("Volume: ",self.tv_volume)
            elif (process == ">"):
                if (self.tv_volume != 30):
                    self.tv_volume += 1
                    print("Volume: ",self.tv_volume)
            else:
                print("Volume updated: ",self.tv_volume)
                break
    
    def add_channel(self,channel_name):
        print("Adding the channel..")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("The channel has been added!..")
        
    def random_channel(self):
        random_ = random.randint(0,len(self.channel_list)-1)
        self.current_channel = self.channel_list[random_]
        print("Current channel: ",self.current_channel)
        
    def __len__(self):
        return len(self.channel_list)
    
    def __str__(self):
        return "Tv Situation: {}\nVolume of TV: {}\nChannel List: {}\nCurrent Channel: {}\n".format(self.tv_situation,self.tv_volume,self.channel_list,self.current_channel)
    
Controller = controller()
print("""
      
-Television Application-

1 - Turn on the television

2 - Turn off the television

3 - Volume settings

4 - Add a new channel

5 - Learn how many channel 

6 - Change the channel randomly

7 - Television informations

If you want to quit press q button...
""")

while True:
    operation = input("Choose the operation: ")
    
    if (operation == "q"):
        print("The program has been ending")
        break
    elif (operation == "1"):
        Controller.tv_on()
    elif (operation == "2"):
        Controller.tv_off()
    elif (operation == "3"):
        Controller.volume_settings()
    elif (operation == "4"):
        channel_names = input("Please write the channel names seperate with ',' : ")
        channel_list = channel_names.split(",")
        for adds in channel_list:
            Controller.add_channel(adds)
    elif (operation == "5"):
        print("How many channel are there : ",len(Controller))
    elif (operation == "6"):
        Controller.random_channel()
    elif (operation == "7"):
        print(Controller)
    else:
        print("Unvalid operation request......")