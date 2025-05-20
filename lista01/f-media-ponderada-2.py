v1, v2 = map(float, input().split())
p1, p2 = map(float, input().split())
weightedMean = (v1*p1 + v2*p2)/(p1+p2)
print(int(weightedMean))