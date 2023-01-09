def orderDatas(squares):
  for j in range(len(squares) - 1):
      for i in range(len(squares) - j - 1):
        if squares[i] > squares[i+1]:
          value = squares[i]
          squares[i] = squares[i+1]
          squares[i + 1] = value
  return squares

s = 5
datas = input()
if datas:
  data = eval(datas)
  data = [int(x) for x in data.get("array")]
  squares = [x*x for x in data if x*x in range(0, int(f"{s}{s}"))]
  squares = orderDatas(squares)
  print(squares)
  
else:
  print("El arreglo no cuenta con datos")