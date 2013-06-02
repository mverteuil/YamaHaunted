#!/usr/bin/env python
import time

import ping

import settings
import xva730

def main():
    powered_on = False
    while 1:
        print "Checkin..."
        delay = ping.do_one(settings.PHONE_IP, 4, 64)
        if not delay and powered_on:
            xva730.power_off()
            powered_on = False
            print "Dude's offline"
        elif delay and not powered_on:
            xva730.power_on()
            powered_on = True
            print "Dude's online"
        print "Sleepin for 5..."
        time.sleep(5)


if __name__ == "__main__":
    main()
