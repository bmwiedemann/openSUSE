#
# spec file for package pagul-fonts
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

%define fontname Pagul

Name:           pagul-fonts
Version:        1.0
Release:        0
Summary:        Pagul Fonts
License:        SUSE-GPL-3.0-with-font-exception
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/pagul/
Source0:        http://downloads.sourceforge.net/project/pagul/%{fontname}_v%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Pagul is a Free Font for Sourashtra Language with Unicode glyphs.

%prep
%setup -q -c -T -a0

%build
dos2unix *.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.txt
%{_ttfontsdir}

%changelog

