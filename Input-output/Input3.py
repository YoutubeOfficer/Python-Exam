A,B,C = map(int, input().split())

while (2 <= A and B and C <=10000):
  print((A+B)%C)
  print(((A%C) + (B%C))%C) 
  print((A*B)%C)
  print(((A%C) * (B%C))%C)
  break
else:
    print("에러")
    
  
