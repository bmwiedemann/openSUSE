#
# spec file for package libwacom
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

Name:           libwacom
Version:        2.11.0
Release:        0
Summary:        Library to identify wacom tablets
License:        MIT
Group:          System/Libraries
URL:            https://linuxwacom.github.io/
Source0:        https://github.com/linuxwacom/libwacom/releases/download/libwacom-%{version}/libwacom-%{version}.tar.xz
Source1:        https://github.com/linuxwacom/libwacom/releases/download/libwacom-%{version}/libwacom-%{version}.tar.xz.sig
# Fetched from https://github.com/whot.gpg
Source2:        %{name}.keyring
Source99:       baselibs.conf
BuildRequires:  meson >= 0.51.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libevdev) >= 1.7.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  doxygen

%description
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package -n libwacom9
Summary:        Library to identify wacom tablets
Group:          System/Libraries
Requires:       %{name}-data >= %{version}

%description -n libwacom9
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package data
Summary:        Library to identify wacom tablets -- Data Files
Group:          System/Libraries

%description data
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package tools
Summary:        Library to identify wacom tablets -- Tools
Group:          Hardware/Other
Requires:       python3-libevdev
Requires:       python3-pyudev

%description tools
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package devel
Summary:        Library to identify wacom tablets -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libwacom9 = %{version}

%description devel
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%prep
%autosetup -p1

%build
%meson -Db_lto=true -Dtests=disabled
%meson_build

%install
%meson_install

sed -e 's-#!/usr/bin/env python3-#!/usr/bin/python3-g' -i %{buildroot}%{_bindir}/*
find %{buildroot} -type f -name "*.la" -delete -print
%python3_fix_shebang

%check
%meson_test

%post -n libwacom9 -p /sbin/ldconfig
%postun -n libwacom9 -p /sbin/ldconfig

%files -n libwacom9
%license COPYING
%doc NEWS README.md
%{_libdir}/libwacom.so.9*

%files data
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%{_datadir}/libwacom/layouts/
%dir %{_udevrulesdir}
%{_udevrulesdir}/65-libwacom.rules
%dir %{_udevhwdbdir}
%{_udevhwdbdir}/65-libwacom.hwdb

%files tools
%{_bindir}/libwacom-list-devices
%{_bindir}/libwacom-update-db
%{_bindir}/libwacom-show-stylus
%{_bindir}/libwacom-list-local-devices
%{_mandir}/man1/libwacom-list-devices.1%{?ext_man}
%{_mandir}/man1/libwacom-list-local-devices.1%{?ext_man}

%files devel
%{_includedir}/libwacom-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwacom.pc

%changelog
