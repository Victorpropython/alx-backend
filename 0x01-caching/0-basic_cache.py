#!/usr/bin/env python3
"""A Class BasicCache that inherits from BaseCaching and is a cachng system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inherits from BaseCaching and implements
    a simple caching system without a size limit
    """
    def put(self, key, item):
        """put method to add key and item value in the cache data

        Args:
            key (str): The key to store the item under.
            item (any): The item to store.
        Returns:
            None
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with the key frm the cache

        Args:
            key (str): The key toretrieve the iten from

        Returns:
            The value associated with the key, or None if the key is not
            found or is None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
