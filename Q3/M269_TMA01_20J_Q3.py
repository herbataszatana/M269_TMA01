"""
Code file for M269 20J TMA01 Question 3.
Student version 4: 24/03/20
"""

"""
The following table determines which amino acid
is produced by a particular 3-base DNA codon.

It uses a Python structure called a dictionary, which we will meet later
in the module, so you do not need to understand at this stage how it works.

Do NOT change the table.
"""

dnaCode = { 'TTT':'Phe', 'TTC':'Phe','TTA':'Phe','TTG':'Phe',
            'TCT':'Ser', 'TCC':'Ser','TCA':'Ser','TCG':'Ser',
            'TAT':'Tyr', 'TAC':'Tyr','TAA':'Stop','TAG':'Stop',
            'TGT':'Cys', 'TGC':'Cys','TGA':'Stop','TGG':'Trp',

            'CTT':'Leu', 'CTC':'Leu','CTA':'Leu','CTG':'Leu',
            'CCT':'Pro', 'CCC':'Pro','CCA':'Pro','CCG':'Pro',
            'CAT':'His', 'CAC':'His','CAA':'Gin','CAG':'Gin',
            'CGT':'Arg', 'CGC':'Arg','CGA':'Arg','CGG':'Arg',

            'ATT':'Ile', 'ATC':'Ile','ATA':'Ile','ATG':'Met',
            'ACT':'Thr', 'ACC':'Thr','ACA':'Thr','ACG':'Thr',
            'AAT':'Asn', 'AAC':'Asn','AAA':'Lys','AAG':'Lys',
            'AGT':'Ser', 'AGC':'Ser','AGA':'Arg','AGG':'Arg',

            'GTT':'Val', 'GTC':'Val','GTA':'Val','GTG':'Val',
            'GCT':'Ala', 'GCC':'Ala','GCA':'Ala','GCG':'Ala',
            'GAT':'Asp', 'GAC':'Asp','GAA':'Glu','GAG':'Glu',
            'GGT':'Gly', 'GGC':'Gly','GGA':'Gly','GGG':'Gly'
         }

# Question 3(b)
# -------------

def percentBases(dnaStrand):
    """
    Return a 4-tuple with the percentage of each base C, G, A and T in a DNA strand.
    You can assume dnaStrand is a string with only those four characters.
    
    Use the python round() function to round percentage answers to 2 d.p.
    e.g.  this would round a raw percentage of 33.3333.... to 33.33 exactly.
    rawPerCent = 100/3
    percentC = round(rawPerCent, 2)

    The return statement has been done for you.
    """
    rawPerCentC = (dnaStrand.count('C')/ len(dnaStrand))*100
    percentC = round(rawPerCentC,2)
    rawPerCentG = (dnaStrand.count('G')/ len(dnaStrand))*100
    percentG = round(rawPerCentG,2)
    rawPerCentA = (dnaStrand.count('A')/ len(dnaStrand))*100
    percentA = round(rawPerCentA,2)
    rawPerCentT = (dnaStrand.count('T')/ len(dnaStrand))*100
    percentT = round(rawPerCentT,2)
    return (percentC, percentG, percentA, percentT)

# Question 3(e)
# -------------

def aminoAcid(dnaCodon):
    """
    Return the abbreviated amino acid name corresponding to a 3-base DNA codon.
    For example, if dnaCodon is 'GTT', the function will return 'Val'.

    Do NOT change this function. Call it from function 'translateGene'.
    """
    return(dnaCode[dnaCodon])


def translateGene(dnaStrand, start, stop):
    """
    Return the protein (sequence of amino acids) obtained by translating the
    gene from the start to the stop indices in dnaStrand.

    Note that the start codon generates a corresponding amino acid (as well
    as indicating the start of the gene) but the stop codon is just a marker
    and does not generate anything.
    """
    protein = []
    
    for dnaCodon in range(start, stop):
        dnaCodon = dnaStrand[start] + dnaStrand[start+1] + dnaStrand[start+2]
        if dnaCodon != 'TAG':
            protein.append(aminoAcid(dnaCodon))
            start = start + 3
        else:
            exit
    return protein

def findCodon(dnaStrand, startPos, dnaCodon):
    """
    Return the position in dnaStrand of the dnaCodon consisting of 3 bases,
    searching from a given start position (a string index).
    Return -1 if the codon is not found.

    Do NOT change this function.
    It's used to test Question 3(e) and to implement Question 3(f)
    """
    if startPos >= 0:                               # check for invalid start positions
        for i in range(startPos, len(dnaStrand)-2):
            if dnaStrand[i:i+3] == dnaCodon:       # compare a 3-base DNA slice to the codon
                return i
    return -1

# Question 3(f)
# -------------
def translateStrand(dnaStrand):
    """
    Translate all genes in a DNA strand, returning a list of proteins,
    each protein being a list of amino acid names for one gene.

    You may wish to use the provided function 'findCodon'
    and the function 'translateGene' that you wrote for Question 3(e).
    """
    proteinList = []
    start = 0
    for gene in range(0,len(dnaStrand)):
        atgPos = findCodon(dnaStrand, start, 'ATG')
        tagPos = findCodon(dnaStrand, atgPos , 'TAG')
        translation = translateGene(dnaStrand, atgPos, tagPos)
        start = tagPos
        if translation != "":
            proteinList.append(translation)
        else:
            pass
    proteinList = list(filter(None, proteinList)) 
    return proteinList
    