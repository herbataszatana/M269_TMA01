"""
Test file for M269 20J TMA01 Question 3.
Student version 3: 23/03/20
"""

from M269_TMA01_20J_Q3 import percentBases, findCodon, translateGene, translateStrand

failed = 0
ran = 0

def test(name, actual, expected):
    """Report if test passed or failed."""
    global ran, failed
    if actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1

# The following DNA strand has three genes producing proteins with 7, 6 and 8 amino acids,
# which we have 'underlined'.
# Note the stray stop codon ('TAG') at the beginning should be ignored by translateGene.
# Only the first stop codon after a start codon ('ATG') should have an effect
dna1 = "TAGCATGTATGCCGGTTACCTGAGATAGACCACTTTCCTTCCGCATGTTACGCGGTATCGTCTAGACCACTTTCCTTCCGATGAATCCGGTGTACGCTAAGAGATAGACCATTACCCCCC"
# genes:    ------------------------                ---------------------               ---------------------------

# The following two strands have no genes, as there's no start/stop codon pair
dna2 = "CGATCGAT"
dna3 = "CCCCCCCC"


print()
print('Tests for percentBases')
print('========================')
print('== % results are in order C/G/A/T ==')
test('percentBases, long segment', percentBases(dna1), (30, 20, 22.5, 27.5))
test('percentBases, short segment ', percentBases(dna2), (25, 25, 25, 25))
test('percentBases, all same base', percentBases(dna3), (100, 0, 0, 0))


print()
print('Tests for translateGene')
print('========================')
dna2Start = findCodon(dna2, 0,'ATG')
dna2Stop  = findCodon(dna2, dna2Start,'TAG')
test('translateGene, short segment, no gene ', translateGene(dna2, dna2Start, dna2Stop), [])
dna1Start = findCodon(dna1, 0,'ATG')
dna1Stop  = findCodon(dna1, dna1Start,'TAG')
test('translateGene, long segment', translateGene(dna1, dna1Start, dna1Stop), ['Met', 'Tyr', 'Ala', 'Gly', 'Tyr', 'Leu', 'Arg'])
dna3Start = findCodon(dna3, 0,'ATG')
dna3Stop  = findCodon(dna3, dna3Start,'TAG')
test('translateGene, all same base, no gene', translateGene(dna3, dna3Start, dna3Stop), [])


print()
print('Tests for translateStrand')
print('==========================')

test('translateStrand, long segment, 3 genes', translateStrand(dna1),
     [['Met', 'Tyr', 'Ala', 'Gly', 'Tyr', 'Leu', 'Arg'],
      ['Met', 'Phe', 'Arg', 'Gly', 'Ile', 'Val'],
      ['Met', 'Asn', 'Pro', 'Val', 'Tyr', 'Ala', 'Lys','Arg']
     ])
test('translateStrand, further truncated segment, 1 gene', translateStrand(dna1[70:]),
     [
      ['Met', 'Asn', 'Pro', 'Val', 'Tyr', 'Ala', 'Lys','Arg']
     ])
test('translateStrand, short segment, no gene', translateStrand(dna2), [])


print()
print('================================================')
print()
print('All tests run:', ran - failed, 'OK,', failed, 'FAILED')
print('===========================================================================')
