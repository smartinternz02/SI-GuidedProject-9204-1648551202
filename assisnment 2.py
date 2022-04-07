import numpy as np

d=np.zeros(10)
print(arr)

arr=np.ones(10)
print(d)

d=np.ones(10)*5
print(d)

d=np.arange(10,51)
print(d)

d=np.arange(10,51,2)
print(d)

d=np.arange(0,9).reshape(3,3)
print(d)

d=np.eye(3,3)
print(d)

d=np.random.rand(1)
print(d)

d=np.random.rand(1,25)
print(d)

d=np.arange(0.01,1.01,0.01).reshape(10,10)
print(d)

d=np.linspace(0,1,20)
print(d)

temp=np.arange(1,26).reshape(5,5)

print(temp[2:,1:])

print(temp[3][-1])

print(temp[:3,1].reshape(3,1))

print(temp[-1])

print(temp[-2:])

print(temp.sum())

print(temp.std())

print(temp.sum(axis=0))