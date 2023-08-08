#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to pointer of the first node of listint_t list
 * @number: Integer to be included in new node
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;

    if (*head == NULL || (*head)->n >= number)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        current = *head;
        while (current && current->n < number)
        {
            prev = current;
            current = current->next;
        }
        new->next = current;
        prev->next = new;
    }

    return (new);
}
