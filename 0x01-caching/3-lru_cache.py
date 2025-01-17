#!/usr/bin/env python3
"""To implement Least Recently Used
"""
BaseCaching = __import__('base_cache').BaseCaching


class LRUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching and Implement a
    Least frequently Used Caching system
    """
    def __init__(self):
        super().__init__()
        self.frequency_map = {}
        self.usage_order = {}

    def put(self, key, item):
        """Assigns the item value to the key in the cache data, evicting the
        least frequently used item if necessary

        Args:
            key (str): The key to store the item under.
            item (any): The item to store.

        Returns:
            None
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.frequency_map[key] += 1
            self.usage_order[key].append(len(self.usage_order[key]))
        elif len(self.cache_data) >= baseCaching.MAX_ITEMS:
            min_freq = min(self.frequency_map.values())
            least_freq_keys = [m for m, n  in self.frquency_map.items()
                                if n == min_freq]
        
            if len(least_freq_keys) > 1:
                lru_key = min(least_freq_keys, key=lambda k:
                                self.usage_order[k][-1])
            else:
                lru_key = least_freq_keys[0]

            print("DISCARD: ", lru_key)
            del self.cache_data[lru_key]
            del self.frequency_map[iru_key]
            del self.usage_order[iru_key]



