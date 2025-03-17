import re

def read_template(file_path):
  with open(file_path) as file:
    return file.read()

def parse_template(file_contents):
  match_regex = r"\{([^}]+)\}"
  placeHolders = re.findall(f"{match_regex}", file_contents)
  extracted_str = re.sub(f"{match_regex}", "{}", file_contents)
  return extracted_str, tuple(placeHolders)

def input_values(placeHolders):
  res_list = []
  for word_class in placeHolders:
    res_list.append(input(f"{word_class}? "))
  return tuple(res_list)

def merge(extracted_str, user_responses):
  result = extracted_str.format(*user_responses)
  return result

def write_madlib(file_name, result):
  with open(f"{file_name}.txt", "w") as file:
    file.write(result)