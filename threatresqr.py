l,b,n=map(int,input().split())   #entering len,breadth and size of tile
if l%n==0:
  c=l//n
else:
  c=l//n+1
if b%n==0:
  z=b//n
else:
  z=b//n+1
print(c*z)
