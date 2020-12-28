quicksort([], []).
quicksort([First|Rest], Sorted) :- 
	partition(First, Rest, Less, More), 
	quicksort(Less, SortedLess), 
	quicksort(More, SortedMore),
	append(SortedLess, [First|SortedMore], Sorted).

partition(_, [], [], []).
partition(Pivot, [First|Rest], [First|Less], More) :- 
	First =< Pivot, 
	partition(Pivot, Rest, Less, More).
partition(Pivot, [First|Rest], Less, [First|More]) :- 
	First > Pivot, 
	partition(Pivot, Rest, Less, More).
	
	
