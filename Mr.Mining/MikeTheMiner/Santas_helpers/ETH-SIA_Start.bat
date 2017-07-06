setx GPU_FORCE_64BIT_PTR 0
setx GPU_MAX_HEAP_SIZE 100
setx GPU_USE_SYNC_OBJECTS 1
setx GPU_SINGLE_ALLOC_PERCENT 100
setx GPU_MAX_ALLOC_PERCENT 100
Santas_helpers\Claymore_dual\EthDcrMiner64.exe -epool eth-eu1.nanopool.org:9999 -ewal 0x3fc999b03089458cbc79b9f206049bbb5edb4565/1/1 -epsw x -dpool stratum+tcp://sia-eu1.nanopool.org:7777 -dwal 12/1/1 -dpsw x -dcoin sia -ftime 10