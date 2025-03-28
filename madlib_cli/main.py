from madlib import read_template, parse_template, input_values, merge, write_madlib

print("This game is called Mad Libs.\n")
print("Instructions:")
print("""When asked for a word class (adjective, noun, verb, etc), type out
any word that fits the category.\n
For example, you might type \"tall\" when asked \"Adjective?\"\n
Once finished, the full story that is created will display.\n""")
print("Have fun!\n")

print("\n=== Game start ===\n")

file_contents = read_template("assets/dark_and_stormy_night_template.txt")
extracted_str, placeHolders = parse_template(file_contents)
user_responses = input_values(placeHolders)

print("\n=== Finished Mad Lib ===\n")
result = merge(extracted_str, user_responses)
print(result)

save = input("\nWould you like to save your finished Mad Lib? y/n: ")

if save.lower() == "y" or save.lower() == "yes":
  file_name = input("\nChoose a file name to save your madlib result: ")
  write_madlib(file_name, result)