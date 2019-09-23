#
# spec file for package tibetan-machine-uni-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define fontname TibetanMachineUnicodeFont

Name:           tibetan-machine-uni-fonts
Version:        1.901
Release:        0
Summary:        Font for Tibetan Script
License:        GPL-3.0
Group:          System/X11/Fonts
Url:            http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%20machine%20uni.html
Source0:        https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/TibetanMachineUnicodeFont.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Tibetan & Himalayan Library is pleased to make available the alpha 
release of the Unicode character based Tibetan Machine Uni OpenType font 
for writing Tibetan, Dzongkha and Ladakhi in dbu can script with full 
support for the Sanskrit combinations found in chos skad texts.

%prep
%setup -q -n %{fontname}

%build
dos2unix ReadMe.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc gpl.txt ReadMe.txt
%{_ttfontsdir}

%changelog
