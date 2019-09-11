#
# spec file for package adwaita-qt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if (0%{?is_opensuse} && 0%{?suse_version} < 1500) || 0%{?is_backports}
%bcond_without qt4
%else
%bcond_with qt4
%endif
Name:           adwaita-qt
Version:        1.1.0
Release:        0
Summary:        Adwaita theme for Qt-based applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-devel
%if %{with qt4}
BuildRequires:  libqt4-devel
%endif

%description
Theme to let Qt applications fit nicely into GNOME desktop.

%package -n adwaita-qt4
Summary:        Adwaita Qt4 theme
Group:          System/GUI/GNOME
Supplements:    packageand(libqt4:gnome-session)

%description -n adwaita-qt4
Adwaita theme variant for applications utilizing Qt4

%package -n adwaita-qt5
Summary:        Adwaita Qt5 theme
Group:          System/GUI/GNOME
Supplements:    packageand(libQt5Core5:gnome-session)

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5

%prep
%setup -q

%build
%if %{with qt4}
# Qt4 build and install
%cmake -DUSE_QT4=ON
make %{?_smp_mflags}
cd ..
%cmake_install
%endif

# Qt5 build
rm -rf build
%cmake -DUSE_QT4=OFF
make %{?_smp_mflags}

%install
# Qt5 install
%cmake_install

%if %{with qt4}
%files -n adwaita-qt4
%defattr(-,root,root)
%license LICENSE.LGPL2
%doc README.md
%dir %{_libdir}/qt4/plugins/styles
%{_libdir}/qt4/plugins/styles/adwaita.so
%endif

%files -n adwaita-qt5
%defattr(-,root,root)
%license LICENSE.LGPL2
%doc README.md
%dir %{_libdir}/qt5/plugins/styles
%{_libdir}/qt5/plugins/styles/adwaita.so

%changelog
