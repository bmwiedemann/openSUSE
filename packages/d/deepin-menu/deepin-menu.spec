#
# spec file for package deepin-menu
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           deepin-menu
Version:        3.4.8
Release:        0
License:        GPL-3.0+
Summary:        Menu service for Linux Deepin
Url:            https://github.com/linuxdeepin/deepin-menu
Group:          System/GUI/Other
Source:         https://github.com/linuxdeepin/deepin-menu/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Menu is the unified menu service for Deepin Desktop Environment.

%prep
# %setup -q -n %{name}-%{commit}
%setup -q

# Remove python shebang
find -iname "*.py" | xargs sed -i '/env python/d'

%build
# python3 setup.py build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
make %{?_smp_mflags}

%install
%qmake5_install

rm -rf %{buildroot}%{_prefix}/deepin_menu
mkdir -p %{buildroot}%{_datadir}/dbus-1/services
install -m 0644 data/com.deepin.menu.service %{buildroot}%{_datadir}/dbus-1/services
mkdir -p %{buildroot}%{_datadir}/dbus-1/interfaces
install -m 0644 data/com.deepin.menu.Manager.xml %{buildroot}%{_datadir}/dbus-1/interfaces
install -m 0644 data/com.deepin.menu.Menu.xml %{buildroot}%{_datadir}/dbus-1/interfaces

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md LICENSE
%{_bindir}/deepin-menu
%{_datadir}/dbus-1/services/com.deepin.menu.service
%{_datadir}/dbus-1/interfaces/com.deepin.menu.*.xml

%changelog
