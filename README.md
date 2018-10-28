# genetic pong game
This project is an application of evolutionary theory to convergence of a solution. This repository contains a game which learns to play pong unsupervised through simulation of evolution.

The AI works like this
1. We have a model that looks like this output (go up down or stay neutral) = tanh(A*inputs)

2. A is the unknown that the genetic algorithm will try to converge to

3. We must represent A in an allele like manner so that crossbreeding and mutations are possible.

4. We start off with initial size n population of randomly generated alleles

5. Run fitness function (how many times can the paddle bounce it without losing) on the population

6. Run a selection process to decide which alleles will breed with which alleles to decide next generation and decide which ones will die.

7. Repeat steps 5-6 until convergence onto A.

# Requirements

1. numpy
2. pygame

# Running the code

~~~
python pong_test.py
~~~

# References

Special thanks to [link](https://github.com/Sarthak-Rijal/goodpong "Sarthak Rijal original game code")

# MIT LICENSE
Copyright 2018 Artur Kashperskiy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.