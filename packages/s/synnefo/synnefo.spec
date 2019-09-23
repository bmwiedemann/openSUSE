#
# spec file for package synnefo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2016 Kai-Uwe Behrmann <ku.b@gmx.de>
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


%define desktopdir      %{_datadir}/applications
Name:           synnefo
Version:        1.1.0
Release:        0
Summary:        Color Management Settings GUI
License:        BSD-2-Clause
Group:          System/GUI/Other
URL:            https://www.oyranos.org/synnefo
Source:         synnefo_%{version}.orig.tar.bz2
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  liboyranos-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
# we need the oyranos_logo.png icon
Requires:       oyranos

%package      -n libOyranosSynnefo1
Summary:        Oyranos Settings GUI
Group:          System/Libraries

%package      -n libOyranosSynnefo-devel
Summary:        Headers, configuration and documentation for synnefo
Group:          Development/Languages/C and C++
Requires:       libOyranosSynnefo1 = %{version}
Requires:       liboyranos-devel

%description
Color Management System (CMS) Settings.
Synnefo uses the Oyranos CMS to provide the ability to set and examine
device profiles, as well as to change system-wide color settings.

%description   -n libOyranosSynnefo1
Core library for Oyranos Settings widgets.

%description   -n libOyranosSynnefo-devel
Headers, configuration and static Libs for Oyranos/Qt based Synnefo.

%package -n libOyranosSynnefo-devel-static
Summary:        Static library for synnefo
Group:          Development/Libraries/C and C++
Requires:       libOyranosSynnefo-devel = %{version}

%description -n libOyranosSynnefo-devel-static
Contains the static libraries for developing with synnefo.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%if 0%{?suse_version} > 0
echo 'X-SuSE-translate=true' >> src/app/extras/oyranos-config-%{name}.desktop
%endif
%cmake_install

%post -n libOyranosSynnefo1 -p /sbin/ldconfig
%postun -n libOyranosSynnefo1 -p /sbin/ldconfig

%files
%doc README.md
%{_bindir}/*%{name}
%{_mandir}/man1/*%{name}*
%{_datadir}/pixmaps/*%{name}.*
%{desktopdir}/*%{name}.desktop

%files -n libOyranosSynnefo1
%doc README.md
%{_libdir}/libOyranosSynnefo*.so.*

%files -n libOyranosSynnefo-devel
%doc README.md
%dir %{_includedir}/synnefo/
%{_includedir}/synnefo/*
%dir %{_libdir}/cmake/
%dir %{_libdir}/cmake/synnefo/
%{_libdir}/cmake/synnefo/*
%{_libdir}/libOyranosSynnefo*.so

%files -n libOyranosSynnefo-devel-static
%{_libdir}/libOyranosSynnefo*-static.a

%changelog
