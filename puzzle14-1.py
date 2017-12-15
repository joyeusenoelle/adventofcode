#test input
# inp = """flqrgnkx
# """

# real input
inp = """jzgqcdpd
"""

dbg = False

def debug(message):
	if dbg:
		print(message)


def hasher(ipt):
	""" Knot hashing algorithm from Day 10
	"""
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
					cycle_a, cycle_b, cycle_c = cycle[:left],cycle[left:pos],cycle[pos:]
					cycle_ba = cycle_c + cycle_a
					cycle_ba.reverse()
					cycle_ba_a, cycle_ba_b = cycle_ba[:right], cycle_ba[right:]
					cycle = cycle_ba_b + cycle_b + cycle_ba_a
				else:
					left = pos
					right = pos + length
					cycle_a, cycle_b, cycle_c = cycle[:left], cycle[left:right], cycle[right:]
					cycle_b.reverse()
					cycle = cycle_a + cycle_b + cycle_c
			pos = (pos + length + skip) % len(cycle)
			skip += 1
#	print(cycle[0] * cycle[1])
	a, b, dh = 0,16,[]
	while b <= len(cycle):
		c = cycle[a:b]
		dh.append(c[0]^c[1]^c[2]^c[3]^c[4]^c[5]^c[6]^c[7]^c[8]^c[9]^c[10]^c[11]^c[12]^c[13]^c[14]^c[15])
		a, b = b, b+16

	dh_hex = [hex(entry)[2:] if len(hex(entry)) == 4 else "0" + hex(entry)[2:] for entry in dh]
	return "".join(dh_hex)

def main(ipt):
	binstr = ""
	for word in ipt:
		hword = hasher(word)
		debug("Word: {}, hashed: {}".format(word, hword))
		binstr += str(bin(int(hword, 16))[2:].zfill(128))
	print(sum([int(x) for x in binstr]))

if __name__ == "__main__":
	inp = inp.strip()
	inp_a = []
	for i in range(128):
		inp_a.append("{}-{}".format(inp, i))
	main(inp_a)