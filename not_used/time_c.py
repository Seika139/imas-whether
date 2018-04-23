import datetime as dt
xd = dt.datetime.today()
xdj = xd + dt.timedelta(hours=9) #Herokuでは時間帯がUTCなので9時間後にずらす
xh = xd.hour
xhj = xdj.hour
print("今は",xh,"時")
print("９時間後は",xhj,"時")
