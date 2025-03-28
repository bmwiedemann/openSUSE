#
# spec file for package libxkbfile
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


%define lname	libxkbfile1
Name:           libxkbfile
Version:        1.1.3
Release:        0
Summary:        X11 keyboard file manipulation library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libxkbfile
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libxkbfile/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch1237429:   U_CVE-2025-26595-0001-xkb-Fix-buffer-overflow-in-XkbVModMaskText.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

%package -n %{lname}
Summary:        X11 keyboard file manipulation library
# O/P added for 12.2
Group:          System/Libraries
Requires:       xkeyboard-config
Provides:       xorg-x11-libxkbfile = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libxkbfile < 7.6_%{version}-%{release}

%description -n %{lname}
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

%package devel
Summary:        Development files for the X11 keyboard file manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libxkbfile-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libxkbfile-devel < 7.6_%{version}-%{release}

%description devel
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

This package contains the development headers for the library found
in %{lname}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libxkbfile.so.1*

%files devel
%{_includedir}/X11/*
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
