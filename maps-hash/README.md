# MAPS & HASH

Maps are key-value structured store. We can lookup an utem by its key. Maps are also called dictionaries

# SETS

Comparable to a list, has no ordering but does not allow duplicates. Just like you cannot have same word, multiple times in a dictionary
A group of maps (key-value pairs) is a set.

In Python, the map concept appears as a built-in data type called a dictionary. A dictionary contains key-value pairs. Dictionaries might soon become your favorite data structure in Python—they're extremely easy to use and useful. Here's a sample of setting up a dictionary

```
udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7

print udacity
# {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}
```

In this case, the letters in "udacity" were each keys in our dictionary, and the position of that letter in the string was the value. Thus, I can do the following:

```
print udacity['t']
#6
```

This statement is saying "go to the key labeled 't' and find it's value, 6".

Dictionaries are wonderfully flexible—you can store a wide variety of structures as values. You store another dictionary or a list:

```
dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print udacity
# {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y':[10]}
```

# HASHING

Using a data structure that employs the use of a hasj function allows you to do lookup in constant time.
In Linear Time

## How Hash Functions Work

The purpose of a hash function is to transform some value into one that can be stored and retrieved easily.
You give it a value, it returns a coded version of the value (using a formula -> hash function) usu the index in an array

# Hash Table / Hash Map

HashMap - A type of data structure that maps keys to its value pairs. The keys are generated via a hash function. Also called dictionary, map, hash table or associative arrays.
It doesn't allow duplicate keys
It takes O(1) to insert, retrieve and delete
In python, use dict
The main components of a hashmap are:

- Array (List) data structure used to store the data
- Hash function - function used to convert the key into a numeric index
- Coliision - When more than one key hashes to the same index. The performance of the hash function depends on not having many values in the same index
- Collision Handling

Hash Function
index = sum(ascii value for each letter in key) % len(list)
