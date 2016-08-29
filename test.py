#!/usr/bin/python3

import Evmmsger

dev1 = Evmmsger.Evmmsg('/dev/ttyUSB1')

dev1.msg('Hello World!')
dev1.write('reboot')
dev1.readlines()
dev1.printlines()

if dev1.match('BOOT COMPLETE'):
    print('boot completed!')

dev1.close()
