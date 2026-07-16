#
# spec file for package oprofile
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           oprofile
Version:        1.4.0
Release:        0
Summary:        System-Wide Profiler for Linux Systems
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            http://oprofile.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/oprofile/oprofile-%{version}.tar.gz
Source2:        %{name}.rpmlintrc
Source3:        baselibs.conf
Source5:        README-BEFORE-ADDING-PATCHES
Patch1:         %{name}-no-libjvm-version.patch
Patch2:         %{name}-pfm-ppc.patch
Patch3:         %{name}-binutils.patch
Patch4:         %{name}-autoconf-fix-perf_events-detection.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  docbook-utils-minimal
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  libICE-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
Requires(pre):  pwdutils
%ifarch ppc ppc64 ppc64le
BuildRequires:  libpfm-devel >= 4.3.0
%endif

%description
OProfile is a system-wide profiler for Linux systems, capable of
profiling all running code at low overhead. OProfile is released under
the GNU GPL.

It consists of a kernel module and a daemon for collecting sample data,
and several post-profiling tools for turning data into information.

OProfile leverages the CPU hardware performance counters to enable
profiling of a wide variety of interesting statistics, which can also
be used for basic time-spent profiling. All code is profiled: hardware
and software interrupt handlers, kernel modules, the kernel, shared
libraries, and applications (the only exception being the oprofile
interrupt handler itself).

OProfile is currently in alpha status; however it has proven stable
over a large number of differing configurations. As always, there is no
warranty.

This is the package containing the userspace tools.

%package devel
Summary:        Development files for oprofile, a system-wide profiler for Linux
Group:          Development/Libraries/C and C++
Requires:       binutils-devel
Requires:       libopagent1 = %{version}-%{release}

%description devel
OProfile is a system-wide profiler for Linux systems, capable of
profiling all running code at low overhead. OProfile is released under
the GNU GPL.

This package contains the files needed to develop JIT agents for other
virtual machines.

%package -n libopagent1
Summary:        System-Wide Profiler for Linux Systems
Group:          System/Libraries

%description -n libopagent1
OProfile is a system-wide profiler for Linux systems, capable of
profiling all running code at low overhead. OProfile is released under
the GNU GPL.

This package contains the library needed at runtime when profiling JITed code
from supported virtual machines.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
  --with-java=${JAVA_HOME}
%make_build

%install
%make_install htmldir=%{_docdir}/oprofile
rm -f %{buildroot}%{_libdir}/oprofile/libopagent.*a
# Hardlink duplicate files automatically (from package fdupes):
# It doesn't save much, but it keeps rpmlint from breaking the package build.
%fdupes %{buildroot}/%{_prefix}

%pre
getent group oprofile >/dev/null || groupadd -r oprofile 2> /dev/null
getent passwd oprofile >/dev/null || \
	useradd -r -g oprofile -d %{_localstatedir}/lib/empty \
	-s /bin/false -c "Special user account to be used by OProfile" \
	oprofile 2> /dev/null

%post -n libopagent1 -p /sbin/ldconfig
%postun -n libopagent1 -p /sbin/ldconfig

%files
%{_bindir}/ocount
%{_bindir}/ophelp
%{_bindir}/opimport
%{_bindir}/opannotate
%{_bindir}/opgprof
%{_bindir}/opreport
%{_bindir}/oparchive
%{_bindir}/opjitconv
%{_bindir}/op-check-perfevents
%{_bindir}/operf
%{_datadir}/oprofile
%{_mandir}/man1/*
%{_libdir}/oprofile/libjvm[tp]i_oprofile.so
%exclude %{_libdir}/oprofile/libjvm[tp]i_oprofile.*a
%doc doc/oprofile.html doc/internals.html doc/opreport.xsd
%{_docdir}/%{name}/ophelp.xsd
%doc README TODO ChangeLog-*
%license COPYING

%files devel
%{_includedir}/*
%{_docdir}/%{name}/op-jit-devel.html
%dir %{_libdir}/oprofile
%{_libdir}/oprofile/libopagent.so

%files -n libopagent1
%dir %{_libdir}/oprofile
%{_libdir}/oprofile/libopagent.so.1*

%changelog
