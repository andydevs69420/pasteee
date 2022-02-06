import os
from cryptography.fernet import Fernet
from datetime import datetime , timedelta


__ALL__ = [ "hash" , "getfileName" , "uploadDate" , "expiryDate" ]

# GLOBAL KEY
__KEY = b'CQ4PoqKT5LLQA1COk0mV0SINOqeuIrUhzNUo2K1xBG8='

def hash(_str:str,ishash:bool=True, key:bytes=__KEY):

    if  type(ishash) != bool:
        ishash = True

    if  len(key) <= 0 or type(key) != bytes:
        key = __KEY

    gkey = Fernet(key)

    if  ishash:
        return gkey.encrypt(_str.encode()).decode()
    
    return gkey.decrypt(_str.encode()).decode()

# extract filename only
def getFileName(path:str):
    return os.path.basename(path).__str__()

# use format mm-dd-yyyy
# private! do not include in __ALL__
__FMT = "%m-%d-%Y"

def uploadDate():

    # use today | now
    updD = datetime.today().strftime(__FMT)

    return updD

# set 7 days expiration
def expiryDate(day:int|None=7):

    if  day == None or type(day) != int:
        day = 7
    
    if  day < 1:
        day = 1

    expD = (datetime.today() + timedelta(day)).strftime(__FMT)

    return expD


