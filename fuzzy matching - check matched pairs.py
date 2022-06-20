
import pandas as pd

path = "C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/matched.csv"

matched = pd.read_csv(path)

path = "C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/new.csv"

new = pd.read_csv(path)

path = "C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/original.csv"

original = pd.read_csv(path)

# LOOKUP facility FOR EVERY original operator AND
# LOOK UP firm FOR EVERY original installation AND
# CHECK WHETHER THEY MATCH

# Operator to installation (firm to facility)
o_t_i = dict(
    zip(
        list(original['firm']), list(original['facility'])
        )
    )

# Installation to operator (facility to firm)
i_t_o = dict(
    zip(
        list(original['facility']), list(original['firm'])
        )
    )

matched['operator to installation'] = matched['original operator'].apply(lambda a: o_t_i[a] if a in o_t_i.keys() else None)

matched['operator to installation match'] = matched['original installation'] == matched['operator to installation']

matched['installation to operator'] = matched['original installation'].apply(lambda a: i_t_o[a] if a in i_t_o.keys() else None)

matched['installation to operator match'] = matched['original operator'] == matched['installation to operator']

matched['complete match'] = (matched['installation to operator match'] and matched['operator to installation match'])



path = "C:/Users/Merlijn Kersten/Documents/Univerzita Karlova/matched 2.csv"

matched.to_csv(path, index=False)

"""
['Installation name','Operator name',
 'original operator','original installation']
['firm','facility']

"""
