#
# spec file for package deepin-polkit-agent
#
# Copyright (c) 2022 SUSE LLC
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


%define _name dde-polkit-agent

Name:           deepin-polkit-agent
Version:        5.5.21
Release:        0
Summary:        Deepin Polkit Agent
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        https://github.com/linuxdeepin/dde-polkit-agent/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  dtkcore
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(polkit-qt5-1)
Recommends:     %{name}-lang

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp
sed -i '/setCancel/d' policykitlistener.cpp
sed -i 's/qdbusxml2cpp/qdbusxml2cpp-qt5/g' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/polkit-1-dde
%{_prefix}/lib/polkit-1-dde/%{_name}

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{_name}/

%files devel
%defattr(-,root,root,-)
%{_includedir}/dpa

%changelog
