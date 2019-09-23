CFLAGS=-Wall -fPIC -O2

all: segv_handler.so testprog

segv_handler.so: segv_handler.o
	ld -shared -o $@ $^ $(LIBS)

testprog: testprog.c
	$(CC) -g -o testprog{,.c}

test: all
	-LD_PRELOAD=./segv_handler.so ./testprog
	ls -l /tmp/segv_testprog.*

clean:
	/bin/rm -f *.o *.so *~ testprog /tmp/segv_testprog.*
