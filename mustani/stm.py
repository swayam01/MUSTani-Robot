
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import config

class short_term_memory():

    def __init__(self, debug):
        self.debug = debug
        self.last_results = [ ]
        self.last_time = 0

    def get_stm_results(self, results):
        stm_results = self.last_results[:]
        stm_results.extend(results)
        return stm_results

    def get_results(self, results):
        if (results == None or len(results) == 0):
            return results
        if (time.time() < self.last_time):
            if (self.debug):
                print ('stm input: ' + str(results) + ' '  + str(self.last_results))
            results = self.get_stm_results(results)
            if (self.debug):
                print ('stm mnodification: ' + str(results))
        self.last_results = results
        self.last_time = time.time() + config.STM_RETENTION
        return results
