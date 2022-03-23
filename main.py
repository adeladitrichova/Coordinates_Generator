#verze s generatorem

from generator import next_point
from generator import get_all_points
import math
first = 0
bodiky = []
bod = next_point()
bod2 = 0 

while first != bod: #while opakuje dokud plati podminka
  if first == 0: 
    first = bod 
  bod2 = bod
  bod = next_point()
  
  if first != 0:
    bodiky.append((round((math.sqrt(((bod2[0]-bod[0])**2)+((bod2[1]-bod[1])**2)))*100))/100)
    print("bod1:", bod)
    print("bod2:", bod2)
    print("soucet:", bodiky)
print("Celkový součet:",(round(100*(sum(bodiky))))/100)

#-------------------------------------------------------------

#verze bez generatoru

import random
import math
soucet_usecek = 0
ab = []
pocet_vrcholu = random.randint(0, 50) #random pocet vrcholu 
print("Úsečky:")
for i in range(pocet_vrcholu):
    A = [random.randint(0, 50),random.randint(0, 50)] #tohle je jakoze A
    B = [random.randint(0, 50),random.randint(0, 50)] #to je jako B, akorat ze nevim
    ab.append((round((math.sqrt(((B[0]-A[0])**2)+((B[1]-A[1])**2)))*100))/100)
    print(f"{i+1}. {ab[i]}")
print("Celkový součet:",(round(100*(sum(ab))))/100)