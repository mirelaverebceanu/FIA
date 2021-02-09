%% Knowledge Base:

top_goal(X) :- tourist(X).
iknow_top_goal(X) :-
	asserta(known(true, clothes, kipa)),
	asserta(known(true, clothes, suit)),
	asserta(known(true, clothes, chiwon)),
	asserta(known(true, clothes, ie)),
	asserta(known(true, clothes, sunglasses)),
	asserta(known(true, clothes, luna)),
	asserta(known(true, language, jewish)),
	asserta(known(true, language, english)),
	asserta(known(true, language, thai)),
	asserta(known(true, language, romanian)),
	asserta(known(true, language, lunish)),
	asserta(known(true, height, 155)),
	asserta(known(true, height, 160)),
	asserta(known(true, height, 165)),
	asserta(known(true, religion, judaism)),
	asserta(known(true, religion, catholic)),
	asserta(known(true, religion, buddhism)),
	asserta(known(true, religion, orthodox)),
	asserta(known(true, religion, lunism)),
	asserta(known(true, skin_color, yellow)),
	asserta(known(true, skin_color, white)),
	asserta(known(true, skin_color, red)),
	asserta(known(true, familiar_with_luna, low)),
	asserta(known(true, familiar_with_luna, medium)),
	asserta(known(true, familiar_with_luna, high)),
	asserta(known(true, visa, has)),
	asserta(known(true, visa, does_not_have)),
	asserta(known(true, visible, is_not_visible_by_human_eye)),
	tourist(X).

%% Askables

clothes(X) :- menuask(clothes, X, [kipa, suit, chiwon, ie, sunglasses, luna]).
language(X) :- menuask(language, X, [jewish, english, thai, romanian, lunish]).
height(X) :- menuask(height, X, [155, 160, 165]).
religion(X) :- menuask(religion, X, [judaism, catholic, buddhism, orthodox, lunism]).
skin_color(X) :- menuask(skin_color, X, [yellow, white, red]).
familiar_with_luna(X) :- menuask(familiar_with_luna, X, [low, medium, high]).
visa(X) :- menuask(visa, X, [has, does_not_have, none]).

visible(X) :- ask(visible, X).

%% Rules

class(est_tourist) :-
	skin_color(yellow),
	familiar_with_luna(medium).

class(west_tourist) :-
	skin_color(white),
	familiar_with_luna(high).

type(foreigner) :-
	visa(has).

type(citezen) :-
	visa(does_not_have).

tourist(jew) :-
	type(foreigner),
	class(est_tourist),
	clothes(kipa),
	language(jewish),
	height(160),
	religion(judaism).

tourist(american) :-
	type(foreigner),
	class(west_tourist),
	clothes(suit),
	language(english),
	height(165),
	religion(catholic).

tourist(buddhist) :-
	type(foreigner),
	class(est_tourist),
	clothes(chiwon),
	language(thai),
	height(155),
	religion(buddhism).

tourist(romanian) :-
	type(foreigner),
	class(west_tourist),
	clothes(ie),
	language(romanian),
	height(165),
	religion(orthodox).

tourist(australian) :-
	type(foreigner),
	clothes(sunglasses),
	language(english),
	height(165),
	religion(catholic),
	skin_color(red),
	familiar_with_luna(low).

tourist(lunian) :-
	type(citezen),
	class(west_tourist),
	clothes(luna),
	language(lunish),
	height(160),
	religion(lunism).

tourist(gost) :-
	visible(is_not_visible_by_human_eye).