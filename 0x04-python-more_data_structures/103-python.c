#include <Python.h>
#include<stdio.h>

/**
 * print_python_list - print basic info
 * @p: a PyObject
*/
void print_python_list(PyObject *p) {
    PyListObject *list;
    PyVarObject *var;
    Py_ssize_t i, size;

    list = (PyListObject *)p;
    var = (PyVarObject *)p;
    size = var->ob_size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", var->ob_alloc);

    for (i = 0; i < size; i++) {
        PyObject *item = list->ob_item[i];
        const char *typeName = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, typeName);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

/**
 * print_python_bytes - print basic info
 * @p: a PyObject
*/

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes;
    PyVarObject *var;
    Py_ssize_t size, i;

    bytes = (PyBytesObject *)p;
    var = (PyVarObject *)p;
    size = var->ob_size;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyUnicode_AsUTF8(PyObject_Repr(p)));

    printf("  first %ld bytes:", (size > 10) ? 10 : size);
    for (i = 0; i < ((size > 10) ? 10 : size); i++) {
        printf(" %02x", bytes->ob_sval[i] & 0xff);
    }
    printf("\n");
}
