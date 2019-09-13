#
# spec file for package keybinder
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname libkeybinder0

Name:           keybinder
Version:        0.3.1
Release:        0
Summary:        A Library for Registering Global Keyboard Shortcuts
License:        GPL-2.0+ and MIT
Group:          Development/Libraries/Other
Url:            http://kaizer.se/wiki/keybinder/
Source:         https://github.com/engla/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ed
BuildRequires:  fdupes
# For Documentation Directory Ownership
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
BuildRequires:  python-devel
BuildRequires:  python-gobject2-devel
BuildRequires:  python-gtk-devel
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Lua bindings, lua-keybinder
- Python bindings, python-keybinder
- An examples directory with programs in C, Lua, Python and Vala.

%package -n %{libname}
Summary:        Library Package for Keybinder
Group:          System/Libraries

%description -n %{libname}
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Lua bindings, lua-keybinder
- Python bindings, python-keybinder
- An examples directory with programs in C, Lua, Python and Vala.

%package devel
Summary:        Development Files for Keybinder
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description devel
This package contains development files needed for developing applications
based on keybinder.

%package lua
Summary:        Lua Files for Keybinder
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description lua
This package contains Lua files for applications based on keybinder.

%package -n python-%{name}

Summary:        Python Bindings for Keybinder
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}
Requires:       python-base = %{py_ver}
Requires:       python-gobject2
Requires:       python-gtk

%description -n python-%{name}
This package contains python bindings for keybinder.

%package -n typelib-1_0-Keybinder-0_0
Summary:        A Library for Registering Global Keyboard Shortcuts -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Keybinder-0_0
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

This package provides the GObject Introspection bindings for libkeybinder0.

%prep
%setup -q
find examples/ \( -name '*.py' -o -name '*.lua' \) -print -exec sh -c '
ed -s "$1" 2>/dev/null <<\EOF
,s/^#!\/usr\/bin\/env /#!\/usr\/bin\//
w
EOF
' {} {} \;
rm examples/.gitignore

%build
NOCONFIGURE=1 ./autogen.sh
export CPPFLAGS="`pkg-config --cflags lua5.1`"
%{configure}\
   --enable-gtk-doc \
   --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot}%{_libdir} -name '*.la' -exec rm -f {} +

find examples -type f -exec chmod 644 {} +

%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libkeybinder.so.*

%files devel
%defattr(-,root,root)
%doc examples
%{_includedir}/keybinder.h
%{_libdir}/libkeybinder.so
%{_libdir}/pkgconfig/keybinder.pc
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Keybinder-0.0.gir

%files lua
%defattr(-,root,root)
%{_libdir}/lua/*/keybinder.so

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/%{name}

%files -n typelib-1_0-Keybinder-0_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Keybinder-0.0.typelib

%changelog
