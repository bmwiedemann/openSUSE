#
# spec file for package lxqt-powermanagement
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


Name:           lxqt-powermanagement
Version:        2.0.0
Release:        0
Summary:        Power Management and Auto-suspend
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-powermanagement
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(lxqt-globalkeys-ui) >= 2.0.0
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-screensaver)
Requires:       upower
Recommends:     %{name}-lang = %{version}-%{release}

%description
LXQt daemon for power management and auto-suspend

%lang_package

%prep
%autosetup
sed -i '/^Categories/s/\(LXQt\;\)/X-\1/' config/lxqt-config-powermanagement.desktop.in

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt --all-name

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_bindir}/lxqt-config-powermanagement
%{_datadir}/applications/lxqt-config-powermanagement.desktop
%{_datadir}/icons/hicolor/*/devices/*.svg
%config %{_sysconfdir}/xdg/autostart/%{name}.desktop

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
