import datetime
time1=datetime.datetime.now()
time2=time1+datetime.timedelta(0,5)
print("Current Time:",time1.time())
print("5 sec after current time",time2.time())
