#
# spec file for package plasma-pass
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


%define lang_name plasma_applet_org.kde.plasma.pass
%define kf5_min_version 5.57.0
%define qt_min_version 5.11
%bcond_without released
Name:           plasma-pass
Version:        1.2.0
Release:        0
Summary:        Plasma 5 widget for the pass password manager
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz.sig
Source2:        plasma-pass.keyring
%endif
# PATCH-FIX-OPENSUSE -- Decrease the minimum Qt version to allow building on 15.2/15.3
Patch0:         0001-Fix-build-Qt-5.12.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5I18n) >= %{kf5_min_version}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_min_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_min_version}
BuildRequires:  cmake(Qt5Concurrent) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt_min_version}
BuildRequires:  pkgconfig(liboath)
Recommends:     password-store

%description
Plasma Pass is a Plasma 5 widget to access, display and copy passwords
generated and stored by the "pass" password manager.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
 %find_lang %{lang_name} %{name}.lang
%endif

%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%dir %{_kf5_plasmadir}/plasmoids
%dir %{_kf5_qmldir}/org/kde/plasma/
%dir %{_kf5_qmldir}/org/kde/plasma/private/
%dir %{_kf5_qmldir}/org/kde/plasma/private/plasmapass
%{_kf5_appstreamdir}/org.kde.plasma.pass.appdata.xml
%{_kf5_debugdir}/plasma-pass.categories
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.pass/
%{_kf5_qmldir}/org/kde/plasma/private/plasmapass/libplasmapassplugin.so
%{_kf5_qmldir}/org/kde/plasma/private/plasmapass/qmldir
%if %{pkg_vcmp cmake(KF5Plasma) < 5.84} || %{pkg_vcmp cmake(KF5Plasma) >= 5.89}
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.pass.desktop
%endif

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
