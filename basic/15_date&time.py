import datetime as dt

#datetime class
startTime = dt.datetime.now()
#dt(datetime) : library, datetime : class, now() : method
print(startTime, type(startTime))
#2023-02-04 15:07:32.139172 <class 'datetime.datetime'>

startTime = startTime.replace(year = 2017, month = 2, day = 1)
print(startTime) #2017-02-01 15:08:34.029408

startTime = dt.datetime(2024, 1, 1)
print(startTime) #2024-01-01 00:00:00

#timedelta class
howLong = startTime - dt.datetime.now()
print(howLong, type(howLong))
#330 days, 8:48:56.116210 <class 'datetime.timedelta'>
print(howLong.days, howLong.seconds) #330 31672

after100 = dt.timedelta(days = 100)
print(dt.datetime.now() + after100)
#2023-05-15 15:18:31.229563

before100 = dt.timedelta(days = -100)
print(dt.datetime.now() + before100)
#2022-10-27 15:20:15.826593

tomorrow = dt.datetime.now().replace(hour = 9, minute = 0, second = 0) + dt.timedelta(days = 1)
print(tomorrow) #2023-02-05 09:00:00.761099