import spacy

nlp = spacy.load('en_core_web_sm')

# 1
story = ''
with open('..\\Material\\TextFiles\\peterrabbit.txt', 'r') as f:
    story = f.read()
doc = nlp(story)
print(doc[:36])

# 2
sents = list(doc.sents)
for t in sents[2]:
    print(f'{t.text:{10}}   {t.pos_:{10}}   {t.tag_:{10}}   {spacy.explain(t.tag_):{10}}')

# 3
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts)

for k,v in sorted(POS_counts.items()):
    print(f"id:{k}  POS:{doc.vocab[k].text}  {v} counts")

# 4
num_tokens = len(doc)
noun_tokens= POS_counts[92]
print(noun_tokens/num_tokens*100)

# 5
spacy.displacy.serve(sents[2], style='dep')

# 6
for ent in doc.ents[:2]:
    print(ent.text + '   ' + ent.label_ + '   ' + str(spacy.explain(ent.label_)))

# 7
print(len(sents))

# 8
entities = [e.text for e in doc.ents]
count = 0
for sentence in sents:
    for word in str(sentence):
        if word in entities:
            count+=1
            break

# 9
spacy.displacy.serve(sents[0], style='dep')