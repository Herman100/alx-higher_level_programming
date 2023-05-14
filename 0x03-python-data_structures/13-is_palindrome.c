#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[2048], i = 0, j;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		values[i] = current->n;
		current = current->next;
		i++;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (values[j] != values[i - j - 1])
			return (0);
	}

	return (1);
}
