import re

def validateDigit(s, array):
    values = []
    for x in array:
        a = (re.sub(f"[^0-{s -1}]", '', x))
        if a:
            values.append(a)
    return values

def reverse(array):
    reversedList = []
    for number in array:
      reversedList = [number] + reversedList
    return reversedList

s = 5
numbers = input()
if numbers:
  datas = numbers.replace("[]","")
  data = datas.split(",")
  values = validateDigit(s,data)
  values = [int(x) for x in values]
  print(reverse(values))
else:
  print("El arreglo no cuenta con datos")