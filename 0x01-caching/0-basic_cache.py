#!/usr/bin/env python3
"""
This module contains a BasicCache class that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class. This caching system doesn’t have limit.
    It inherits self.cache_data - dictionary
    from the parent class BaseCaching.
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
