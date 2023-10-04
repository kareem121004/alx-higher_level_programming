#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *temp;

	temp = *head;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (temp == NULL || temp->n >= number)
	{
		newnode->next = temp;
		*head = newnode;
		return (newnode);
	}

	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}

	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
