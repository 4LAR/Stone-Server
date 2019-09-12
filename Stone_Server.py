#
#     Stone Server
#    [Stolar Studio]
#   

import configparser, time, os, os.path

ver = "0.1.2"

if not os.path.exists("Stone_server.txt"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "command", "")
    config.set("Settings", "loop", "false")
    with open("Stone_server.txt", "w") as config_file:
        config.write(config_file)
    print("Write command in settings file")
    print("\nPress enter...")
    input()
    exit()

config = configparser.ConfigParser()
config.read("Stone_server.txt")
com = config.get("Settings", "command")
loop_s = config.get("Settings", "loop")

if len(com)<1:
    print("Not found command file")
    print("\nPress enter...")
    input()
    exit()

loop_t = ["True","true"]
loop_f = ["False","false"]

if loop_s in loop_t:
    loop = True
elif loop_s in loop_f:
    loop = False
else:
    print("Error loop")
    print("\nPress enter...")
    input()
    exit()

print("\n [ Stone Server Started ]\n")
if loop:
    while loop:
        os.system(com)
        print("\n [ Stone Server Rebooting ] \n")
else:
    os.system(com)
    

print("\n [ Stone Server Stopped ] Press enter...")
input()
