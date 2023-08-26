# Chapter 2 Arrays
We use Python lists to implement different array classes.

## Array
An Array class with simple methods.
* __Constructor__ - The array is stored as a list.
* __Length__ - A special def for `len()` to return the number of items.
* __Getter__ - Returns the value at index `n` with bounds check.
* __Setter__ - Set the value at index `n` with bounds check.
* __Insertion__ - Insert item at the end of the array.
* __Find__ - Find the index for an item, if not found return -1.
* __Searching__ - Search for an item and return the item if found.
* __Deletion__ - Delete first occurrences of an item; move items from right over 1.
* __Traversing__ - Traverse all items and apply a function (print by default).

## OrdereArray
An Array with ordered items.
* __Constructor__ - The array is stored as a list.
* __Length__ - A special def for `len()` to return the number of items.
* __Getter__ - Returns the value at index `n` with bounds check.
* __Traversing__ - Traverse all items and apply a function (print by default).
* __String__ - Return the array as a string.
* __Find__ - Use _binary search_ algorithm to search for item.
* __Searching__ - Search for an item and return the item if found.
* __Insertion__ - Insert item into the correct position.
* __Deletion__ - Delete first occurrences of an item; move items from right over 1.

## Logarithms
Comparisons needed for linear and binary searches.
Range | binary | linear
:--|:--|:--
10 | 4 | 5
100 | 7 | 50
1,000 | 10 | 500
10,000 | 14 | 5,000
100,000 | 17 | 50,000
1,000,000 | 20 | 500,000
10,000,000 | 24 | 5,000,000
100,000,000 | 27 | 50,000,000
1,000,000,000 | 30 | 500,000,000

## OrderedRecordArray
An Array of records instead of single items.
* __Constructor__ - The array stored as a list  with a key.
* __Length__ - A special def for `len()` to return the number of items.
* __Getter__ - Return the value at index `n` with bounds check.
* __Traversing__ - Traverse all items and apply a function (print by default).
* __String__ - Return the array as a string.
* __Find__ - Find index at or just below key in ordered list.
* __Searching__ - Search for a record by its key and return item if found.
* __Insertion__ - Insert item into the correct position.
* __Deletion__ - Delete any occurrence, try to find the item if found.
