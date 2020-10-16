from datetime import datetime, timedelta
#while function
dt = datetime(2020, 10, 16, 11, 58 , 50)

x=0
while x<10:
    print(dt)
    dt= dt+timedelta(days=14)
    x=x+1



#loop function
mydate = datetime(2020, 10, 17, 12, 15, 50)

for i in range(10):
    print(mydate)
    mydate = mydate + timedelta(days=14)
