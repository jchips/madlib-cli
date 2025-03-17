import re

def read_template(file_path):
  with open(file_path) as file:
    return file.read()

file_contents = read_template('assets/dark_and_stormy_night_template.txt')
print(file_contents)

def parse_template(file_contents):
  placeHolders = re.findall('\\{(\\w+)\\}', file_contents)
  extracted_str = re.sub('\{(\w+)\}', '{}', file_contents)
  print(placeHolders)
  print(extracted_str)
  return extracted_str, tuple(placeHolders)

parse_template(file_contents)

def merge(arg):
  pass