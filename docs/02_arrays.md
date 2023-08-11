# DataPython

## Chapter 2 Arrays
We use Python lists to implement different array classes.

### Array
An Array class with simple methods:
* __Constructor__ - The array is stored as a list.
* __Length__ - A special def for len() to return the number of items.
* __Getter__ - Returns the value at index `n` with bounds check.
* __Setter__ - Set the value at index `n` with bounds check.
* __Insertion__ - Insert item at the end of the array.
* __Find__ - Find the index for an item, if not found return -1.
* __Searching__ - Search for an item and return the item if found.
* __Deletion__ - Delete first occurrences of an item; move items from right over 1.
* __Traversing__ - Traverse all items and apply a function (print by default).

### OrdereArray
An Array with ordered items
* __Constructor__ - The array is stored as a list.
* __Length__ - A special def for len() to return the number of items.
* __Getter__ - Returns the value at index `n` with bounds check.
* __Traversing__ - Traverse all items and apply a function (print by default).
* __String__ - Return the array as a string.
* __Find__ - Use _binary search_ algorithm to search for item.
* __Searching__ - Search for an item and return the item if found.
* __Insertion__ - Insert item at the end of the array.
* __Deletion__ - Delete first occurrences of an item; move items from right over 1.
