# test input
inp = """
"""
#real input
# inp = """46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204
# """

dbg = False

def debug(message):
	if dbg:
		print(message)

def main(ipt):
	# test cycle
	#cycle = list(range(5))
	# real cycle
	cycle = list(range(256))
	ipt_orig = ipt
	ipt_a = [ord(char) for char in ipt] + [17,31,73,47,23]
	pos, skip = 0, 0
	for _ in range(64):
		for length in ipt_a:
			if length > 1:
				if pos + length > len(cycle):
					left = (pos + length) % len(cycle)
					right = length - left
					debug("Cycle: {}, left: {}, right: {}, pos: {}, length: {}".format(cycle, left, right, pos, length))
					cycle_a, cycle_b, cycle_c = cycle[:left],cycle[left:pos],cycle[pos:]
					debug("First: {}, second: {}, third: {}".format(cycle_a, cycle_b, cycle_c))
					cycle_ba = cycle_c + cycle_a
					cycle_ba.reverse()
					cycle_ba_a, cycle_ba_b = cycle_ba[:right], cycle_ba[right:]
					debug("After reverse: first: {}, second: {}, third: {}".format(cycle_ba_b, cycle_b, cycle_ba_a))
					cycle = cycle_ba_b + cycle_b + cycle_ba_a
				else:
					left = pos
					right = pos + length
					debug("Cycle: {}, left: {}, right: {}, pos: {}, length: {}".format(cycle, left, right, pos, length))
					cycle_a, cycle_b, cycle_c = cycle[:left], cycle[left:right], cycle[right:]
					debug("First: {}, second: {}, third: {}".format(cycle_a, cycle_b, cycle_c))
					cycle_b.reverse()
					cycle = cycle_a + cycle_b + cycle_c
					debug("After reverse: first: {}, second: {}, third: {}".format(cycle_a, cycle_b, cycle_c))
			pos = (pos + length + skip) % len(cycle)
			skip += 1
			debug("Final: {}".format(cycle))
#	print(cycle[0] * cycle[1])
	a, b, dh = 0,16,[]
	while b < len(cycle):
		c = cycle[a:b]
		dh.append(c[0]^c[1]^c[2]^c[3]^c[4]^c[5]^c[6]^c[7]^c[8]^c[9]^c[10]^c[11]^c[12]^c[13]^c[14]^c[15])
		a, b = b, b+16
	dh_hex = ['%x' % entry for entry in dh]
	print("".join(dh_hex))


if __name__ == "__main__":
	main(inp.strip())