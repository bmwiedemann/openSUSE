#
# spec file for package daemonize
#
# Copyright (c) 2024 SUSE LLC
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


Name:           daemonize
Version:        1.7.8
Release:        0
Summary:        Command line utility to run any program as a Unix daemon
License:        BSD-3-Clause
Group:          System/Console
URL:            https://github.com/bmc/daemonize
Source0:        %{name}-%{version}.tar.gz

%description
daemonize runs a command as a Unix daemon. As defined in W. Richard Stevens'
1990 book, Unix Network Programming (Addison-Wesley, 1990), a daemon is "a
process that executes 'in the background' (i.e., without an associated
terminal or login shell) either waiting for some event to occur, or waiting
to perform some specified task on a periodic basis." Upon startup, a typical
daemon program will:

- Close all open file descriptors (especially standard input, standard output
  and standard error)
- Change its working directory to the root filesystem, to ensure that it
  doesn’t tie up another filesystem and prevent it from being unmounted
- Reset its umask value
- Run in the background (i.e., fork)
- Disassociate from its process group (usually a shell), to insulate itself
  from signals (such as HUP) sent to the process group
- Ignore all terminal I/O signals
- Disassociate from the control terminal (and take steps not to reacquire one)
- Handle any SIGCLD signals

Most programs that are designed to be run as daemons do that work for
themselves. However, you’ll occasionally run across one that does not.
When you must run a daemon program that does not properly make itself into a
true Unix daemon, you can use daemonize to force it to run as a true daemon.

%prep
%autosetup

%build
sed -i -e 's|/sbin|/bin|' Makefile.in
%configure
%make_build

%install
%make_install

%files
%license LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog

