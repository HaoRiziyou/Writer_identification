from distutils.core import setup as __setup
from distutils.core import Extension as __extension
import os as __os
import glob as __glob
import sys
import os

def __build():
    import os
    devnull = open(os.devnull,"w")
    stdout, stderr=sys.stdout,sys.stderr
    sys.stdout,sys.stderr = devnull, devnull

    cwd_bup = __os.getcwd()

    try:
        modulePath = __os.path.dirname(__os.path.realpath(__file__))
        print("Building library '" + __os.path.basename(modulePath) + "' ...")
    
        __os.chdir(modulePath)
    
        sources = __glob.glob('__src/*.c')
        #print("   Sources:", sources)
    
        module1 = __extension('__lib',
                              sources=sources)

        __setup(name='__lib',
                ext_modules=[module1],
                script_args=["build_ext", "--inplace"])

    finally:
        __os.chdir(cwd_bup)
        sys.stdout,sys.stderr = stdout, stderr

__build()

from .__src.wrappers import *
