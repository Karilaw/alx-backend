#!/usr/bin/env python3
"""
This module contains a LRUCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    LRUCache class. This caching system uses a LRU alg
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
