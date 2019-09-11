#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <errno.h>
#include <limits.h>
#include <pty.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <termios.h>
#include <unistd.h>

static sig_atomic_t died;
static void sigchld(int sig __attribute__((__unused__)))
{
    const int old_errno = errno;
    int status;
    pid_t pid;
    while ((pid = waitpid(-1, &status, WNOHANG|WUNTRACED)) != 0) {
	if (errno == ECHILD)
	    break;
	if (pid < 0)
	    continue;
	died = 1;
    }
    errno = old_errno;
}

static pid_t pid = -1;
static void sigother(int sig)
{
    printf("%s\n", strsignal(sig));
    if (sig == SIGINT)
	sig = SIGTERM;
    if (pid > 0) kill(pid, sig);
}

int main(int argc, char* argv[])
{
    int ptm, pts;
    ssize_t len;
    static struct termios o;
    static struct winsize w;
    char devname[NAME_MAX+1];
    char buffer[65536];
    sigset_t set;
    struct sigaction sa;

    if (ioctl(0, TIOCGWINSZ, &w) < 0) {
	w.ws_row = 24;
	w.ws_col = 160;
	errno = 0;
    }
    if (tcgetattr(0, &o) < 0) {
#ifdef B115200
	cfsetispeed(&o, B115200);
	cfsetospeed(&o, B115200);
#elif defined(B57600)
	cfsetispeed(&o, B57600);
	cfsetospeed(&o, B57600);
#elif defined(B38400)
	cfsetispeed(&o, B38400);
	cfsetospeed(&o, B38400);
#endif
    }

    o.c_iflag  = TTYDEF_IFLAG;
    o.c_oflag  = TTYDEF_OFLAG;
    o.c_lflag  = TTYDEF_LFLAG;
# ifdef CBAUD
    o.c_lflag &= ~CBAUD;
# endif
#ifdef B115200
    o.c_cflag  = B115200;
#elif defined(B57600)
    o.c_cflag  = B57600;
#elif defined(B38400)
    o.c_cflag  = B38400;
#endif
    o.c_cflag |= TTYDEF_CFLAG;

    /* Sane setting, allow eight bit characters, no carriage return delay
     * the same result as `stty sane cr0 pass8'
     */
    o.c_iflag |=  (BRKINT | ICRNL | IMAXBEL);
    o.c_iflag &= ~(IGNBRK | INLCR | IGNCR | IXOFF | IUCLC | IXANY | INPCK | ISTRIP);
    o.c_oflag |=  (OPOST | ONLCR | NL0 | CR0 | TAB0 | BS0 | VT0 | FF0);
    o.c_oflag &= ~(OLCUC | OCRNL | ONOCR | ONLRET | OFILL | OFDEL |\
		   NLDLY|CRDLY|TABDLY|BSDLY|VTDLY|FFDLY);
    o.c_lflag |=  (ISIG | ICANON | IEXTEN | ECHO|ECHOE|ECHOK|ECHOKE);
    o.c_lflag &= ~(ECHONL|ECHOCTL|ECHOPRT | NOFLSH | XCASE | TOSTOP);
    o.c_cflag |=  (CREAD | CS8 | HUPCL);
    o.c_cflag &= ~(PARODD | PARENB);
    /*
     * VTIME and VMIN can overlap with VEOF and VEOL since they are
     * only used for non-canonical mode. We just set the at the
     * beginning, so nothing bad should happen.
     */
    o.c_cc[VTIME]    = 0;
    o.c_cc[VMIN]     = CMIN;
    o.c_cc[VINTR]    = CINTR;
    o.c_cc[VQUIT]    = CQUIT;
    o.c_cc[VERASE]   = CERASE; /* ASCII DEL (0177) */
    o.c_cc[VKILL]    = CKILL;
    o.c_cc[VEOF]     = CEOF;
# ifdef VSWTC
    o.c_cc[VSWTC]    = _POSIX_VDISABLE;
# else
    o.c_cc[VSWTCH]   = _POSIX_VDISABLE;
# endif
    o.c_cc[VSTART]   = CSTART;
    o.c_cc[VSTOP]    = CSTOP;
    o.c_cc[VSUSP]    = CSUSP;
    o.c_cc[VEOL]     = _POSIX_VDISABLE;
    o.c_cc[VREPRINT] = CREPRINT;
    o.c_cc[VDISCARD] = CDISCARD;
    o.c_cc[VWERASE]  = CWERASE;
    o.c_cc[VLNEXT]   = CLNEXT;
    o.c_cc[VEOL2]    = _POSIX_VDISABLE;

    if (openpty(&ptm, &pts, devname, &o, &w) < 0) {
	perror("pty: can not open pty/tty pair");
	exit(1);
    }

    (void)sigemptyset(&set);
    (void)sigaddset(&set, SIGCHLD);
    sigprocmask(SIG_UNBLOCK, &set, (sigset_t*)0);

    sa.sa_flags = SA_RESTART;
    sa.sa_handler = sigchld;
    sigemptyset (&sa.sa_mask);
    sigaction(SIGCHLD, &sa, (struct sigaction*)0);

    (void)sigemptyset(&set);
    (void)sigaddset(&set, SIGTERM);
    sigprocmask(SIG_UNBLOCK, &set, (sigset_t*)0);

    sa.sa_flags = SA_RESTART;
    sa.sa_handler = sigother;
    sigemptyset (&sa.sa_mask);
    sigaction(SIGTERM, &sa, (struct sigaction*)0);

    (void)sigemptyset(&set);
    (void)sigaddset(&set, SIGHUP);
    sigprocmask(SIG_UNBLOCK, &set, (sigset_t*)0);

    sa.sa_flags = SA_RESTART;
    sa.sa_handler = sigother;
    sigemptyset (&sa.sa_mask);
    sigaction(SIGHUP, &sa, (struct sigaction*)0);

    switch ((pid = fork())) {
    case 0:
	ioctl(1, TIOCNOTTY);
	if (setsid() < 0) {
	    perror("pty: can not get controlling tty");
	    exit(1);
	}
	dup2(pts, 0);
	dup2(pts, 1);
	dup2(pts, 2);
	close(pts);
	close(ptm);
	if (ioctl (0, TIOCSCTTY, 1) < 0) {
	    perror("pty: can not get controlling tty");
	    exit(1);
	}
	break;
    case -1:
	close(pts);
	close(ptm);
	perror("pty: can not fork");
	exit(1);
    default:
	dup2(ptm, 0);
	close(pts);
	close(ptm);
	while ((len = read(0, buffer, sizeof(buffer)))) {
	    ssize_t p = 0;
	    const char* ptr = buffer;
	    while (len > 0) {
		p = write(1, ptr, len);
		if (p < 0) {
		    if (errno == EPIPE)
			exit (0);
		    if (errno == EINTR || errno == EAGAIN)
			continue;
		    return 1;
		}
		ptr += p;
		len -= p;
	    }
	    if (died)
		break;
	}
	return 0;
    }

    (void)sigfillset(&set);
    sigprocmask(SIG_UNBLOCK, &set, (sigset_t*)0);

    (void)sigemptyset(&set);
    (void)sigaddset(&set, SIGCHLD);
    sigprocmask(SIG_BLOCK, &set, (sigset_t*)0);

    sa.sa_flags = SA_RESTART;
    sa.sa_handler = SIG_DFL;
    sigemptyset (&sa.sa_mask);

    sigaction(SIGHUP, &sa, (struct sigaction*)0);
    sigaction(SIGINT, &sa, (struct sigaction*)0);
    sigaction(SIGPIPE, &sa, (struct sigaction*)0);
    sigaction(SIGTERM, &sa, (struct sigaction*)0);
    sigaction(SIGURG,  &sa, (struct sigaction*)0);
    sigaction(SIGXFSZ,  &sa, (struct sigaction*)0);
    sigaction(SIGQUIT, &sa, (struct sigaction*)0);

    sa.sa_handler = SIG_IGN;
    sigaction(SIGQUIT, &sa, (struct sigaction*)0);

    return  execv(argv[1], &argv[1]);
}
