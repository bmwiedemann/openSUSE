#
# spec file for package sil-gentium-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           sil-gentium-fonts
Version:        6.200
Release:        0
Summary:        A International Typeface for Languages Using the Latin Script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://software.sil.org/gentium/
Source0:        https://software.sil.org/downloads/r/gentium/GentiumPlus-%{version}.zip
Source1:        31-sil-gentium.conf
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       locale(vi)
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Gentium is a typeface family designed to enable the diverse ethnic
groups around the world who use the Latin script to produce readable,
high-quality publications. It supports a wide range of Latin-based
alphabets and includes glyphs that correspond to all the Latin ranges
of Unicode.

%prep
%setup -q -n GentiumPlus-%{version}
chmod 644 *.txt *.ttf
# Remove DOS line endings:
for i in *.txt; do
 sed -i 's/.$//' $i
done

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}
%install_fontsconf %{SOURCE1}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%license OFL.txt
%doc FONTLOG.txt OFL-FAQ.txt README.txt
%{_ttfontsdir}
%files_fontsconf_availdir
%files_fontsconf_file -l 31-sil-gentium.conf

%changelog
