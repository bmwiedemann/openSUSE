#
# spec file for package google-cardo-fonts
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


%define fontname cardo

Name:           google-cardo-fonts
Version:        1.04
Release:        0
Summary:        Serif Font for Classicists, Biblical Scholars, Medievalists, and Linguists
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://code.google.com/webfonts/family?family=Cardo
Source0:        %{fontname}104.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Cardo is a large Unicode font specifically designed for the needs
of classicists, Biblical scholars, medievalists, and linguists. 
It also works well for general typesetting in situations where a
high-quality Old Style font is appropriate. Its large character
set supports many modern languages as well as those needed by
scholars. Cardo also contains features that are required for
high-quality typography such as ligatures, text figures (also
known as old style numerals), true small capitals and a variety
of punctuation and space characters.

Designer: David Perry

%prep
%setup -T -c %{name} -n %{name}
unzip %{SOURCE0}


%build
# -- nothing to do --

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp Cardoi*.ttf   %{buildroot}%{_ttfontsdir}/Cardo-Italic.ttf
cp Cardob*.ttf   %{buildroot}%{_ttfontsdir}/Cardo-Bold.ttf
cp Cardo[0-9]*.ttf %{buildroot}%{_ttfontsdir}/Cardo-Regular.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(0644,root,root,755)
%doc Manual*.pdf
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
