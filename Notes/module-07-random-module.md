# The random module


The [random ](https://docs.python.org/3/library/random.html#)module allows us to generate pseudo-random number from a seed that is very hard to predict. This comes into play for games and modeling.


Where does unpredictability come from?

- From a ‘seed’, a number that is very hard to predict

- Values from your specific system: e.g., the last 10,000 keystrokes


But sometimes we need some level of determinism to check code to see if it is working as expected.

You can enter a number or string (something that can be converted to bytes) that can be the seed: random.seed(‘grapefuit’). When you set the seed, subsequent calls become predictable.
