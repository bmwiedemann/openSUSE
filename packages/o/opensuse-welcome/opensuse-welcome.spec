#
# spec file for package opensuse-welcome
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


%define __builder ninja
%define _name openSUSE-welcome

Name:           opensuse-welcome
Version:        0.1.9+git.0.66be0d8
Release:        0
Summary:        Welcome utility for openSUSE
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/openSUSE-welcome
Source0:        %{_name}-%{version}.tar.xz
# Source file to produce opensuse-welcome-lang.inc
Source98:       opensuse-welcome-lang-recommends.sh
# REcommend the lang package based on installed locales
# the -lang package actually does not install the translations
# to a standard location, which results in the lang not having the
# relevant supplements added.
Source99:       opensuse-welcome-lang.inc
BuildRequires:  hicolor-icon-theme
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildRequires:  libqt5-linguist
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngine)
%include %{SOURCE99}

%lang_package

%description
A welcome utility built to welcome new users to openSUSE.

%prep
%setup -q -n %{_name}-%{version}

%build
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
