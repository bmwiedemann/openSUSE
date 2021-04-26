#
# spec file for package deepin-polkit-agent
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _name dde-polkit-agent

Name:           deepin-polkit-agent
Version:        5.3.0.3
Release:        0
Summary:        Deepin Polkit Agent
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        https://github.com/linuxdeepin/dde-polkit-agent/archive/%{version}/%{_name}-%{version}.tar.gz
Group:          System/GUI/Other
BuildRequires:  dtkcore
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gsettings-qt)
Recommends:     %{name}-lang

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name} = %{version}-%{release}
Group:          Development/Languages/C and C++

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp

%build
%qmake5 PREFIX=%{_prefix}
%make_build

%install
%qmake5_install

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
