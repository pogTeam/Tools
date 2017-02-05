#!/usr/local/bin/python
# -*- coding: utf-8 -*-

### BASE64
import base64
data = "U0hDe2lzc29fw6lfdW1hX2ZsYWd9"
dec = base64.b64decode(data)
print(dec)

### BASE32
data = "KNEEG63JNZUWG2LBNZSG6X3PL5TWC3LFPU======"
dec = base64.b32decode(data)
print(dec)
