#
# spec file for package twemoji-color-font
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


Name:           twemoji-color-font
Version:        14.0.2
Release:        0
Summary:        Font using Twitter’s color emoji
License:        CC-BY-4.0
Group:          System/X11/Fonts
URL:            https://github.com/13rac1/twemoji-color-font/
Source:         %{url}/releases/download/v%{version}/TwitterColorEmoji-SVGinOT-Linux-%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description
A color and monochrome emoji SVG-in-OpenType font built from the
Twitter Emoji for Everyone artwork with support for ZWJ,
skin tone diversity and country flags.

The font works in all operating systems, but will currently only
show color emoji in Firefox, Thunderbird and other Mozilla Gecko-based
applications. This is not a limitation of the font but of the
operating systems and applications. Regular monochrome outline
emoji are included for backwards/fallback compatibility.

%prep
%setup -q -n TwitterColorEmoji-SVGinOT-Linux-%{version}

%build
# Nothing to do

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
install -m 0644 *.ttf %{buildroot}/%{_datadir}/fonts/truetype

%reconfigure_fonts_scriptlets

%files
%doc *.txt *.md
%{_datadir}/fonts/truetype

%changelog
