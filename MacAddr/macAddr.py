import uuid
import time
def getMacAddr():
    _mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    return ":".join([_mac[e:e+2] for e in range(0,11,2)])

def getMd5Value(string):
    import hashlib
    return hashlib.md5(string.encode('utf-8')).hexdigest()

def getCurrentTime():
    return time.strftime("%Y%m%d")

def createRigsterCode(_macAddr, _startTime, endTime):
    pass
    
    
def getRegisterCode():
    pass

if __name__ == "__main__":

    macAddr = getMacAddr()
    print(macAddr)
    md5Vaule = getMd5Value(macAddr)
    print(md5Vaule)
    print(getCurrentTime())