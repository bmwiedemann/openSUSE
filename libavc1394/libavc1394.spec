#
# spec file for package libavc1394
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


Name:           libavc1394
Version:        0.5.4
Release:        0
Summary:        Programming Interface to the AV/C Specification
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Libraries
URL:            https://sourceforge.net/projects/libavc1394/
Source:         https://downloads.sf.net/libavc1394/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         libavc1394.no-mkrfc2734.patch
Patch1:         libavc1394.raw1394_set_fcp_handler.patch
Patch2:         libavc-fix-symbolexports.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libraw1394-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libavc1394 is a programming interface to the AV/C (Audio/Video
Control) specification. Applications use the library to control the
tape transport mechanism on DV camcorders. However, there are many
devices and functions of devices that can be controlled via AV/C.

%package 0
Summary:        Programming Interface to the AV/C Specification
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Libraries

%description 0
libavc1394 is a programming interface to the AV/C (Audio/Video
Control) specification. Applications use the library to control the
tape transport mechanism on DV camcorders. However, there are many
devices and functions of devices that can be controlled via AV/C.

%package devel
Summary:        Development files for libavc1394, a library to the AV/C specification
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libavc1394-0 = %{version}

%description devel
libavc1394 is a programming interface to the AV/C (Audio/Video
Control) specification. Applications use the library to control the
tape transport mechanism on DV camcorders. However, there are many
devices and functions of devices that can be controlled via AV/C.

%package tools
Summary:        Utilities for AV/C 1394
# added on 2015-11-14
License:        GPL-2.0-or-later
Group:          Hardware/Other
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description tools
Command-line utilities to inspect and control AV/C hardware.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fvi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post 0 -p /sbin/ldconfig
%postun 0 -p /sbin/ldconfig

%files tools
%license COPYING
%doc README AUTHORS
%{_mandir}/man1/*
%{_bindir}/*

%files 0
%{_libdir}/libavc1394.so.*
%{_libdir}/librom1394.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/libavc1394
%{_libdir}/pkgconfig/*.pc

%changelog
