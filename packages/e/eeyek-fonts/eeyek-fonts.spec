#
# spec file for package eeyek-fonts
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

Name:           eeyek-fonts
Version:        20091204
Release:        0
Summary:        Meetei Mayek Unicode Font
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://tabish.freeshell.org/eeyek/
Source0:        http://tabish.freeshell.org/eeyek/eeyek.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRequires:  dos2unix
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Eeyek Unicode TrueType Font allows you to read and write in Meetei Mayek script.

%prep
%setup -q -n Eeyek_Unicode

%build
dos2unix copying.txt 

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc copying.txt README.txt
%{_ttfontsdir}

%changelog
