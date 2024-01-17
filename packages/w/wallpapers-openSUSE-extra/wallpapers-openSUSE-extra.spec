#
# spec file for package wallpapers-openSUSE-extra
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


Name:           wallpapers-openSUSE-extra
Version:        15
Release:        0
Summary:        openSUSE Extra Wallpapers
License:        CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-4.0
Group:          System/GUI/Other
URL:            https://github.com/openSUSE/wallpapers
Source0:        wallpapers.tar.xz
Provides:       extra-wallpapers
BuildArch:      noarch

%description
Extra wallpapers for openSUSE Leap %{version}

%prep
%setup -q -c

%build

%install
%make_install

%files
%license leap%{version}/license/*
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/wallpapers-leap%{version}.xml
%{_datadir}/wallpapers
%{_datadir}/wallpapers/leap%{version}

%changelog
