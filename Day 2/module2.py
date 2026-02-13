"""chromo1 = input("Enter the first seq: ")
chromo1 = input("Enter the second seq: ")
print("The sum of two chromosomes is ", chromo1 + chromo1)

# solution1

gene = input("Gene Name: ")
dna_seq = input("DNA Seq: ")
print("The fasta format is: >", gene + dna_seq + "*")

# solution2

prot1 = input("Protein seq1: ")
prot2 = input("Protein seq2: ")
if len(prot1) > len(prot2):
    print("Protein 1 is longer")
else:
    print("Protein 2 is longer")

# solution3

seq = input("Enter the sequence: ")
gc_content = seq.count('G') + (seq.count('C') / len(seq)) * 100
print(gc_content, "%")

# solution4

protein = ['keratin', 'myosin', 'thrombin']
protein.insert(1, 'rho')
protein.remove('keratin')
print("Final sequence: ", protein)

# solution5

genes = ('trep', 'nycc', 'erop', 'erop', 'tp53')
no_of_times = genes.count('erop')
print("No of times it appeared: ", no_of_times)
print(genes[4])

# solution6

gene1 = {'brca1', 'rpgr', 'tp53'}
gene2 = {'rho', 5, 'brca1', true, '45'}
print(gene1.intersection(gene2))"""

# solution7

stud = {}
ans = 'Y'
while ans.upper() == 'Y':
    roll = input("Roll Number: ")
    stud[roll] = {"Name":input("Name of student: "), "Course":input("Course: ")}
    ans = input("Continue?(Y/N) ")
print("Student Records", '\n')
for key,value in stud.items():
    print(key,":",value)