#! /usr/bin/env python
import math

doubles = 0
throws = 0
notdoubles = 0
miscasts = 0

#for t in range(6):
t = 6
#	for u in range(6):
u = 6
#		for w in range(6):
w = 6
for x in range(6):
	for y in range(6):
		for z in range(6):
			if x == y or x == z or y == z or w == x or w == y or w == z or u == w or u == x or u == y or u == z or t == u or t == w or t == x or t == y or t == z:
				doubles += 1
				if x == y == 5 or x == z == 5 or y == z == 5 or w == x == 5 or w == y == 5 or w == z == 5 or u == w == 5 or u == x == 5 or u == y == 5 or u == z == 5 or t == u == 5 or t == w == 5 or t == x == 5 or t == y == 5 or t == z == 5:
					miscasts += 1
			else:
				notdoubles += 1
			throws += 1
			

print "Doubles: ",doubles, ". Not Doubles: ", notdoubles, ". Throws: ",throws, "Miscasts: ", miscasts, "Percent Irresistable force: ",100.0*doubles/throws, "percent miscast: ", 100.0*miscasts/throws, "Percent not doubles: ", notdoubles*100.0/throws
