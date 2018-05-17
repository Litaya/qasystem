import struct


class BinaryReader:

    @staticmethod
    def readStringWithoutBlank(f):
        try:
            seq = bytes()
            b = f.read(1)
            while 1:
                if b == b' ' or b == b'\n' or b == b'\t' or b == b'':
                    break
                seq += b
                b = f.read(1)
            return bytes.decode(seq)
        except EOFError:
            pass

    @staticmethod
    def readStringWithBlank(f):
        try:
            seq = bytes()
            b = f.read(1)
            while 1:
                if b == b'\t' or b == b'\n' or b == b'':
                    break
                seq += b
                b = f.read(1)
            # print(seq)
            return bytes.decode(seq)
        except EOFError:
            pass

    @staticmethod
    def readFloat(f):
        try:
            b = f.read(4)
            return struct.unpack('f', b)[0]
        except:
            pass
