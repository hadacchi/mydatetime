# mydatetime
 This script is convert from/into date into/from serial date of Excel.
 Excels count 1900/2/29 (ref. Microsoft Help & Support No. 214019),
 but python don't count. Thus, return value from this script.
 `toSerial()' is equals only after 1900/3/1.

 if you need valid serial date, change base date `__ZERODATE'
 from (datetime.datetime(1970,1,1),25569) to (datetime.datetime(1900,1,1),1).
