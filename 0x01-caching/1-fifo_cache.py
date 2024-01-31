#!/usr/bin/env python3
"""
This module contains a FIFOCache class that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class. This caching system uses a FIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        if key not in self.keys:
            self.keys.append(key)
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
