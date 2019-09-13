#
# spec file for package google-opensans-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        20180610
Release:        0
Summary:        Humanist Sans Serif Typeface
License:        Apache-2.0
Group:          System/X11/Fonts
Url:            https://github.com/googlefonts/opensans
Source0:        %{fontname}-%{version}.tar.gz
Obsoletes:      %{name} <= 1.0
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

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
%setup -q -n %{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 hinted_ttfs/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%license LICENSE.txt

%changelog
