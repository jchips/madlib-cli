import re

def read_template(file_path):
  with open(file_path) as file:
    return file.read()

def parse_template(file_contents):
  placeHolders = re.findall(r'\{([^}]+)\}', file_contents)
  extracted_str = re.sub(r'\{([^}]+)\}', '{}', file_contents)
  return extracted_str, tuple(placeHolders)

def input_values(placeHolders):
  res_list = []
  for word_class in placeHolders:
    res_list.append(input(f'{word_class}? '))
  return tuple(res_list)

def merge(extracted_str, user_responses):
  result = extracted_str.format(*user_responses)
  return result