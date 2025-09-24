#ifndef _GNU_SOURCE
# define _GNU_SOURCE
#endif
#define REPORT	/* Default is to report the kbs character */
#include <errno.h>
#include <fcntl.h>
#include <getopt.h>
#include <ncursesw/curses.h>
#include <ncursesw/term.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#ifndef REPORT
# include <termios.h>
#endif
#include <unistd.h>
extern char *program_invocation_short_name;

int main(int argc, char *argv[])
{
    char *kbs;
    char *errmsg;
    const char *term = secure_getenv("TERM");
#ifdef REPORT
    int erase;
#else
    struct termios tio;
#endif
    int c, index = 0;
    static struct option options[] = {
        {"help",  no_argument,       0, 'h'},
        {"term",  required_argument, 0, 't'}
    };

    while (1) {
        c = getopt_long(argc, argv, "ht:", options, &index);
        if (c < 0)
            break;
        switch (c) {
        case 't':
            term = optarg;
            break;
        case 'h':
        case '?':
        default:
            fprintf(stderr, "%s reports the control character used for erase in the terminfo database.\n", program_invocation_short_name);
            fprintf(stderr, "Usage: %s [-h] [-t <TERM>]\n", program_invocation_short_name);
            return 0;
        }
    }

    errmsg = "The environment variable TERM is missed";
    if (!term || *term == '\0')
        goto fail;
    errmsg = "setupterm() failed";
    if (setupterm(term, STDIN_FILENO, (int *)0) != OK)
        goto fail;
    errmsg = "tigetstr() failed";
    if ((kbs = tigetstr("kbs")) == NULL || kbs == (char *)-1)
        goto fail;
    errmsg = "erase value not a character";
    errno = EINVAL;
    if (strlen(kbs) != 1)
        goto fail;
#ifdef REPORT
    if (*kbs < 20)
        erase = (*kbs)+64;
    else if (*kbs == 127)
        erase = '?';
    else {
        errmsg = "erase value is a printable character";
        goto fail;
    }
    printf("^%c\n", erase);
#else
    errmsg = "tcgetattr() failed";
    if (tcgetattr(STDIN_FILENO, &tio) < 0)
        goto fail;
    tio.c_cc[VERASE] = *kbs;
    errmsg = "tcsetattr() failed";
    if (tcsetattr(STDIN_FILENO, TCSANOW, &tio) < 0)
        goto fail;
#endif
    return 0;
fail:
    fprintf(stderr, "%s: %s: %m\n", program_invocation_short_name, errmsg);
    return 1;
}
