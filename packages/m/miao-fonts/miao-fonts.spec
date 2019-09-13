#
# spec file for package miao-fonts
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

%define fontname MiaoUnicode

Name:           miao-fonts
Version:        20131031
Release:        0
Summary:        Miao Unicode Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://phjamr.github.io/miao.html
Source0:        %{fontname}-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Miao Unicode is an open-source, Graphite enabled font which 
supports the Miao, or ‘Pollard’, script.

%prep
%setup -q -n %{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 MiaoUnicode-Regular.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc LICENSE.md README.md
%{_ttfontsdir}

%changelog
