#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about a Python list object
 * @p: The Python object to be analyzed
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i,
				list->ob_item[i]->ob_type->tp_name);
		if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}



/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: The Python object to be analyzed
 */

void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = bytes->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}
