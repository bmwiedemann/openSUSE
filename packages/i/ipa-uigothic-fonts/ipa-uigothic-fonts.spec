#
# spec file for package ipa-uigothic-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ipa-uigothic-fonts
Version:        002.003
Release:        0
Summary:        "UI Gothic" Japanese TrueType Font Made by IPA
License:        IPA
Group:          System/X11/Fonts
Url:            http://ossipedia.ipa.go.jp/ipafont/
Source0:        IPAfont00203.tar.bz2
Source1:        enduser_license_english.txt
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       IPUIGothic = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      IPUIGothic <= 002.003
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
"UI Gothic" Japanese TrueType font made by IPA (Information-technology
Promotion Agency).

%prep
%setup -q -n IPAfont00203
cp $RPM_SOURCE_DIR/enduser_license_english.txt .

%build
for i in Readme00203.txt enduser_license.txt
do
    iconv -f SJIS -t UTF-8 < $i > $i.tmp
    mv $i.tmp $i
    dos2unix $i
done

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 644 ipagui.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipagui.ttf

%changelog
