def mapper():
	for line in sys.stdin:
		data = line.strip().split("\t")
		date, time, store, item, cost, payment = data
		print "{}\t{1}".format(store, cost)