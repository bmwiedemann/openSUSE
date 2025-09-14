#
# spec file for package plasma-pass
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.3.0
%define plasma6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           plasma-pass
Version:        1.3.0
Release:        0
Summary:        Plasma widget for the pass password manager
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma-pass/%{name}-%{version}.tar.xz.sig
Source2:        plasma-pass.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Plasma5Support) >= %{plasma6_version}
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  pkgconfig(liboath)
Recommends:     password-store

%description
Plasma Pass is a Plasma widget to access, display and copy passwords
generated and stored by the "pass" password manager.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/plasma-pass.categories
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.pass/
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/plasmapass/
%if %{pkg_vcmp cmake(KF6Package) < 6.18}
%{_kf6_appstreamdir}/org.kde.plasma.pass.appdata.xml
%endif

%files lang -f %{name}.lang

%changelog
