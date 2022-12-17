#
# spec file for package gtkmm2
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


%define _name gtkmm
Name:           gtkmm2
Version:        2.24.5
Release:        0
Summary:        C++ Interface for GTK2 (a GUI Library for X)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gtkmm.org/
Source:         http://download.gnome.org/sources/gtkmm/2.24/%{_name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atkmm-1.6) >= 2.22.2
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(giomm-2.4) >= 2.27.93
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(pangomm-1.4) >= 2.27.1
BuildRequires:  pkgconfig(sigc++-2.0)

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n libgtkmm-2_4-1
Summary:        C++ Interface for GTK2 (a GUI library for X)
Group:          System/Libraries
Provides:       gtkmm2 = %{version}
Obsoletes:      gtkmm2 < %{version}
Provides:       gtkmm24 = %{version}
Obsoletes:      gtkmm24 < %{version}

%description -n libgtkmm-2_4-1
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package devel
Summary:        C++ Interface for GTK2 (a GUI library for X)
Group:          Development/Libraries/GNOME
Requires:       libgtkmm-2_4-1 = %{version}
Provides:       gtkmm24-devel = %{version}
Obsoletes:      gtkmm24-devel < %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
        --disable-static
make %{?_smp_mflags} gtkmm_docdir=%{_docdir}/%{name}/docs

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libgtkmm-2_4-1 -p /sbin/ldconfig
%postun -n libgtkmm-2_4-1 -p /sbin/ldconfig

%files -n libgtkmm-2_4-1
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gdkmm-2.4/
%{_libdir}/gtkmm-2.4/
%doc %{_datadir}/devhelp/books/%{_name}-2.4/
%doc %{_datadir}/doc/%{_name}-2.4/

%changelog
