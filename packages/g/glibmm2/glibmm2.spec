#
# spec file for package glibmm2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define so_ver -2_68-1
# Define a baseversion to ease updates
%define base_ver 2.68
# Define upstream name
%define _name glibmm

Name:           glibmm2
Version:        2.86.0
Release:        0
Summary:        C++ Interface for Glib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/2.86/%{_name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  m4
BuildRequires:  meson >= 0.62
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.85.2
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sigc++-3.0) >= 2.99.5

# Do not export private Perl modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)

%description
Glibmm is the official C++ interface for the popular cross-platform
library Glib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package -n libglibmm%{so_ver}
Summary:        C++ Interface for Glib
Group:          System/Libraries

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
%autosetup -p1 -n %{_name}-%{version}
chmod -x NEWS
chmod -x glib/glibmm/environ.h

%build
%meson \
	%{nil}
%meson_build

# Temp disable test, currently needs internet during tests, disable until we figure out how to disable those
%dnl %check
%dnl %meson_test

%install
%meson_install
%fdupes %{buildroot}%{_prefix}

chmod +x %{buildroot}%{_libdir}/glibmm-%{base_ver}/proc/generate_wrap_init.pl
chmod +x %{buildroot}%{_libdir}/glibmm-%{base_ver}/proc/gmmproc

%ldconfig_scriptlets -n libglibmm%{so_ver}
%ldconfig_scriptlets -n libgiomm%{so_ver}

%files -n libglibmm%{so_ver}
%license COPYING
%{_libdir}/libglibmm-%{base_ver}.so.*
%{_libdir}/libglibmm_generate_extra_defs-%{base_ver}.so.*

%files -n libgiomm%{so_ver}
%{_libdir}/libgiomm-%{base_ver}.so.*

%files devel
%doc ChangeLog NEWS README.md
%{_libdir}/libgiomm-%{base_ver}.so
%{_libdir}/libglibmm-%{base_ver}.so
%{_libdir}/libglibmm_generate_extra_defs-%{base_ver}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/giomm-%{base_ver}
%{_includedir}/glibmm-%{base_ver}
%{_libdir}/glibmm-%{base_ver}
%{_libdir}/giomm-%{base_ver}

%changelog
