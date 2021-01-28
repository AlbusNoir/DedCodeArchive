#sec min hour day blahblah converter :D v1.0


time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("Day:Hour:Minute:Second-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
