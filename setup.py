##from distutils.core import setup
##import py2exe
##setup(console=['LiteATS_v3.1.py'])
#!/usr/bin/python
 
from distutils.core import setup
import py2exe
 

setup(
    options={"py2exe":{"optimize": 2,
##                       "bundle_files": 2,
                       "dll_excludes": ["packet"]}},
    console=[
        dict(script = 'Advent10.py',
			dest_base = "Advent10")],
    zipfile = "resources.lib",
 
)
