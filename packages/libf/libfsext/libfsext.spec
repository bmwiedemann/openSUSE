#
# spec file for package libfsext
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


%define lname	libfsext1
Name:           libfsext
Version:        20210513
Release:        0
Summary:        Library and tools to access the Extended File System
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfsext
Source:         %name-%version.tar.xz
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
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package -n %{lname}
Summary:        Library to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package tools
Summary:        Tools to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Extended File System.  See libfsext for additional details.

%package devel
Summary:        Development files for libfsext, Extended File System (ext) library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libfsext is a library to access the extended file system (ext) format.  see libfsext for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfsext.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfsext, a extended file system (ext) parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pyfsext

%description -n python3-%{name}
libfsext is a library to access extended file system (ext) format. See libfsext for details.

This package contains Python 3 bindings for libfsext.

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
%{_libdir}/libfsext.so.*

%files tools
%license COPYING*
%{_bindir}/fsext*
%{_mandir}/man1/fsext*.1*

%files devel
%license COPYING*
%{_includedir}/libfsext.h
%{_includedir}/libfsext/
%{_libdir}/libfsext.so
%{_libdir}/pkgconfig/libfsext.pc
%{_mandir}/man3/libfsext.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyfsext.so

%changelog
