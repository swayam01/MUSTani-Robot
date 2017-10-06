#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import json
import numpy

class numpyjsonencoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = numpy.ascontiguousarray(obj)
                if (cont_obj.flags['C_CONTIGUOUS']):
                    obj_data = cont_obj.data
                else:
                    raise Exception("numpyjsonencoder err: C_CONTIGUOUS not present in object!")
            data_base64 = base64.b64encode(obj_data)
            return dict(__ndarray__= data_base64, dtype = str(obj.dtype), shape = obj.shape)
        return json.JSONEncoder(self, obj)

def numpyjsonhook(obj):
    if isinstance(obj, dict) and '__ndarray__' in obj:
        data = base64.b64decode(obj['__ndarray__'])
        return numpy.frombuffer(data, obj['dtype']).reshape(obj['shape'])
    return obj
