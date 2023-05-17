#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: The Python object to be analyzed
 */
void print_python_list(PyObject *p)
{
	long int size;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (int i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: The Python object to be analyzed
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size;
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
	for (int i = 0; i <= size && i < 10; i++)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
}
