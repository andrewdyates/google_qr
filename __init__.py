#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
# Copyright © 2010 Andrew D. Yates
# All Rights Reserved.
"""QR Code Interface for Google Charts HTTP API.

References:
  [Documentation]
  http://code.google.com/apis/chart/docs/gallery/qr_codes.html
"""
__authors__ = ['"Andrew D. Yates" <andrew.yates@hhmds.com>',]


import os
import urllib
import urllib2


# API constants
URL = "http://chart.apis.google.com/chart"
CHT = 'qr'
MIME = 'image/png'

# Default values for API
SIZE = 540
CODE = 'UTF-8'
LEVEL = 'H'
MARGIN = 0


class QR(object):
  """Fetch a QR Code from Google's Chart API.

  Attributes:
    chart: str of binary output in 'image/png' format or None
  """

  def __init__(self, data, size=SIZE, code=CODE, level=LEVEL, margin=MARGIN):
    """Initialize and fetch QR code image from HTTP API web service.

    See [Documentation] for complete Google Chart API for QR Codes.

    Args:
      data: str to encode in QR code image
      size: int of width and height of QR image
      code: str of QR character output encoding
      level: str of output QR error correction level
      margin: int of rows of margin in QR image

    Raises:
      ValueError: HTTP service returned an error
    """
    # set to None in case of an exception
    self.chart = None
    parameters = {
      'cht': CHT,
      'chl': data,
      'chs': str(size),
      'chld': "%s|%s" % (level, margin),
      'choe': code,
      }
    post_data = urllib.urlencode(parameters)
    try:
      response = urllib2.urlopen(URL, post_data)
    except urllib2.HTTPError, e:
      if e.code == 400:
        raise ValueError(e.read())
      else:
        raise
    self.chart = response.read()
