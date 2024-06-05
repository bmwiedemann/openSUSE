#
# spec file for package lxqt-openssh-askpass
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


Name:           lxqt-openssh-askpass
Version:        2.0.1
Release:        0
Summary:        GUI to query passwords on behalf of SSH agents
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-openssh-askpass
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt) >= 2.0.0
Recommends:     %{name}-lang = %{version}-%{release}

%description
lxqt-openssh-askpass is a GUI to query credentials on behalf of other
programs. As indicated by its name it's primarily targeted at ssh-agent,
the SSH agent of OpenSSH, but it works with other applications like e. g.
EncFS as well.

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}
%license LICENSE

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
