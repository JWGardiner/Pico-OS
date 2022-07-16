import machine
import network
import os

#Setup - Create all the directories, folders etc that are required for normal function
def setup():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()
    try:
        os.mkdir("bin")
    except OSError:
        print("/bin already exists")
    try:
        os.mkdir("usr")
    except OSError:
        print("/usr already exists")
    finally:
        try:
            f = open("usr/user.cfg", "w")
            fileSize = os.stat("usr/user.cfg")[6]
            if fileSize == 0:
                f.write("default")
                f.close()
            else:
                print("/usr/user.cfg already exists")
        except OSError:
            print("/usr/user.cfg already exists")
    try:
        os.mkdir("startup")
    except OSError:
        print("/startup already exists")    
    led.off()
f = open("usr/user.cfg", "r")
name = f.read()
f.close()

#Store some important information for later
class system:
    led = machine.Pin("LED", machine.Pin.OUT)
    username = name
    ver = "0.0.1"

#Startup code - Runs all the files in the /startup directory.
def startup():
    for file in os.listdir("startup"):
        try:
            exec(open("startup/"+file).read())
        except OSError:
            print("A startup program encountered an error: \""+file+"\"")

#Command line interface
def cli():
    command = input(name+" $: ")
    try:
        exec(open("bin/"+command).read())
    except OSError:
        print("Couldn't find command \""+command+"\"")
    cli()
    
#Start the OS
setup()
startup()
print("\nPico OS v"+system.ver)
cli()
