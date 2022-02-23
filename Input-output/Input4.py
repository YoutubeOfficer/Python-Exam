# A,B = map(int, input().split()) #두수비교

# if(-10000<= A and B <= 10000):
#   if(A>=B):
#     if(A>B):
#       print(">")
#     else:
#       print("==")
#   else:
#     print("<")
# else:
#   print("값오류")

# A = int(input()) #학점계산

# if (0<=A<= 100):
#   if(90<=A):
#     print("A")
#   else:
#     if(80<=A):
#       print("B")
#     else:
#       if(70<=A):
#         print("C")
#       else:
#         if(60<=A):
#           print("D")
#         else:
#           print("F")
# else:
#   print("값오류")

A = int(input())

if(1<=A<=4000):
  if((A%4 == 0 and A%100 ==0) or A%400 ==0  ):
    print("1")
  else:
    print("0")
else:
  print("값오류")