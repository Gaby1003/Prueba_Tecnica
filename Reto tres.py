import itertools
def permutationsSet(coins):
  sums = []
  permutations = []
  for i in range(2,len(coins)+1):
    permutations.extend(list(itertools.combinations(coins, r=i)))
    sums = [sum(x) for x in permutations]
    sums.extend(coins)
    sums.sort()
    set(sums)
  return sums

print('Ingrese las monedas en el siguiente formato: {"coins": [1, 5, 1, 1, 1, 10, 15, 20, 100]}')
coins = input()
if coins:
  coinsInt = eval(coins)
  coinsInt = [int(x) for x in coinsInt.get("coins")]
  sums = permutationsSet(coinsInt)

  s = [x for x in range(1, max(sums)) if x not in sums]
  if s:
    print(min(s))
  else:
    print(max(sums) + 1)
else:
  print("El arreglo no cuenta con datos") 
