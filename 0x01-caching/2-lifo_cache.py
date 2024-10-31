#!/usr/bin/env python3
"""Class to implement Last in First out
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class inherits from BaseCaching and implements
    a Last-In-First-Out (LIFO) caching system."""

    def put(self, key, item):
        """Assigns the item value to the key in the cache data,
        evicting the newest item if necessary.

        Args:
            key (str): The key to store the item under.
            item (any): The item to store.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]  # Get the last key
                print("DISCARD:", last_key)
                del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item associated with the key from the cache.

        Args:
            key (str): The key to retrieve the item from.

        Returns:
            The value associated with the key, or None if the key
            is not found or is None.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
