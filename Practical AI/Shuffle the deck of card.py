import itertools,random

deck=list(itertools.product(range(1,14),['spade','diamond','club','heart']))

random.shuffle(deck)

print('You Got: ')

for i in range(5):
    print(deck[i][0],' of ',deck[i][1])
