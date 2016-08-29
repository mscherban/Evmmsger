# Evmmsger

Provide a Python EVM class  to easily communicate through a serial port. This is useful for scripting tasks that are tedious to do by hand.

# How to use

Simply clone this repository and import Evmmsger. Refer to test.py for an example.

# Methods

**1. Evmmsg(str 'device', baudrate=115200, timeout=1)** - Create the EVM message object. The only required parameter is the location of your serial device, such as '/dev/ttyUSB1'. Timeout will default to 1, but is the number of seconds that will elapse with no communication before Evmmsger.readlines() times out and returns.

	dev1 = Evmmsger.Evmmsg('dev/ttyUSB1')
    
    
**2. close()** - Close the EVM message object.

	dev1.close()
    
**3. write()** - Write to the EVM over the serial port. This will automatically append a return-newline.

	dev1.write('reboot')
    
**4. readlines()** - Read the output of the EVM. It will return a list of strings, one for each line. This will timeout and return after *timeout=1* seconds, given in the Evmmsg() method. It will also internally store the list of strings.

	evm_output = dev1.readlines()   or   dev1.readlines() #to just use internally stored list output
    
**5. printlines(list=read_list[])** - Print out a list of strings returned by readlines(), or call on it's own to print out the internally stored list from the last readlines().

	dev1.printlines(evm_output)   or   dev1.printlines() #to print internally stored list from last readlines()
    
**6. msg(str string)** - Print a message to console appended with the serial name.

	dev1.msg('Hello world')    #prints '/dev/ttyUSB1: Hello world'
    
**7. match(str string_to_match)** - Returns the line which string_to_match was found on. Can be used for parsing output for conditionals. Returns False if it is not found. This is case sensitive.

	if dev1.match('BOOT COMPLETE'):
    	print('Boot Completed')
