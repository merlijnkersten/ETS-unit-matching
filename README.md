# README
_February-March 2022_


This folder contains files to match ETS (European Union emission trading system) facility and company names in the Czech Republic across two files. `ETS_id_list_2015.xlsx` is the original file which contains 2015 data, `ETS_art10a_national_alocation_2021-2026_Czechia.xlsx` is the new file which contains 2021-2026 data. They both use different naming conventions for the same unit, the goal is to match the specific facilities across the two files in order to get the ETS codes from the 2015 file for each unit in the 2021-2026 file. Both files were converted into a new/original ETS units list `.csv`. 

| Data     | Scope     | Excel file                                        | CSV file                 | 
| -------- | --------- |-------------------------------------------------- | ------------------------ |
| Original | 2015      | `ETS_id_list_2015`                                | `original ets unit list` |
| New      | 2021-2026 | `ETS_art10a_national_alocation_2021-2026_Czechia` | `new ets unit list`      |

There are two versions of the code. `fuzzy matching - original.py` matches the facility and company names independently. The new version of the code, `fuzzy matching - current.py` combines the facility and company names before matching, resulting in more correct matches. However, the matched data still needs extensive editing and QA. The efficacy of the original and new scripts is listed in the table below:

| Result        | Old method | New method    |
| ------------- | ---------- | ------------- |
| Match         | 183 (79%)  | 214-216 (93%) |
| Partial match | 37 (16%)   | n/a           |
| No match      | 11 (5%)    | 17-15 (7%)    |

The 'fuzzy matching - check matched pairs.py` is for quality control.

The `matched ETS units.csv` is the output of the fuzzymatching, correction, and QA process. 