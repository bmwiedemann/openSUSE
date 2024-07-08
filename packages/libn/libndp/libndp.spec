#
# spec file for package libndp
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libndp
Version:        1.8
Release:        0
Summary:        Library for Neighbor Discovery Protocol
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            http://libndp.org/
Source:         http://libndp.org/files/libndp-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libndp-CVE-2024-5564.patch bsc#1225771 mgorse@suse.com -- add a check on the route information option length field.
Patch0:         libndp-CVE-2024-5564.patch
BuildRequires:  pkgconfig

%description
This package contains a library which provides a wrapper for IPv6 Neighbor
Discovery Protocol.  It also provides a tool named ndptool for sending and
receiving NDP messages.

%package -n libndp0
Summary:        Libraries and header files for libndp development
Group:          System/Libraries

%description -n libndp0
This package contains a library which provides a wrapper for IPv6 Neighbor
Discovery Protocol.

%package devel
Summary:        Libraries and header files for libndp development
Group:          Development/Libraries/C and C++
Requires:       libndp0 = %{version}

%description devel
The libndp-devel package contains the header files necessary for developing
programs using libndp.

%prep
%autosetup -p1

%build
%configure \
  --disable-static
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libndp0 -p /sbin/ldconfig
%postun -n libndp0 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8%{?ext_man}

%files -n libndp0
%license COPYING
%{_libdir}/libndp.so.*

%files devel
%license COPYING
%{_includedir}/ndp.h
%{_libdir}/libndp.so
%{_libdir}/pkgconfig/libndp.pc

%changelog
