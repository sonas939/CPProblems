def time_calculation(startTime, endTime, base):
    if endTime < startTime:
        return [base-startTime+endTime, False]
    else:
        return [endTime-startTime, True]

start = input().split(":")
end = input().split(":")
start = [int(i) for i in start]
end = [int(i) for i in end]
seconds = time_calculation(start[2],end[2],60)
minutes = time_calculation(start[1],end[1],60)
if (not seconds[1]):
    minutes[0] -= 1
hours = time_calculation(start[0],end[0],24)
if (not minutes[1]):
    hours[0] -= 1
if (minutes[0] == -1):
    hours[0] -= 1
    minutes[0] = 59
if (hours[0] == -1):
    hours[0] = 23
if (hours[0] == 0 and minutes[0] == 0 and seconds[0] == 0):
    hours[0] = 24
print(f'{hours[0]:02d}',":",f'{minutes[0]:02d}',":",f'{seconds[0]:02d}',sep="")
