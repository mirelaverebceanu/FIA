%% User Interface:

go :-
	greeting,
	repeat,
	write('> '),
	read(X),
	do(X),
	X == quit.

greeting :-
	write('This is the Expert Prolog shell.'), nl,
	write('Enter load, consult, known or quit at the prompt.'), nl.

do(load) :- load_kb, !.
do(consult) :- solve, !.
do(known) :- know, !.
do(iknow) :- iknow, !.
do(quit).

do(X) :-
	write(X),
	write('is not a legal command.'), nl,
	fail.


ask(A, V) :-
	known(true, A, V),
	writeln(A:V),
	!.	% stop looking

ask(A, V) :-
	known(yes, A, V), % succeed if true
	!.	% stop looking

ask(A, V) :-
	known(_, A, V), % fail if false
	!, fail.

ask(A, V):-
	write(A:V), % ask user
	write('? : '),
	read(Y), % get the answer
	asserta(known(Y, A, V)), % remember it
	Y == yes.	% succeed or fail


menuassert(_, _, []).
menuassert(X, A, [X|T]) :- asserta( known(yes, A, X) ), menuassert(X, A, T).
menuassert(X, A, [H|T]) :- asserta( known(no, A, H) ), menuassert(X, A, T).


menuask(A, V, _) :-
	known(true, A, V),
	writeln(A:V),
	!.

menuask(A, V, _) :-
	known(yes, A, V), % succeed if true
	!.

menuask(A, V, _) :-
	known(_, A, V), % fail if false
	!, fail.

menuask(A, V, MenuList) :-
	write('What is the value for '), write(A), write('?'), nl,
	write(MenuList), nl,
	read(X),
	check_val(X, A, V, MenuList),
	menuassert(X, A, MenuList),
	!,
	X == V.

check_val(X, _, _, MenuList) :-
	member(X, MenuList), !.

check_val(X, A, V, MenuList) :-
	write(X), write(' is not a legal value, try again.'), nl,
	menuask(A, V, MenuList).



%% Inference Engine:

solve :-
	abolish(known/3),
	dynamic(known/3),
	top_goal(X),
	write('The tourist is a/an '), write(X), nl.

solve :-
	write('No touristfound.'), nl.

load_kb :-
	write('Enter file name: '),
	read(F),
	consult(F).

know :-  known(X, Y, Z), write('> '), write(Y), write(' '), write(Z), write(' '), write(X), nl, fail.
know.

iknow :-
	abolish(known/3),
	dynamic(known/3),
	write('Enter your hypothesis: '),
	read(F),
	iknow_top_goal(F).