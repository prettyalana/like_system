"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to
create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names
of people that like an item. It must return the display text as
shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.  
"""

def like_summary(names):
    
    display_text = ""
    
    if len((names)) == 0:
        display_text = "no one likes this" 
    elif len((names)) == 1: 
       display_text = f"{names[0]} likes this"
    elif len((names)) == 2:
        display_text = f"{names[0]} and {names[1]} like this"
    elif len((names)) == 3:
        display_text = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len((names)) >= 4:
        display_text = f"{names[0]}, {names[1]} and {len((names)) - 2} others like this"
        
    return display_text

# Our testing code is below.
# 🔒 Please do not make changes below this line!

prompt_answers = [
    {'names': [], 'expected': "no one likes this"},
    {'names': ["Peter"], 'expected': "Peter likes this"},
    {'names': ["Jacob", "Alex"], 'expected': "Jacob and Alex like this"},
    {'names': ["Max", "John", "Mark"], 'expected': "Max, John and Mark like this"},
    {'names': ["Alex", "Jacob", "Mark", "Max"], 'expected': "Alex, Jacob and 2 others like this"},
    {'names': ["Alex", "Jacob", "Mark", "Max", "Bob"], 'expected': "Alex, Jacob and 3 others like this"},
]

def test_like_summary(prompt, expected_result):
    result = like_summary(prompt)
    response = f"like_summary: {prompt} becomes `{result}`. "
    success = result == expected_result
    response += "✅ correct!" if success else "🤔 not quite"
    print(response)
    return success

for prompt_item in prompt_answers:
    assert test_like_summary(prompt_item['names'], prompt_item['expected']), "Looks like it still needs some work..."
