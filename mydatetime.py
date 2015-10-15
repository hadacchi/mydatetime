from datetime import datetime,timedelta
import numpy

'''
-----------------------------------------------------------------
 mydatetime v0.2  for python
     Copyright (c) 2015 hadacchi
-----------------------------------------------------------------

*** This script requires numpy, i.e. numerical python ***

This script converts from/into date into/from serial date.
MS Excel counts 1900/2/29 (ref. Microsoft Help & Support No. 214019),
but python doesn't count. Thus, return value from this script
`toSerial()' is equals only after 1900/3/1

If you need valid serial date, change base date `__ZERODATE'
from (datetime.datetime(1970,1,1),25569)
to (datetime.datetime(1900,1,1),1)
'''

class mydatetime(datetime):
    ## base date
    # to identify Excels
    __ZERODATE=(datetime(1970,1,1,0,0,0,0),25569)
    # to return valid serial date
    #__ZERODATE=(datetime(1900,1,1,0,0,0,0),1)

    ## expression for milliseconds
    __MILLIFMT='%u'

    def __init__(self,year,month,day,hour=0,minute=0,second=0,microsecond=0,tzinfo=0):
        '''constructor'''
        # call parent's constructor
        super(mydatetime,self).__init__(
            year,month,day,hour,
            minute,second,microsecond,tzinfo
            )

    def __sub__(self,t):
        # if return value is <type 'timedelta'>
        if t.__class__ == self.__class__ or \
           t.__class__ == self.__ZERODATE[0].__class__:
            return super(mydatetime,self).__sub__(self,t)
        # else (mydatetime-timedelta) should be mydatetime
        else:
            tmp = super(mydatetime,self).__sub__(t)
            return self.__class__(
                tmp.year,tmp.month,tmp.day,tmp.hour,
                tmp.minute,tmp.second,tmp.microsecond,tmp.tzinfo
                )

    def __add__(self,t):
        # if return value is <type 'timedelta'>
        if t.__class__ == self.__class__ or \
           t.__class__ == self.__ZERODATE[0].__class__:
            return datetime.__add__(self,t)
        # else (mydatetime-timedelta) should be mydatetime
        else:
            tmp = super(mydatetime,self).__add__(self,t)
            return self.__class__(
                tmp.year,tmp.month,tmp.day,tmp.hour,
                tmp.minute,tmp.second,tmp.microsecond,tmp.tzinfo
                )

    def strftime(self,fmt):
        '''milliseconds (output by %u) is implemented'''
        tmp=[]
        for i in fmt.split('%%'):
            tmp.append(('%06d'%self.microsecond)[:3]\
                       .join(i.split(self.__MILLIFMT)))
        return super(mydatetime,self).strftime(self,'%%'.join(tmp))

    def toSerial(self):
        '''return serial date'''
        tmp=self-self.__ZERODATE[0]
        serial_val=self.__ZERODATE[1]+tmp.days
        serial_val=serial_val+float(tmp.seconds)/24/3600\
                    +float(tmp.microseconds)/24/3600/1000000
        return serial_val

    @staticmethod
    def fromTuple(d,t=(0,0,0)):
        '''d=(year,month,day),t=(hour,min,sec),sec can be float'''
        if type(t[2]) is float: f=int(t[2]*1000000-int(t[2])*1000000)
        elif len(t)>=4: f=t[3]
        else: f=0
        # call parent's constructor
        return mydatetime(d[0],d[1],d[2],t[0],t[1],int(t[2]),f)

    @staticmethod
    def fromSerial(val):
        '''return mydatetime from serial value'''
        tmp=val-mydatetime._mydatetime__ZERODATE[1]
        day=int(tmp)
        sec=round((tmp-day)*24*3600,3)
        dt=timedelta(days=day,seconds=sec)
        tmp=mydatetime._mydatetime__ZERODATE[0]+dt
        # call parent's constructor
        return mydatetime(tmp.year,tmp.month,tmp.day,
                          tmp.hour,tmp.minute,tmp.second,tmp.microsecond,tmp.tzinfo)

    @staticmethod
    def Serial2Sec(val,comp=False):
        '''if comp is True, return complete seconds(LongInt) from ZERODATE '''
        if type(val)!=numpy.ndarray:
            if type(val)!=type([]): numpy.array([val])
            else: numpy.array(val)
        else: True
        c=24*3600
        if not comp: return numpy.round((val-numpy.array(val,dtype=int))*c,3)
        else:
            val=val-mydatetime._mydatetime__ZERODATE[1]
            return numpy.round((val-numpy.array(val,dtype=int))*c+numpy.array(val,dtype=int)*c,3)
        if len(ret)==1: return ret[0]
        else: return ret

