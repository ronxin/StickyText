#!/usr/bin/env python
from docstructure import *
from readability import *
from cohesion import *

s = "Today I am going to drink some beer. The beer comes from Chicago.\n\nMy wife, Lily, likes the bear. She says she would often love watching me drinking. What a lovely wife.\n\nI would so much want this to end as soon as possible. My life. This is so counterintuitive. I call it counterintuitivitabilism."

d = Document(s)

'''
print "[WHOLE DOCUMENT]"
print d
print "[PAR 0]"
print d.pars[0]
print "[PAR 1]"
print d.pars[1]
print "[SENT 1 PAR 1]"
print d.pars[1].sents[1]
print "[PWORD 1 PAR 1]"
print d.pars[1].pwords[1]
print "[WORD 2 SENT 1 PAR 1]"
print d.pars[1].sents[1].words[2]
print "[WORD 0 SENT 1 PAR 1]"
print d.pars[1].sents[1].words[0]
print "[NUMSYL WORD 0 SENT 1 PAR1]"
print d.pars[1].sents[1].words[0].numsyl()

# Test number of syllables
#for i in d.words:
#    print str(i)+' '+str(i.numsyl())


print "[FLESCH READING EASE]"
print flesch_reading_ease(d)

print "[FLESCH-KINCIAD GRADE-LEVEL]"
print flesch_kinciad_grade_level(d)

print "[FOG GRADE-LEVEL]"
print fog_grade_level(d)

print "[EXAMPLE STEMMED WORDS]"
print ' '.join([str(x) for x in d.sents[5].scwords])

'''

print "\n[JACCARD INDEX]"
print jaccard_index(d.sents[0], d.sents[1], words_typed(True, False))
print jaccard_index(d.sents[0], d.sents[1], words_typed(False, True))
print jaccard_index(d.sents[0], d.sents[1], words_typed(False, False))


print "\n[WORD OVERLAP COHESION]"
print word_overlap_cohesion(d, True, words_typed(False, True))
print word_overlap_cohesion(d, True, words_typed(True, True))
print word_overlap_cohesion(d, False, words_typed(False, True))
print word_overlap_cohesion(d, False, words_typed(False, False))

print "\n[WORD FREQ DIST COHESION]"
print word_dist_cohesion(d, True, words_typed(True, True))
print word_dist_cohesion(d, False, words_typed(True, True))
