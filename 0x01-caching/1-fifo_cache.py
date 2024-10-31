#!/usr/bin/env python3
"""A class FIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A simple class for a firstin first out order of caching
    """
    def __init__(self):
        """to iniitialize the queue
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assigns item value to the key in cache data evicting the
        oldest item if necessary

        Args:
            key (str): The key to store the item under
            item (any): The item to be store

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.queue.pop(0)
                print("DISCARD:", first_key)
                del self.cache_data[first_key]
        
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with the key from the cache

        Args:
            key (str): The key to retrievr the item from

        Returns:
            The value associated with the key, or None if the key is not
            found or is None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
