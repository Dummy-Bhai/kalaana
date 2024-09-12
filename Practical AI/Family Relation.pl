male(javed).
male(abdulla).
male(nadim).
male(hanif).

female(tabasum).
female(shabira).
female(naziya).
female(faruka).

parent(javed,tabasum,nadim).
parent(hanif,faruka,tabasum).
parent(javed,tabasum,naziya).
parent(abdulla,shabira,javed).

father(X,Y):-
    parent(X,_,Y).
mother(X,Y):-
    parent(_,X,Y).

grandfather(X,Y):-
    male(X),father(X,Z),father(Z,Y).
grandmother(X,Y):-
    female(X),mother(X,Z),father(Z,Y).



