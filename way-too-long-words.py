for t in range(int(input())):
  n=input()
  if len(n)<=10:
    print(n)
  else:
    p=n
    l=len(p)
    p=p[1:l-1]                                   #slicing off the inner section
    k=len(p)
    j=str(k)
    g=n[0]
    m=n[-1]
    print(g+j+m)
