
'''

import datetime

timestamp = 1463460958000

datetimeobj = datetime.datetime.fromtimestamp(timestamp / 1000)
print(datetimeobj)
a = str(datetimeobj)

print(a)
print(a[0:10])


start = '2019-12-13T17:45:00'

a = start[0:10] + " " + start[11:19]
print(a)

now = datetime.datetime.now()
print(now)
print(now.timestamp())

datetime.timedelta(hours="9")
b = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
print(b)
print(b.timestamp())

'''


