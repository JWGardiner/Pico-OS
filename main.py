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
        try:
            file = open('usr/user.cfg', 'w')
            f.close()
        except OSError:
            print("/usr/user.cfg already exists")
    except OSError:
        print("/usr already exists")        
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
        if command == "ls-cmd":
            try:
                print(os.listdir("bin/"))
            except OSError:
                print("Unable to access /bin to retrieve commands.")
        else:
            print("Couldn't find command \""+command+"\"")
        
    cli()
    
#Start the OS
setup()
startup()
print("\nPico OS v"+system.ver)
cli()

