#
# spec file for package plasma-pass
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


%define lang_name plasma_applet_org.kde.plasma.pass
%bcond_without lang
Name:           plasma-pass
Version:        1.1.0
Release:        0
Summary:        Plasma 5 widget for the pass password manager
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz.sig
Source2:        plasma-pass.keyring
%endif
Patch0:         0001-Fix-build-against-Qt-5.15.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5I18n) >= 5.42.0
BuildRequires:  cmake(KF5ItemModels) >= 5.42.0
BuildRequires:  cmake(KF5Plasma) >= 5.42.0
BuildRequires:  cmake(Qt5Core) >= 5.9
BuildRequires:  cmake(Qt5DBus) >= 5.9
BuildRequires:  cmake(Qt5Gui) >= 5.9
BuildRequires:  cmake(Qt5Qml) >= 5.9
Recommends:     %{name}-lang
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
%if %{with lang}
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
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.pass.desktop

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
