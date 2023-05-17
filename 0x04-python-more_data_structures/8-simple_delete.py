#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
  Deletes a key from a dictionary.

  Args:
    a_dictionary: The dictionary to delete the key from.
    key: The key to delete.

  Returns:
    The dictionary without the key.
    """

    try:
        del a_dictionary[key]
    except KeyError:
        pass

    return a_dictionary
