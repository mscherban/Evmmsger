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

#The output of this looks like:
#
#mike@ubuntu:~/workdir/pyserial/Evmmsger$ sudo ./test.py 
#/dev/ttyUSB1: Hello World!
#/dev/ttyUSB1: |   [00:00:24]  Executing command "reboot"
#/dev/ttyUSB1: |   [00:00:24]  Full Reset Begin
#/dev/ttyUSB1: |   [00:00:24]  Full Reset Complete
#/dev/ttyUSB1: |   [00:00:24]  SOC RST Begin
#/dev/ttyUSB1: |   [00:00:24]  Current BootMode is set to dsp no boot 
#/dev/ttyUSB1: |   [00:00:24]  SOC RST Complete
#/dev/ttyUSB1: |   [00:00:25]  BOOT COMPLETE    
#/dev/ttyUSB1: |   BMC>
#boot completed!
#mike@ubuntu:~/workdir/pyserial/Evmmsger$ 

