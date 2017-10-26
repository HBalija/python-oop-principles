#!/usr/bin/python3

from abc import ABC, abstractmethod
from datetime import datetime


class MainClass(ABC):
    """
    Simple class using inheritence, method overload, abstract methods.
    """

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def write(self, data):
        with open(self.file, 'a') as fh:
            fh.write(data + '\n')


class LogFile(MainClass):

    def write(self, text):
        data = '{0} {1}'.format(
            datetime.now().strftime('%Y-%m-%d %H:%M'), text)
        super().write(data)


class AgreementPass(MainClass):

    def write(self, data):
        pass


class AgreementFail(MainClass):
    pass


class DelimFile(MainClass):

    def __init__(self, file, delimiter):
        super().__init__(file)
        self.delimiter = delimiter

    def write(self, text):
        data = self.delimiter.join(text)
        super().write(data)


# example

log_file = LogFile('log.txt')

delimeter_file = DelimFile('text.csv', ',')

# instance is created but doesn't do much since we pass write() method
agree = AgreementPass('pass.txt')


"""
instance cannot be instanciated.
Abstract class MainClass requires write() method - TypeError raised.
"""
# fail = AgreementFail('fail.txt')


log_file.write('log message')
log_file.write('another log message')

delimeter_file.write(['a', 'b', 'c', 'd'])
delimeter_file.write(['1', '2', '3', '4'])
