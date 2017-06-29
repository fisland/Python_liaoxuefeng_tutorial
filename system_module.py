# Datetime
from datetime import datetime

# 获取当前
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015,4,19,12,20)
print(dt)

# Datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为Datetime
timestamp1 = 1429417211.0
dt1 = datetime.fromtimestamp(timestamp1)
dt1_utc = datetime.utcfromtimestamp(timestamp1)
print(dt1)
print(dt1_utc)
# 本地时间

# str转换为datetime
cday = datetime.strptime('2017/06/29 18:00:00', '%Y/%m/%d %H:%M:%S')
print(cday)
# Datetime转换为str
print(cday.strftime('%Y/%m/%d %H:%M:%S'))

# datetime加减
# 需要引入timedelta类
from datetime import timedelta
print('now->>>>>>>>', now)
time = now + timedelta(hours = 2)
print(time)
# 本地时间转换为UTC时间  
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
print(now)
dt2 = now.replace(tzinfo=tz_utc_8)
print(dt2)
# 时区转化
# 需要的时候再看吧

# 二 collections

# 1. namedtuple
# 相当于swift里面的typelias
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.y)
