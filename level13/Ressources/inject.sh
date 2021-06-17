gcc -shared -fpic lib.c -o libnike.so -m32
LD_PRELOAD=./libnike.so $*
