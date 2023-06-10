#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print a pyhton list
 *
 * @p: list object to be printed
 *
 * Return: list
 */

void print_python_list_info(PyObject *p)
{
	const char *type_name;
	PyObject *element;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
