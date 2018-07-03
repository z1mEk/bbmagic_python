######################################################################################
# Descirption: BBMagic class use the bbmagic_lib for support the MMBagic devices.
#              Site of BBMagic project is http://bbmagic.net
# author: Gabriel Zima (z1mEk)
# e-mail: gabriel.zima@wp.pl
# date: 2018-07-02
# compatibile verion: 1.2
######################################################################################

import ctypes
from ctypes import *
bbm_bt_lib = ctypes.CDLL("./bbmagic_lib_1.2.so")

class BBMagic:
   
    #Function: open bt hci and starts bt scanning
    def bbm_bt_open(self, led_pin):
        return bbm_bt_lib.bbm_bt_open(led_pin)

    #Function: stops bt scanning and closes bt hci
    def bbm_bt_close(self):
        return bbm_bt_lib.bbm_bt_close()

    #Function: reads data from bbmagic modules
    def bbm_bt_read(self, bbm_data):
        bbm_buf = (c_byte * 23)()
        i = bbm_bt_lib.bbm_bt_read(byref(bbm_buf))
        bbm_data = bbm_buf
        return i

    #Function: returns version of bbm_bt library
    def bbm_bt_lib_version(self):
        return bbm_bt_lib.bbm_bt_lib_version()