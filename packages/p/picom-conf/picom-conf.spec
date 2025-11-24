#
# spec file for package picom-conf
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define  _name  picom_conf
Name:           picom-conf
Version:        0.17.0
Release:        0
Summary:        GUI configuration tool for Picom X composite manager
License:        LGPL-2.1-or-later
URL:            https://github.com/qtilities/picom-conf
Source0:        https://github.com/qtilities/picom-conf/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  qtilitools
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libconfig)
Requires:       picom
Conflicts:      compton-conf

%description
picom-conf is a configuration tool for X composite manager picom.

%lang_package

%prep
%autosetup -p1

%build
%cmake \
    -DPICOM_ENABLE_AUTOSTART=ON \
    -DPROJECT_TRANSLATIONS_UPDATE=ON
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_sysconfdir}/xdg/autostart/picom.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/lxqt-picom.desktop

%find_lang %{name} --with-qt

%files
%doc AUTHORS README.md
%license COPYING
%exclude %{_datadir}/%{name}/translations
%config %{_sysconfdir}/xdg/autostart/lxqt-picom.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/metainfo/%{_name}.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/picom.conf.example

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations

%changelog
