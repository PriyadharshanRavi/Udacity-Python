#Take all the datatypes and convert it to bytes(1,0)

from struct import *

#Store as bytes data 
packed_data = pack('iif', 11,19,19.95) #pack comtains the (fmt,value) i is for integer and f is for float
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))


# To get the byte data back to normal

unpack_data = unpack('iif', packed_data)

print(unpack_data)
print(unpack('iif', b'\x0b\x00\x00\x00\x13\x00\x00\x00\x9a\x99\x9fA'))
#works both ways 