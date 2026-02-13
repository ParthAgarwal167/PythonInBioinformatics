genes = ['braca1', 'TRAV', 'PP53', 'ERTH', 'YERO']
genes.append("PP53")
genes.insert(1, "NTR")
genes.remove("PP53")

print(genes[3])
for g in genes:
    print(g)

# studying variables 19-01-2026

a = 4
b = 7.8
c = 56
x = (a*b) - c
print(x)

print("Hello World")
prot = "keratin"
prot_len = len(prot)
print("Protein: ", prot)
dna = ['A','T','T','G','C','C','A','A','T']
print(dna)

# practice

protein = ['T','A','G','T','T','A','R','E','C','C','B']
total_len = len(protein)
gc_content = ((protein.count('G') + protein.count('C')) / total_len) * 100
print(gc_content)

# proteins play

prot1 = 'ATTRRRTCGGAAC'
prot2 = 'YTURIRATTCGEAIAAAA'
if len(prot1) > len(prot2):
    print("Protein 1 is longer")
else:
    print("Protein 2 is longer")

count_AT = prot1.count('A') + prot1.count('T')
print(count_AT)

# practice 1

PROTEIN = ['YEU', 'EIJD', 'IOPJF', 'ART']
PROTEIN.append('YEU')
PROTEIN.remove('YEU')
PROTEIN.insert(2, 'KLO')
print(PROTEIN)
PROTEIN.sort()
print(PROTEIN)
PROTEIN.reverse()
print(PROTEIN)





















