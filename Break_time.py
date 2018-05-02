import time
import webbrowser


total_break = 3
break_count = 0
print("this program started on" +time.ctime())
while(break_count < total_break):
    time.sleep(1000)
    print("break time")
    webbrowser.open("https://youtu.be/FzLpP8VBC6E")
    break_count = break_count + 1
