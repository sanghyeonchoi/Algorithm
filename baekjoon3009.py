x_ =[]
y_ =[]


for _ in range(3):
    x,y = map(int, input().split())
    x_.append(x)
    y_.append(y)

for i in range(3):
    if x_.count(x_[i]) ==1:
        x4 = x_[i]
    if y_.count(y_[i]) ==1:
        y4 = y_[i]
    
print(x4, y4)