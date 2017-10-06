#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import filter
import visual
import util
import config
import hatch

class preparing():

    def __init__(self, hatch):
        self.hatch = hatch
        self.visual = visual.visual()
        self.util = util.util(self.hatch.get('debug'))
        self.filter = filter.filtering(self.hatch)
        self.silence = 0
        self.force = False
        self.counter = 0
        self.token_start = False
        self.new_token = False
        self.new_word = False
        self.token_counter = 0
        self.buffer = [ ]
        self.peaks = [ ]
        self.token_peaks = [ ]
        self.last_low_pos = 0
        self.force = False
        self.entered_silence = False

    def tokenize(self, meta):
        if (self.valid_token(meta)):
            if (len(self.buffer) == 0):
                self.buffer = [ 0 ] * 512
            self.filter.filter(self.buffer, meta)
            self.buffer = [ ]
            self.peaks.extend(self.token_peaks)
            self.token_peaks = [ ]
            if (self.force):
                self.reset()
                self.filter_reset()

    def valid_token(self, meta):
        for m in meta:
            if (m['token'] == 'noop'):
                self.reset()
                return False
        return True

    def stop(self):
        if (self.hatch.get('plot') == True):
            self.visual.create_sample(self.hatch.get_plot_cache(), 'sample.png')
        self.tokenize([{ 'token': 'stop' }])
        self.filter.stop()
        self.filter_reset()
        self.reset()

    def reset(self):
        self.counter = 0
        self.token_start = False
        self.new_token = False
        self.new_word = False
        self.token_counter = 0
        self.buffer = [ ]
        self.peaks = [ ]
        self.token_peaks = [ ]
        self.last_low_pos = 0
        self.force = False

    def filter_reset(self):
        if (self.token_counter > 0):
            self.filter.reset()

    def force_tokenizer(self):
        self.force = True
        self.tokenize([ { 'token': 'start analysis', 'silence': self.silence, 'pos': self.counter, 'adapting': 0, 'volume': 0, 'peaks': self.peaks } ])
  
    def prepare(self, buf, volume):
        data = numpy.fromstring(buf, dtype=numpy.int16)
        if (self.hatch.get('plot') == True and self.hatch.get('endless_loop') == False):
            self.hatch.extend_plot_cache(data)
        self.buffer.extend(data)
        self.counter += 1
        abs_data = abs(data)
        adaptive = sum(abs_data)
        self.token_peaks.append(adaptive)
        meta = [ ]

        if (volume < config.THRESHOLD):
            self.silence += 1
            if (self.silence == config.LONG_SILENCE):
                self.new_word = True
                self.entered_silence = True
                self.peaks.extend(self.token_peaks)
                meta.append({ 'token': 'start analysis', 'silence': self.silence, 'pos': self.counter, 'adapting': adaptive, 'volume': volume, 'token_peaks': self.token_peaks, 'peaks': self.peaks })
                self.peaks = [ ]
            elif (self.silence > config.LONG_SILENCE):
                meta.append({ 'token': 'noop', 'silence': self.silence, 'pos': self.counter, 'adapting': adaptive, 'volume': volume })
        else:
            self.entered_silence = False
            self.silence = 0

        if (len(self.buffer) == config.CHUNKS):
            self.new_token = True
            meta.append({ 'token': 'token', 'silence': self.silence, 'pos': self.counter, 'adapting': adaptive, 'volume': volume, 'token_peaks': self.token_peaks })

        if (self.new_token == True or self.new_word == True):
            self.new_token = False
            self.token_counter += 1
            self.tokenize(meta)
            if (self.new_word == True):
                self.new_word = False
