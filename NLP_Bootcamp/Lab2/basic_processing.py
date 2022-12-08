import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')

# 1
story = ''
with open('..\\Material\\TextFiles\\owlcreek.txt', 'r') as f:
    story = f.read()
doc = nlp(story)
print(doc[:36])

# 2
print(len(doc))

# 3
sents = list(doc.sents)
print(len(sents))

# 4
print(sents[1])

# 5
for t in sents[1]:
    print(f'{t.text:{10}} {t.pos_:{10}} {t.lemma_:{10}}  {t.dep_:{10}}')

# 6
matcher = Matcher(nlp.vocab)
pattern = [[{'LOWER': 'swimming'}, {'IS_SPACE':True, 'OP':'*'}, {'LOWER': 'vigorously'}]]
matcher.add('Swimming',pattern)
found_matches = matcher(doc)
print(found_matches)

# 7
for found in found_matches:
    print(str(doc[found[1]-5:found[2]+5]).replace('\n', ' '))