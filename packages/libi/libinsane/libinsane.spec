#
# spec file for package libinsane
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libinsane
Version:        1.0.9
Release:        0
Summary:        Library for accessing image scanners
Group:          Productivity/Office/Other
License:        LGPL-3.0-or-later
URL:            https://doc.openpaper.work/libinsane/latest/
Source:         https://gitlab.gnome.org/World/OpenPaperwork/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  plantuml
BuildRequires:  valgrind
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  vala

%description
Libinsane is a library to access scanners on multiple platforms.
It takes care of quirks of platforms and scanners.

%package -n libinsane1
Summary:        Library for accesssing image scanners

%description -n libinsane1
Libinsane is a library to access scanners on multiple platforms.
It takes care of quirks of platforms and scanners.

%package devel
Summary:        Development files for libinsane
Group:          Development/Libraries/C and C++
Requires:       %{name}1 >= %{version}
Requires:       typelib-1_0-Libinsane-1_0 = %{version}

%description devel
Development libraries and header files for libinsane.

%package -n libinsane_gobject1
Summary:        GObject access to image scanners
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
Requires:       %{name}1 >= %{version}

%description -n libinsane_gobject1
Libinsane is a library to access scanners on multiple platforms.
It takes care of quirks of platforms and scanners.

This package provides GObject wrappers around the main library.

%package -n libinsane_gobject-devel
Summary:        Development files for libinsane-gobject
Group:          Development/Libraries/Other
Requires:       %{name}-devel >= %{version}
Requires:       %{name}_gobject1 >= %{version}
Requires:       typelib-1_0-Libinsane-1_0 = %{version}

%description -n libinsane_gobject-devel
Development libraries and header files for libinsane-gobject.
It also includes the vala bindings.

%package -n typelib-1_0-Libinsane-1_0
Summary:        Introspection bindings for libinsane
Group:          System/Libraries

%description -n typelib-1_0-Libinsane-1_0
This package provides the GObject Introspection bindings for the
libinsane library.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n libinsane1 -p /sbin/ldconfig
%postun -n libinsane1 -p /sbin/ldconfig
%post -n libinsane_gobject1 -p /sbin/ldconfig
%postun -n libinsane_gobject1 -p /sbin/ldconfig

%files -n libinsane1
%doc README.markdown ChangeLog
%license LICENSE
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%doc doc
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n libinsane_gobject1
%{_libdir}/%{name}_gobject.so.1
%{_libdir}/%{name}_gobject.so.1.*

%files -n typelib-1_0-Libinsane-1_0
%{_libdir}/girepository-1.0/Libinsane-1.0.typelib

%files -n libinsane_gobject-devel
%{_includedir}/%{name}-gobject
%{_libdir}/%{name}_gobject.so
%{_datadir}/gir-1.0/Libinsane-1.0.gir
%{_datadir}/gtk-doc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi

%changelog
