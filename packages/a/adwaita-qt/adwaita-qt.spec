#
# spec file for package adwaita-qt
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


%define sover 1
Name:           adwaita-qt
Version:        1.2.1
Release:        0
Summary:        Adwaita theme for Qt-based applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/FedoraQt/adwaita-qt
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-devel >= 5.12
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libxcb-devel
Requires:       adwaita-qt5
Obsoletes:      adwaita-qt4 < 1.2.0

%description
Theme to let Qt applications fit nicely into GNOME desktop.

%package -n adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       libadwaitaqt%{sover} = %{version}-%{release}
Supplements:    (libQt5Core5 and gnome-session)

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5

%package -n libadwaitaqt%{sover}
Summary:        Adwaita Qt5 library
# The package was wwronlgy called  libadwaitaqt1_2_0 in the past
# As long as we are at .so.1, we can obsolete this old, wrong
# package name
Obsoletes:      libadwaitaqt1_2_0

%description -n libadwaitaqt%{sover}
Adwaita theme variant for applications utilizing Qt5

%package -n libadwaitaqt-devel
Summary:        Development files for libadwaitaqt
Requires:       libadwaitaqt%{sover} = %{version}-%{release}

%description -n libadwaitaqt-devel
The libadwaitaqt-devel package contains libraries and header files for
developing applications that use libadwaitaqt%{sover}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post   -n libadwaitaqt%{sover} -p /sbin/ldconfig
%postun -n libadwaitaqt%{sover} -p /sbin/ldconfig

%files -n adwaita-qt5
%license LICENSE.LGPL2
%doc README.md
%dir %{_libdir}/qt5/plugins/styles
%{_libdir}/qt5/plugins/styles/adwaita.so

%files -n libadwaitaqt%{sover}
%{_libdir}/libadwaitaqt.so.*
%{_libdir}/libadwaitaqtpriv.so.*

%files -n libadwaitaqt-devel
%dir %{_includedir}/AdwaitaQt
%{_includedir}/AdwaitaQt/*.h
%dir %{_libdir}/cmake/AdwaitaQt
%{_libdir}/cmake/AdwaitaQt/*.cmake
%{_libdir}/pkgconfig/adwaita-qt.pc
%{_libdir}/libadwaitaqt.so
%{_libdir}/libadwaitaqtpriv.so

%changelog
