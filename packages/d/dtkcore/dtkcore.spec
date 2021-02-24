#
# spec file for package dtkcore
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017-2021 Hillwood Yang <hillwood@opensuse.org>
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


%define libver 5
%define apiver 5.0.0

Name:           dtkcore
Version:        5.4.0
Release:        0
Summary:        Deepin Tool Kit Core
License:        LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        https://github.com/linuxdeepin/dtkcore/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  pkgconfig(gsettings-qt)
Requires:       deepin-desktop-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepint Tool Kit (Dtk) is the base devlopment tool of all C++/Qt Developer work
on Deepin.

You shoud read the [Deepin Application Specification](doc/Specification)
firstly.

%package -n lib%{name}%{libver}
Summary:        Deepin Toolkit Core libraries
Group:          System/Libraries

%description -n lib%{name}%{libver}
Deepint Tool Kit (Dtk) is the base devlopment tool of all C++/Qt Developer work
on Deepin.

%package devel
Summary:        Development tools for dtkcore
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
The dtkcore-devel package contains the header files and developer
docs for dtkcore.

You shoud firstly read the "Deepin Application Specification".

%prep
%setup -q
sed -i 's/system(lrelease/system(lrelease-qt5/g' src/dtk_translation.prf
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' tools/script/dtk-license.py
sed -i 's|#!env python|#!/usr/bin/python3|g' tools/script/dtk-translate.py

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install
# Remove useless files
rm -rf %{buildroot}/usr/tests

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libdtk-%{apiver}
%{_datadir}/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%files -n lib%{name}%{libver}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/dtkcore.pc
%{_includedir}/libdtk-%{apiver}
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/mkspecs
%{_libdir}/qt5/mkspecs/features
%{_libdir}/qt5/mkspecs/modules
%dir %{_libdir}/cmake
%{_libdir}/cmake/*

%changelog
