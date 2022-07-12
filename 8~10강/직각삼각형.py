def right_triangle(i, j, k) :
  x_list = []
  x_list.append(i)
  x_list.append(j)
  x_list.append(k)
  x_list.sort() 
  
  if x_list[2]**2 == x_list[0]**2+x_list[1]**2 :
    print("right")

  else :
    print("wrong")

while True :
  a, b, c = map(int,input().split())

  if a == 0 and b == 0 and c == 0 :
    break;
  
  right_triangle(a,b,c)