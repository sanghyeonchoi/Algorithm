A, B, V = map(int, input().split())

days = 0
if(V-B) % (A-B) != 0:
    days = ((V-B)//(A-B))+1
else:
    days = ((V-B)//(A-B))

print(days)
