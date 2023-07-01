monthly(X) :-
    people(X),
    shifts(X).
	
people(X) :-
    length(X, 50),
    maplist(length_(30), X),
    maplist(maplist(in_([m, e, n, r])), X).
	
shifts(X) :-
    maplist(shift_count(X), [m, e, n]),
    maplist(mnm_no(X), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]).
	
constrain_shifts(X) :-
    maplist(shift_count(X), [m, e, n]),
    maplist(no_morning_after_night(X), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]).

shift_count(X, m) :-
    maplist(count_shift(m), X, Counts),
    maplist(>=(15), Counts).

shift_count(X, e) :-
    maplist(count_shift(e), X, Counts),
    maplist(>=(10), Counts).

shift_count(X, n) :-
    maplist(count_shift(n), X, Counts),
    maplist(>=(8), Counts).

mnm_no(X, J) :-
    maplist(mnm_no(J), X, Workers),
    maplist(call, Workers).

mnm_no(J, [X1 | Xs], (X1 \== n -> Xs1 \== m)) :-
    J1 is J + 1,
    mnm_no(J1, Xs, Worker),
    (X1 \== n -> Worker).
mnm_no(_, _, true).