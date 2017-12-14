# test input
# inp = """0: 3
# 1: 2
# 4: 4
# 6: 4
# """

#real input
inp = """0: 3
1: 2
2: 5
4: 4
6: 6
8: 4
10: 8
12: 8
14: 6
16: 8
18: 6
20: 6
22: 8
24: 12
26: 12
28: 8
30: 12
32: 12
34: 8
36: 10
38: 9
40: 12
42: 10
44: 12
46: 14
48: 14
50: 12
52: 14
56: 12
58: 12
60: 14
62: 14
64: 12
66: 14
68: 14
70: 14
74: 24
76: 14
80: 18
82: 14
84: 14
90: 14
94: 17
"""

def main(ipt):
	""" Each scanner reaches the top layer every (range-1)*2 picoseconds starting at 0
		and is "in" the top layer the picosecond after that. 
		So it's tripped if picoseconds % (range-1)*2 == 0.
	"""
	delay = -1
	tgl = True
	while tgl:
		delay += 1
		score = 0
		caught = False
		for line in ipt:
			if not caught:
				#print(line)
				depth, rng = line.split(": ")
				depth, rng = int(depth), int(rng)
				cycle = (rng-1) * 2
				#print("Depth: {}, delay: {}, cycle: {}".format(depth, delay, cycle))
				if cycle > depth + delay: # it can't get back in time
					continue
				else:
					if (depth + delay) % cycle == 0:
						print("Caught! Delayed {} picos but caught at depth {} (range {}, cycle time {})".format(delay, depth, rng, cycle))
						caught = True

		if not caught:
			tgl = False
		else:
			caught = False
	print(delay)

if __name__ == "__main__":
	main(inp.strip().split("\n"))
