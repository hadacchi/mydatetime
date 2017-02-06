import mydatetime.mydatetime as mdt
import datetime

serial = 42758.4166666666642413474619388580322265625
mdt_fromymdh = mdt.mydatetime(2017,1,23,10)
mdt_fromserial = mdt.mydatetime.fromSerial(serial)
mdt_now = mdt.mydatetime.now()
dt_now = datetime.datetime.now()
dt_fromymdh = datetime.datetime(2017,1,23,10)
#print('serial date `{serial:.40f}` makes'.format(serial=serial))
#print('    mydatetime class `{mdt}`.'.format(mdt=dt_fromserial))
#print('mydatetime class `{mdt}` makes'.format(mdt=dt_fromymdh))
#print('    serial `{serial:.40f}`.'.format(serial=dt_fromymdh.toSerial()))

mdt_timedelta = mdt_now-mdt_fromserial
dt_timedelta = dt_now-dt_fromymdh

print('serial is `{s:.40f}`'.format(s=serial))
print('created mydatetime class is `{dt}`'.format(dt=mdt_fromserial))
print('created now() is `{dt}`'.format(dt=mdt_now))
print('created now() is mydatetime class ? => {res}'.format(res=str(type(mdt_now)) == "<class 'mydatetime.mydatetime.mydatetime'>"))
print('from serial == from yyyy,mm,dd,hh ? => {result}'.format(serial=serial,result=mdt_fromserial == mdt_fromymdh))
print('now - created mydatetime class is {res}'.format(res=mdt_timedelta))
print('datetime version is {res}'.format(res=dt_timedelta))
print('datetime + mdt_timedelta == mdt_now ? => {res}'.format(res=mdt_now==dt_fromymdh + mdt_timedelta))
print('mydatetime + dt_timedelta == dt_now ? => {res}'.format(res=dt_now==mdt_fromymdh + dt_timedelta))

