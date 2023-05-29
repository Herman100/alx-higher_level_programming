#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: The PyObject pointer representing the Python list.
 *
 * Description: This function prints information about a Python list object.
 * It checks if the provided PyObject is
 * a valid list object, retrieves the size
 * of the list, the allocated memory, and prints information about each element
 * in the list.
 */

void print_python_list(PyObject *p)
{
	long int size;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (int i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
}


/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: The PyObject pointer representing the Python bytes object.
 *
 * Description: This function prints information about a Python bytes object.
 * It checks if the provided PyObject is a
 * valid bytes object, retrieves the size
 * of the bytes object, the string representation,
 * and prints the first 10 bytes
 * in hexadecimal format.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (int i = 0; i <= size && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}



/**
 * print_python_float - Prints information about a Python float object.
 * @p: The PyObject pointer representing the Python float object.
 *
 * Description: This function prints information about a Python float object.
 * It checks if the provided PyObject
 * is a valid float object and retrieves the
 * float value, which is then printed with a precision of 16 decimal places.
 */
void print_python_float(PyObject *p)
{
	double val;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %.16g\n", val);
}
