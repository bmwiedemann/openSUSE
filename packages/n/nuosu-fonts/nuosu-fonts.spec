#
# spec file for package nuosu-fonts
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

%define src_name ttf-sil-nuosusil

Name:           nuosu-fonts
Version:        2.1.1
Release:        0
Summary:        SIL Yi Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.sil.org/resources/software_fonts/nuosu-sil
Source0:        %{src_name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Nuosu SIL Font is a single Unicode font for the standardized 
Yi script used by a large ethnic group in southwestern China.

%prep
%setup -q -c -T -a0

%build
dos2unix OFL.txt doc/FONTLOG.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL*.txt doc
%{_ttfontsdir}

%changelog
