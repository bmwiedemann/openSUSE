#if 0
set -- gcc -W -Wall -g -O2 -shared -nostdlib -Wl,-f,libopenal.so.1 -Wl,-soname,libopenal.so.0 -fPIC -DPIC -o libopenal.so.0 libopenalcompat.c 
echo "$@"
exec "$@"
exit 1
#endif
#if 0
void* alcOpenDevice (void* p) { return (void*)0; }
#endif
void _openal_soft_dummy_ () { }
