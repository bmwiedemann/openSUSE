#
# spec file for package wimlib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_version 15
Name:           wimlib
Version:        1.13.1
Release:        0
Summary:        Library to extract, create, modify, and mount WIM files
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND CC0-1.0
Group:          Development/Libraries/C and C++
URL:            https://wimlib.net
Source:         https://wimlib.net/downloads/wimlib-%{version}.tar.gz
Patch0:         mkwinpeimg-syslinux-modules-may-be-in-usr-share-sysl.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libntfs-3g)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)

%description
Tools to create, extract, modify, and mount files in the Windows Imaging Format
(WIM files).  These files are normally created by using the `imagex.exe' utility
on Windows, but this package contains an implementation of ImageX called
"wimlib-imagex".

%package -n wimtools
Summary:        Tools to create, extract, modify, and mount WIM files
Group:          System/Console
Requires:       fuse

%description -n wimtools
Tools to create, extract, modify, and mount files in the Windows Imaging Format
(WIM files).  These files are normally created by using the `imagex.exe' utility
on Windows, but this package contains an implementation of ImageX called
"wimlib-imagex".

%package devel
Summary:        Development files for wimlib
Group:          Development/Libraries/C and C++
Requires:       libwim%{so_version}

%description devel
Development files for wimlib

%package -n libwim%{so_version}
Summary:        Library to extract, create, modify, and mount WIM files
Group:          System/Libraries

%description -n libwim%{so_version}
wimlib is a C library for creating, extracting, modifying, and mounting files in
the Windows Imaging Format (WIM files).

%post -n libwim%{so_version} -p /sbin/ldconfig
%postun -n libwim%{so_version} -p /sbin/ldconfig

%prep
%setup -q
%autopatch -p1

%build
%configure --disable-static \
           --with-libcrypto	\
           --with-ntfs-3g \
           --with-fuse

make %{?_smp_mflags}

%install
%make_install

sed -i '1 s,#!.*,#!/bin/bash,' %{buildroot}%{_bindir}/mkwinpeimg
rm %{buildroot}%{_libdir}/libwim.la

%files -n wimtools
%{_bindir}/mkwinpeimg
%{_bindir}/wim*
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%doc README
%{_libdir}/libwim.so
%{_includedir}/wimlib.h
%{_libdir}/pkgconfig/wimlib.pc

%files -n libwim%{so_version}
%license COPYING*
%{_libdir}/libwim.so.*

%changelog
