import math


def minute_scale(minute):
  minutescalesmall = 0
  minutescalelarge = 0
  if minute <= 60:
    minutescalesmall = minute / 60
    return float(minutescalesmall)
  if minute > 60:
    minutescalelarge = (minute % 60) / 100
    return float(minutescalelarge)


def sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP):
  slept = 0
  if (hourS <= hourW < 12 and (sAP == wAP)) or (sAP != wAP and hourW == 12):
    slept = (hourW + minute_scale(minuteW)) - (hourS + minute_scale(minuteS))
  if sAP == wAP and hourS == 12:
    hourS -= 12
    slept = (hourW + minute_scale(minuteW)) - (hourS + minute_scale(minuteS))
  if (sAP != wAP and hourW != 12) or (sAP == wAP and hourW == 12):
    hourW += 12
    slept = (hourW + minute_scale(minuteW)) - (hourS + minute_scale(minuteS))
  return float(slept)


def user_sleep(amount):
  sleptString = str(amount)
  sleptList = sleptString.split(".")
  sleptHours = sleptList[0]
  sleptMinutes = round(60 * float("." + sleptList[1]))
  return "You can sleep for " + str(sleptHours) + " hour(s) and " + str(
      round(sleptMinutes, 2)) + " minute(s)."


def cycle(hourS, minuteS, sAP, hourW, minuteW, wAP):
  cycleNum = math.floor(
      sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) / 1.5)
  return cycleNum


def cycle_time(hourS, minuteS, sAP, hourW, minuteW, wAP):
  cycleStr = ""
  code = "\n"
  temp = hourS
  temp2 = minuteS
  if sAP == wAP and hourS != 12:
    for i in range(int((cycle(hourS, minuteS, sAP, hourW, minuteW, wAP)))):
      cycleStart = temp + minute_scale(temp2)
      cycleEndFl = cycleStart + 1.5
      cycleEndH = math.floor(cycleEndFl)
      cycleEndM = int((60 * (cycleEndFl - cycleEndH)) % 60)
      cycleStr += "Cycle " + str(i + 1) + " finishes at " + str(cycleEndH) + ":" + str(cycleEndM).zfill(2) + " " + wAP + ". "
      temp = cycleEndH
      temp2 = cycleEndM
  if (sAP == "PM" and wAP == "AM") or (sAP == wAP == "AM" and hourS == 12):
    for i in range(
        int(math.floor(cycle(hourS, minuteS, sAP, hourW, minuteW, wAP)))):
      cycleStart = temp + minute_scale(temp2)
      cycleEndFl = cycleStart + 1.5
      cycleEndH = math.floor(cycleEndFl)
      cycleEndM = int((60 * (cycleEndFl - cycleEndH)) % 60)
      if cycleEndH >= 13 or (cycleEndH == 12 and cycleEndM >= 0):
        cycleEndHChange = 12
        if cycleEndH >= 13:
          cycleEndHChange = cycleEndH - 12
        cycleEndMFinal = str(cycleEndM).zfill(2) + " AM"
        cycleStr += "Cycle " + str(i + 1) + " finishes at " + str(cycleEndHChange) + ":" + cycleEndMFinal + ". "
      if cycleEndH < 12:
        cycleStr += "Cycle " + str(i + 1) + " finishes at " + str(cycleEndH) + ":" + str(cycleEndM).zfill(2) + " PM. "
      temp = cycleEndH
      temp2 = cycleEndM
  if sAP == "AM" and wAP == "PM":
    for i in range(
        int(math.floor(cycle(hourS, minuteS, sAP, hourW, minuteW, wAP)))):
      cycleStart = temp + minute_scale(temp2)
      cycleEndFl = cycleStart + 1.5
      cycleEndH = math.floor(cycleEndFl)
      cycleEndM = int((60 * (cycleEndFl - cycleEndH)) % 60)
      if cycleEndH >= 13 or (cycleEndH == 12 and cycleEndM >= 0):
        cycleEndHChange = 12
        if cycleEndH >= 13:
          cycleEndHChange = cycleEndH - 12
        cycleEndMFinal = str(cycleEndM).zfill(2) + " PM"
        cycleStr += "Cycle " + str(i + 1) + " finishes at " + str(cycleEndHChange) + ":" + cycleEndMFinal + ". "
      else:
        cycleStr += "Cycle " + str(i + 1) + " finishes at " + str(cycleEndH) + ":" + str(cycleEndM).zfill(2) + " " + sAP + ". "
      temp = cycleEndH
      temp2 = cycleEndM
  return cycleStr

ageDict = {"child": 9, "teen": 8, "adult": 7}


def age_rec(old, hourS, minuteS, sAP, hourW, minuteW, wAP):
  if old < 12:
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 9:
      sleepRem = 9 - sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP)
      sleptH = math.floor(sleepRem)
      sleptM = round(60 * (sleepRem % 1))
      return "You should be sleeping " + str(sleptH) + " hour(s) and " + str(sleptM) + " minute(s) more. It's past your bedtime!"
    if 9 <= sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 12:
      return "Congratulations on getting enough sleep! You're better than the rest of us."
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) >= 12:
      return "... Don't you have homework to do?"
  if 12 <= old <= 18:
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 8:
      sleepRem = 8 - sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP)
      sleptH = math.floor(sleepRem)
      sleptM = round(60 * (sleepRem % 1))
      return "You should be sleeping " + str(sleptH) + " hour(s) and " + str(sleptM) + " minute(s) more. Go to bed!"
    if 8 <= sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 11:
      return "Congratulations on getting enough sleep! You're better than the rest of us."
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) >= 11:
      return "Come on, stay up a little later. You're wasting your youth!"
  if old >= 19:
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 7:
      sleepRem = 7 - sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP)
      sleptH = math.floor(sleepRem)
      sleptM = round(60 * (sleepRem % 1))
      return "You should be sleeping " + str(sleptH) + " hour(s) and " + str(sleptM) + " minute(s) more. Go to bed!"
    if 7 <= sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) < 11:
      return "Congratulations on getting enough sleep! You're a well-adjusted adult."
    if sleep_calc(hourS, minuteS, sAP, hourW, minuteW, wAP) >= 11:
      return "Just so you know, oversleeping raises the risk of chronic diseases in adults..."

# sleephour = input("Sleep Hour: ")
# sleepminute = input("Sleep Minute: ")
# sleepAP = input("AM or PM: ")
# wakehour = input("Wake Hour: ")
# wakeminute = input("Wake Minute: ")
# wakeAP = input("AM or PM: ")
# age = input("Age: ")
# print(
#     user_sleep(
#         sleep_calc(int(sleephour), int(sleepminute), sleepAP, int(wakehour),
#                    int(wakeminute), wakeAP)))
# print("You can undergo at most " + str(
#     cycle(int(sleephour), int(sleepminute), sleepAP, int(wakehour),
#           int(wakeminute), wakeAP)) + " sleep cycles.")
# print(
#     cycle_time(int(sleephour), int(sleepminute), sleepAP, int(wakehour),
#                int(wakeminute), wakeAP))
# print(
#     age_rec(int(age), int(sleephour), int(sleepminute), sleepAP, int(wakehour),
#             int(wakeminute), wakeAP))
