#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL || list->next == NULL)
		return (0);

	do {
		first = first->next;
		second = second->next;

		if (second == NULL || second->next == NULL)
			return (0);

		second = second->next;
	} while (first != second);

	return (1);
}

