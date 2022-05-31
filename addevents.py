import datetime

now = datetime.datetime.now()
text = now.strftime("%m/%d/%Y, %H:%M:%S")

f = open("dfile/events.txt", "a")
f.write(text)
f.close()

#open and read the file after the appending:
f = open("dfile/events.txt", "r")
print(f.read())