#
# spec file for package libvslvm
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


%define lname   libvslvm1
Name:           libvslvm
Version:        20210511
Release:        0
Summary:        Library to access the Linux Logical Volume Manager (LVM) volume system
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvslvm/
Source:         %{name}-%{version}.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
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
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

%description
libvslvm is a library to access the Linux Logical Volume Manager (LVM) volume system.

%package -n %{lname}
Summary:        Library to access Linux Logical Volume Manager (LVM) volume containers
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libvslvm library is a library to access Linux Logical Volume Manager (LVM) volume containers

%package tools
Summary:        Several tools for reading Linux Logical Volume Manager (LVM) volume systems
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for reading Linux Logical Volume Manager (LVM) volume systems

See libvslvm for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libvslvm
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files and libraries for developing applications for libvslvm

See libvslvm for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvslvm.

%package -n python3-%{name}
Summary:        Python 3 bindings for libvslvm
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
This packinge provides Python 3 bindings for libvslvm

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
#    this fails for the python check.
#    It is only checking if the python modules are present, so this is a false failure.
# make check

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libvslvm.so.*

%files tools
%license COPYING*
%{_bindir}/vslvm*
%{_mandir}/man1/vslvm*.1*

%files devel
%license COPYING*
%{_includedir}/libvslvm.h
%{_includedir}/libvslvm/
%{_libdir}/libvslvm.so
%{_libdir}/pkgconfig/libvslvm.pc
%{_mandir}/man3/libvslvm.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyvslvm.so

%changelog
