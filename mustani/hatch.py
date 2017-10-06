
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

class hatch():

    def __init__(self):
        self.plot_cache = [ ]
        self.key_value_store = { }

    def add(self, key, value):
        self.key_value_store[key] = value

    def get(self, key):
        if (key in self.key_value_store):
            return self.key_value_store[key]
        return None

    def extend_plot_cache(self, data):
        self.plot_cache.extend(data)

    def get_plot_cache(self):
        return self.plot_cache
