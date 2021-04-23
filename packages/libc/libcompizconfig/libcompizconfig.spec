#
# spec file for package libcompizconfig
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


%define _rev    ada252d7170ae626651a98fd03569e1f
%define sover   0
Name:           libcompizconfig
Version:        0.8.18
Release:        0
Summary:        CompizConfig plugin required for CCSM
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/libcompizconfig
Source:         https://gitlab.com/compiz/libcompizconfig/uploads/%{_rev}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE libcompizconfig-config-dir.patch boo#438081 rodrigo@novell.com
Patch0:         %{name}-config-dir.patch
# PATCH-FIX-UPSTREAM libcompizconfig-configure-retval.patch ro@suse.de
Patch1:         %{name}-configure-retval.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(x11)
Requires:       compiz < 0.9
Suggests:       libcompizconfig-backend < 0.9

%description
CompizConfig plugin required for compizconfig-settings-manager.

%package devel
Summary:        Development files for libcompizconfig
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(compiz) < 0.9
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(protobuf)
Requires:       pkgconfig(x11)

%description devel
CompizConfig plugin required for compizconfig-settings-manager.

This package contains development files.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING LICENSE*
%doc NEWS README.md
%dir %{_sysconfdir}/compizconfig/
%config %{_sysconfdir}/compizconfig/config
%{_libdir}/%{name}.so.%{sover}*
%{_libdir}/compizconfig/
%dir %{_datadir}/compiz/
%{_libdir}/compiz/*ccp*
%{_datadir}/compiz/*ccp.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/compizconfig/
%{_libdir}/%{name}.so

%changelog
