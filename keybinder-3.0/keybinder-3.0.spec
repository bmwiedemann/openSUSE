#
# spec file for package keybinder-3.0
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libkeybinder-3_0-0

Name:           keybinder-3.0
Version:        0.3.2
Release:        0
Summary:        A library for registering global keyboard shortcuts
License:        MIT and X11
Group:          Development/Libraries/C and C++
Url:            https://github.com/kupferlauncher/keybinder/tree/keybinder-3.0
Source0:        https://github.com/kupferlauncher/keybinder/releases/download/%{name}-v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Obsoletes:      keybinder3 = 3.0

%description
keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Python bindings, python-keybinder

%package -n %{libname}
Summary:        Library Package for Keybinder
Group:          System/Libraries
Obsoletes:      %{libname} = 3.0

%description -n %{libname}
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Gobject-Introspection bindings

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig
Obsoletes:      keybinder3-devel = 3.0

%description devel
This package contains the development files for %{name}.

%package -n typelib-1_0-Keybinder-3_0
Summary:        Introspection bindings for Keybinder
Group:          System/Libraries
Obsoletes:      typelib-1_0-Keybinder-3_0 = 3.0

%description -n typelib-1_0-Keybinder-3_0
Library for registering global keyboard shortcuts. Keybinder
works with GTK-based applications using the X Window System.

This package provides the GObject Introspection bindings for libkeybinder0.

%prep
%setup -q
rm examples/*.lua
rm examples/*.py

%build
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install
# Clean up
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libkeybinder-3.0.so.*

%files devel
%defattr(-,root,root)
%doc examples
%doc %{_datadir}/gtk-doc/html/keybinder-3.0
%{_includedir}/keybinder-3.0/
%{_includedir}/keybinder-3.0/keybinder.h
%{_libdir}/pkgconfig/keybinder-3.0.pc
%{_libdir}/libkeybinder-3.0.so
%{_datadir}/gir-1.0/Keybinder-3.0.gir

%files -n typelib-1_0-Keybinder-3_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Keybinder-3.0.typelib

%changelog
