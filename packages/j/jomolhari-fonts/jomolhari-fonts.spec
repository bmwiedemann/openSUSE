#
# spec file for package jomolhari-fonts
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

Name:           jomolhari-fonts
Version:        alpha003
Release:        0
Summary:        Tibetan Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/jomolhari.html
Source0:        https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/Jomolhari-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Created in 2006 by Chris Fynn, Jomolhari is an OpenType Tibetan/Bhutanese font that supports 
both the Unicode encoding for Tibetan and part A of the Chinese encoding for pre-composed 
Tibetan characters. Based on Bhutanese manuscript examples, it is in its preliminary stage 
or alpha version. This version was made for trial purposes, and its author, Chris Fynn, 
welcomes feedback. 

%prep
%setup -q -c -T -a0

%build
dos2unix OFL*.txt FONTLOG.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL*.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
