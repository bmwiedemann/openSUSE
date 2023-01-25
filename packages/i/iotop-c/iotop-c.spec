#
# spec file for package iotop-c
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           iotop-c
Version:        1.23
Release:        0
Summary:        Simple top-like I/O monitor (implemented in C)
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/Tomas-M/iotop
Source:         %{name}-%{version}.tar.xz
Conflicts:      iotop
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)

%description
iotop-c does for I/O usage what top(1) does for CPU usage. It watches I/O usage
information output by the Linux kernel and displays a table of current I/O usage
by processes on the system. It is handy for answering the question "Why is the
disk churning so much?".

iotop-c requires a Linux kernel built with the CONFIG_TASKSTATS,
CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING and CONFIG_VM_EVENT_COUNTERS
config options on.

iotop-c is an alternative re-implementation of iotop in C, optimized for
performance. Normally a monitoring tool intended to be used on a system under
heavy stress should use the least additional resources as possible.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
V=1 STRIP=: %make_install

%files
%{_sbindir}/*
%{_mandir}/man8/*
%license LICENSE
%doc README.md

%changelog
