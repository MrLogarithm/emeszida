# 𒅴𒋃𒀀 (emešida) - "language of counting"

This project is an attempt to write a programming language using Sumerian cuneiform as defined in the Unicode standard [cuneiform codeblock](https://en.wikipedia.org/wiki/Cuneiform_(Unicode_block\)).
It is of course, (almost) completely useless but serves as an interesting thought experiment, and an opportunity to learn more about the fascinating history of the ancient Near East, in particular the cuneiform writing system and its associated languages (Sumerian, Akkadian, etc.).

## Inspiration

The initial inspiration for this project came from [قلب](https://nas.sr/%D9%82%D9%84%D8%A8/) (Qalb) a programming language written in both the Arabic script and language.
قلب was initially designed as both an art project and an attempt to bring attention to the issue of English-language bias in computer science.

I decided I wanted to try something similar but with Cuneiform.  Many languages used cuneiform to inscribed their text, however Sumerian stood out as one most suited to a simple programming environment.
There is relatively high-fidelity between cuneiform signs and Sumerian words (cuneiform having been invented probably to write Sumerian).  So with mostly single cuneiform signs I could construct a concise protected vocabulary.

Another side effect of this project is to stress test my programming environment as much as possible by trying to use the high unicode values of the cuneiform code block anywhere possible.

NB: I doubt your default installed fonts have cuneiform signs in them (if so, that's amazing!).
So to aid in seeing the code below please install one of the fonts listed under "Cuneiform Fonts" on this [page](http://oracc.museum.upenn.edu/doc/help/visitingoracc/fonts/)

## Example Programs

Adding two numbers, multiplying by a third and printing the result:

(10+40)*30
> 10 40 **add** 30 **multiply** **write**

10+40*30

> 40 30 **multiply** 10 **add** **write**

with an intermediate variable

> *result* 10 40 **add** **see** *output* *result* 30 **multiply** **see** *output* **write**

An example of defining a function, a program to compute the area of a field given width and length:

> *area* **name** *width* *length* **take** *result* *width* *length* **multiply** **see** *result* **give** **named**
4 1:30 *area* **do** **write**

in Python:
```
def area(width, length):
    result = width * length
    return result
    
print(area(4, 1.5))
```
## Grammar

The language (𒅴, eme) follows Sumerian itself in placing the verb at the end of a clause, traditionally called SOV-notation.
I've translated that into programming syntax as [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Operators take a fixed number of arguments.

Read the program L → R, push each operand on to the stack, when you hit an operator, pop off the number of operands that the operator requires (i.e. 'add' needs two operands), and put the results back on the stack.

### Numbers

Mathematics in cuneiform is a fascinating (full stop), in this implementation of a programming language numbers are sexigesimal in their base value.
There is also no demarcation between whole numbers and factional values.  
When a unit is to be skipped (i.e. in the case of 1 15 meaning 1 0 15) the ":" character is used to denote the empty unit.

### References:

https://en.wikipedia.org/wiki/Reverse_Polish_notation
https://en.wikipedia.org/wiki/RPL_(programming_language)
http://blog.reverberate.org/2013/07/ll-and-lr-parsing-demystified.html
https://en.wikipedia.org/wiki/Cuneiform_(Unicode_block)
