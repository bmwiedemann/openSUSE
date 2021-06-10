#
# spec file for package libfvde
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


%define lname	libfvde1
%define timestamp 20191221
Name:           libfvde
Version:        20210425
Release:        0
Summary:        Library to access the File Vault Drive Encryption format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfvde/
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcaes) >= 20201012
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfplist) >= 20210404
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

%description
libfvde is a library to access the File Vault Drive Encryption format.

%package -n %{lname}
Summary:        Library to access the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libfvde library is a library to access the File Vault Drive Encryption format

%package tools
Summary:        Several tools for reading the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Several tools for reading the File Vault Drive Encryption format

See libfvde for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libfvde
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files and libraries for developing applications for libfvde

See libfvde for additional details.

This package contains libraries and header files for developing
applications that want to make use of libfvde.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfvde
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python

%description -n python3-%{name}
This packinge provides Python 3 bindings for libfvde

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
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
%{_libdir}/libfvde.so.*

%files tools
%license COPYING*
%{_bindir}/fvde*
%{_mandir}/man1/fvde*.1*

%files devel
%license COPYING*
%{_includedir}/libfvde.h
%{_includedir}/libfvde/
%{_libdir}/libfvde.so
%{_libdir}/pkgconfig/libfvde.pc
%{_mandir}/man3/libfvde.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyfvde.so

%changelog
