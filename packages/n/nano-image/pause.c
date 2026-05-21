// SPDX-License-Identifier: MIT
// SPDX-FileCopyrightText: (c) 2026 SUSE LLC

#include <sys/syscall.h>
#include <unistd.h>

void _start() {
#ifdef SYS_pause
    syscall(SYS_pause);
#else
    syscall(SYS_ppoll, NULL, 0, NULL, NULL);
#endif
}
