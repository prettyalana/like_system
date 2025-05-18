=begin
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
=end

def like_summary(names)
  display_text = ""

  if names.length == 0
    display_text = "no one likes this"
  elsif names.length == 1
    display_text = "#{names[0]} likes this"
  elsif names.length == 2
    display_text = "#{names[0]} and #{names[1]} like this"
  elsif names.length == 3
    display_text = "#{names[0]}, #{names[1]} and #{names[2]} like this"
  elsif names.length >= 4
    display_text = "#{names[0]}, #{names[1]} and #{names.length - 2} others like this"
  end
end

# Our testing code is below.
# 🔒 Please do not make changes below this line!

prompt_answers = [
  {names: [], expected: "no one likes this"},
  {names: ["Peter"], expected: "Peter likes this"},
  {names: ["Jacob", "Alex"], expected: "Jacob and Alex like this"},
  {names: ["Max", "John", "Mark"], expected: "Max, John and Mark like this"},
  {names: ["Alex", "Jacob", "Mark", "Max"], expected: "Alex, Jacob and 2 others like this"},
  {names: ["Alex", "Jacob", "Mark", "Max", "Bob"], expected: "Alex, Jacob and 3 others like this"},
]

def test_like_summary(prompt, expected_result)
  result = like_summary(prompt)
  response = "like_summary: #{prompt} becomes `#{result}`. "
  success = result == expected_result
  if success
    response += "✅ correct!"
  else
    response += "🤔 not quite"
  end
  puts response
  return success
end

prompt_answers.each do |prompt_item|
  if test_like_summary(prompt_item[:names], prompt_item[:expected])
  else
    puts "Looks like it still needs some work..."
  end
end
