#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>

static int segv_handler(int sig)
{
	char cmd[100];
	char progname[100];	
	char *p;
	int n;

	n = readlink("/proc/self/exe",progname,sizeof(progname));
	progname[n] = 0;

	p = strrchr(progname, '/');
	*p = 0;
	
	snprintf(cmd, sizeof(cmd), "backtrace %d > /tmp/segv_%s.%d.out 2>&1", 
		 (int)getpid(), p+1, (int)getpid());
	system(cmd);
	signal(SIGSEGV, SIG_DFL);
	return 0;
}

void _init(void)
{
	signal(SIGSEGV, segv_handler);
}
