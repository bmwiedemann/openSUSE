#
# spec file for package lxqt-notificationd
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


Name:           lxqt-notificationd
Version:        2.0.1
Release:        0
Summary:        LXQt Notification daemon
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-notificationd
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt) >= 6.0.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt) >= 2.0.0
Recommends:     %{name}-lang = %{version}-%{release}

%description
The LXQt Notification daemon

%lang_package

%prep
%autosetup
sed -i '/Categories/s/\(LXQt\)/X-\1/' ./config/lxqt-config-notificationd.desktop.in

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
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%config %{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
