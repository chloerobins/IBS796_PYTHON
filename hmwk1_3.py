# Homework 1 Question 3
# Due Sept. 19
# Chloe Robins

# 3. GenBank File
import sys, re

def gb_to_fasta(filename):
	dna_beg_pos = 0
	dna_end_pos=0
	data_lines = 0
	data_array = []
	dna_array = []
	pos_array = []
	start_array = []
	end_array =[]
	translation = []
	codontable = {'ttt':'F', 'tct':'S', 'tat':'Y', 'tgt':'C','ttc':'F', 'tcc':'S', 'tac':'Y', 'tgc':'C','tta':'L', 'tca':'S', 'taa':'*', 'tga':'*','ttg':'L', 'tcg':'S', 'tag':'*', 'tgg':'W','ctt':'L', 'cct':'P', 'cat':'H', 'cgt':'R','ctc':'L', 'ccc':'P', 'cac':'H', 'cgc':'R','cta':'L', 'cca':'P', 'caa':'Q', 'cga':'R','ctg':'L', 'ccg':'P', 'cag':'Q', 'cgg':'R','att':'I', 'act':'T', 'aat':'N', 'act':'S','atc':'I', 'acc':'T', 'aac':'N', 'agc':'S','ata':'I', 'aca':'T', 'aaa':'K', 'aga':'R','atg':'M', 'acg':'T', 'aag':'K', 'agg':'R','gtt':'V', 'cgt':'A', 'gat':'D', 'ggt':'G','gtc':'V', 'gcc':'A', 'gac':'D', 'ggc':'G','cta':'V', 'gca':'A', 'gaa':'E', 'gga':'G','gtg':'V', 'gcg':'A', 'gag':'E', 'ggg':'G',}
	with open(filename, 'r') as f:
		for line in f:
			if 'CDS' in line:
				CDS = line.rstrip('\n')
				CDS = CDS[21:]
				list = CDS.rsplit("..")
				if len(CDS)<17:
					start = list[0]
					start_array.append(start)
					end=list[-1]
					end_array.append(end)
				if len(CDS)>17:
					start = list[0]
					start = start[11:]
					start_array.append(start)
					end = list[-1]
					end = end[:-1]	
					end_array.append(end)
				tag = next(f)
				tag= tag.rstrip('\n')
			if 'product' in line:
				product=line.rstrip('\n')
				product = product[21:]
				string = '>' + tag[21:] + product
				pos_array.append(string)
			if 'ORIGIN' in line:
				dna_beg_pos=data_lines+1
			if  dna_beg_pos>0:
				data=line.rstrip('\n')
				data2=''.join(e for e in data if e.isalpha())
				data_array.append(data2)
			data_lines=data_lines+1
		dnastring=''.join(data_array)
		dnastring=dnastring[6:]
		start_array=start_array[2:]
		end_array=end_array[2:] 
		for i in range(1,10,1):
			print pos_array[i]
			stringstart=int(start_array[i])-1
			stringend=int(end_array[i])-1
			seq = dnastring[stringstart:stringend]
			proteinseq=''
			for n in range(0,len(seq),3):
				#print seq[n:n+3]
				if seq[n:n+3] in codontable:
					proteinseq+=codontable[seq[n:n+3]]
			print proteinseq
	return ''

print(gb_to_fasta(sys.argv[1]))
