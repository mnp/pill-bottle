# pill-bottle
Experimenting with a simple probability problem produces an interesting function.

A medicine bottle contains `n` tablets and you are supposed to take a
half tablet per day. Every day, you draw at random from the bottle
either a half or a whole tablet.  If a half, it's consumed.  If it's a
whole, half is consumed and half is returned to the bottle. After `2n`
draws, the bottle is empty.

The question is, what are the odds of drawing a half tablet at every turn?

## Choices

Before the first draw, there are `n` wholes and 0 halves, which we can write as `(n,0)`. After the first draw, one whole
was consumed and one half returned to the bottle, so the second state is `(n-1, 1)`. The third draw gets interesting because in one world, a whole is chosen and in another world, a half is chosen, so `(2,2)` and `(3,0)`.

![N](images/overview.png){ width=70% align=center }


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

