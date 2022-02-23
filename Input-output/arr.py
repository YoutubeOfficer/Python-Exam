
n = int(input())
s = list(map(int, input().split()))
A = range(1,n+1)
n1 = len(A)
n2 = len(s)

if 1<=n<=250 and n1 == n2:
  for i in A:
      print(i, end=' ')
else :
  print("값오류")