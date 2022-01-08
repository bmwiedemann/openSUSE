#
# spec file for package libfsntfs
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


%define lname	libfsntfs1
Name:           libfsntfs
Version:        20211229
Release:        0
Summary:        Library and tools to access the NTFS filesystem
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfsntfs
Source:         https://github.com/libyal/libfsntfs/releases/download/%version/libfsntfs-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfsntfs/releases/download/%version/libfsntfs-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20210526
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20211115
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20211023
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfusn) >= 20180726
BuildRequires:  pkgconfig(libfwnt) >= 20210906
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20210801
BuildRequires:  pkgconfig(python3)

%description
Library and tools to access the New Technology File System (NTFS).

Note that this project currently only focuses on the analysis of the format.

%package -n %{lname}
Summary:        Library to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libfsntfs is a library to access the New Technology File System (NTFS).

Note that this project currently only focuses on the analysis of the format.

%package tools
Summary:        Tools to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
libfsntfs-tools is a project to access the NTFS filesystem

Note that this project currently only focuses on the analysis of the format.

%package devel
Summary:        Development files for libfsntfs
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
%{name} is a library to access the New Technology File System (NTFS).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfsntfs
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
Python 3 binding for libfsntfs, which can access the NTFS filesystem.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfsntfs.so.*

%files tools
%{_bindir}/fsntfs*
%{_mandir}/man1/fsntfsinfo.1*

%files devel
%{_includedir}/libfsntfs.h
%{_includedir}/libfsntfs/
%{_libdir}/libfsntfs.so
%{_libdir}/pkgconfig/libfsntfs.pc
%{_mandir}/man3/libfsntfs.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyfsntfs.so

%changelog
