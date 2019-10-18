#
# spec file for package pangomm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define base_ver 2.44
# Update baselibs.conf when changing the version here
%define libname  lib%{name}-2_44-1

Name:           pangomm
Version:        2.43.1
Release:        0
Summary:        C++ interface for pango
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/2.43/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM pangomm-use-glibmm-262.patch -- Forward port to use glibmm-2.62
Patch0:         pangomm-use-glibmm-262.patch

BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  mm-common
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairomm-1.16) >= 1.2.2
BuildRequires:  pkgconfig(glibmm-2.62)
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
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
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
