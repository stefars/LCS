# LCS
For LCS homework

To use the program, copy + paste into your python interpreter.

Curretly there are 4 available options:

1. Verify proposition | Makes sure the string input is a WFF
1. Compute given interpretation | Will ask the user for an interpretation
1. Compute table of all interpretations | Will generate a table with all the interpretation and will specify weather the proposition is valid, satisfiable or unsatisfiable.
1. Compute logical equivalence | Will ask the user for 2 propositions and will verify if they are logically equivalent (Not completed)

## Fixed issues:
- Table updated with Pandas library, fixed lazy operations.
- Fixed the Contradiction/Tautology issue. (Anihilation Laws)
- Fixed ordered atomic proposition in table

## Known issues:
- Reduction laws don't hold due to the difference in tables sizes and the use of the anihilation law module.
- Strong syntax breaks with extra characters at the end. (There is no concret end, and something like
  > (AvB).!FA

would still be a WFF since it's only taking (AvB)

  

## Other:
  - Not all steps are included, if needed, I could add them hopefuly.
  - Relaxed syntax is wip.
  
## Specifications:
  - The program only works for strong syntax.
  - To run the program, pandas library needs to be installed.
 
  
