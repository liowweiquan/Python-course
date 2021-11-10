>>> t.localtime()
time.struct_time(tm_year=2021, tm_mon=7, tm_mday=16, tm_hour=1, tm_min=10, tm_sec=58, tm_wday=4, tm_yday=197, tm_isdst=0)
>>> time_now = t.localtime()
>>> print("Transaction completed at" , str(time_now.tm_hour)+ "h" + str(time_now.tm_min)+ "min")
Transaction completed at 1h11min
>>> t.time()
1626369187.985805
>>> t.time()
1626369192.269651
>>> time_now = t.time()
>>> delivery_time = time_now + (86400*7)
>>> t.localtime(delivery_time)
time.struct_time(tm_year=2021, tm_mon=7, tm_mday=23, tm_hour=1, tm_min=14, tm_sec=2, tm_wday=4, tm_yday=204, tm_isdst=0)
>>> t.sleep(5)
