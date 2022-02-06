import os
from datetime import datetime , timedelta


__ALL__ = [ "getfileName" , "uploadDate" , "expiryDate" ]



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

    if  day == None:
        day = 7
    
    if  day < 1:
        day = 1

    expD = (datetime.today() + timedelta(day)).strftime(__FMT)

    return expD


