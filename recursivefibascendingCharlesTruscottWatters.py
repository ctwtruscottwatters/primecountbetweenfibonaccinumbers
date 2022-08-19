import random
import struct
from matplotlib import pyplot as plot
import numpy as np
import math
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393]
# Charles Truscott, MIT '22 6.0002 practice
# This program is roughly drafted in PyDroid on a Caterpillar S60 militarised smart phone, roughly drafted to inquire about the generalisation of ratios of primes in each interval between the Fibonacci numbers up to 100000, but need an i7 or i9 CPU and at least 16 gigabytes of RAM not on a weaker mobile ARM instruction set architecture
def recursive_fibonacci(a, b, fibs):
	fibs.append(b)
	if b >= 100000:
		print(fibs)
	else:
		recursive_fibonacci(b, a  + b, fibs)
	return fibs

def main():
	x = recursive_fibonacci(0, 1, [])
	y = []
	primeCountL = []
	primeCount = 0
	for q in x:
		print(q)
		for upTo in range(2, q, 1):
			for prime_or_not in range(2, upTo, 1):
				if upTo % prime_or_not == 0:
					continue
				else:
					primeCount += 1
			primeCountL.append(primeCount)
			primeCount = 0
	print(primeCountL)
	plot.figtext = "Charles Truscott"
	plot.xlabel("Intervals of Fibonacci numbers under one-hundred-thousand")
	plot.ylabel("Amount of primes in that interval")
	plot.plot(x, primeCountL)
	plot.savefig('/sdcard/fibreciprocalCharlesTruscott.jpg')
if __name__ == "__main__": main()