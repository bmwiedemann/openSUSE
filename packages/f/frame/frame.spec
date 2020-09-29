#
# spec file for package frame
#
# Copyright (c) 2020 SUSE LLC
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


%define soname  libframe
%define sover   6
%define _version 2.5.0daily13.06.05+16.10.20160809
Name:           frame
Version:        2.5.0+bzr20160809
Release:        0
Summary:        Touch frame library
License:        LGPL-3.0-only AND GPL-3.0-only
Group:          System/GUI/Other
URL:            https://launchpad.net/frame
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
Source1:        baselibs.conf
Patch:          frame-cstdio.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(inputproto) >= 2.1.99.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.5.99.1
BuildRequires:  pkgconfig(xorg-server)
Provides:       %{name}-tools = %{version}
Obsoletes:      %{name}-tools < %{version}

%description
This package provides the tree that handles the buildup and
synchronisation of a set of simultaneous touches.

%package -n %{soname}%{sover}
Summary:        Touch frame library
Group:          System/Libraries

%description -n %{soname}%{sover}
This package provides the tree that handles the buildup and
synchronisation of a set of simultaneous touches.

%package devel
Summary:        Touch frame library development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}

%description devel
This package provides the tree that handles the buildup and
synchronisation of a set of simultaneous touches.

This package includes the development files for frame.

%prep
%setup -q -c
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static       \
  --disable-silent-rules
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%doc COPYING* README
%{_bindir}/%{name}-test-x11
%{_mandir}/man?/%{name}-test-x11.?%{?ext_man}

%files -n %{soname}%{sover}
%doc COPYING* README
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/oif/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
