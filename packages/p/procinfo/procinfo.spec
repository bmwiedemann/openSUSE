#
# spec file for package procinfo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           procinfo
Version:        18
Release:        0
Summary:        Tool to Display System Status Gathered from /proc
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            ftp://ftp.cistron.nl/pub/people/00-OLD/svm/
Source:         ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.bz2
Patch0:         procinfo-%{version}.dif
Patch1:         procinfo-uptime.dif
Patch2:         procinfo-ia64.diff
Patch3:         procinfo-hz
Patch4:         procinfo-TERM.dif
Patch5:         procinfo-26.diff
Patch6:         procinfo-gccver.diff
Patch7:         procinfo-irq.dif
Patch8:         procinfo-loadavg.dif
Patch9:         procinfo-lsdev.dif
Patch10:        procinfo-socklist.dif
Patch11:        procinfo-float.dif
Patch12:        procinfo-intr.dif
Patch13:        procinfo-gcc.dif
Patch14:        procinfo-tickless.dif
Patch15:        procinfo-termcap.diff
Patch16:        procinfo-disks.dif
Patch17:        procinfo-gccver2.dif
Patch18:        procinfo-man.dif
Patch19:        procinfo-maxdev.dif
Patch20:        procinfo-sysconf.dif
Patch21:        procinfo-ranges.dif
Patch22:        procinfo-strsignal.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ncurses-devel
Provides:       ps:/usr/bin/lsdev

%description
The "procinfo" command gathers some system data from the /proc
directory and prints it nicely formatted on the standard output device.

%prep
%setup -q
%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7
%patch -P 8
%patch -P 9
%patch -P 10
%patch -P 11
%patch -P 12
%patch -P 13
%patch -P 14
%if %suse_version > 1100
%patch -P 15 -p1
%endif
%patch -P 16
%patch -P 17
%patch -P 18
%patch -P 19
%patch -P 20
%patch -P 21
%patch -P 22

%build
CFLAGS="-D_GNU_SOURCE $(getconf LFS_CFLAGS) %{optflags} -pipe"
export CFLAGS
make LDFLAGS= CC="%__cc" %{?_smp_mflags}

%check
#
TERM=vt100
LANG=POSIX
unset ${!LC_*}
export TERM LANG
#
./procinfo -ai > output
! grep "can't parse" output
cat output

%install
make prefix=$RPM_BUILD_ROOT/usr install

%files
%defattr (-,root,root,755)
%doc README CHANGES
%{_bindir}/procinfo
%{_bindir}/lsdev
%{_bindir}/socklist
%{_mandir}/man8/procinfo.8*
%{_mandir}/man8/lsdev.8*
%{_mandir}/man8/socklist.8*

%changelog
