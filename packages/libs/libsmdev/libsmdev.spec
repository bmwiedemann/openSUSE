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
Version:        20221028
Release:        0
Summary:        Library to access storage media devices
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsmdev
Source:         https://github.com/libyal/libsmdev/releases/download/%version/libsmdev-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libsmdev/releases/download/%version/libsmdev-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt/"* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

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
