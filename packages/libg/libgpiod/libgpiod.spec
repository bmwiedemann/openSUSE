#
# spec file for package libgpiod
#
# Copyright (c) 2022 SUSE LLC
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


%define libgpiod_soversion 2
%define libgpiodcxx_soversion 1
%define libgpiomockup_soversion 0
# Tests are only available for kernel 5.5+ (so TW and 15.4+ only)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without libgpiod_tests
%else
%bcond_with libgpiod_tests
%endif
Name:           libgpiod
Version:        1.6.3
Release:        0
Summary:        C library and tools for interacting with the linux GPIO character device
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:        https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libkmod-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel >= 3.5
%if %{with libgpiod_tests}
%if 0%{suse_version} > 1550
# Only Tumbleweed bumped Catch2 to version 3.x
BuildRequires:  Catch2-2-devel
%else
BuildRequires:  Catch2-devel
%endif
BuildRequires:  glib2-devel >= 2.50
BuildRequires:  kernel-devel >= 5.5
BuildRequires:  pkgconfig(libudev)
%else
BuildRequires:  kernel-devel >= 4.8
%endif

%description
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

%package utils
Summary:        Tools for interacting with the linux GPIO character device
Group:          Development/Libraries/C and C++
Provides:       libgpiod = %{version}-%{release}
Obsoletes:      libgpiod < %{version}-%{release}

%description utils
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Command-line tools part.

%package -n libgpiod%{libgpiod_soversion}
Summary:        C library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiod%{libgpiod_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C library part.

%package -n libgpiodcxx%{libgpiodcxx_soversion}
Summary:        C++library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiodcxx%{libgpiodcxx_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C++ library part.

%package -n libgpiomockup%{libgpiomockup_soversion}
Summary:        C library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiomockup%{libgpiomockup_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

GPIO mockup library part.

%package devel
Summary:        Devel files for libgpiod
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       libgpiod%{libgpiod_soversion} = %{version}
Requires:       libgpiodcxx%{libgpiodcxx_soversion} = %{version}
%if %{with libgpiod_tests}
Requires:       libgpiomockup%{libgpiomockup_soversion} = %{version}
%endif

%description devel
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Devel files part.

%package -n python3-gpiod
Summary:        Python binding for libgpiod
Group:          Development/Languages/Python
Provides:       python-libgpiod
Obsoletes:      python-libgpiod

%description -n python3-gpiod
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Python binding part.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
%if %{with libgpiod_tests}
	--enable-tests \
%endif
	--enable-tools=yes \
	--enable-bindings-python \
	--enable-bindings-cxx
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.{a,la}
rm -rf %{buildroot}%{python3_sitearch}/*.{a,la}

%if %{with libgpiod_tests}
# Fix scripts interpreters
sed -i 's#%{_bindir}/env bash#/bin/bash#' %{buildroot}/%{_bindir}/gpio-tools-test
sed -i 's#%{_bindir}/env bats#%{_bindir}/bats#' %{buildroot}/%{_bindir}/gpio-tools-test.bats
sed -i 's#%{_bindir}/env python3#%{_bindir}/python3#' %{buildroot}/%{_bindir}/gpiod_py_test.py
%endif

%post -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%postun -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%post -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig
%postun -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig

%if %{with libgpiod_tests}
%post -n libgpiomockup%{libgpiomockup_soversion} -p /sbin/ldconfig
%postun -n libgpiomockup%{libgpiomockup_soversion} -p /sbin/ldconfig
%endif

%files utils
%{_bindir}/gpio*

%files -n libgpiod%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}.*

%files -n libgpiodcxx%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}.*

%if %{with libgpiod_tests}
%files -n libgpiomockup%{libgpiomockup_soversion}
%{_libdir}/libgpiomockup.so.%{libgpiomockup_soversion}
%{_libdir}/libgpiomockup.so.%{libgpiomockup_soversion}.*
%endif

%files devel
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_libdir}/pkgconfig/libgpiodcxx.pc

%files -n python3-gpiod
%{python3_sitearch}/*.so

%changelog
