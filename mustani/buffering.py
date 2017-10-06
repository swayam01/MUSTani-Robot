#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import processing
import hatch

class buffering(multiprocessing.Process):

    def __init__(self, hatch, queue):
        multiprocessing.Process.__init__(self, name="buffering queue")
        self.hatch = hatch
        self.queue = queue
        self.proc = processing.processor(hatch, self)
        self.PROCESS_ROUND_DONE = False
        self.test_counter = 0
        self.start()
  
    def run(self):
        if (self.hatch.get('debug') == True):
            print ("buffering queue runner")
        while True:
            buf = self.queue.get()
            if ((self.hatch.get('endless_loop') == False or self.hatch.get('outfile') != None) and self.PROCESS_ROUND_DONE):
                break
            self.proc.check_silence(buf)
        if (self.hatch.get('debug') == True):
            print ("terminating queue runner")

    def flush(self, message):
        self.proc.stop(message)
 
    def stop(self):
        if (self.hatch.get('debug') == True):
            print ("stop buffering")
        self.PROCESS_ROUND_DONE = True
