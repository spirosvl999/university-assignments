precede_list([],[H|T]).
precede_list([X|Ta],[X|Tai]):-precede_list(Ta,Tai).