"""
Practice dictionary and efficient ways to execute it

"""

dict_one = {"zara": 20, "h&M": 40, "vero-moda": 10}

"""
copy  a dictionary
"""

dct_copy_one = dict_one.copy()
print(f" Copy of the original dictionary is  {dct_copy_one}")

# ways to merge two dictionaries
dict_two = {
    "sparx": 2,
    "skechers": 30
}
merge = dict_one.copy()
for key, value in dict_two.items():
    merge[key] = value

print(f" Merged dictionary is  {merge}")
# use update to merge two dictionaries
(merge_copy_update := dict_one.copy()).update(dict_two)

print(f" New merged dictionary using copy/update  {merge_copy_update}")

# with python 3.9 , it has become a lot easier to update dictionaries
# | will create a new dictionary and |= with update it, order of operations is important in this case
merge_3_9 = dict_one | dict_two

print(f" New merged dictionary with python 3.9  {merge_3_9}")

print(f" Before merged dictionary with python 3.9  {dict_one}")
dict_one |= dict_two

print(f" Update merged dictionary with python 3.9  {dict_one}")

# get max value in dictionary, if you run the max operation on the dictionary then it will fetch the max key

max_key = max(dict_one)

print(f" max operation on the dictionary  {max_key.upper()}")

# now to get the key with the max value

max_value_key = max(dict_one, key=lambda k: dict_one[k])
print(f" max value of the key operation on the dictionary  {max_value_key.upper()}")

key = lambda k: dict_one[k]
print(f" key  {key('vero-moda')}")

# get the default value in the dictionary if the key does not exist
locations = {'meeting1': 'room1', 'meeting2': 'room2'}
locations_value = locations.get("meeting2", "Unknown")
print(f" fetch value from dictionary  {locations_value.upper()}")
locations_value = locations.get("meeting3", "Unknown")
print(f" fetch value from dictionary {locations_value.upper()}")

#  use nested dictionary

fruits = [
    {"name": "apple", "attr": {"color": "red", "taste": "sweet"}},
    {"name": "orange", "attr": {"taste": "sour"}},
    {"name": "grape", "attr": {"color": "purple"}},
    {"name": "banana"},
]

# it will replace the colour with unknown if the key is not present
color = [fruit.get("attr", {}).get("color", "unknown") for fruit in fruits]
print(f" list of colours in the fruit")

# create a dictionary from a list

list_1 = ["bottle", "glass", "cup"]
value_1 = "home center"

item_dict = dict.fromkeys(list_1, value_1)

print(f" dictionary created from list {item_dict}")

