#
# spec file for package gtkmm3
#
# Copyright (c) 2022 SUSE LLC
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


%define so_ver -3_0-1
%define _name gtkmm

Name:           gtkmm3
Version:        3.24.7
Release:        0
Summary:        C++ Interface for GTK3 (a GUI Library for X)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/3.24/%{_name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE gtkmm3-docs-without-timestamp.patch -- We do not want __DATE__ and __TIME__ in our packages
Patch0:         gtkmm3-docs-without-timestamp.patch

BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atkmm-1.6) >= 2.24.2
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.12.0
BuildRequires:  pkgconfig(epoxy) >= 1.2
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.35.5
BuildRequires:  pkgconfig(giomm-2.4) >= 2.54.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(pangomm-1.4) >= 2.38.2

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n libgtkmm%{so_ver}
Summary:        C++ Interface for GTK3 (a GUI library for X)
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgtkmm%{so_ver}
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package devel
Summary:        C++ Interface for GTK3 (a GUI library for X)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       libgtkmm%{so_ver} = %{version}

%description devel
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package doc
Summary:        C++ Interface for GTK3 (a GUI Library for X)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/HTML
Requires:       glibmm2-doc
BuildArch:      noarch

%description doc
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
	-Dbuild-documentation=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}

%post -n libgtkmm%{so_ver} -p /sbin/ldconfig
%postun -n libgtkmm%{so_ver} -p /sbin/ldconfig

%files -n libgtkmm%{so_ver}
%license COPYING
%doc NEWS
%{_libdir}/libgdkmm-3.0.so.*
%{_libdir}/libgtkmm-3.0.so.*

%files devel
%{_includedir}/gdkmm-3.0/
%{_includedir}/gtkmm-3.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gdkmm-3.0.pc
%{_libdir}/pkgconfig/gtkmm-3.0.pc
%{_libdir}/gdkmm-3.0/
%{_libdir}/gtkmm-3.0/

%files doc
%doc AUTHORS ChangeLog README
%{_datadir}/devhelp/books/gtkmm-3.0/
%{_datadir}/doc/gtkmm-3.0/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
