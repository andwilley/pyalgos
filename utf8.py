class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return False
        i = 0
        while i < len(data):
            if data[i] >> 7 == 0:
                i += 1
            elif data[i] >> 5 == 0b110:
                if not self.check_bytes(data[i+1:i+2], 1):
                    return False
                i += 2
            elif data[i] >> 4 == 0b1110:
                if not self.check_bytes(data[i+1:i+3], 2):
                    return False
                i += 3
            elif data[i] >> 3 == 0b11110:
                if not self.check_bytes(data[i+1:i+4], 3):
                    return False
                i += 4
            else:
                return False
        return True

    @staticmethod
    def check_bytes(bytes_list, count):
        if len(bytes_list) != count:
            return False
        for byte in bytes_list:
            if byte >> 6 != 0b10:
                print(byte)
                return False
        return True