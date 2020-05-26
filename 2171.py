a = 1
while(a != 0):
  p = 1
  f = 1 
  j = 1
  a = 1
  a = input()
  a = int(a)
  if (a != 0):
    for i in range(a):
      if(f+p < a):
        p+=1
        j+=1
        f+=j
      if(f+p > a):
        while(f+p > a):
          p = p-1
    print(f,p)
  
