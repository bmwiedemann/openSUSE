#
# spec file for package libsigscan
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


%define lname	libsigscan1
%define timestamp 20201117
%define experimental_tag experimental-
Name:           libsigscan
Version:        0~%{timestamp}
Release:        0
Summary:        Library for binary signature scanning
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsigscan/wiki
Source:         https://github.com/libyal/libsigscan/releases/download/%{timestamp}/%{name}-%{?experimental_tag}%{timestamp}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbfio) >= 20120701
BuildRequires:  pkgconfig(libcdata) >= 20120701
BuildRequires:  pkgconfig(libcerror) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20120426
BuildRequires:  pkgconfig(libuna) >= 20120425

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
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pysigscan = %{version}

%description -n python3-%{name}
Python 3 bindings for libsigscan.

libsigscan is a library for scanning for binary signatures.

%prep
%setup -q -n libsigscan-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python3
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libsigscan.so.*

%files tools
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/sigscan
%{_mandir}/man1/sigscan.1%{?ext_man}
%config %{_sysconfdir}/sigscan.conf

%files devel
%doc AUTHORS README ChangeLog
%license COPYING
%{_includedir}/libsigscan.h
%{_includedir}/libsigscan/
%{_libdir}/libsigscan.so
%{_libdir}/pkgconfig/libsigscan.pc
%{_mandir}/man3/libsigscan.3%{?ext_man}

%files -n python3-%{name}
%{python3_sitearch}/pysigscan.so

%changelog
