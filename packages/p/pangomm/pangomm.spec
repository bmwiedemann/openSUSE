#
# spec file for package pangomm
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


%define base_ver 2.48
# Update baselibs.conf when changing the version here
%define libname  lib%{name}-2_48-1

Name:           pangomm
Version:        2.48.0
Release:        0
Summary:        C++ interface for pango
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/%{base_ver}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairomm-1.16) >= 1.2.2
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(pangocairo) >= 1.31.0
Recommends:     %{name}-doc = %{version}

%description
pangomm provides a C++ interface to the pango library.

%package -n %{libname}
Summary:        C++ interface for Pango
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
pangomm provides a C++ interface to the pango library.

%package devel
Summary:        Development files for pangomm, a C++ API for Pango
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} >= %{version}

%description devel
pangomm provides a C++ interface to the pango library.

%package doc
Summary:        Developer documentation for pangomm, a C++ interface for Pango
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/HTML

%description doc
pangomm provides a C++ interface to the pango library.
This package contains the developer documentation.

%prep
%autosetup -p1

%build
%meson \
	-Dbuild-documentation=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libpangomm-%{base_ver}.so.*

%files devel
%license COPYING.tools
%{_includedir}/pangomm-%{base_ver}/
%{_libdir}/libpangomm-%{base_ver}.so
%{_libdir}/pkgconfig/pangomm-%{base_ver}.pc
%{_libdir}/pangomm-%{base_ver}

%files doc
%doc AUTHORS README
%{_datadir}/devhelp/books/pangomm-%{base_ver}/
%{_datadir}/doc/pangomm-%{base_ver}/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
