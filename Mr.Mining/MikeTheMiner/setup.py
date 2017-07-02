#from distutils.core import setup
#import py2exe

#setup(console=['main.py'])

#coding=utf-8

from cx_Freeze import setup, Executable

includes = ["atexit"]

"""buildOptions = dict(
    #create_shared_zip=False,
    append_script_to_exe=True,
    includes=includes
)"""

executables = [
    Executable(
        script='main.py',
        targetName='MisterMiner.exe',
        base="Win32GUI" # THIS ONE IS IMPORTANT FOR GUI APPLICATION
    )
]

setup(
    name="MisterMiner",
    version="1.0",
    description="GUI for CryptoCurrency Mining",
    #options=dict(build_exe=buildOptions),
    executables=executables
)