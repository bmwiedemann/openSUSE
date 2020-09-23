/*
 * Copyright Gerd Knorr <kraxel@suse.de>, 2003
 *
 * small tool to figure whenever a tty runs in utf8 mode or not.
 * writes a utf-8 multibyte sequence and then checks how far the
 * cursor has been moved.
 *
 * return codes:
 *	0 - don't know (stdin isn't a terminal, timeout, some error, ...)
 *      1 - not in utf8
 *      2 - utf-8
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <termios.h>
struct termios  saved_attributes;
int             saved_fl;
void
tty_raw()
{
    struct termios tattr;
        fcntl(0,F_GETFL,&saved_fl);
    tcgetattr (0, &saved_attributes);
    fcntl(0,F_SETFL,O_NONBLOCK);
    memcpy(&tattr,&saved_attributes,sizeof(struct termios));
    tattr.c_lflag &= ~(ICANON|ECHO);
    tattr.c_cc[VMIN] = 1;
    tattr.c_cc[VTIME] = 0;
    tcsetattr (0, TCSAFLUSH, &tattr);
}
void
tty_restore()
{
    fcntl(0,F_SETFL,saved_fl);
    tcsetattr (0, TCSANOW, &saved_attributes);
}
int
select_wait()
{
    struct timeval  tv;
    fd_set          se;
        FD_ZERO(&se);
    FD_SET(0,&se);
    tv.tv_sec = 3;
    tv.tv_usec = 0;
    return select(1,&se,NULL,NULL,&tv);
}
int
main(int argc, char **argv)
{
	static char *teststr = "\r\xc3\xb6";
	static char *cleanup = "\r  \r";
	static char *getpos  = "\033[6n";
	char retstr[16];
	int pos,rc,row,col,verbose;
	verbose = 0;
	if (argc > 1 && 0 == strcmp(argv[1],"-v"))
		verbose = 1;
	if (!isatty(0) || !isatty(1)) {
		if (verbose)
			fprintf(stderr,"Not a tty.\n");
		exit(0);
	}
	tty_raw();
	write(1,teststr,strlen(teststr));
	write(1,getpos,strlen(getpos));
	for (pos = 0; pos < sizeof(retstr)-1;) {
		if (0 == select_wait())
			break;
		if (-1 == (rc = read(0,retstr+pos,sizeof(retstr)-1-pos))) {
			perror("read");
			exit(0);
		}
		pos += rc;
		if (retstr[pos-1] == 'R')
			break;
	}
	retstr[pos] = 0;
	write(1,cleanup,strlen(cleanup));
	tty_restore();
	rc = sscanf(retstr,"\033[%d;%dR",&row,&col);
	if (2 == rc && 2 == col) {
		if (verbose)
			fprintf(stderr,"Terminal is in UTF-8 mode.\n");
		exit(2);
	} else {
		if (verbose)
			fprintf(stderr,"Terminal is in byte mode.\n");
		exit(1);
	}
}
