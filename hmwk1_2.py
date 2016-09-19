# Homework 1 Question 2
# Due Sept. 19
# Chloe Robins

# 2. FASTQ summary stats

# Still have to figure these out....
#Read length distribution
#quality per base

import sys

def parse_fastq(filename):
	numreads = 0
	bp = []
	qual = []
	with open(filename, 'r') as f:
		for i,line in enumerate(f):
			if i % 4 == 0:
				numreads = numreads + 1
			if i % 4 == 1:
				current_sequence = line.rstrip('\n')
				bp.append(len(current_sequence))
			if i % 4 == 3:
				qualities = [ord(x) - 33 for x in line.rstrip('\n')]
				average_quality = sum(qualities) / len(qualities)
				qual.append(average_quality)
    	totalbp = sum(bp)
    	minbp = min(bp)
    	maxbp = max(bp)
    	meanbp = sum(bp)/len(bp)
    	minqual = min(qual)
    	maxqual = max(qual)
    	meanqual = sum(qual)/len(qual)
    	print 'Total Reads:', numreads
    	print 'Total Base Pairs:', totalbp
    	print 'Mean (Min,Max) read length:', meanbp,'(',minbp,',',maxbp,')'
    	print 'Mean Quality (Min,Max) Per Read:',meanqual,'(',minqual,',',maxqual,')'
    	return ''

print(parse_fastq(sys.argv[1]))