#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
import datetime
def is_leap_year(yy):
    return  yy % 400 == 0 or (yy%100) and yy%4==0

def jetlag(yy, mm, dd, hh, mi, gap): #Function to calculate parallax
    hh +=gap                         #Korea and California time difference
    if hh < 0 :                      #If the time is negative, adjust the date
        dd = dd - 1
        hh += 24
    if dd ==0:                       #When the adjusted date reaches 0, the month is adjusted.
        mm = mm-1
        if mm ==0:                   #If the adjusted month is 0, adjust the year
            mm = 12
            yy -= 1
        if mm in [4, 6, 9, 11]:      #Calculate the last day of the adjusted month
            dd = 30                  #30 days last
        elif mm in [1,3,5,7,8,10,12]:#The last day is the 31st
            dd=31
        else:                        #The leap month needs to be calculated
            if is_leap_year(yy):     #Leap year
                dd = 29
            else:
                dd =28               #If it's not a leap month
    date= "%d/%d/%d %d:%d" % (yy,mm,dd, hh,mi)
    return date
today=datetime.datetime.now()
gap=int(input("Parallax (positive/negative) >>"))
print("Current date and time in Korea:",today.strftime("%Y/%m/%d %H:%M"))

date=jetlag(today.year,today.month,today.day,today.hour,today.minute,gap)
print("California Current Date and Time:",date)