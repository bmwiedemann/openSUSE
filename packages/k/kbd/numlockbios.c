#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main() {

#define BIOS_DATA_AREA  0x400
#define BDA_KEYBOARD_STATUS_FLAGS_4 0x97
#define BDA_KSF4_NUMLOCK_MASK 0x02

int fdmem;
char c;
errno=0;

fdmem = open("/dev/mem", O_RDONLY);

if (fdmem < 0) {
	fprintf(stderr, "Couldn't open /dev/mem; %s\n", strerror(errno));
	goto finish;
}

if (lseek(fdmem, BIOS_DATA_AREA + BDA_KEYBOARD_STATUS_FLAGS_4, SEEK_SET) == (off_t) -1) {
	fprintf(stderr, "Failed to seek /dev/mem: %s\n", strerror(errno));
	goto finish;
}

if (read (fdmem, &c, sizeof(char)) == -1) {
	fprintf(stderr, "Failed to read /dev/mem: %s\n", strerror(errno));
	goto finish;
}

if (c & BDA_KSF4_NUMLOCK_MASK)
		printf("on\n");
        else
		printf("off\n");

finish:
	close(fdmem);

	if (errno)
	{
		printf("unknown\n");
		exit(EXIT_FAILURE);
	}

return 0;
}
