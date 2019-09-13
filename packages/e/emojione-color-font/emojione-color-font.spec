#
# spec file for package emojione-color-font
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           emojione-color-font
Version:        1.3
Release:        0
Summary:        Colored Emoji Font
License:        CC-BY-4.0
Group:          System/X11/Fonts
Url:            https://github.com/eosrei/emojione-color-font
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A color and B&W emoji SVGinOT font built from EmojiOne artwork with support
for ZWJ, skin tone diversity and country flags.

The font works in all operating systems, but will currently only show color
emoji in Firefox, Thunderbird and other Mozilla Gecko-based applications.
This is not a limitation of the font, but of the operating systems and
applications. Regular B&W outline emoji are included for backwards/fallback
compatibility.

%prep
%setup -q

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
