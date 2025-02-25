#
# spec file for package libwacom
#
# Copyright (c) 2025 SUSE LLC
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

# library version from upstream meson.build
%define sover 9

Name:           libwacom
Version:        2.14.0
Release:        0
Summary:        Tablet description library
License:        HPND
Group:          Development/Libraries/C and C++
URL:            https://linuxwacom.github.io/
Source0:        https://github.com/linuxwacom/libwacom/releases/download/libwacom-%{version}/libwacom-%{version}.tar.xz
Source1:        https://github.com/linuxwacom/libwacom/releases/download/libwacom-%{version}/libwacom-%{version}.tar.xz.sig
# Fetched from https://github.com/whot.gpg
Source2:        %{name}.keyring
Source99:       baselibs.conf
BuildRequires:  meson >= 0.57.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libevdev) >= 1.7.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  doxygen

%description
libwacom is a library to identify graphics tablets and their model-specific
features. It provides access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package -n libwacom%{sover}
Summary:        Library to identify wacom tablets
Group:          System/Libraries
Requires:       %{name}-data >= %{version}

%description -n libwacom%{sover}
libwacom is a library to identify graphics tablets and their model-specific
features. It provides easy access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc. The name libwacom is
historical — it was originally developed for Wacom devices only but now
supports any graphics tablet from any vendor.

%package data
Summary:        Data files for libwacom, a table identification library
Group:          System/Libraries

%description data
libwacom is a library to identify graphics tablets and their model-specific
features. It provides access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package tools
Summary:        Command-line tools for libwacom
Group:          Hardware/Other
Requires:       python3-libevdev
Requires:       python3-pyudev

%description tools
libwacom is a library to identify graphics tablets and their model-specific
features.
This subpackage provides command-line utilities to query/update the database.

%package devel
Summary:        Header files for libwacom
Group:          Development/Libraries/C and C++
Requires:       libwacom%{sover} = %{version}

%description devel
libwacom is a library to identify graphics tablets and their model-specific
features.
This subpackage provides the header files for the library.

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

%ldconfig_scriptlets -n libwacom%{sover}

%files -n libwacom%{sover}
%license COPYING
%doc NEWS README.md
%{_libdir}/libwacom.so.%{sover}*

%files data
%license COPYING
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%{_datadir}/libwacom/layouts/
%dir %{_udevrulesdir}
%{_udevrulesdir}/65-libwacom.rules
%dir %{_udevhwdbdir}
%{_udevhwdbdir}/65-libwacom.hwdb

%files tools
%license COPYING
%{_bindir}/libwacom-list-devices
%{_bindir}/libwacom-update-db
%{_bindir}/libwacom-show-stylus
%{_bindir}/libwacom-list-local-devices
%{_mandir}/man1/libwacom-list-devices.1%{?ext_man}
%{_mandir}/man1/libwacom-list-local-devices.1%{?ext_man}
%{_mandir}/man1/libwacom-show-stylus.1%{?ext_man}

%files devel
%license COPYING
%{_includedir}/libwacom-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwacom.pc

%changelog
