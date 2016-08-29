#!/usr/bin/python3

import Evmmsger

evm1bmc = Evmmsger.Evmmsg('/dev/ttyUSB1')

evm1bmc.msg('Hello World!')
evm1bmc.write('reboot')
evm1bmc.readlines()
evm1bmc.printlines()

if evm1bmc.match('BOOT COMPLETE'):
    print('boot completed!')

evm1bmc.close()
