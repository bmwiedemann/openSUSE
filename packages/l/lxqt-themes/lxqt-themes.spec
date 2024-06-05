#
# spec file for package lxqt-themes
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


Name:           lxqt-themes
Version:        2.0.0
Release:        0
Summary:        Themes, graphics and icons for LXQt
License:        LGPL-2.1-or-later
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-themes
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        lxqt-themes.keyring
Source3:        logo.tar.xz
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(lxqt2-build-tools) >= 2.0.0
BuildArch:      noarch

%description
Themes, graphics and icons for LXQt.

%prep
%autosetup -a3

%build
%cmake

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/lxqt/themes
install -Dm 0644 opensuse-*.svg -t %{buildroot}%{_datadir}/lxqt/graphics/

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/palettes
%dir %{_datadir}/lxqt/wallpapers
%{_datadir}/lxqt/graphics
%{_datadir}/lxqt/themes
%{_datadir}/icons/hicolor/*/places/*.??g
%{_datadir}/icons/hicolor/*/apps/*.??g
%{_datadir}/lxqt/palettes/*
%{_datadir}/lxqt/wallpapers/*

%changelog
