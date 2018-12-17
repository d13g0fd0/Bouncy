def IsBouncy(number):
  isIncreasing = None
  isBouncy = 0
  numberArray = list(str(number))

  for pos in range(len(numberArray)-1):
    if isIncreasing is None:
      if int(numberArray[pos]) < int(numberArray[pos+1]):
        isIncreasing = True
      elif int(numberArray[pos]) > int(numberArray[pos+1]):
        isIncreasing = False
    else:
      if int(numberArray[pos]) < int(numberArray[pos+1]) and isIncreasing == False:
        isBouncy = 1
        break
      elif int(numberArray[pos]) > int(numberArray[pos+1]) and isIncreasing == True:
        isBouncy = 1
        break
  return isBouncy

def FindLeastNumber(goalPercentage):
  number = 100
  bouncies = 0
  percentage = 0

  try:
    if int(goalPercentage) >= 0 and int(goalPercentage) < 100:
      while True:
        if IsBouncy(number):
          bouncies += 1
        percentage =round(float(bouncies)/float(number)*100,1)
        if percentage == goalPercentage:
          break
        number += 1
        if percentage == 99:
          print ('Not found')
          number = -1
          break
    else:
      print('Number must be between 0 and 99')
      number = -1
  except:
    print('Number must be between 0 and 99')
    number = -1

  return number

print ('The least number is: ' + str(FindLeastNumber(99)))