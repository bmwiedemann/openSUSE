#
# spec file for package openSUSE-xfce-icon-theme
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


%define theme_name openSUSE-Xfce
Name:           openSUSE-xfce-icon-theme
Version:        4.16.1+git.6.2345514
Release:        0
Summary:        openSUSE Xfce Default Icon Theme
License:        GPL-2.0-only
URL:            https://code.opensuse.org/xfce/openSUSE-xfce-icon-theme
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  adwaita-icon-theme
Requires:       adwaita-icon-theme
BuildArch:      noarch

%description
Add-on to Adwaita icon theme for Xfce. Inherits from Adwaita

%prep
%autosetup

%build
# Nothing to build

%install
mkdir -p  %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a ./ %{buildroot}%{_datadir}/icons/%{theme_name}
rm %{buildroot}%{_datadir}/icons/%{theme_name}/{COPYING,README.md}

%files
%license COPYING
%doc README.md
%dir %{_datadir}/icons/%{theme_name}
%{_datadir}/icons/%{theme_name}/*

%changelog
