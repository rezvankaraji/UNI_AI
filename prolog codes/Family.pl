female(rezvan).
female(azita).
female(pooraan).
female(leyla).
female(fatemeh).
female(farangis).

male(mohammad).
male(mohammadreza).
male(hojat).
male(shahram).
male(ahmadali).
male(amir).

parent(azita, rezvan).
parent(azita, mohammadreza).
parent(mohammad, rezvan).
parent(mohammad, mohammadreza).

parent(pooraan, azita).
parent(hojat, azita).
parent(pooraan, leyla).
parent(hojat, leyla).
parent(pooraan, shahram).
parent(hojat, shahram).

parent(fatemeh, mohammad).
parent(ahmadali, mohammad).
parent(fatemeh, farangis).
parent(ahmadali, farangis).
parent(fatemeh, amir).
parent(ahmadali, amir).

grandparent(GrandParent, GrandChild) :- 
	parent(GrandParent, Parent),
	parent(Parent, GrandChild).
sibling(Child1, Child2) :- 
	parent(Parent, Child1),
	parent(Parent, Child2),
	Child1 \== Child2.
		
mother(Mom, Child) :- 
	parent(Mom, Child), 
	female(Mom).
father(Dad, Child) :- 
	parent(Dad, Child), 
	male(Dad).
grandmother(GrandMother, GrandChild) :- 
	grandparent(GrandMother, GrandChild),
	female(GrandMother).
grandfather(GrandFather, GrandChild) :- 
	grandparent(GrandFather, GrandChild),
	male(GrandFather).
sister(Girl, Sibling) :- 
	sibling(Girl, Sibling), 
	female(Girl).
brother(Boy, Sibling) :- 
	sibling(Boy, Sibling), 
	male(Boy).
aunt(Aunt, Child) :-
	parent(Parent, Child),
	sister(Aunt, Parent).
uncle(Uncle, Child) :-
	parent(Parent, Child),
	brother(Uncle, Parent).
