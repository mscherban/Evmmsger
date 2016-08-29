import serial

class Evmmsg():
    def __init__(self, name, baudrate=115200, timeout=1):
        self.dev = serial.Serial(name, baudrate, timeout=timeout)
        self.name = name
        self.read_list = ['', b'Do', b'a', b'read', b'first']

    def close(self):
        self.dev.close()

    def write(self, string_to_send, end='\r\n'):
        string_to_send += end
        self.dev.write(bytes(string_to_send, encoding='ascii'))

    def readlines(self):
        self.read_list = ['', b'Nothing', b'read.']
        self.read_list = self.dev.readlines()
        return self.read_list

    def msg(self, string):
        print(self.name + ': ' + string)

    def printlines(self, evm_output=[]):
        if not evm_output:
            evm_output = self.read_list
        for i in evm_output[1:]:
            print(self.name + ':', '|  ', i.decode('utf-8').rstrip('\r\n'))

    def match(self, to_match, evm_output=[]):
        if not evm_output:
            evm_output = self.read_list
        for i in evm_output[1:]:
            if to_match in i.decode('utf-8'):
                return i.decode('utf-8')
        else:
            return False








