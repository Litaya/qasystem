# from src.Helper.Reader import Reader
#
# Reader.readAllWordEmbeddings()

file = open('test.bin', 'rb')

seq = b''
while 1:
    b = file.read(1)
    if b == b'':
        break
    seq += b

print(seq.decode())
