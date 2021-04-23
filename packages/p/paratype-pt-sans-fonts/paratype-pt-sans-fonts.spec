#
# spec file for package paratype-pt-sans-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           paratype-pt-sans-fonts
Version:        2.005OFL
Release:        0
Summary:        Sans Fonts for Minority Languages of Russia
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTSansOFL.zip
Source1:        http://www.paratype.ru/public/Info_PT_SS.pdf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       PTSans-fonts = %{version}
Provides:       locale(be;ru;uk)
Obsoletes:      PTSans-fonts < 2.005OFL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
PT Sans is based on Russian sans serif types of the second part of
the XX century, but at the same time has a very distinctive features of
modern humanistic design. The family consists of 8 styles: 4 basic
styles; 2 captions styles for small sizes and 2 narrows styles for
economic setting.

The fonts beside standard Western, Central European and Cyrillic code
pages contain characters of all title languages of Russian Federation
that make them unique and very important tool of the modern digital
communications.

%prep
%setup -cqn %{name}-%{version}
cp %{SOURCE1} .
sed -i 's/\r$//' PTSSM_OFL.txt

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc Info_PT_SS.pdf PTSSM_OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
