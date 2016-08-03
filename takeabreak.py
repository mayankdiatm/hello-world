#!/usr/bin/python
import time
import webbrowser

a = time.strftime("%I:%M:%S")
print(time.strftime(a))
break_count=4
count =0
while(count<break_count):
    print("====== Current Time When Program Started is ======"+ time.ctime())
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/")
    count = count +1

print "Good Bye!"




