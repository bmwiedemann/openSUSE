/*
 Copyright (c) 2020 SUSE LLC

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
*/

#define _GNU_SOURCE

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <errno.h>
#include <getopt.h>
#include <fcntl.h>

#ifndef RENAME_EXCHANGE
# define RENAME_EXCHANGE   (1 << 1)
#endif

static int verbose;

void help(const char* prog, int ret)
{
	printf("Usage: %s SOURCE TARGET\n", prog);
	puts("Exchange names of SOURCE and TARGET");
	exit(ret);
}

int main(int argc, char** argv)
{
	int c;
	int r;

	static struct option long_options[] = {
		{"verbose", no_argument,       0,  'v' },
		{"help",    no_argument,       0,  255 },
		{0,         0,                 0,  0 }
	};

        while ((c = getopt_long(argc, argv, "v", long_options, NULL)) != -1) {
		switch(c) {
			case 'v': ++verbose; break;
			case 255: help(argv[0], 0); break;
		}
	}

	if (argc-optind < 2)
		help(argv[0], 1);

	r = syscall (SYS_renameat2, AT_FDCWD, argv[optind], AT_FDCWD, argv[optind+1], RENAME_EXCHANGE);
	if (r < 0) {
		perror("renameat2");
		return 1;
	}

	return 0;
}
