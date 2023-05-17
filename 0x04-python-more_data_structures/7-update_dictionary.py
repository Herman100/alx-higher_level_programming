#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
  """
  Replaces or adds key/value in a dictionary.

  Args:
    a_dictionary: The dictionary to update.
    key: The key to update or add.
    value: The value to update or add.

  Returns:
    The updated dictionary.
  """

  if key in a_dictionary:
    a_dictionary[key] = value
  else:
    a_dictionary[key] = value

  return a_dictionary

