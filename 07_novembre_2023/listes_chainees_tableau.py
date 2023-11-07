t1 = [3, None]
t2 = [6,[7, None]]

print(t1)
print(t2)
      
t2[1][0] = 1

print(t1)
print(t2)

t1[1] = t2

print(t1)

print(id(t1))
print(id(t2))
print(id(t1[1]))

t2[1][1] = [5, None]
t2[1][1][1] = [11, None]
print(t2)

print(t1)

t3 = [1,[2,[3,[4, None]]]]

print(t3)



