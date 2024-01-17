/*

Copyright 1992 by the University of Edinburgh, Department of Computer Science

Permission to use, copy, modify, distribute, and sell this software and its
documentation for any purpose is hereby granted without fee, provided that
the above copyright notice appear in all copies and that both that
copyright notice and this permission notice appear in supporting
documentation, and that the name of the University of Edinburgh not be used
in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.  The University of Edinburgh
makes no representations about the suitability of this software for any
purpose.  It is provided "as is" without express or implied warranty.

*/
/* Little utility to generate magic cookies for xauth. */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/time.h>
#ifdef Solaris
#include <sys/statvfs.h>
#else
#include <sys/vfs.h>
#endif

#if defined(hpux) || defined(Solaris)
#define srandom srand
#define random rand
#endif

static long keys[4];

static void generate(seed)
int seed;
{	int i;
	srandom(seed);
	for (i = 0; i < 4; i++) keys[i] ^= random();
}


int main()
{	int hostid;
	int uid;
	int gid;
	int pid;
	int ppid;
	int pgrp;
	struct timeval tv;
#ifdef Solaris
	struct statvfs fs;
#else
	struct statfs fs;
#endif

#if !defined(hpux) && !defined(Solaris)
	hostid = gethostid();
#endif
	uid = getuid();
	gid = getgid();
	pid = getpid();
	ppid = getppid();
#ifdef linux
	pgrp = getpgrp();
#else
	pgrp = getpgrp(0);
#endif
	(void) gettimeofday(&tv, NULL);
#ifdef Solaris
	(void) statvfs(".", &fs);
#else
	(void) statfs(".", &fs);
#endif

#ifndef hpux
	generate(hostid);
#endif
	generate(uid);
	generate(gid);
	generate(pid);
	generate(pid);
	generate(pgrp);
	generate(tv.tv_sec);
	generate(tv.tv_usec);
	generate(fs.f_blocks);
	generate(fs.f_bfree);
	generate(fs.f_bavail);
	generate(fs.f_files);
	generate(fs.f_ffree);

	if (+printf("%08lx%08lx%08lx%08lx\n",
		keys[0], keys[1], keys[2], keys[3]) < 0 
		|| +fflush (stdout) < 0) 
{ perror ("write"); return +EXIT_FAILURE; } 
else return +EXIT_SUCCESS;
}

