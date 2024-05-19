# print("Hello World")

# i = "강한친구 대한육군"
# print(i)
# print(i)

# print("\    /\\"'\n'" )  ( ')"'\n'"(  /  )"'\n'" \(__)|")
# print('\n')
# print("|\_/|\n|q p|   /}"'\n''( 0 )"""\\''\n''|"^"`    |''\n'"||_/=\\\__|")

# print("""         ,r'"7""")
# print("""r`-_   ,'  ,/""")
# print(""" \. ". L_r'""")
# print("""   `~\/""")
# print("""      |""")
# print("""      |""")

# T = 10  
# results = [] 

# for t in range(1, T + 1):
#     N = int(input())
#     assert 4 <= N <= 1000

#     n1 = list(map(int, input().split())) 
#     assert len(n1) == N
#     assert all(0 <= n <= 255 for n in n1)
#     assert n1[0] == n1[1] == n1[-1] == n1[-2] == 0

#     result = 0
#     for i in range(2, N-2):
#         high = n1[i-2:i+3] 
#         high.remove(n1[i]) 
#         max2 = max(high)  
#         if n1[i] > max2:  
#             n2 = n1[i] - max2  
#             result += n2  

#     results.append(f"#{t} {result}")

# a = int(input())
# c = 0
# for _ in range(a):
#     b = int(input())
#     result = [[0]*b for _ in range(b)]
#     x, y, count = 0, -1, 1
#     direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
#     d_turn = 0
#     c+=1
#     print(f"#{c}")
#     for i in range(b*b):
#         dx, dy = direction[d_turn]
#         if not (0 <= x + dx < b and 0 <= y + dy < b) or result[x + dx][y + dy] != 0:
#             d_turn = (d_turn + 1) % 4  
#             dx, dy = direction[d_turn]
#         x += dx
#         y += dy
#         result[x][y] = count
#         count += 1

#     for results in result:
#         print(f"{' '.join(map(str, results))}")

# a = 3
# t = 0
# result = 0
# bigmax = 0
# count = 0
# number = 0
# 5
# for _ in range(a):
#     b = int(input())
#     c = list(map(int, input().split()))
#     number +=1
#     assert len(c) == b
#     while c and len(c) > 1 and len(set(c)) > 1 and c != sorted(c, reverse=True):
#         indx = c.index(max(c))
#         if not(max(c) == min(c)) or indx == 0:
#             for i in range(indx):
#                 result += c[i]
#                 count += 1
#             results = max(c)*count-result
#             bigmax += results
#             del c[:indx+1]
#             result = 0
#             count = 0
#         else:
#             print(0)
#     print(f"#{number} {bigmax}")
#     bigmax = 0

# b = 0
# c = 0
# d = 0
# count = 0 
# a=int(input())
# for _ in range(a):
# 	test = list(map(int,input().split()))
# 	t1 = test[0]
# 	t1_d = list(map(int,str(t1)))
# 	count+=1
# 	for i in range(test[1]):
# 		if t1_d != sorted(t1_d,reverse=True):
# 			while max(t1_d[b:]) == t1_d[b]:
# 				b+=1
# 			else:
# 				c = t1_d[b]
# 				if not (t1_d.count(max(t1_d[b:])) + 2 == len(t1_d[b:]) or len(t1_d[b:]) != 3 and t1_d.count(max(t1_d[b:])) > 1 and t1_d[-1] != max(t1_d[b:]) and (t1_d[1] != max(t1_d[b:]))) or test[1] == 1:
# 					if t1_d.count(max(t1_d[b:])) > 1:
# 						back =  len(t1_d[b:]) - 1 - t1_d[::-1].index(max(t1_d[b:]))
# 						d = back
# 						t1_d[b] = max(t1_d[b:])
# 						t1_d[d+b] = c
# 					else:
# 						d = t1_d.index(max(t1_d[b:]))
# 						t1_d[b] = max(t1_d[b:])
# 						t1_d[d] = c
# 				else:
# 					min1 = min(t1_d[:-1])
# 					min2 = t1_d.index(min1) - b
# 					if max(t1_d[b:]) > 1:
# 						max2 = len(t1_d[b:]) - 1 - t1_d[::-1].index(max(t1_d[b:]))
# 						t1_d[min2+b], t1_d[max2+b] = t1_d[max2+b], t1_d[min2+b]
# 		else:
# 			if i < test[1]:
# 				if t1_d.count(i) > 1 or len(set(t1_d)) == len(t1_d):
# 					if t1_d.count(min(t1_d)) == 1:
# 						min1 = t1_d.index(min(t1_d))
# 						t1_d[min1], t1_d[min1-1] = t1_d[min1-1], t1_d[min1]
# 					else:
# 						break
# 			break
# 	for i in t1_d:
# 		result = ''.join(map(str,t1_d))
# 	print(f"#{count} {result}")
# 	b = 0

# a = 10
# for _ in range(a):
#     number = int(input())
#     b = list(map(int, input().split()))
#     c = len(b)
#     maxnumber=0
#     result = []
#     cout= []
#     for i in range(1,101):
#         cout.append(b.count(i))
#     listmax = max(cout)
#     for i in range(len(cout)):
#       if cout[maxnumber] == listmax:
#           result.append(maxnumber+1)
#           maxnumber += 1
#       else:
#           maxnumber += 1
#     print(f"#{number} {max(result)}")

# T = 10
# count = 0
# for i in range(1,T):
#     a = int(input())
#     b = list(map(int, input().split()))
#     for _ in range(a+1):
#         # assert len(b) == 100
#         maxb = max(b)
#         minb = min(b)
#         if maxb - minb > 0:
#             b[b.index(max(b))] -= 1
#             b[b.index(min(b))] += 1
#         else:
#             break
#     b = []
#     result = maxb - minb
#     count += 1
#     print(f"#{count} {result}")

# import heapq
# T = 10
# count = 0
# def dp():
#     test = []
#     heapq.heappush(test, (array[0][0], 0, 0))
#     distance[0][0] = array[0][0]
#     while test:
#         dist, x, y = heapq.heappop(test)
#         if distance[x][y] < dist:
#             continue
#         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < n:
#                 cost = dist + array[nx][ny]
#                 if cost < distance[nx][ny]:
#                     distance[nx][ny] = cost
#                     heapq.heappush(test, (cost, nx, ny))

# for _ in range(1,T+1):
#     count += 1
#     n = int(input()) 
#     array = [] 
#     for _ in range(n): 
#         array.append([int(i) for i in input().strip()]) 
#     distance = [[float('inf')]*n for _ in range(n)]
#     dp()
#     result = distance[n-1][n-1]
#     print(f"#{count} {result}")