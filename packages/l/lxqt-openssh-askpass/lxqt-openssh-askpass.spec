#
# spec file for package lxqt-openssh-askpass
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


Name:           lxqt-openssh-askpass
Version:        0.16.0
Release:        0
Summary:        OpenSSH password tool
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.12
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt) >= %{version}
Recommends:     %{name}-lang

%description
Tool that will prompt user for password when using OpenSSH in LXQt

%lang_package

%prep
%setup -q

%build
%cmake -DPULL_TRANSLATIONS=No
make %{?_smp_mflags}

%install
%cmake_install
install -Dm 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{ext_man}

%files lang -f %{name}.lang 
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/lxqt-openssh-askpass
%{_datadir}/lxqt/translations/lxqt-openssh-askpass/*

%changelog
