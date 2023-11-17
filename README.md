# LCS
For LCS homework

To use the program, copy + paste into your python interpreter.

Curretly there are 4 available options:

[1] Verify proposition | Makes sure the string input is a WFF

[2] Compute given interpretation | Will ask the user for an interpretation

[3] Compute table of all interpretations | Will generate a table with all the interpretation and will specify weather the proposition is valid, satisfiable or unsatisfiable.

[4] Compute logical equivalence | Will ask the user for 2 propositions and will verify if they are logically equivalent (Not completed)


#Table updated with Pandas library, fixed lazy operations.

Known issues:
  F=>F ~ T  or any operations similar won't work due to the fact that the number of results for F=>F is 2 and T has only one result. (Difference in the amount of results)
  
  The program only works for strong syntax.
  Relaxed syntax is wip.
  
