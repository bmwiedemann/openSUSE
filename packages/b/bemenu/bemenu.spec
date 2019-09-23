#
# spec file for package bemenu
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


%define bcond_with curses
Name:           bemenu
Version:        0.1.0
Release:        0
Summary:        Dynamic menu library and client program inspired by dmenu
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Cloudef/bemenu
Source0:        https://github.com/Cloudef/bemenu/archive/%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.2
%if %{with curses}
BuildRequires:  pkgconfig(ncurses)
%endif

%description
Dynamic menu library and client program inspired by dmenu with support
for X, Wayland and ncurses.

%package -n libbemenu0
Summary:        Dynamic menu library inspired by dmenu
Group:          Development/Libraries/C and C++
# you need renderers
Requires:       %{name}

%description -n libbemenu0
Library for Bemenu, dynamic menu inspired by dmenu.

%package devel
Summary:        Development files for bemenu
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       gcc-c++
Requires:       libbemenu0 = %{version}
Requires:       pkgconfig

%description devel
Files required for development for Bemenu.

%prep
%setup -q

%if %{with curses}
# fix colliding name with our ncurses library specifics
sed -i 's@stdscr@std_scr@g' lib/renderers/curses/curses.c
%endif

%build
%cmake -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"


make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%post -n libbemenu0 -p /sbin/ldconfig
%postun -n libbemenu0 -p /sbin/ldconfig

%files -n libbemenu0
%{_libdir}/libbemenu.so.*

%files devel
%{_libdir}/libbemenu.so
%{_includedir}/bemenu.h

%files
%{_bindir}/%{name}*
%{_libdir}/%{name}

%changelog
