#
# spec file for package plasma5-pa
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


%define kf5_version 5.62.0
%define qt5_version 5.12.0
%bcond_without lang
Name:           plasma5-pa
Version:        5.20.2
Release:        0
Summary:        The Plasma5 Volume Manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-pa-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-pa-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 0.0.14
BuildRequires:  kf5-filesystem
BuildRequires:  libcanberra-devel
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse)
Supplements:    packageand(plasma5-desktop:pulseaudio-module-x11)
# boo#1092871
%if 0%{?suse_version} > 1500
Recommends:     pulseaudio-module-gsettings
%else
Recommends:     pulseaudio-module-gconf
%endif
Requires:       kirigami2 >= %{kf5_version}
Requires:       pulseaudio-module-x11
Recommends:     %{name}-lang

%description
A volume manager plasmoid superseding kmix.

%lang_package
%prep
%setup -q -n plasma-pa-%{version}

%build
%if 0%{?suse_version} > 1500
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} -DUSE_GSETTINGS=TRUE
%else
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} -DUSE_GCONF=TRUE
%endif
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
%kf5_find_lang
%kf5_find_htmldocs
%endif

%files
%license COPYING*
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kpackage/
%{_kf5_servicesdir}/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/
%dir %{_kf5_sharedir}/kde4
%dir %{_kf5_sharedir}/kde4/apps
%dir %{_kf5_sharedir}/kde4/apps/kconf_update
%{_kf5_sharedir}/kde4/apps/kconf_update/disable_kmix.upd
%{_kf5_sharedir}/kde4/apps/kconf_update/plasmaVolumeDisableKMixAutostart.pl
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %{_kf5_htmldir}/en/*/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
