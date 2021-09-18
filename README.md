# pill-bottle
Experimenting with a probability problem.

A medicine bottle contains N tablets and you are supposed to take a
half tablet per day. Every day, you draw at random from the bottle
either a half or a whole tablet.  If a half, it's consumed.  If it's a
whole, half is consumed and half is returned to the bottle. After 2N
draws, the bottle is empty.

Is there anything interesting about the numbers of whole and half
tablets in the bottle over time?

## Choices

Graphing the choices at any step as a progression leads to finding Triangular Numbers.

## Randomness

start with n pills

draw a pill at random, odds are 1:1 of drawing a whole pill. replace 1/2.

now there are (n-1/2) pills, that is 1 half and  (n-1) wholes

Draw a pill at random.  The odds are 1:n of drawing a half and (n-1):n of drawing a whole.

...

|         |       |      | odds  | odds |
| total   | whole | half | whole | half |
|:-------:|:-----:|:----:|:-----:|:----:|
| n       | n     | 0    | 1     | 0    |
| n - 0.5 | n-1   | 1    |       |      |

