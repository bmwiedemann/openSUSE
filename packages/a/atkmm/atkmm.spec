#
# spec file for package atkmm
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


%define base_ver 2.36
%define libname  lib%{name}-2_36-1

Name:           atkmm
Version:        2.36.2
Release:        0
Summary:        C++ Binding for the ATK library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/%{name}/%{base_ver}/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson >= 0.55.0
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atk) >= 2.33.3
BuildRequires:  pkgconfig(glibmm-2.68)
Recommends:     %{name}-doc = %{version}

%description
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

%package -n %{libname}
Summary:        C++ Binding for the ATK library -- Shared Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

This package provides the ATK library's C++'s bindings shared library.

%package devel
Summary:        C++ Binding for the ATK library -- Development Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} >= %{version}

%description devel
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

This package provides all the necessary files for development with ATK
library's C++ bindings.

%package doc
Summary:        C++ Binding for the ATK library -- Documentation
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/HTML
Requires:       glibmm2-doc
BuildArch:      noarch

%description doc
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

This package provides the documentation files for the ATK library's
C++ bindings.

%prep
%autosetup -p1

%build
# NEWS should not be executable
chmod -x NEWS
%meson \
	-Dbuild-documentation=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libatkmm-%{base_ver}.so.*

%files devel
%{_includedir}/atkmm-%{base_ver}/
%{_libdir}/libatkmm-%{base_ver}.so
%{_libdir}/pkgconfig/atkmm-%{base_ver}.pc
%{_libdir}/atkmm-%{base_ver}/include/
%dir %{_libdir}/atkmm-%{base_ver}
%dir %{_libdir}/atkmm-%{base_ver}/proc
%{_libdir}/atkmm-%{base_ver}/proc/m4/

%files doc
%license COPYING.tools
%doc AUTHORS ChangeLog README.md
%{_datadir}/devhelp/books/atkmm-%{base_ver}/
%{_datadir}/doc/atkmm-%{base_ver}/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
