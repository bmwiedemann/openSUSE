#
# spec file for package atkmm1_6
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


%define _name   atkmm
Name:           atkmm1_6
Version:        2.28.0
Release:        0
Summary:        C++ Binding for the ATK library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gtkmm.org/
Source:         https://download.gnome.org/sources/atkmm/2.28/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk) >= 1.18
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46.2

%description
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

%package -n libatkmm-1_6-1
Summary:        C++ Binding for the ATK library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libatkmm-1_6-1
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

%package devel
Summary:        C++ Binding for the ATK library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libatkmm-1_6-1 = %{version}

%description devel
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

%package doc
Summary:        C++ Binding for the ATK library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/HTML
Requires:       glibmm2-doc
BuildArch:      noarch

%description doc
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libatkmm-1_6-1 -p /sbin/ldconfig

%postun -n libatkmm-1_6-1 -p /sbin/ldconfig

%files -n libatkmm-1_6-1
%defattr (-, root, root)
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libatkmm-1.6.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/atkmm-1.6/
%{_libdir}/libatkmm-1.6.so
%{_libdir}/pkgconfig/atkmm-1.6.pc
%dir %{_libdir}/atkmm-1.6
%{_libdir}/atkmm-1.6/include/
%dir %{_libdir}/atkmm-1.6/proc
%{_libdir}/atkmm-1.6/proc/m4/

%files doc
%defattr (-, root, root)
%{_datadir}/devhelp/books/atkmm-1.6/
%{_datadir}/doc/atkmm-1.6/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
