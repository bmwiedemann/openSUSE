#
# spec file for package oprofile
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


Name:           oprofile
Version:        1.3.0
Release:        0
Summary:        System-Wide Profiler for Linux Systems
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            http://oprofile.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/oprofile/oprofile-%{version}.tar.gz
Source2:        %{name}.rpmlintrc
Source3:        baselibs.conf
Source4:        jvmpi.h
Source5:        README-BEFORE-ADDING-PATCHES
Patch1:         %{name}-no-libjvm-version.patch
Patch2:         %{name}-pfm-ppc.patch
Patch3:         %{name}-handle-empty-event-name-spec-gracefully-for-ppc.patch
# PATCH-FIX-UPSTREAM
Patch4:         %{name}-handle-binutils-2_34.patch
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
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
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

mkdir -p java/include
# copy files necessary to build Java agent libraries
# libjvmpi_oprofile.so and libjvmti_oprofile.so
# %S:4 is rpm speak for Source4 (jvmpi.h)
ln -s %{_libdir}/jvm/java/include/* java/include
test -f java/include/jvmpi.h || ln -s %{SOURCE4} java/include

%build
./autogen.sh
%configure \
  --with-java=$PWD/java
# Change DATE/TIME macros to use last change time of oprofile.changes
# See http://lists.opensuse.org/opensuse-factory/2011-05/msg00304.html
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec grep -E -e __DATE__ -e __TIME__ {} +
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
%make_build

%install
%make_install htmldir=%{_docdir}/oprofile
rm -f %{buildroot}%{_libdir}/oprofile/libopagent.*a
# Hardlink duplicate files automatically (from package fdupes):
# It doesn't save much, but it keeps rpmlint from breaking the package build.
%fdupes %{buildroot}/%{_prefix}

%pre
getent group oprofile >/dev/null || \
	%{_sbindir}/groupadd -r oprofile
getent passwd oprofile >/dev/null || \
	%{_sbindir}/useradd -r -g oprofile -d %{_localstatedir}/lib/empty \
	-s /bin/false -c "Special user account to be used by OProfile" \
	oprofile

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
