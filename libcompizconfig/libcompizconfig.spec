#
# spec file for package libcompizconfig
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _rev    f5a51bfcae611276064ba8b9048c294e
%define sover   0
Name:           libcompizconfig
Version:        0.8.16
Release:        0
Summary:        CompizConfig plugin required for CCSM
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://gitlab.com/compiz/libcompizconfig
Source:         https://gitlab.com/compiz/libcompizconfig/uploads/%{_rev}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE libcompizconfig-config-dir.patch boo#438081 rodrigo@novell.com
Patch0:         %{name}-config-dir.patch
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
Group:          Development/Libraries/C and C++
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
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static
make %{?_smp_mflags} V=1

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
