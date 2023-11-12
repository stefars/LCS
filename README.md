# LCS
For LCS homework

To use the program, copy + paste into your python interpreter.

Curretly there are 4 available options:

[1] Verify proposition | Makes sure the string input is a WFF

[2] Compute given interpretation | Will ask the user for an interpretation

[3] Compute table of all interpretations | Will generate a table with all the interpretation and will specify weather the proposition is valid, satisfiable or unsatisfiable. (Some mentions afterwards)

[4] Compute logical equivalence | Will ask the user for 2 propositions and will verify if they are logically equivalent


Disclaimer: for [3], due to pythons nature to do lazy evaluation, it will not compute all the values if they are not needed
I.E:
  (A=>(B^C))
  If A is False, the program won't compute (B^C) and will just directly give the result (True)
  How it should normally look:
  
  A B C (B^C) (A=>(B^C))
  
  F T F   F       T <-Final Result
  

  How it actually looks:
  
  A B C (B^C) (A=>(B^C))
  
  F T F   T <- Final Result
  
  
  Due to that, the table could be considered incomplete, but it is readable if the concept is grasped.
  The table, is not 100% accurate, but the end result is, there are still bugs to fix.
  
  The program only works for strong syntax.
  
