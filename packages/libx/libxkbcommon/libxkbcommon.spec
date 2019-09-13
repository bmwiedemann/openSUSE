#
# spec file for package libxkbcommon
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


%if ! 0%{?suse_version} || 0%{?suse_version} >= 1315
%bcond_without x11
%else
%bcond_with    x11
%endif

Name:           libxkbcommon
Version:        0.8.4
Release:        0
Summary:        Library for handling xkb descriptions
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xkbcommon.org/

#Git-Clone:	git://github.com/xkbcommon/libxkbcommon
Source:         https://xkbcommon.org/download/%name-%version.tar.xz
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:  autoconf >= 2.62
#git#BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
#git#BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
BuildRequires:  xz
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

%prep
%setup -q

%build
if [ ! -e configure ]; then
	NOCONFIGURE=1 ./autogen.sh
fi
%if %{with x11}
extra_opts=--enable-x11
%else
extra_opts=--disable-x11
%endif
# Ensure people will use pkgconfig to locate headers.
%configure --disable-static --includedir="%_includedir/%name" $extra_opts
make %{?_smp_mflags} V=1

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
make check

%post   -n libxkbcommon0 -p /sbin/ldconfig
%postun -n libxkbcommon0 -p /sbin/ldconfig
%post   -n libxkbcommon-x11-0 -p /sbin/ldconfig
%postun -n libxkbcommon-x11-0 -p /sbin/ldconfig

%files -n libxkbcommon0
%defattr(-,root,root)
%doc LICENSE NEWS
%_libdir/libxkbcommon.so.*

%files devel
%defattr(-,root,root)
%doc LICENSE NEWS
%_includedir/%name/
%if %{with x11}
%exclude %_includedir/%name/xkbcommon/xkbcommon-x11.h
%endif
%_libdir/libxkbcommon.so
%_libdir/pkgconfig/xkbcommon.pc

%if %{with x11}
%files -n libxkbcommon-x11-0
%defattr(-,root,root)
%doc LICENSE NEWS
%_libdir/libxkbcommon-x11.so.*

%files x11-devel
%defattr(-,root,root)
%doc LICENSE NEWS
%dir %_includedir/%name
%dir %_includedir/%name/xkbcommon
%_includedir/%name/xkbcommon/xkbcommon-x11.h
%_libdir/libxkbcommon-x11.so
%_libdir/pkgconfig/xkbcommon-x11.pc
%endif

%changelog
