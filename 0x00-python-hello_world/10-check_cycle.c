#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of linked list
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *l1, *l2;

	if (!list)
	{
		return (0);
	}
	l1 = list;
	l2 = list->next;
	while (l2 && l1 && l2->next)
	{
		if (l1 == l2)
		{
			return (1);
		}
		l1 = l1->next;
		l2 = l2->next->next;
	}
	return (0);
}
