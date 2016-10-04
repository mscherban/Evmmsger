# Evmmsger

Provide a Python EVM class to easily communicate through a serial port. This is useful for scripting tasks that are tedious to do by hand.

# How to use

Simply clone this repository and import Evmmsger. Refer to test.py for an example. Needs to be ran with sudo or administer account.

Requires Python3 and the pyserial module. Instructions here: http://pyserial.readthedocs.io/en/latest/pyserial.html

Most successful method is installation through source:
```
wget https://github.com/pyserial/pyserial/releases/download/v3.1.1/pyserial-3.1.1.tar.gz
tar -xzvf pyserial-3.1.1.tar.gz
cd pyserial-3.1.1
sudo python3 setup.py install
```

If you want to log everything either use open() or use tee:

	sudo ./test.py | tee log-1.log

# Methods

**1. Evmmsg(str 'name', int baudrate=115200, int timeout=1)** - Create the EVM message object. The only required parameter is the location of your serial device, such as '/dev/ttyUSB1'. Timeout will default to 1, but is the number of seconds that will elapse with no communication before Evmmsger.readlines() times out and returns. The baudrate by default is 115200 but is adjustable.

	dev1 = Evmmsger.Evmmsg('dev/ttyUSB1')
    
    
**2. close()** - Close the EVM message object.

	dev1.close()
    
**3. write(str string_to_send, str end='\r\n')** - Write a message to the EVM over serial port. This will automatically append a return-newline, unless you override it by passing end=''.

	dev1.write('reboot')
    
**4. readlines()** - Read the output of the EVM. It will return a list of strings, one for each line. This will timeout and return after *timeout=1* seconds, given in the Evmmsg() method. It will also internally store the list of strings.

	evm_output = dev1.readlines()   or   dev1.readlines() #to just use internally stored list output
    
**5. printlines(list read_list=[])** - Print out a list of strings returned by readlines(), or call on it's own to print out the internally stored list from the last readlines().

	dev1.printlines(evm_output)   or   dev1.printlines() #to print internally stored list from last readlines()
    
**6. msg(str string)** - Print a message to console appended with the serial name.

	dev1.msg('Hello world')    #prints '/dev/ttyUSB1: Hello world'
    
**7. match(str to_match, list evm_output=[])** - Returns the line which _to_match_ was found in in list _evm_output_ (which is also True). Passing a list is optional, and if not passed it will parse the last read output from readlines(). Can be used for parsing output for conditionals. Returns False if it is not found. This is case sensitive.

	if dev1.match('BOOT COMPLETE'):
    	    print('Boot Completed')

**8. wait_for_msg(str msg, int timeout=60, int debug=0)** - This will monitor the output and wait for string 'msg' to appear, returning True, otherwise returns False. Has a default monitor time of 60 seconds, and debugging can be enabled to see the output which is being monitored.

	if evm1arm.wait_for_msg('Log-in'):
	    print('At log-in prompt')
	    
**9. clear_input()** - Clears the input buffer.

	evm1arm.clear_input()
