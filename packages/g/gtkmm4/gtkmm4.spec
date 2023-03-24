#
# spec file for package gtkmm4
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


%define so_ver -4_0-0
%define _name gtkmm

Name:           gtkmm4
Version:        4.10.0
Release:        0
Summary:        C++ Interface for GTK4 (a GUI Library for X)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/4.10/%{_name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM gtkmm4-docs-without-timestamp.patch -- Do not add timestamps to generated doc files
Patch0:         gtkmm4-docs-without-timestamp.patch

BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairomm-1.16) >= 1.15.4
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.35.5
BuildRequires:  pkgconfig(giomm-2.68) >= 2.68.0
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(pangomm-2.48) >= 2.50.0

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n libgtkmm%{so_ver}
Summary:        C++ Interface for GTK4 (a GUI library for X)
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgtkmm%{so_ver}
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package devel
Summary:        C++ Interface for GTK4 (a GUI library for X)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       libgtkmm%{so_ver} = %{version}

%description devel
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm3 wraps
GTK+ 3. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package doc
Summary:        C++ Interface for GTK4 (a GUI Library for X)
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
chmod -x NEWS

%build
%meson \
	-D build-documentation=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_prefix}

%post -n libgtkmm%{so_ver} -p /sbin/ldconfig
%postun -n libgtkmm%{so_ver} -p /sbin/ldconfig

%files -n libgtkmm%{so_ver}
%license COPYING
%doc NEWS
%{_libdir}/libgtkmm-4.0.so.*

%files devel
%{_includedir}/gtkmm-4.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gtkmm-4.0.pc
%{_libdir}/gtkmm-4.0/

%files doc
%doc AUTHORS ChangeLog README.md
%{_datadir}/devhelp/books/gtkmm-4.0/
%{_datadir}/doc/gtkmm-4.0/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
