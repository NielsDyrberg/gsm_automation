
import gsm_interface
from time import sleep

def main():
    gs = gsm_interface.GSMInterface()
    #while 1:
    gs.send_cmd()
        #sleep(5)

if __name__ == "__main__":
    main()