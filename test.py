from readability import Readibility

text = '''he idea of ‘plant behaviour’ may seem odd, given the association of the word ‘behaviour’ with animals, including humans. When we think of classic animal behaviours – dancing honeybees, dogs wagging their tails, primates grooming each other – we may wonder what there could possibly be in plant life corresponding to this.'''

print(Readibility._flesch_kincaid_eval_fn(text))