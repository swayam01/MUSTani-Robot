#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

class compare():

    def __init__(self, debug, util):
        self.debug = debug
        self.util = util
        self.learned_dictionary = self.util.getDICT()
        self.dict_analysis = self.util.compile_analysis(self.learned_dictionary)
        self.results = { }

    def reset(self):
        self.results = { }

    def get_results(self):
        return self.results

    def word(self, characteristics):
        ll = len(characteristics)-1
        if (ll == 0):
            self.results = { }
            for id in self.dict_analysis:
                self.results[id] = [ ]
        self.area(characteristics[ll], ll)

    def area(self, characteristic_object, ll):
        characteristic, _ = characteristic_object
        for id in self.dict_analysis:
            self.results[id].append([ ])
            for x in range(0, len(self.results[id])):
                self.results[id][x].append(0)
        for dict_entries in self.learned_dictionary['dict']:
            id = dict_entries['id']
            for x in range(0, len(self.results[id])):
                dict_c_pos = len(self.results[id][x])-1
                if (dict_c_pos < len(dict_entries['characteristic'])):
                    dcharacteristic = dict_entries['characteristic'][dict_c_pos]
                    fast_sim = self.util.single_similarity(characteristic['fc'], dcharacteristic['fc'])
                    if (fast_sim > self.results[id][x][dict_c_pos]):
                        self.results[id][x][dict_c_pos] = fast_sim
