#!/usr/bin/env python3

import pytest
import time
from rangetime import RangeCheck

current_time = time.strftime('%H:%M')

def timechange(current_time, act, _time=None):
    spt = current_time.split(':')

    if _time == None:
        _time = 2
        pass

    if act == 'up':
        return ''.join([str((int(spt[0]) + _time)), ':', spt[1]])
    elif act == 'low':
        return ''.join([str((int(spt[0]) - _time)), ':', spt[1]])
        pass

rc = RangeCheck()

def low_up_ok():
    try:
        assert rc.check('08:00', '16:00', '19:00') == True
        print('low_up_ok - Ok')
    except Exception as e:
        print('low_up_ok - Error')

def low_up_err():
    try:
        assert rc.check('12:00', '20:00', '19:00') == False
        print('low_up_err - Ok')
    except Exception as e:
        print('low_up_err - Error')

def up_low_ok():
    try:
        assert rc.check('19:00', '20:00', '08:00') == True
        print('up_low_ok - Ok')
    except Exception as e:
        print('up_low_ok - Error')

def up_low_err():
    try:
        assert rc.check('19:00', '16:00', '08:00') == False
        print('up_low_err - Ok')
    except Exception as e:
        print('up_low_err - Error')


def mid_n_ok():
    try:
        assert rc.check('00:00', '02:00','08:00') == True
        print('mid_n_ok - Ok')
    except Exception as e:
        print('mid_n_ok - Error')


def mid_n_err():
    try:
        assert rc.check('00:00', '16:00','03:00') == False
        print('mid_n_err - Ok')
    except Exception as e:
        print('mid_n_err - Error')

def objectve_test_ok():
    try:
        assert rc.check('00:00', '01:00', '08:00') == True
        print('objectve_test_ok - Ok')
    except Exception as e:
        print('objectve_test_ok - Error')

def objectve_test_err():
    try:
        assert rc.check('00:00', current_time,'08:00') == False
        print('objectve_test_err - Ok')
    except Exception as e:
        print('objectve_test_err - Error')

def endmidnight_ok():
    try:
        assert rc.check('22:00', '23:00', '00:00') == True
        print('endmidnight_ok - Ok')
    except Exception as e:
        print('endmidnight_ok - Error')

def endmidnight_err():
    try:
        assert rc.check('22:00', '19:00','00:00') == False
        print('endmidnight_err - Ok')
    except Exception as e:
        print('endmidnight_err - Error')

def endmidnight_err2():
    try:
        assert rc.check('22:00', '01:00','00:00') == False
        print('endmidnight_err2 - Ok')
    except Exception as e:
        print('endmidnight_err2 - Error')

if __name__ == '__main__':
    low_up_ok()
    low_up_err()
    up_low_ok()
    up_low_err()
    mid_n_ok()
    mid_n_err()
    objectve_test_ok()
    objectve_test_err()
    endmidnight_ok()
    endmidnight_err()
    endmidnight_err2()