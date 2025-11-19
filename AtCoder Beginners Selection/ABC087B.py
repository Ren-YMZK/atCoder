a= int(input())
b= int(input())
c= int(input())
x= int(input())

# a= 2
# b= 2
# c= 2
# x= 100

count= 0

for i in range(a + 1):
  for j in range(b + 1):
    for k in range (c + 1):
      n= 500*i + 100*j + 50*k
      if n == x:
        count += 1
        
  
print(count)