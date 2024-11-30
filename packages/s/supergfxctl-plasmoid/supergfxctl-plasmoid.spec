#
# spec file for package supergfxctl-plasmoid
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
%define qt6_version 6.4.0

Name:           supergfxctl-plasmoid
Version:        2.1.1
Release:        0
Summary:        KDE Plasma plasmoid for supergfxctl
License:        MPL-2.0
URL:            https://gitlab.com/Jhyub/supergfxctl-plasmoid
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= 6.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
Requires:       hicolor-icon-theme = 0.17
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-ksvg-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       supergfxctl

%description
KDE Plasma plasmoid for supergfxctl.
Features:
* Graphics mode switching
* dGPU power indication
* Dynamic plasmoid logo, tooltip, status
* Filter available switches
* Display dbus error message
* Revert change

%lang_package

%prep
%autosetup

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes %{buildroot}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_kf6_appstreamdir}/dev.jhyub.supergfxctl.appdata.xml
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-dgpu-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-dgpu-off.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-dgpu-suspended.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-compute-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-compute.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-dedicated-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-dedicated.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-egpu-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-egpu.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-hybrid-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-hybrid.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-integrated-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-integrated.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-vfio-active.svg
%{_kf6_iconsdir}/hicolor/scalable/status/supergfxctl-plasmoid-gpu-vfio.svg
%{_kf6_plasmadir}/plasmoids/dev.jhyub.supergfxctl/
%{_kf6_plugindir}/plasma/applets/dev.jhyub.supergfxctl.so

%changelog
