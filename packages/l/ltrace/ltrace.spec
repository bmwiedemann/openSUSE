#
# spec file for package ltrace
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


%define git_id gea8928d
Name:           ltrace
Version:        0.7.91
Release:        0
Summary:        Library and system call tracer for programs
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://ltrace.org/
Source:         ltrace-%{version}-%{git_id}.tar.bz2
Source2:        baselibs.conf
Patch0:         readdir.patch
Patch1:         https://src.fedoraproject.org/rpms/ltrace/raw/rawhide/f/ltrace-0.7.91-ppc64le-scv.patch
Patch3:         ppc-ptrace.patch
Patch4:         arm-trace.patch
Patch5:         gcc9-printf-s-null-argument.patch
Patch6:         lens-double-free.patch
Patch7:         gcc9-Wlto-type-mismatch.patch
Patch8:         s390x-ptrace.patch
Patch9:         ppc64le-use-after-free.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  dejagnu
BuildRequires:  gcc-c++
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libtool
ExclusiveArch:  %{ix86} s390x ppc ppc64 ppc64le %{arm} x86_64 alpha ia64 m68k aarch64

%description
Ltrace is a program that runs the specified command until it exits. It
intercepts and records the dynamic library calls that are called by the
executed process and the signals that are received by that process. It
can also intercept and print the system calls executed by the program.

The program to trace need not be recompiled for this, so ltrace can be
used on binaries for which no source is available.

This is still a work in progress, so, for example, the tracking to
child processes may fail or some things may not work as expected.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
./autogen.sh
export CFLAGS="%{optflags} -Wall -Wno-unused-local-typedefs"
%configure --disable-shared
%make_build

%check
%if 1
if timeout 180 make check
then
	echo 'no make check errors' > testresults.txt
else
	for file in `find testsuite -name "*.ltrace"`
	do
		echo
		echo $file
		echo
		cat $file
		echo
	done >> testresults.txt
fi
mv testresults.txt %{_target_cpu}-testresults.txt
ln testsuite/testrun.sum testsuite/%{_target_cpu}-testrun.sum
%else
echo no make check > %{_target_cpu}-testresults.txt
echo no make check > testsuite/%{_target_cpu}-testrun.sum
%endif

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/ltrace

%files
%doc README
%license COPYING
%{_bindir}/ltrace
%{_datadir}/ltrace
%{_mandir}/man1/ltrace.1%{?ext_man}
%{_mandir}/man5/ltrace.conf.5%{?ext_man}

%changelog
