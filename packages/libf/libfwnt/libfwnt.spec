#
# spec file for package libfwnt
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


%define lname	libfwnt1
Name:           libfwnt
Version:        20210717
Release:        0
Summary:        Library for Windows NT data types
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwnt
Source:         https://github.com/libyal/libfwnt/archive/refs/tags/%version.tar.gz
Source2:        Locale_identifier_LCID.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(python3)

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwnt
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family
of libraries. libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwnt.

%package -n python3-%{name}
Summary:        Python 3 bindings for ${name}
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3

%description -n python3-%{name}
This packinge provides Python 3 bindings for ${name}

%prep
%autosetup -p1
cp "%{S:2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# make check

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfwnt.so.*

%files devel
%license COPYING*
%doc Locale_identifier_LCID.pdf
%{_includedir}/libfwnt.h
%{_includedir}/libfwnt/
%{_libdir}/libfwnt.so
%{_libdir}/pkgconfig/libfwnt.pc
%{_mandir}/man3/libfwnt.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyfwnt.so

%changelog
