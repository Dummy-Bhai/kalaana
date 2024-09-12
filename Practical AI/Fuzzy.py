elt=['w', 'x', 'y', 'z']
A=[0.5,0.4, 0.3,0.2]
B=[0.2,0.2,0.1,1]

def printset(m):
    for i in range(0,4):
        print("(",elt[i],",",m[i],")",end="")
    print()

print("A=")
printset(A)
print("B=")
printset(B)

#Union

U=[]

for i in range(0,4):
    if(A[i]>B[i]):
        U.append(A[i])
    else:
        U.append(B[i])
print("Union: ")
printset(U)

#Intersection

I=[]

for i in range(0,4):
    if(A[i]<B[i]):
        I.append(A[i])
    else:
        I.append(B[i])
print("Intersection: ")
printset(I)

#A complement

AC=[]

for i in range(0,4):
    AC.append(1-A[i])
print("AC=")
printset(AC)

#B complement

BC=[]

for i in range(0,4):
    BC.append(1-B[i])
print("BC=")
printset(BC)


#A-B

AMB=[]

for i in range(0,4):
    if(A[i]<BC[i]):
        AMB.append(A[i])
    else:
        AMB.append(BC[i])
print("A-B: ")
printset(AMB)

#B-A

BMA=[]

for i in range(0,4):
    if(B[i]<AC[i]):
        BMA.append(B[i])
    else:
        BMA.append(AC[i])
print("B-A: ")
printset(BMA)














