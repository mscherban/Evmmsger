import serial
import time

class Evmmsg():
    def __init__(self, name, baudrate=115200, timeout=1, callme=''):
        self.dev = serial.Serial(name, baudrate, timeout=timeout)
        if not callme:
            self.name = name
        else:
            self.name = callme
        self.read_list = ['', b'Do', b'a', b'read', b'first']
        self.read_line = 'empty'

    def close(self):
        self.dev.close()

    def write(self, string_to_send, end='\r\n'):
        string_to_send += end
        self.dev.write(bytes(string_to_send, encoding='ascii'))

    def readlines(self):
        self.read_list = ['', b'Nothing', b'read.']
        self.read_list = self.dev.readlines()
        return self.read_list

    def readline(self):
        self.read_line = self.dev.readline().decode('utf-8')
        return self.read_line

    def msg(self, string):
        print(self.name + ': ' + string)

    def printlines(self, evm_output=[]):
        if not evm_output:
            evm_output = self.read_list
        for i in evm_output[1:]:
            print(self.name + ':', '|  ', i.decode('utf-8').rstrip('\r\n'))

    def match_lines(self, to_match, evm_output=[]):
        if not evm_output:
            evm_output = self.read_list
        for i in evm_output[1:]:
            if to_match in i.decode('utf-8'):
                return i.decode('utf-8')
        else:
            return False

    def match_line(self, to_match, evm_output=''):
        if not evm_output:
            evm_output = self.read_line
        if to_match in evm_output:
            return True
        else:
            return False

    def wait_for_msg(self, msg, timeout=60, debug=0):
        t = 0
        tstamp0 = int(time.time())
        #Dummy read, since input is usually first line in output stream.
        line = self.dev.readline() 
        while t < timeout:
            line = self.dev.readline().decode('utf-8')
            if debug:
                print(line.rstrip())
            if msg in line:
                return True
            t = int(time.time()) - tstamp0
        else:
            return False
        

    def clear_input(self):
        self.dev.reset_input_buffer()

    def __del__(self):
        self.dev.close()

