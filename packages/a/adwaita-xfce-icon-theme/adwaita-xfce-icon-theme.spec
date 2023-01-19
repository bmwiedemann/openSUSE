#
# spec file for package adwaita-xfce-icon-theme
#
# Copyright (c) 2023 SUSE LLC
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


Name:           adwaita-xfce-icon-theme
Version:        0.0.3+git0.e0f73b9
Release:        0
Summary:        Icon theme for Xfce complementing Adwaita
License:        GPL-2.0-only
URL:            https://github.com/shimmerproject/adwaita-xfce-icon-theme
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  adwaita-icon-theme
BuildArch:      noarch
Provides:       openSUSE-xfce-icon-theme = 4.16.2
Obsoletes:      openSUSE-xfce-icon-theme < 4.16.2

%description
This icon theme is an extension for Adwaita fixing missing icons that are used in Xfce.
It is not a complete theme and inherits the bulk of icons from Adwaita.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_datadir}/icons/adwaita-xfce/

%changelog
