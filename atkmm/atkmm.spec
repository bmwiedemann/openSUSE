#
# spec file for package atkmm
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


%define base_ver 2.30
# Update baselibs.conf when changing the version here
%define libname  lib%{name}-2_30-1
Name:           atkmm
Version:        2.29.1
Release:        0
Summary:        C++ Binding for the ATK library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/%{name}/2.29/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk) >= 1.18
BuildRequires:  pkgconfig(glibmm-2.60)
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
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
%doc AUTHORS ChangeLog README
%{_datadir}/devhelp/books/atkmm-%{base_ver}/
%{_datadir}/doc/atkmm-%{base_ver}/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
