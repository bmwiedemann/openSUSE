#
# spec file for package keybinder
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


%if 0%{?suse_version} > 1500
%define do_python 0
%else
%define do_python 1
%endif

%define libname libkeybinder0

Name:           keybinder
Version:        0.3.1
Release:        0
Summary:        A Library for Registering Global Keyboard Shortcuts
License:        GPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/kupferlauncher
Source:         https://github.com/kupferlauncher/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        example_gi.py
Patch:          keybinder-doc-xml-fallback.patch
BuildRequires:  ed
BuildRequires:  fdupes
# For Documentation Directory Ownership
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
%if 0%{?do_python}
BuildRequires:  python-devel
BuildRequires:  python-gobject2-devel
BuildRequires:  python-gtk-devel
%endif
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)

%description
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Lua bindings, lua-keybinder
- Python bindings, python-keybinder
- An examples directory with programs in C, Lua, Python and Vala.

%package -n %{libname}
Summary:        A library for registering global keyboard shortcuts
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
Group:          Development/Languages/Lua
Requires:       %{libname} = %{version}

%description lua
This package contains Lua files for applications based on keybinder.

%package -n python-%{name}

Summary:        Python Bindings for Keybinder
Group:          Development/Languages/Python
Requires:       %{libname} = %{version}
Requires:       python-base = %{py_ver}
Requires:       python-gobject2
Requires:       python-gtk

%description -n python-%{name}
This package contains python bindings for keybinder.

%package -n typelib-1_0-Keybinder-0_0
Summary:        Introspection bindins for the Keybinder library
Group:          System/Libraries

%description -n typelib-1_0-Keybinder-0_0
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

This package provides the GObject Introspection bindings for libkeybinder0.

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%prep
%setup -q
%patch -p1
cp -a %{SOURCE1} examples
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
%if ! 0%{?do_python}
   --disable-python \
%endif
   --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot}%{_libdir} -name '*.la' -exec rm -f {} +

find examples -type f -exec chmod 644 {} +

%fdupes %{buildroot}/%{_prefix}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libkeybinder.so.*

%files devel
%doc examples
%{_includedir}/keybinder.h
%{_libdir}/libkeybinder.so
%{_libdir}/pkgconfig/keybinder.pc
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Keybinder-0.0.gir

%files lua
%{_libdir}/lua/*/keybinder.so

%if 0%{?do_python}
%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/%{name}
%endif

%files -n typelib-1_0-Keybinder-0_0
%{_libdir}/girepository-1.0/Keybinder-0.0.typelib

%changelog
