import sys

def orderDatas(squares):
  for j in range(len(squares) - 1):
      for i in range(len(squares) - j - 1):
        if squares[i] > squares[i+1]:
          value = squares[i]
          squares[i] = squares[i+1]
          squares[i + 1] = value
  return squares

s = 5
print('Ingrese el arreglo en el siguiente formato: {"array": [-6, -5, 0, 5, 6]}')
datas = input()
if datas:
  try:
    data = eval(datas)
    data = [int(x) for x in data.get("array")]
  except:
    print("el formato ingresado no es correcto")
    sys.exit()
    
  squares = [x*x for x in data if x*x in range(0, int(f"{s}{s}"))]
  squares = orderDatas(squares)
  print(squares)
 
else:
  print("El arreglo no cuenta con datos")
