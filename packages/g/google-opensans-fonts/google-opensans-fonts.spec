#
# spec file for package google-opensans-fonts
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


%define  fontname   opensans
Name:           google-opensans-fonts
Version:        20210927
Release:        0
Summary:        Humanist Sans Serif Typeface
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/opensans
Source0:        https://github.com/googlefonts/opensans/archive/27d060e1aad6886daeda67629ee28189f795f534.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Obsoletes:      %{name} <= 1.0
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Open Sans is a humanist sans serif typeface designed by
Steve Matteson, Type Director of Ascender Corp.

This version contains the complete 897 character set, which
includes the standard ISO Latin 1, Latin CE, Greek and Cyrillic
character sets. Open Sans was designed with an upright stress,
open forms and a neutral, yet friendly appearance. It was
optimized for print, web, and mobile interfaces, and has
excellent legibility characteristics in its letterforms.

Designer: Steve Matteson

%prep
%setup -q -n %{fontname}-27d060e1aad6886daeda67629ee28189f795f534

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -p -m 0644 fonts/ttf/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%license OFL.txt

%changelog
