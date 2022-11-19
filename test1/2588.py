a= int(input())
b= int(input())

f = b//100
s = (b-f*100)//10
t = b-f*100-s*10

print(t*a)
print(s*a)
print(f*a)
print(b*a)
