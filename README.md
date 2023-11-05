# Attempting to build a Quine Relay

Let's build a Quine Relay

## How to build a quine
A quine is a program P such that Eval P = P. That is, evaluating the program produces the original program, or at least a textual representation thereof. A quine relay is a sequence of programs, say [P, Q, R] such that

- Eval P = Q
- Eval Q = R
- Eval R = P

The exact number of programs does not matter. What matters is that the programs cyclically produce one another. The programs are not required to be written in the same language; it is more interesting when they are not. The Eval functions are taken to be appropriate for the languages at hand. If P, Q, and R are written in different languages, we would require distinct Eval functions, say python, ruby, and lua interpreters.

## Generate ordinary quines? Maybe just 1 quine


## References
- https://drcabana.org/quine/