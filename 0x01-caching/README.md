PROJECT      0X01. CACHING
Repo:
    •	GitHub repository: alx-backend
    •	Directory: 0x01-caching
Background Context
    •	In this project, you learn different caching algorithms.
Resources Read or watch:
    •	Cache replacement policies - FIFO
    •	Cache replacement policies - LIFO
    •	Cache replacement policies - LRU
    •	Cache replacement policies - MRU
    •	Cache replacement policies - LFU
General learning objectives at the end of this project, you are expected to be able to explain to anyone, without the help of google:
    •	What a caching system is
    •	What FIFO means
    •	What LIFO means
    •	What LRU means
    •	What MRU means
    •	What LFU means
    •	What the purpose of a caching system
    •	What limits a caching system have
Python scripts requirements
    •	All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    •	All your files should end with a new line
    •	The first line of all your files should be exactly #!/usr/bin/env python3
    •	A README.md file, at the root of the folder of the project, is mandatory
    •	Your code should use the pycodestyle style (version 2.5)
    •	All your files must be executable
    •	The length of your files will be tested using wc
    •	All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    •	All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    •	All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    •	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
More Info
    •	Parent class BaseCaching
    •	All your classes must inherit from BaseCaching defined below:
Tasks
0.	Basic dictionary
    •	Create a class BasicCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	This caching system doesn’t have limit
        o	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
    •	If key or item is None, this method should not do anything.
        o	def get(self, key): Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
1.	FIFO caching
    Create a class FIFOCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    •	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
        o	If key or item is None, this method should not do anything.
        o	If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            	you must discard the first item put in cache (FIFO algorithm)
            	you must print DISCARD: with the key discarded and following by a new line
    •	def get(self, key):
        o	Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
    1-fifo_cache.py
2.	LIFO Caching
    Create a class LIFOCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    •	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
        o	If key or item is None, this method should not do anything.
        o	If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            	you must discard the last item put in cache (LIFO algorithm)
            	you must print DISCARD: with the key discarded and following by a new line
    •	def get(self, key):
        o	Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
    •	File: 2-lifo_cache.py
3.	LRU Caching
    Create a class LRUCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    •	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
        o	If key or item is None, this method should not do anything.
        o	If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        o	you must discard the least recently used item (LRU algorithm)
        o	you must print DISCARD: with the key discarded and following by a new line
    •	def get(self, key):
        o	Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
    •	File: 3-lru_cache.py
4.	MRU Caching
    Create a class MRUCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    •	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
        o	If key or item is None, this method should not do anything.
        o	If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            	you must discard the most recently used item (MRU algorithm)
            	you must print DISCARD: with the key discarded and following by a new line
    •	def get(self, key):
        o	Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
    •	File: 4-mru_cache.py
5. LFU Caching this is an advanced task 
    Create a class LFUCache that inherits from BaseCaching and is a caching system:
    •	You must use self.cache_data - dictionary from the parent class BaseCaching
    •	You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    •	def put(self, key, item):
        o	Must assign to the dictionary self.cache_data the item value for the key key.
        o	If key or item is None, this method should not do anything.
        o	If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            	you must discard the least frequency used item (LFU algorithm)
            	if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
            	you must print DISCARD: with the key discarded and following by a new line
    •	def get(self, key):
        o	Must return the value in self.cache_data linked to key.
        o	If key is None or if the key doesn’t exist in self.cache_data, return None.
    •	File: 100-lfu_cache.py
