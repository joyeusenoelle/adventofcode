inputs = [1, 12, 23, 1024, 312051]
outputs = [0, 3, 2, 31]

def manhattan(inp):
	""" In a counter-clockwise spiral starting with 1, the number inp is on the outermost edge
		of a square whose sides are the square root of inp, rounded up.
		The Manhattan distance to the center is always the length of a side minus the distance 
		to the last corner, minus one if the side length is odd. 
		(The distance to the last corner is inp % side length.)
	"""
	slen = int(inp**(0.5)) + 1 if inp != 1 else 1 #1 is a special case
	odd = 1 if slen%2 == 1 else 0
	if odd == 1:
		dist = inp - (slen * (slen-1)) - 1
	else:
		dist = inp - ((slen-1)**2) - 1
	print(inp, slen, dist, odd)
	
	return (slen + dist) - odd

def main(test=None):
	if test == None:
		test = False
	cap = 4 if test == False else 5
	for i in range(cap):
		inp = inputs[i]
		out = manhattan(inp)
		comp = out == outputs[i] if i < 4 else "unknown"
		print(inp, out, comp)


if __name__ == "__main__":
	main(False) # Set to True to use the final value