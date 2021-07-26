#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
import time
import winsound

print("current time:",time.strftime("%H:%M:%S"))
alarm_time=input("Alarm time:")
alarm_hms=alarm_time.split(':')
if len(alarm_hms)==3 and 0<=int(alarm_hms[0]) \
        and 0<=int(alarm_hms[1]) and 0<=int(alarm_hms[2]):
    time.sleep(int(alarm_hms[0])* 60 * 60
               + int(alarm_hms[1]) * 60 + int(alarm_hms[2]))
    for i in range(1, 10):
        winsound.Beep(i * 100, 200)
else:
    print("There is an error in the entered alarm time display.")
