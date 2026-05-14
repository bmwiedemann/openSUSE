#include <sys/syscall.h>
#ifdef __aarch64__
#include <signal.h>
#endif
#include <unistd.h>
#ifdef __aarch64__
sigset_t mask;
#endif

void _start() {
#ifdef __aarch64__
    sigemptyset(&mask);
    syscall(SYS_rt_sigsuspend, &mask, 8);
#else
    syscall(SYS_pause);
#endif
}
