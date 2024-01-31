#!/usr/bin/env python3
"""
This module contains a LFUCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching
from collections import Counter

class LFUCache(BaseCaching):
    """
    LFUCache class. This caching system uses a LFU alg
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = []
        self.counts = Counter()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        if key not in self.keys:
            if len(self.keys) >= BaseCaching.MAX_ITEMS:
                least_common = self.counts.most_common()[:-2:-1]
                if len(least_common) > 1:
                    least_common = [item for item in least_common if item[1] == least_common[0][1]]
                    least_common = sorted(least_common, key=lambda x: self.keys.index(x[0]))
                discarded_key = least_common[0][0]
                self.keys.remove(discarded_key)
                del self.cache_data[discarded_key]
                del self.counts[discarded_key]
                print('DISCARD: {}'.format(discarded_key))
            self.keys.append(key)
        self.cache_data[key] = item
        self.counts[key] += 1

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.counts[key] += 1
        return self.cache_data[key]

