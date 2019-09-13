#
# spec file for package tai-heritage-pro-fonts
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

%define fontname TaiHeritagePro

Name:           tai-heritage-pro-fonts
Version:        2.500
Release:        0
Summary:        Tai Viet Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.sil.org/resources/software_fonts/tai-heritage-pro
Source0:        TaiHeritagePro2_500developer.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Tai Heritage Pro font is a Unicode-encoded font designed to reflect the 
traditional hand-written style of the Tai Viet script, which is used by the 
Tai Dam, Tai Daeng and Tai Don people who live in northwestern Vietnam and 
surrounding areas.

%prep
%setup -q -n %{fontname}-%{version}-developer

%build
dos2unix OFL*.txt FONTLOG.txt documentation/README.txt documentation/DOCUMENTATION.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL*.txt FONTLOG.txt documentation
%{_ttfontsdir}

%changelog
