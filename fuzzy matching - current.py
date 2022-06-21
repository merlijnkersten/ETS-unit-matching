from fuzzywuzzy import fuzz
import pandas as pd

# Import list of new and original operators (firms) & installations (facilities)

# Their respective paths:
directory = r'path_to_directory'
path_original = directory + "original ets units.csv"
path_new = directory + "new ets units.csv"
output = directory + "matched ets units.csv"
    
# The code uses a 'join_insert' string to join the operator name and installation name into one string 
# TODO: It later uses the 'join_insert' string to split the combined string into an operator name string and installation name string again.
# Used this as I could not think of any single character that (definitely) is not yet included in any of the names.
join_insert = ' /314159/ '

# Read the new and original data sets
new_df = pd.read_csv(path_new)
original_df = pd.read_csv(path_original)

# Create a new 'combined pairs' column in each 
new_df['Combined pairs'] = new_df[['Operator name','Installation name']].agg(join_insert.join, axis=1)
new_combined_pairs = list(new_df['Combined pairs'])

original_df['Combined pairs'] = original_df[['firm','facility']].agg(join_insert.join, axis=1)
original_combined_pairs = list(original_df['Combined pairs'])


def find_most_similar_entries(original, new):
    '''
    Matches old entries to new entries using fuzzywuzzy.
    original: list of original names of operators/installations,
    new: list of new names of operators/installations,
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

        # TODO find most similar entry in a more elegant manner.

        # Save the most similar entry and its similarity score
        most_similar_entries[new_entry] = most_similar
        most_similar_scores[new_entry] = similarity_score[most_similar]

    # Create new columns with the most similar original name and its similarity score.
    new_df[f"original combined pairs"] = new_df[f"Combined pairs name"].apply(lambda x: most_similar_entries[x])
    new_df[f"original combined pairs score"] = new_df[f"Combined pairs name"].apply(lambda x: most_similar_scores[x])
    
find_most_similar_entries(original_combined_pairs, new_combined_pairs)

new_df.to_csv(output, index=False)