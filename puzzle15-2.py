# test input
#inp = [65, 8921]

# real input
inp = [591, 393]

class Generator:
	DIV = 2147483647
	def __init__(self, initial, factor):
		self.current = initial
		self.factor = factor

	def cycle(self):
		""" Passes the generator through a cycle:
			Multiply the current value for the factor
			Divide by DIV
			Set the current value to be the remainder
		"""
		self.current = (self.current * self.factor) % self.DIV
		return self.current

	def bin(self):
		""" Returns the last 16 digits of the binary representation of the current value
		"""
		return bin(self.current)[-16:]

	def getCurrent(self):
		""" Returns the current value in decimal form
		"""
		return self.current


def main(ipt):
	score = 0
	gena, genb = Generator(ipt[0], 16807), Generator(ipt[1], 48271)
	for i in range(5000000):
		print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b{}    score: {}".format(i, score), end="")
		aval, bval = gena.cycle(), genb.cycle()
		while (aval % 4 != 0):
			aval = gena.cycle()
		while (bval % 8 != 0):
			bval = genb.cycle()
		abin, bbin = gena.bin(), genb.bin()
		#print("{}\t\t{}".format(aval, abin))
		#print("{}\t\t{}".format(bval, bbin))
		if abin == bbin:
			score += 1
	print("\nScore: ", score)


if __name__ == "__main__":
	main(inp)