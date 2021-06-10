#
# spec file for package libfwsi
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


%define lname	libfwsi1
Name:           libfwsi
Version:        20210419
Release:        0
Summary:        Library to access the Windows Shell Item format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwsi
Source:         %name-%version.tar.xz
Source2:        Windows_Shell_Item_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfole) >= 20170502
BuildRequires:  pkgconfig(libfwps) >= 20191221
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library to access the Windows Shell Item format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwsi
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to access the Windows Shell Item format for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwsi.

%package -n python2-%{name}
Summary:        Python2 bindings for libfwsi
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python2)
Obsoletes:      pyfwsi <= 20191221
Obsoletes:      python-%{name} <= 20191221

%description -n python2-%name
Python2 bindings for libfwsi, a library to access Windows Shell Items.

%package -n python3-%{name}
Summary:        Python bindings for libfwsi
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python

%description -n python3-%name
Python3 bindings for libfwsi, a library to access Windows Shell Items.

%prep
%autosetup -p1
cp "%{S:2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-python2 --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfwsi.so.*

%files devel
%license COPYING*
%doc Windows_Shell_Item_format.pdf
%{_includedir}/libfwsi.h
%{_includedir}/libfwsi/
%{_libdir}/libfwsi.so
%{_libdir}/pkgconfig/libfwsi.pc
%{_mandir}/man3/libfwsi.3*

%files -n python2-%name
%license COPYING*
%python2_sitearch/pyfwsi.so

%files -n python3-%name
%license COPYING*
%python3_sitearch/pyfwsi.so

%changelog
