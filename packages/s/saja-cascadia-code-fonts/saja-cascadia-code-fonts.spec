#
# spec file for package saja-cascadia-code-fonts
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Xu Zhao (i@xuzhao.net).
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


%define fontname cascadia-code

Name:           saja-cascadia-code-fonts
Version:        2009.14
Release:        0
Summary:        Monospace terminal fonts from Microsoft
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/microsoft/cascadia-code
Source0:        https://github.com/microsoft/cascadia-code/releases/download/v%{version}/CascadiaCode-%{version}.zip
Source1:        LICENSE.txt
Source2:        OFL-FAQ.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Cascadia Code is a monospaced font that was designed also with Visual Studio / Visual Studio Code in mind.

%prep
%setup -q -n ttf
cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%license OFL-FAQ.txt LICENSE.txt

%changelog
