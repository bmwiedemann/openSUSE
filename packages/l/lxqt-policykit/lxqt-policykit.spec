#
# spec file for package lxqt-policykit
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


Name:           lxqt-policykit
Version:        2.1.0
Release:        0
Summary:        PolicyKit authentication agent
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-policykit
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt) >= 2.1.0
BuildRequires:  pkgconfig(polkit-agent-1)
Recommends:     %{name}-lang = %{version}-%{release}

%description
PolicyKit authentication agent for LXQt

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name}-agent --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}-agent
%{_mandir}/man?/%{name}-agent.?%{?ext_man}
%config %{_sysconfdir}/xdg/autostart/%{name}-agent.desktop
%license LICENSE

%files lang -f %{name}-agent.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/%{name}-agent

%changelog
