#
# spec file for package libxkbcommon
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


%if ! 0%{?suse_version} || 0%{?suse_version} >= 1315
%bcond_without x11
%else
%bcond_with    x11
%endif

Name:           libxkbcommon
Version:        1.5.0
Release:        0
Summary:        Library for handling xkb descriptions
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xkbcommon.org/

#Git-Clone:	https://github.com/xkbcommon/libxkbcommon
Source:         https://xkbcommon.org/download/libxkbcommon-%version.tar.xz
Source2:        baselibs.conf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  meson >= 0.51
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayland-client) >= 1.2.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.7
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
%if %{with x11}
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
%endif

%description
xkbcommon is a keymap handling library, which can parse XKB
descriptions (e.g. from xkeyboard-config), and use this to help its
users make sense of their keyboard input. Unfortunately, X11's
requirements mean this is not actually usable for the X server, but it
should be perfectly usable for client toolkits, as well as alternative
windowing systems, compositors and system-level clients such as
Wayland and kmscon.

%package -n libxkbcommon0
Summary:        Library for handling xkb descriptions
Group:          System/Libraries
Requires:       xkeyboard-config

%description -n libxkbcommon0
xkbcommon is a keymap handling library, which can parse XKB
descriptions (e.g. from xkeyboard-config), and use this to help its
users make sense of their keyboard input. Unfortunately, X11's
requirements mean this is not actually usable for the X server, but it
should be perfectly usable for client toolkits, as well as alternative
windowing systems, compositors and system-level clients such as
Wayland and kmscon.

%package -n libxkbcommon-x11-0
Summary:        Library for handling xkb descriptions using XKB-X11
Group:          System/Libraries

%description -n libxkbcommon-x11-0
An addon library that supports creating keymaps with the XKB X11
protocol by querying the X server directly.

%package devel
Summary:        Development files for the libxkbcommon library
Group:          Development/Libraries/C and C++
Requires:       libxkbcommon0 = %version-%release

%description devel
xkbcommon is a keymap handling library, which can parse XKB
descriptions (e.g. from xkeyboard-config), and use this to help its
users make sense of their keyboard input. Unfortunately, X11's
requirements mean this is not actually usable for the X server, but it
should be perfectly usable for client toolkits, as well as alternative
windowing systems, compositors and system-level clients such as
Wayland and kmscon.

This package contains the development headers for the library found
in libxkbcommon.

%package tools
Summary:        Utilities from xkbcommon
Group:          System/X11/Utilities

%description tools
xkbcommon tools for introspection and debugging.

%package x11-devel
Summary:        Development files for the libxkbcommon-x11 library
Group:          Development/Libraries/C and C++
Requires:       libxkbcommon-x11-0 = %version-%release

%description x11-devel
xkbcommon is a keymap handling library, which can parse XKB
descriptions (e.g. from xkeyboard-config), and use this to help its
users make sense of their keyboard input.

This package contains the development headers for the library found
in %name-x11-0.

%package -n libxkbregistry0
Summary:        Library for handling xkb descriptions
Group:          System/Libraries

%description -n libxkbregistry0
libxkbregistry is a C library that lists available XKB models,
layouts and variants for a given ruleset.

%package -n libxkbregistry-devel
Summary:        Header files for xkbregistry
Group:          Development/Libraries/C and C++
Requires:       libxkbregistry0 = %version-%release

%description -n libxkbregistry-devel
libxkbregistry is a C library that lists available XKB models,
layouts and variants for a given ruleset.

This is aimed at tools that provide a listing of available keyboard
layouts to the user.

%prep
%autosetup -p1

%build
%if %{with x11}
ef=-Denable-x11=true
%else
ef=-Denable-x11=false
%endif
# includedir intentional, cf. bugzilla.opensuse.org/795968
%meson -Denable-docs=false --includedir="%_includedir/%name" $ef
%meson_build

%install
%meson_install

%post   -n libxkbcommon0 -p /sbin/ldconfig
%postun -n libxkbcommon0 -p /sbin/ldconfig
%post   -n libxkbcommon-x11-0 -p /sbin/ldconfig
%postun -n libxkbcommon-x11-0 -p /sbin/ldconfig
%post   -n libxkbregistry0 -p /sbin/ldconfig
%postun -n libxkbregistry0 -p /sbin/ldconfig

%files -n libxkbcommon0
%license LICENSE
%_libdir/libxkbcommon.so.*

%files devel
%doc NEWS
%_includedir/%name/
%if %{with x11}
%exclude %_includedir/%name/xkbcommon/xkbcommon-x11.h
%endif
%_libdir/libxkbcommon.so
%_libdir/pkgconfig/xkbcommon.pc

%files tools
%_bindir/xkbcli
%_libexecdir/xkbcommon/
%_mandir/man1/xkbcli*

%if %{with x11}
%files -n libxkbcommon-x11-0
%license LICENSE
%_libdir/libxkbcommon-x11.so.*

%files x11-devel
%license LICENSE
%dir %_includedir/%name
%dir %_includedir/%name/xkbcommon
%_includedir/%name/xkbcommon/xkbcommon-x11.h
%_libdir/libxkbcommon-x11.so
%_libdir/pkgconfig/xkbcommon-x11.pc
%endif

%files -n libxkbregistry0
%_libdir/libxkbregistry.so.0*

%files -n libxkbregistry-devel
%_libdir/libxkbregistry.so
%_libdir/pkgconfig/xkbregistry.pc

%changelog
