safe(_, []) :- !.
	   
safe(q(R,C),Board) :- member(q(Ra,Ca), Board), abs(Ra-R) =:= abs(Ca-C), !, fail.

safe(_,_).            
 
queens([], [], Board, Board).     
                       
queens([q(R)|Queens], Columns, Board, Solution) :- nth0(_,Columns,C,Free), safe(q(R,C),Board), queens(Queens,Free,[q(R,C)|Board], Solution).    
 
queens :- findall(q(N), between(0,7,N), Queens), findall(N, between(0,7,N), Columns), findall(B, queens(Queens, Columns, [], B), Boards),     
  length(Boards, Len), writef('%w solutions:\n', [Len]),  member(R,Boards), reverse(R,Board), writef('  - %w\n', [Board]), fail.
  
queens.



