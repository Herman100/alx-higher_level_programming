#!/usr/bin/python3
def weight_average(my_list=[]):
    """
  Returns the weighted average of all integers tuple (<score>, <weight>).

  Args:
    my_list: A list of tuples, where the first element is
    the score and the second element is the weight.

  Returns:
    The weighted average of all scores in the list.
    """

    if not my_list:
        return 0

    sum_of_weights = sum(weight for score, weight in my_list)
    sum_of_weighted_scores = sum(score * weight for score, weight in my_list)

    return sum_of_weighted_scores / sum_of_weights
