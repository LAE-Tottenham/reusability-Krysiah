import pyfiglet 
from pyfiglet import Figlet
import time

def intro():
     f = Figlet(font="slant")
     print(f.renderText("HEY!"))
     
     time.sleep(2)
     
     welcome = pyfiglet.figlet_format("Welcome", font = "bulbhead" ) 
     print(welcome)

     time.sleep(2)

     to_the = pyfiglet.figlet_format("To The...", font = "5lineoblique" ) 
     print(to_the)

     time.sleep(1.5)

     weird = pyfiglet.figlet_format("Weird", font = "alligator" ) 
     print(weird)
     
     time.sleep(1)

     weather = pyfiglet.figlet_format("Weather", font = "alligator" ) 
     print(weather)

     time.sleep(1)

     bot = pyfiglet.figlet_format("Bot!", font = "alligator" ) 
     print(bot)

     time.sleep(3)