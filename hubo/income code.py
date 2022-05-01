n = int(input())
k= 0
d = list(map(int, input().split()))
d.sort()

l = d.pop(-1)
for i in range(0,len(d)):
    a = d[i]
    c = (a/l)*100
    k = c +k
lol = l
lol= ((lol/l)*100)
print((lol+c)/n)