#
# spec file for package kajongg
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%{?sle15_python_module_pythons}
%if 0%{?suse_version} > 1500
%define pyver python3
%else
%define pyver python311
%endif

%bcond_without released
Name:           kajongg
Version:        24.05.2
Release:        0
Summary:        4 Player Mahjongg game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kajongg
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  %{pyver}-Twisted >= 16.6.0
BuildRequires:  %{pyver}-base >= 3.8.0
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KMahjongglib6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       %{pyver}-Twisted
Requires:       %{pyver}-PyQt6
BuildArch:      noarch

%description
Kajongg is a version of the four player Mahjongg tile game.

%lang_package

%prep
%autosetup -p1 -n kajongg-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license COPYING*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/kajongg/
%{_kf6_applicationsdir}/org.kde.kajongg.desktop
%{_kf6_sharedir}/kajongg/
%{_kf6_appstreamdir}/org.kde.kajongg.appdata.xml
%{_kf6_bindir}/kajongg
%{_kf6_bindir}/kajonggserver
%{_kf6_iconsdir}/hicolor/*/actions/games-kajongg-law.*
%{_kf6_iconsdir}/hicolor/*/apps/kajongg.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kajongg/

%changelog
