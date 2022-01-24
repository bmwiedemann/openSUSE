#
# spec file for package libsmdev
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


%define lname	libsmdev1
Name:           libsmdev
Version:        20210418
Release:        0
Summary:        Library to access storage media devices
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsmdev
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libuna) >= 20201204
%python_subpackages

%description
libsmdev is a library to access and read storage media devices.

%package -n %{lname}
Summary:        Library to access storage media devices
Group:          System/Libraries

%description -n %{lname}
libsmdev is a library to access and read storage media devices.

%package devel
Summary:        Development files for libsmdev, a storage media access library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libsmdev is a library to access and read storage media devices.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmdev.

%package tools
Summary:        Utilities for reading storage media devices through libsmdev
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libsmdev, which
can access and read storage media devices and will determine
information about such.

%prep
%autosetup -p1

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}"
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libsmdev.so.1*

%files -n %name-devel
%license COPYING*
%{_includedir}/libsmdev*
%{_libdir}/libsmdev.so
%{_libdir}/pkgconfig/libsmdev.pc
%{_mandir}/man3/libsmdev.3*

%files -n %name-tools
%license COPYING*
%{_bindir}/smdevinfo
%{_mandir}/man1/smdevinfo.1*

%files %python_files
%license COPYING*
%{python_sitearch}/pysmdev.so

%changelog
