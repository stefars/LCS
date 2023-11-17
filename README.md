# LCS
For LCS homework

To use the program, copy + paste into your python interpreter.

Curretly there are 4 available options:

[1] Verify proposition | Makes sure the string input is a WFF

[2] Compute given interpretation | Will ask the user for an interpretation

[3] Compute table of all interpretations | Will generate a table with all the interpretation and will specify weather the proposition is valid, satisfiable or unsatisfiable.

[4] Compute logical equivalence | Will ask the user for 2 propositions and will verify if they are logically equivalent (Not completed)


#Table updated with Pandas library, fixed lazy operations.
#Fixed the Contradiction/Tautology issue.

Known issues:
  For Logical Equivalenge, in distribution, the order of atomic propozitions changes, hence the result is different than the one expected
  (FvG)=>H has the order F,G,H
  But (F=>H) ^ (G=>H) has the order F,H,G
  So the end result even if it's correct, it's different for the verification I'm doing.


  Not all steps are included, if needed, I could add them hopefuly.
  
  
  The program only works for strong syntax.
  Relaxed syntax is wip.
  
