# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

S = "01:22:21"
T = "22:22:23"

def increase(count):
    HH = 0
    MM = 0
    time_array = count.split(":")
    if int(time_array[-1]) + 1 == 60:
        MM = 1
        time_array[-1] = 0
    else:
        time_array[-1] = int(time_array[-1]) + 1
    if MM == 1:
        if int(time_array[-2]) + 1 == 60:
            HH = 1
            time_array[-2] = 0
        else:
            time_array[-2] = int(time_array[-2]) + 1
    if HH == 1:
        if int(time_array[-3]) + 1 == 25:
            HH = 1
            time_array[-3] = 0
        else:
            time_array[-3] = int(time_array[-3]) + 1
    HH = "%02d" % int(time_array[-3])
    MM = "%02d" % int(time_array[-2])
    SS = "%02d" % int(time_array[-1])
    return "%s:%s:%s" % (HH, MM, SS)

def counter(S, T):
    counts = 0
    start = 0
    end = 0
    start_array = S.split(":")
    end_array = T.split(":")
    start = int(int(int(start_array[0])*60*60) + int(int(start_array[1])*60) + int(start_array[2]))
    end = int(int(int(end_array[0])*60*60) + int(int(end_array[1])*60) + int(end_array[2]))
    counts = end - start + 1
    return counts

def compare(courrent):
    diff_digts = 0
    if courrent.find("1") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("2") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("3") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("4") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("5") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("6") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("7") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("8") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("9") != -1:
        diff_digts = diff_digts + 1
    if courrent.find("0") != -1:
        diff_digts = diff_digts + 1
    return diff_digts

def solution(S, T):
    interest_points = 0
    for i in range(counter(S, T)):
        if compare(S) < 3:
            interest_points = interest_points + 1
        S = increase(S)
    return interest_points



print solution(S, T)
