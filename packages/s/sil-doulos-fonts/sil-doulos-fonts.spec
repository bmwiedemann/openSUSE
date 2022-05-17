#
# spec file for package sil-doulos-fonts
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


%define fontname Doulos

Name:           sil-doulos-fonts
# Provides:       locale(vi)
Version:        6.101
Release:        0
Summary:        Doulos SIL Fonts Similar to Times
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/doulos
Source0:        https://software.sil.org/downloads/r/doulos/DoulosSIL-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      sil-doulos < %{version}
Provides:       sil-doulos = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Doulos SIL provides glyphs for a wide range of Latin and Cyrillic
characters. Doulos's design is similar to the design of the Times-like
fonts, but only has a single regular face. It is intended for use alongside
other Times-like fonts where a range of styles (italic, bold) are not
needed.

%prep
%setup -q -n %{fontname}SIL-%{version}
chmod 644 *.txt *.ttf
# Remove DOS line endings:
for i in *.txt; do
 sed -i 's/.$//' $i
done

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license OFL*.txt
%doc README.txt documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
