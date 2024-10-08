#
# spec file for package wallpapers-openSUSE-extra
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


Name:           wallpapers-openSUSE-extra
Version:        16
Release:        0
Summary:        openSUSE Extra Wallpapers
License:        CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-4.0 AND SUSE-Public-Domain
Group:          System/GUI/Other
URL:            https://github.com/openSUSE/wallpapers
Source0:        wallpapers-master.zip
# Building svg's at the build time
BuildRequires:  optipng
BuildRequires:  rsvg-convert
BuildRequires:  unzip
Provides:       extra-wallpapers
BuildArch:      noarch

%description
Extra wallpapers for openSUSE Leap %{version}

%prep
%autosetup -p1 -n wallpapers-master

%build

%install
%make_install

%files
%license leap%{version}/license/*
%dir %{_datadir}/gnome-background-properties
%dir %{_datadir}/wallpapers
%{_datadir}/gnome-background-properties/wallpapers-leap%{version}.xml
%{_datadir}/wallpapers/leap%{version}

%package 		leap15
Summary:        wallpapers from openSUSE Leap 15.
Group:          System/GUI/Other

%description leap15
This package contains wallpapers from openSUSE Leap 15.

%files leap15
%license leap15/license/*
%{_datadir}/gnome-background-properties/wallpapers-leap15.xml
%{_datadir}/wallpapers/leap15

%changelog
