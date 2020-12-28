reverse([], []).
reverse([First|Rest], Reversed) :- 
	reverse(Rest, ReversedRest), 
	append(ReversedRest, [First], Reversed).
