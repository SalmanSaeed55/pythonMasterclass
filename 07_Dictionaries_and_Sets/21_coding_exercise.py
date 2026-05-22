text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
text_words = set(text.casefold().split())
preps_used = text_words.intersection(prepositions)
print(preps_used)