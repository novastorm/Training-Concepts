#!/usr/bin/env python

import os
import sys 

here = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(here, '../'))

from project import app as application