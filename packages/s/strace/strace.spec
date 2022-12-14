#
# spec file for package strace
#
# Copyright (c) 2021 SUSE LLC
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


Name:           strace
Version:        6.1
Release:        0
Summary:        A utility to trace the system calls of a program
License:        BSD-3-Clause
Group:          Development/Tools/Debuggers
URL:            http://strace.io/
#Freecode-URL:	http://freecode.com/projects/strace
#Git-Clone:	git://github.com/strace/strace
Source:         https://github.com/strace/strace/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source2:        https://github.com/strace/strace/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source3:        %{name}.keyring
Source4:        baselibs.conf
BuildRequires:  haveged
BuildRequires:  libacl-devel
BuildRequires:  libaio-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  libdw-devel
%else
# libunwind is broken on ppc and ppc64 and aarch64
%ifarch %ix86 ia64 x86_64 %arm ppc64le
BuildRequires:  libunwind-devel
%endif
%endif
BuildRequires:  lksctp-tools-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1140
BuildRequires:  sysvinit-tools
BuildRequires:  time
%endif
%ifarch x86_64
Obsoletes:      strace-32bit
%endif

%description
With strace, you can trace the activity of a program.  Information
about any system calls the program makes and the signals it receives
and processes can be seen.  Child processes can also be tracked.

%prep
%setup -q

%build
%configure \
%ifarch aarch64
  --disable-mpers \
%endif
  %{nil}
make %{?_smp_mflags}

# Exclude testsuite for qemu builds, qemu-linux-user doesn't support ptrace.
%if !0%{?qemu_user_space_build}
%check
haveged=$(PATH=$PATH:/sbin:%{_sbindir} type -p haveged)
if test -n "$haveged" && ! /sbin/checkproc $haveged ; then
    $haveged --pidfile=$PWD/haveged.pid < /dev/null 1>&0 2>&0 || true
fi
make %{?_smp_mflags} check || cat tests/test-suite.log
if test -s $PWD/haveged.pid ; then
    /sbin/killproc -p $PWD/haveged.pid $haveged
fi
%endif

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc CREDITS README doc/README-linux-ptrace NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace.1%{ext_man}
%{_mandir}/man1/strace-log-merge.1%{ext_man}

%changelog
