#
# spec file for package glibmm2_4
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


# Update baselibs.conf when changing this
%define so_ver -2_4-1
%define _name glibmm
Name:           glibmm2_4
Version:        2.66.6
Release:        0
Summary:        C++ Interface for Glib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/2.66/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM glibmm2_4-docs-without-timestamp.patch -- Do not add timestamps to generated doc files
Patch0:         glibmm2_4-docs-without-timestamp.patch

BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.61.2
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.49.7
BuildRequires:  pkgconfig(gobject-2.0) >= 2.49.7
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.9.1

%description
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package -n libglibmm%{so_ver}
Summary:        C++ Interface for Glib
Group:          System/Libraries
Provides:       glibmm2 = %{version}
Obsoletes:      glibmm2 < %{version}
Provides:       glibmm24 = %{version}
Obsoletes:      glibmm24 < %{version}

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
Summary:        C++ Interface for GLib
Group:          Development/Libraries/C and C++
Requires:       libgiomm%{so_ver} = %{version}
Requires:       libglibmm%{so_ver} = %{version}
Provides:       glibmm24-devel = %{version}
Obsoletes:      glibmm24-devel < %{version}
# glibmm2-devel keeps on existing beyond version 2.50 - make it easy for upgraders
Provides:       glibmm2-devel = %{version}
Obsoletes:      glibmm2-devel < 2.51
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%prep
%autosetup -p1 -n %{_name}-%{version}
chmod -x NEWS

%build
%meson \
	-Dbuild-documentation=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}/{_prefix}

%ldconfig_scriptlets -n libglibmm%{so_ver}
%ldconfig_scriptlets -n libgiomm%{so_ver}

%files -n libglibmm%{so_ver}
%license COPYING
%{_libdir}/libglibmm-2.4.so.*
%{_libdir}/libglibmm_generate_extra_defs-2.4.so.*

%files -n libgiomm%{so_ver}
%{_libdir}/libgiomm-2.4.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README.md
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/glibmm-2.4
%{_libdir}/giomm-2.4
%{_datadir}/devhelp/books/%{_name}-2.4
%{_datadir}/doc/%{_name}-2.4
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
