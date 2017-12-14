#pzin = "0	2	7	0" #test input
pzin = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14" # real input

pzin_a = [int(x) for x in pzin.split("\t")]

sum, memo, pzin_c, toggle, toggle_2, pzin_len = 0, [], pzin_a, False, False, len(pzin_a)
while not toggle_2:
	memo.append([x for x in pzin_c])
	sum += 1
	#print("First run: ", pzin_c, memo)
	mx = max(pzin_c)
	pos = pzin_c.index(mx)
	pzin_c[pos] = 0
	while mx > 0:
		pos = (pos + 1)%pzin_len
		pzin_c[pos] += 1
		mx -= 1
	#print("Second run: ", pzin_c, memo)
	if pzin_c in memo:
		if toggle:
			toggle_2 = True
		else:
			memo = []
			toggle = True
			sum = 0
print(memo)
print(sum)