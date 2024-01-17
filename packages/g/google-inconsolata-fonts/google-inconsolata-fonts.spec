#
# spec file for package google-inconsolata-fonts
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


%define  fontname   inconsolata

Name:           google-inconsolata-fonts
Version:        3.000
Release:        0
Summary:        Monospace Font Designed for Printed Code Listings
License:        OFL-1.1
URL:            https://www.levien.com/type/myfonts/inconsolata.html
Source0:        https://github.com/googlefonts/Inconsolata/archive/v%{version}.tar.gz
BuildRequires:  bzip2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
Inconsolata Bold is a Unicode typeface family that supports
languages that use the Latin script and its variants, and
could be expanded to support other scripts.

Designer: Raph Levien

%prep
%autosetup -n Inconsolata-%{version}
chmod -x README.md *.txt

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 fonts/ttf/*.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 fonts/variable/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc README.md AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt documentation/*pdf
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
