import gsm
from time import sleep

def main():
    gs = gsm.GSMModule("20405458")

    while not gs.is_ready():
        print("Not ready, yet")
        sleep(1)
    #while 1:
    gs.send_sms("Ready for sms!")
    gs.receive_msg()
        #sleep(5)

if __name__ == "__main__":
    main()