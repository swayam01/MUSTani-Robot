#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class err_logger():

    def __init__(self):
        print ('redirecting stderr to error.log!')
        fsock = open('error.log', 'a')
        sys.stderr = fsock
