#
# spec file for package opensuse-welcome
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define __builder ninja

Name:           opensuse-welcome
Version:        0.1.6
Release:        0
Summary:        Welcome utility for openSUSE
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/openSUSE-welcome
Source0:        https://github.com/openSUSE/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  hicolor-icon-theme
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngine)
Recommends:     %{name}-lang = %{version}

%lang_package

%description
A welcome utility built to welcome new users to openSUSE.

%prep
%setup -q

%build
./i18n.sh
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/opensuse-welcome
%{_datadir}/applications/org.opensuse.opensuse_welcome.desktop
%{_sysconfdir}/xdg/autostart/org.opensuse.opensuse_welcome.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.opensuse.opensuse_welcome.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.opensuse.opensuse_welcome-symbolic.svg
%{_datadir}/metainfo/org.opensuse.opensuse_welcome.appdata.xml

%files lang
%{_datadir}/openSUSE-Welcome/

%changelog
