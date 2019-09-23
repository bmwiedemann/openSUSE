#
# spec file for package glibmm2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Update baselibs.conf when changing this
%define so_ver -2_60-1
# Define a baseversion to ease updates
%define base_ver 2.60
# Define upstream name
%define _name glibmm
Name:           glibmm2
Version:        2.59.1
Release:        0
Summary:        C++ Interface for Glib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org/
Source0:        http://download.gnome.org/sources/glibmm/2.59/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.55.1
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sigc++-3.0) >= 2.99.5

%description
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package -n libglibmm%{so_ver}
Summary:        C++ Interface for Glib
Group:          System/Libraries
Provides:       glibmm2 = %{version}
Obsoletes:      glibmm2 < %{version}

%description -n libglibmm%{so_ver}
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package -n libgiomm%{so_ver}
Summary:        C++ Interface for Gio
Group:          System/Libraries

%description -n libgiomm%{so_ver}
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package devel
Summary:        Development files for the Glib C++ API
Group:          Development/Libraries/C and C++
Requires:       libgiomm%{so_ver} = %{version}
Requires:       libglibmm%{so_ver} = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%post -n libglibmm%{so_ver} -p /sbin/ldconfig
%postun -n libglibmm%{so_ver} -p /sbin/ldconfig
%post -n libgiomm%{so_ver} -p /sbin/ldconfig
%postun -n libgiomm%{so_ver} -p /sbin/ldconfig

%files -n libglibmm%{so_ver}
%license COPYING
%{_libdir}/libglibmm-%{base_ver}.so.*
%{_libdir}/libglibmm_generate_extra_defs-%{base_ver}.so.*

%files -n libgiomm%{so_ver}
%{_libdir}/libgiomm-%{base_ver}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/glibmm-%{base_ver}
%{_libdir}/giomm-%{base_ver}
%{_datadir}/devhelp/books/%{_name}-%{base_ver}
%{_datadir}/doc/%{_name}-%{base_ver}
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
