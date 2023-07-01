family(person(tom, fox, date(7, may, 1950), works(bbc, 15200)), person(ann, fox, date(9, may, 1951), works(unemployed)), [person(pat, fox, date(5, may, 1973), works(unemployed)), person(jim, fox, date(5, may, 1973), works(unemployed))]).
family(person(dimitris, vlachos, date(23, june, 1969), works(freelancer, 1000000)), person(efi, vlachos, date(30, may, 1969), works(unemployed)), [person(sophia, vlachos, date(4, march, 2000), works(unemployed)), person(spiros, vlachos, date(4, october, 2002), works(freelancer, 100000))]).
family(person(nektarios, goudelis, date(9, november, 1970), works(accountant, 1000000)), person(litsa, goudelis, date(5, may, 1970), works(accountant, 100000)), [person(johny, goudelis, date(2, december, 1996), works(security, 10800)), person(harry, goudelis, date(9, august, 2002), works(freelancer, 100000))]).
family(person(nikos, koukos, date(1, january, 1968), works(unemployed)), person(maria, koukos, date(2, february, 1977), works(unemployed)), [person(marios, koukos, date(7, august, 2000), works(unemployed)), person(zina, koukos, date(21, july, 2001), works(unemployed)), person(mary, koukos, date(21, july, 2001), works(unemployed)), person(zoe, koukos, date(30, november, 2002), works(unemployed))]).
family(person(derrick, rose, date(4, october, 1988), works(basketballer, 2500000)), person(brenda, rose, date(15, november, 1994), works(unemployed)), [person(junior, rose, date(1, january, 2012), works(unemployed)), person(layla, rose, date(6, march, 2018), works(unemployed)), person(london, rose, date(26, may, 2019), works(unemployed))]).

male(tom).
male(pat).
male(jim).
male(dimitris).
male(spiros).
male(nikos).
male(marios).
male(derrick).
male(junior).
female(ann).
female(efi).
female(sophia).
female(litsa).
female(maria).
female(zina).
female(mary).
female(zoe).
female(brenda).
female(layla).
female(london).

parent(tom, pat).
parent(tom, jim).
parent(ann, pat).
parent(ann, jim).
parent(dimitris, sophia).
parent(dimitris, spiros).
parent(efi, sophia).
parent(efi, spiros).
parent(nektarios, johny).
parent(nektarios, harry).
parent(litsa, johny).
parent(litsa, harry).
parent(nikos, marios).
parent(nikos, zina).
parent(nikos, mary).
parent(nikos, zoe).
parent(maria, marios).
parent(maria, zina).
parent(maria, mary).
parent(maria, zoe).
parent(derrick, junior).
parent(derrick, layla).
parent(derrick, london).
parent(brenda, junior).
parent(brenda, layla).
parent(brenda, london).


father(X, Y):- parent(X, Y), male(X).
mother(X, Y):- parent(X, Y), female(X).
child(X, Y):- parent(Y, X).

mother_of_three_kids(X):- family(_,person(X,_,_,_),[_,_,_]).

family_with_three_kids(X):- family(person(_,X,_,_),_,[_,_,_]).