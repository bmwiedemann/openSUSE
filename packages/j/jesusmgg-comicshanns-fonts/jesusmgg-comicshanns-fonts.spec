#
# spec file for package jesusmgg-comicshanns-fonts
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


Name:           jesusmgg-comicshanns-fonts
Version:        1.3.0+git15
%define rev 5a13931471e3a5546adcf5dd772946aa34602e79
Release:        0
Summary:        Sans-serif casual script typeface
License:        MIT
Group:          System/X11/Fonts
URL:            https://github.com/jesusmgg/comic-shanns-mono/
Source:         https://github.com/jesusmgg/comic-shanns-mono/archive/%rev.tar.gz
Obsoletes:      shannpersand-comicshanns-fonts <= 2
Provides:       shannpersand-comicshanns-fonts
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Comic Shanns is a sans-serif casual script typeface inspired by Comic
Sans (MS). Comic Shanns has slightly better weight management, and
the issue of letterfit is not as much a concern in a monospace
setting anyway.

%prep
%autosetup -p1 -n comic-shanns-mono-%rev

%build

%install
b="%buildroot"
d="%_datadir/fonts-config/conf.avail"
e="%_sysconfdir/fonts/conf.d"
mkdir -p "$b/$d" "$b/$e" "$b/%_ttfontsdir"
cp -av fonts/*.otf "$b/%_ttfontsdir/"
cat >"$b/$d/31-comicshanns-alias.conf" <<-EOF
	<?xml version='1.0'?>
	<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
	<fontconfig>
	<alias><family>Comic Shanns</family><prefer><family>Comic Shanns Mono</family></prefer></alias>
	</fontconfig>
EOF
ln -s "$d/31-comicshanns-alias.conf" "$b/$e/"

%reconfigure_fonts_scriptlets

%files
%license LICENSE.md
%_ttfontsdir/
%_sysconfdir/fonts/
%_datadir/fonts-config/

%changelog
