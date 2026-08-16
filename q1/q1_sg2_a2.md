Annex C
Code Quality Assessment Worksheet

Section: Pinatubo                                         Score:____________

C# / Name: #16 Umayan, #17 Aguilar, #19 Atencio Date:     August 13, 2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.
| PseudoCode 1                        | Pseudocode 2                           |
| ----------------------------------- | -------------------------------------- |
| Algorithm FindMax1(numbers)         | Algorithm FindMax2(numbers)            |
|   max ← numbers[0]                  |   For i from 1 to length(numbers)-1    |
|   For i from 1 to length(numbers)-1 |     For j from 0 to length(number)-1   |
|     If numbers[i] > max Then        |       If numbers[j] > numbers [i] Then |
|       max ← numbers[i]              |         bigger ← false                 |
|     EndIf                           |       EndIf                            |
|   EndFor                            |     EndFor                             |
|   Return max                        |     If bigger = true Then              |
| EndAlgorithm                        |       Return numbers [i]               |
|                                     |     EndIf                              |
|                                     |   EndFor                               |
|                                     | EndAlgorithm                           |

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

Algorithm 1 is significantly faster when dealing with lists that contain large numbers because it uses one single loop and

| PseudoCode 1                                             | Pseudocode 2                                             |
| -------------------------------------------------------- | -------------------------------------------------------- |
| [/] Does the algorithm use one loop or two nested loops? | [ ] Does the algorithm use one loop or two nested loops? |
|                                                          |                                                          |
| [ ] Does the algorithm repeat work unnecessarily?        | [/] Does the algorithm repeat work unnecessarily?        |
|                                                          |                                                          |
| [/] Which algorithm finishes in fewer steps?             | [ ] Which algorithm finishes in fewer steps?             |
