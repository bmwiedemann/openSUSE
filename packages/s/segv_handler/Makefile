CFLAGS=-Wall -fPIC -O2

all: segv_handler.so testprog

segv_handler.so: segv_handler.o
	gcc $(CFLAGS) -shared -o $@ $^ $(LIBS)

segv_handler64.so: segv_handler.c
	gcc $(CFLAGS) -m64 -shared -o $@ $^ $(LIBS)

segv_handler32.so: segv_handler.c
	gcc $(CFLAGS) -m32 -shared -o $@ $^ $(LIBS)

testprog: testprog.c
	$(CC) -g -o testprog testprog.c

test: all
	-LD_PRELOAD=./segv_handler.so ./testprog
	ls -l /var/log/segv/segv_testprog.*

clean:
	/bin/rm -f *.o *.so *~ testprog /tmp/segv_testprog.*
