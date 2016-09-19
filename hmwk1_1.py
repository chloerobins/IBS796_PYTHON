# Homework 1 Question 1
# Due Sept. 19
# Chloe Robins

# 1. Create a Random Sequence Generator

import sys, random

# define the sequence generator
def randseqs(num,length,gc):
	for i in range(1,num+1,1):
		gcweight = int(round(gc/2*length))
		atweight = int(round((1-gc)/2*length))
		valid_letters = ''.join(['A'*atweight,'T'*atweight,'G'*gcweight,'C'*gcweight])
		seq = ''.join((random.choice(valid_letters) for i in xrange(length)))
		nG=seq.count("G",0,length)
		nC=seq.count("C",0,length)
		GC_con=float(nG+nC)/length
		print '>Sequence:', i, 'Length:', length, 'GC:', GC_con 
		print seq
		return ''
				

# print to the screen
print(randseqs(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3])))


