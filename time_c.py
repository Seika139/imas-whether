import datetime as dt
xd = dt.datetime.today()
xdj = xd - dt.timedelta(hours=9) #Herokuでは時間帯がUTCなので9時間前にずらす
xh = xd.hour
xhj = xdj.hour
print("今は",xh,"時")
print("９時間前は",xhj,"時")
