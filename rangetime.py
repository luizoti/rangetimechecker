#!/usr/bin/env python3

# https://pydbus.readthedocs.io/en/latest/legacydocs/shortexamples.html
# https://simple.wikipedia.org/wiki/12-hour_clock


from datetimerange import DateTimeRange
import time

class RangeCheck():
    def convertAM(self, pmtime):
        return time.strftime( "%I:%M", time.strptime(pmtime, "%H:%M"))

    def convertMidNi(self, time):
        if time == '00:00':
            return '24:00'
        elif time == '24:00':
            return '00:00'
        else:
            return time

    def check(self, START, CURRENT, END):
        if CURRENT == None:
            CURRENT_TIME = time.strftime('%H:%M')
        else:
            CURRENT_TIME = CURRENT
            pass
        

        CURRENT_TIME = self.convertMidNi(CURRENT_TIME)

        if START <= CURRENT_TIME and not START == '00:00':
            if CURRENT_TIME <= END:
                return True
            if CURRENT_TIME > END:
                if END >= '10:00':
                    return False
                if END <= '10:00':
                    return True


        if START > CURRENT_TIME:
            return False

        if '00:00' <= START <= '01:00':
            if self.convertMidNi(START) >= CURRENT_TIME and CURRENT_TIME >= '10:00':
                return False
                pass
            if START < CURRENT_TIME:
                if CURRENT_TIME < END:
                    return True
