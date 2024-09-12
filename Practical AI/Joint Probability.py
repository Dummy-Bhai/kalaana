cardnumber=input("Enter the card number: ")
cardcolor=input("Enter the card color: ")

PofA=4/52
PofB=26/52

print("P(A)=>Prabability of drawing card with number ",round(PofA,2))
print("P(B)=>Prabability of drawing card with color ",round(PofB,2))

print("Joint Probability of A and B=P(A) * P(B)")

PofAANDPofB=round(PofA*PofB,2)

print("P(A and B)=",PofAANDPofB)

print("Chance: ",PofAANDPofB*100,"%")

