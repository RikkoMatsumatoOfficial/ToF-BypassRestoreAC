import os
import os.path as px
from time import sleep
def Main():
    if(px.exists("HottaGame.exe")):
        os.system("HottaGame /launcher")
        print("Successfully Bypassed... This Bypass is Created by RikkoMatsumatoOfficial")
        sleep(4)
        os._exit(433)
    else:
        print("Failed to Get File HottaGame.exe, pls make sure what you're bypass in game folder of Tower of Fantasy(Global Version)!!!")
        sleep(12)
        os._exit(456)

if __name__ == "__main__":
    Main()