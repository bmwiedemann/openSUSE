#
# spec file for package compton-conf
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


Name:           compton-conf
Version:        0.16.0
Release:        0
Summary:        Compositor Configuration
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
# compton-conf desktop file uses compton icon
# Adding it as BR so that checks detect the file
BuildRequires:  compton
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(lxqt)
Requires:       compton
Recommends:     %{name}-lang

%description
X composite manager configuration for compton

%lang_package

%prep
%setup -q
sed -i '/Categories/s/\(LXQt\;\)/X-\1/' compton-conf.desktop.in

%build
%cmake \
      -DUSE_QT5=ON \
      -DPULL_TRANSLATIONS=OFF
%make_jobs

%install
%cmake_install

# ERROR: Icon file not installed (preferences-system-windows)
mkdir -p %{buildroot}%{_datadir}/pixmaps
touch %{buildroot}%{_datadir}/pixmaps/preferences-system-windows

%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/compton-conf
%{_datadir}/applications/*.desktop
%dir %{_datadir}/compton-conf/
%{_datadir}/compton-conf/compton.conf*
%{_sysconfdir}/xdg/autostart/lxqt-compton.desktop
%ghost %{_datadir}/pixmaps/preferences-system-windows

%files lang
%{_datadir}/compton-conf/translations/

%changelog
