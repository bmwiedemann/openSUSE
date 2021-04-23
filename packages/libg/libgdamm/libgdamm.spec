#
# spec file for package libgdamm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libgdamm
Version:        4.99.11
Release:        0
Summary:        C++ wrappers for libgda
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gtkmm.org/
Source:         http://download.gnome.org/sources/libgdamm/4.99/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46.1
BuildRequires:  pkgconfig(libgda-5.0) >= 5.0.2

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package -n %{name}-5_0-13
Summary:        C++ wrappers for libgda
Group:          System/Libraries

%description -n %{name}-5_0-13
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package devel
Summary:        C++ wrappers for libgda
Group:          Development/Libraries/GNOME
Requires:       %{name}-5_0-13 = %{version}

%description devel
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

This package contains headers and libraries that programmers will need
to develop applications which use libgdamm.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/doc/libgdamm-5.0/

%post -n %{name}-5_0-13 -p /sbin/ldconfig
%postun -n %{name}-5_0-13 -p /sbin/ldconfig

%files -n %{name}-5_0-13
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/libgdamm-5.0.so.*

%files devel
%{_includedir}/libgdamm-5.0/
%{_libdir}/libgdamm-5.0.so
%{_libdir}/libgdamm-5.0/
%{_libdir}/pkgconfig/libgdamm-5.0.pc
%doc %{_datadir}/devhelp/books/libgdamm-5.0/
%doc %{_datadir}/doc/libgdamm-5.0/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
