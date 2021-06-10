#
# spec file for package libsigscan
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


%define lname	libsigscan1
Name:           libsigscan
Version:        20210419
Release:        0
Summary:        Library for binary signature scanning
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsigscan
Source:         %{name}-%{version}.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libsigscan is a library for binary signature scanning

libsigscan is part of the libyal family of libraries

%package -n %{lname}
Summary:        Library for binary signature scanning
Group:          System/Libraries

%description -n %{lname}
libsigscan is a library for binary signature scanning

%package tools
Summary:        Tools to scan for binary signatures
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to scan binary files for signatures.

%package devel
Summary:        Development files for libigscan
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libsigscan is a library for binary signature scanning

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%package -n python3-%{name}
Summary:        Python 3 bindings for libsigscan
Group:          Development/Languages/Python
Provides:       pysigscan = %{version}

%description -n python3-%{name}
Python 3 bindings for libsigscan.

libsigscan is a library for scanning for binary signatures.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libsigscan.so.*

%files tools
%license COPYING*
%{_bindir}/sigscan
%{_mandir}/man1/sigscan.1%{?ext_man}
%config %{_sysconfdir}/sigscan.conf

%files devel
%license COPYING*
%{_includedir}/libsigscan.h
%{_includedir}/libsigscan/
%{_libdir}/libsigscan.so
%{_libdir}/pkgconfig/libsigscan.pc
%{_mandir}/man3/libsigscan.3%{?ext_man}

%files -n python3-%{name}
%{python3_sitearch}/pysigscan.so

%changelog
