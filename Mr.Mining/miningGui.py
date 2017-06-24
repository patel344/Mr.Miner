#!/usr/bin/env python
from subprocess import call
"""

setx GPU_FORCE_64BIT_PTR 0
setx GPU_MAX_HEAP_SIZE 100
setx GPU_USE_SYNC_OBJECTS 1
setx GPU_SINGLE_ALLOC_PERCENT 100
setx GPU_MAX_ALLOC_PERCENT 100
ethminer.exe -F http://eth-eu1.nanopool.org:8888/YOUR_ADDRESS/MINER_NAME/YOUR_EMAIL -U

"""

def ethereumConfig():
    address = '0x2fc7723d8623eb414abb4fa6d81395d81b87a8f9'
    miner_name = 'MikeTheMiner'
    email = 'igalfsg@gmail.com'
    call("setx GPU_FORCE_64BIT_PTR 0", shell=True)
    call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
    call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
    call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
    call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)
    call("ethminer.exe -F http://eth-eu1.nanopool.org:8888/"+address+"/"+miner_name+"/"+email+" -I", shell=True)


def setupGeth():
    pass

if __name__ == '__main__':
    ethereumConfig()