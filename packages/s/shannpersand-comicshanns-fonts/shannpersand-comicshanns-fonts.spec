#
# spec file for package shannpersand-comicshanns-fonts
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


Name:           shannpersand-comicshanns-fonts
Version:        2
Release:        0
Summary:        Sans-serif casual script typeface
License:        MIT
Group:          System/X11/Fonts
URL:            https://github.com/shannpersand/comic-shanns
Source:         https://github.com/shannpersand/comic-shanns/raw/master/v2/comic%20shanns%202.ttf#/comic_shanns.ttf
Source2:        https://github.com/shannpersand/comic-shanns/raw/master/LICENSE
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Comic Shanns is a sans-serif casual script typeface inspired by Comic
Sans (MS). Comic Shanns has slightly better weight management, and
the issue of letterfit is not as much a concern in a monospace
setting anyway.

%prep
%setup -Tcq
cp -av %_sourcedir/LICENSE .

%build

%install
mkdir -pv "%buildroot/%_ttfontsdir"
cp -av %_sourcedir/*.ttf "%buildroot/%_ttfontsdir/"

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%_ttfontsdir/

%changelog
