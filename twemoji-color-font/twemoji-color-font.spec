#
# spec file for package twemoji-color-font
#
# Copyright © 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright © 2016 Yunhe Guo <guoyunhebrave@gmail.com>
# Copyright © 2018–2019 Markus S. <kamikazow@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           twemoji-color-font
Version:        12.0.1
Release:        0
Summary:        Font using Twitter’s color emoji
License:        CC-BY-4.0
Group:          System/X11/Fonts
Url:            https://github.com/eosrei/twemoji-color-font
Source:         TwitterColorEmoji-SVGinOT-Linux-%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -n TwitterColorEmoji-SVGinOT-Linux-%{version}

%build
# Nothing to do

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
install -m 0644 *.ttf %{buildroot}/%{_datadir}/fonts/truetype

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.txt *.md
%{_datadir}/fonts/truetype

%changelog
