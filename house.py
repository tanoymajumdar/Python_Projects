import itertools
l = int(input("Length of riverfront: "))
k = int(input("Number of animals: "))
x = 1
isempty = 1
river = [x]*l
for j in range(0, k):
    a,b = input('Animal {}: '.format(j+1)).split()
    for i in range(int(a),int(b)+1):
        river[i] = 0
for i in range(0, len(river)):
    if(river[i] == 1):
        isempty = 0
if isempty:
    print(0)
else:
    m = max(len(list(y)) for (c,y) in itertools.groupby(river) if c==1)
    print(m)