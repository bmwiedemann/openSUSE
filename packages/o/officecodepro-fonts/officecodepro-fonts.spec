#
# spec file for package officecodepro-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           officecodepro-fonts
%define _name   Office-Code-Pro
Version:        1.004
Release:        0
Summary:        A set of OpenType fonts designed for coding environments
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/nathco/Office-Code-Pro
Source:         Office-Code-Pro-%{version}.tar.gz
Source2:        officecodepro-fonts.metainfo.xml
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Office Code Pro is a customized version of Source Code Pro, the monospaced sans serif 
originally created by Paul D. Hunt for Adobe Systems Incorporated. The customizations 
were made specifically for text editors and coding environments, but are still very 
usable in other applications.


%prep
%setup -q -n Office-Code-Pro-1.004
# Fix line endings
sed -i 's/\r$//g' LICENSE.txt
chmod a-x LICENSE.txt

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 Fonts/Office\ Code\ Pro/OTF/*.otf Fonts/Office\ Code\ Pro/TTF/*.ttf %{buildroot}%{_ttfontsdir}
install -m 644 Fonts/Office\ Code\ Pro\ D/OTF/*.otf Fonts/Office\ Code\ Pro\ D/TTF/*.ttf %{buildroot}%{_ttfontsdir}
install -d -m0755  %{buildroot}%{_datadir}/appdata
ls /home/abuild/rpmbuild/SOURCES/

install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md
%dir %{_datadir}/appdata
%{_datadir}/appdata/officecodepro-fonts.metainfo.xml
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
