#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta, timezone

now = datetime.now();
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(now);
print(dt);

dtime = dt.timestamp()
print(dtime);
print(datetime.fromtimestamp(dtime));  ## 北京时间
print(datetime.utcfromtimestamp(dtime));   ## 格林尼治时间


cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now();
print(now.strftime('%a, %b %d %H:%M'));

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  ## 得到格林尼治时间
print(utc_dt)