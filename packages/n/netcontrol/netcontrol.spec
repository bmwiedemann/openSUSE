#
# spec file for package netcontrol
#
# Copyright (c) 2023 SUSE LLC
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


Name:           netcontrol
Version:        0.3.2
Release:        0
Summary:        A network configuration library
#
# License note:
# libnetcontrol contains source code which is based on wicked.
# Wicked is licensed under the GPL-2.0-or-later, but permission has
# been granted by the authors of wicked to use the code derived from
# wicked under the LGPL-2.1-or-later in libnetcontrol.
#
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/System
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch1:         0001-xml-reader-fix-xml_getc-and-xml_ungetc.patch
Patch2:         0002-xml-reader-allow-uppercase-for-lt-gt-and-amp-expansi.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       sysconfig >= 0.80.0

%description
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.

%package -n     libnetcontrol0
Summary:        A network configuration library
Group:          Productivity/Networking/System

%description -n libnetcontrol0
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.

The libnetcontrol0 package provides the shared library.

%package -n     libnetcontrol-devel
Summary:        Development header and library files
Group:          Development/Libraries/C and C++
Requires:       libnetcontrol0 = %{version}

%description -n libnetcontrol-devel
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.

The libnetcontrol-devel package contains libraries and header files
required for development.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure \
	--enable-network-service \
	--enable-pthreads \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libnetcontrol0 -p /sbin/ldconfig
%postun -n libnetcontrol0 -p /sbin/ldconfig

%files -n libnetcontrol0
%{_libdir}/*.so.*

%files -n libnetcontrol-devel
%license COPYING.LGPL COPYING.GPL
%doc README ChangeLog.git
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/netcontrol.pc

%changelog
