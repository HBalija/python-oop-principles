#!/usr/bin/python3

from io import StringIO


class WriteMyStuff:
    """
    Simple class using composition (write() method called).
    """

    def __init__(self, writer):
        self.writer = writer

    def write(self, text):
        self.writer.write(text)


# example

fh = open('text.txt', 'w')
text_writer = WriteMyStuff(fh)
text_writer.write('some text')

buff = StringIO()
buff_writer = WriteMyStuff(buff)
buff_writer.write('some text')

print('Buffer object data:', buff.getvalue())  # some text
