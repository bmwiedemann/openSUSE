#
# spec file for package blockzone-fonts
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           blockzone-fonts
Version:        1.004
Release:        0
Summary:        A faithful recreation of the original DOS font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/ansilove/BlockZone
Source:         https://github.com/ansilove/BlockZone/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
BlockZone is a faithful, pixel-perfect recreation of the original IBM VGA font.
It contains each of the 256 characters, including those in the 128-255 range,
referred to as extended ASCII.
BlockZone is capabable of rendering ANSI and ASCII art, in fact that is the
purpose it was created for. It supports a wide range of codepages, the legendary
codepage 437 (MS-DOS Latin US) as well as Baltic, Cyrillic, French Canadian,
Greek, Hebrew, Icelandic, Latin-1, Latin-2, Nordic, Portuguese, Turkish charsets,
Windows codepage 1252 and even more.
All characters are mapped to their Unicode equivalents. You get the best results
when anti-aliasing (font smoothing) is disabled.

%prep
%setup -q -n BlockZone-%{version}

%build

%install
install -D -m0644 BlockZone.ttf %{buildroot}%{_ttfontsdir}/BlockZone.ttf
%reconfigure_fonts_scriptlets

%files
%license LICENSE
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/BlockZone.ttf

%changelog
