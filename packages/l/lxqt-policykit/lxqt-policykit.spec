#
# spec file for package lxqt-policykit
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


Name:           lxqt-policykit
Version:        0.16.0
Release:        0
Summary:        PolicyKit authentication agent
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(lxqt) >= %{version}
BuildRequires:  pkgconfig(lxqt-globalkeys) >= %{version}
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-qt5-core-1)
Recommends:     %{name}-lang

%description
PolicyKit authentication agent for LXQt

%lang_package

%prep
%setup -q

%build
%cmake -DPULL_TRANSLATIONS=No

make %{?_smp_mflags}

%install
%cmake_install
install -Dm 0644 man/%{name}-agent.1 %{buildroot}%{_mandir}/man1/%{name}-agent.1

%find_lang lxqt-policykit-agent --with-qt

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/lxqt-policykit-agent
%{_mandir}/man?/%{name}-agent.?%{ext_man}
%{_sysconfdir}/xdg/autostart/lxqt-policykit-agent.desktop

%files lang -f lxqt-policykit-agent.lang 

%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-policykit-agent

%changelog
