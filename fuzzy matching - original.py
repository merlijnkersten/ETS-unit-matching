from fuzzywuzzy import fuzz
import pandas as pd

"""
# Simple ratio - Levenshtein distance
fuzz.ratio(string1, string2)
# Partial ratio - matches the shortest string to a substring of the longer string
fuzz.partial_ratio(string1, string2)
# Token-sort ratio - tokenises and sorts string before matching
fuzz.token_sort_ratio(string1, string2)
# Token-set ratio - tokenises and analyses ratios of common/not-common tokens.
fuzz.token_set_ratio(string1, string2)
"""

# Import list of new and original operators (firms) & installations (facilities)
path_new = r"C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/ETS units_new.csv"

new_df = pd.read_csv(path_new)
new_operators = list(new_df['Operator name'])
new_installations = list(new_df['Installation name'])

path_original = r"C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/ETS units_original.csv"

original_df = pd.read_csv(path_original)
original_operators = list(original_df['firm'])
original_installations = list(original_df['facility'])

"""#Alternative, DataFrame approach
from itertools import product

# Create a new 
# Slower
df = pd.DataFrame(list(product(new_operators, original_operators)))

df.columns = ['new','original']

def fuzzy_ratio(a, b):
    return fuzz.token_set_ratio(a, b)

df['fuzzy_ratio'] = df.apply(lambda row: fuzzy_ratio(row.new, row.original), axis=1)

idx = df.groupby(['new'])['fuzzy_ratio'].transform(max) == df['fuzzy_ratio']


df[idx].reset_index().to_csv(r"C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/ETS units OUTPUT 2.csv")

#print(df.groupby(by=['new'])['fuzzy_ratio'].sort())

#df['col_3'] = df.apply(lambda x: f(x.col_1, x.col_2), axis=1)

"""


def find_most_similar_entries(original, new, kind):
    '''
    Matches old entries to new entries using fuzzywuzzy.
    original: list of original names of operators/installations,
    new: list of new names of operators/installations,
    kind: 'Operator' or 'Original'
    '''

    # Empty dictionaries. Key: new name, 
    # value: most similar original name/similarity score of the most similar original name.
    most_similar_entries = dict()
    most_similar_scores = dict()


    for new_entry in new:

        # Key: original entry, value: similarity score to the new entry.
        similarity_score = dict()

        # Find similarity score for every original entry to the new entry.
        for original_entry in original:
            similarity_score[original_entry] = fuzz.token_set_ratio(new_entry, original_entry)
        
        # Find the most similar entry 
        most_similar = sorted(similarity_score, key=similarity_score.get, reverse=True)[0]

        # Save the most similar entry and its similarity score
        most_similar_entries[new_entry] = most_similar
        most_similar_scores[new_entry] = similarity_score[most_similar]

    # Create new columns with the most similar original name and its similarity score.
    new_df[f"original {kind.lower()}"] = new_df[f"{kind} name"].apply(lambda x: most_similar_entries[x])
    new_df[f"original {kind.lower()} score"] = new_df[f"{kind} name"].apply(lambda x: most_similar_scores[x])

# Run previous function for both operator and installation names.
find_most_similar_entries(original_operators, new_operators, "Operator")
find_most_similar_entries(original_installations, new_installations, "Installation")

new_df.to_csv(r"C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/ETS units OUTPUT 3.csv", index=False)