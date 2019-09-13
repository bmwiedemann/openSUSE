#
# spec file for package orkhon-fonts
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

Name:           orkhon-fonts
Version:        20100509
Release:        0
Summary:        Font for Old Turkic Script
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://m10lmac.blogspot.cz/2010/03/typing-orkhonold-turkic.html
Source0:        https://dl.dropbox.com/u/46870715/k/orkhon.zip
Source1:        OFL.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Emir Yasin Sari's unicode font for writing Old turkic script.

%prep
%setup -q -c -T -a0

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 orkunmac/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL.txt
%{_ttfontsdir}

%changelog

