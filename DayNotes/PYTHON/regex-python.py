"""
Code to understand the regex in python
1. First thing is to import the re module
2. We know we have to match/search patterns in a string ,we need to ideally create pattern
re.compile(r'\d\d\d')
3.Character class in regex
3. match the pattern in the given input. pattern.search("string_to_be_searched") --> looks for only first possible match
4. re.finditer(text) --> find all instances  [extract all the patterns and print it]
"""
import re
import logging

logging.basicConfig(filename='regex_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

text_passed = 'ABCD 123'
pattern = re.compile(r'\d\d\d')
# now search will give only the first instance found in the data,
# but we need to find all the patterns so use re.finditer
matched_data = pattern.search(text_passed)
logging.debug(f" matched found is {matched_data} {matched_data.group()} {type(matched_data)}")

matched_loop = pattern.finditer(text_passed)

for match in matched_loop:
    logging.debug(f" The patterns are {match} {match.group()} {type(matched_data)}")

# Understanding character class
"""
\d --> matches all digits from 0-9
\w --> match any letter/digit/underscore
\s --> for space character
\D --> for any digit character
\W  --> non - word character (not a letter digit or underscore)
\S --> non-space character

Symbols
() : group patterns together
+: look for the charcter one or more than one 
*:
{}: repeat character  like \d{3} -- three digits continuously , \d{3,5} match for min of three or max of five,
 \d{,5} from zero to max of 5
?: indicate optional value '\d?', if used after {}, then it means the patterns needs to be matched with a single pattern
.: Special character it can match with any value other than \n
[]: create your own character class, like search for vowels [aeiou]
|: it is a OR search
^: match the beginning of the text, [^] every character other than the mentioned in the square bracket
$: ends with this character

"""

# question -one : match all the dates coming in the data

text_to_be_matched = '''So today, in this post 12-Apr-2021 I’d like to share with you 10 methods that we can use to convert ,12-Jan-2021,
a text to date format in Excel. For converting a text to date we need to use a combination of different functions.
12-Jun-2032, 24.06.2022, 24/06/2022, 25-09-2022
'''

# pattern_date = re.compile(r'\d{2}-[a-zA-Z]{3}-\d{4}')
# match = pattern_date.finditer(text_to_be_matched)
# if match is not None:
#     logging.debug(f" diff pattern  matched value is {match}  {type(match)}")
#     for mat in match:
#         logging.debug(f" diff pattern  matched value is  {mat.group()}")

logging.debug(f" proceed further ")
# for mat in match:
#     logging.debug(f" matched value is {mat}")
pattern_date = re.compile(r'\d{2}[./-]([a-zA-z]{3}|[0-9]{2})[./-]\d{4}')
match = pattern_date.finditer(text_to_be_matched)
if match is not None:
    # logging.debug(f" diff pattern  matched value is {match}  {type(match)}")
    for mat in match:
        logging.debug(f" diff pattern  matched value is  {mat.group()}")

text_value = 'www.twitter.com// www.reddit.com www.toad.com'
pattern_social = re.compile(r'[w]{3}[.][twitter]*[.][com]*')
match_social = pattern_social.finditer(text_value)

if match_social is not None:
    for mat_scl in match_social:
        logging.debug(f" The social matched value is {mat_scl.group()}")

# match email id coming in the data
text_to_be_email = '''So today, in this post 12-Apr-2021 I’d like to share with you 10 methods that we can use to convert ,12-Jan-2021,
a text to date format in Excel. extrernal_90@dummy.com whyhow123@neut.com For converting a text to date we need to use a combination of different functions.
12-Jun-2032, 24.06.2022, 24/06/2022, 25-09-2022 new_dummy@newvale.co.in
+60230-112 1221 ,+601101-100 3344,017-20202000
'''

pattern_email = re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+')
match_social = pattern_email.finditer(text_to_be_email)

if match_social is not None:
    for mat_scl in match_social:
        logging.debug(f" The email  matched value is {mat_scl.group()}")


