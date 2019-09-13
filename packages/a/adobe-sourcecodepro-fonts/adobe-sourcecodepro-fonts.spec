#
# spec file for package adobe-sourcecodepro-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         roman_version 2.030
%define         italic_version  1.050

Name:           adobe-sourcecodepro-fonts
%define _name   SourceCodePro
Version:        %{roman_version}
Release:        0
Summary:        A set of OpenType fonts designed for coding environments
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/sourcecodepro.adobe
Source:         %{italic_version}R-it.tar.gz
Source1:        adobe-sourcecodepro-fonts.metainfo.xml
Obsoletes:      SourceCodePro-fonts < %version-%release
Provides:       SourceCodePro-fonts = %version-%release
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Source Code is a set of monospaced OpenType fonts that have been designed to
work well with coding environments. This family of fonts is a complementary
design to the Source Sans family.

%prep
%setup -q -n source-code-pro-%{roman_version}R-ro-%{italic_version}R-it
# Fix line endings
sed -i 's/\r$//g' LICENSE.txt
chmod a-x LICENSE.txt README.md

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 OTF/*.otf %{buildroot}%{_ttfontsdir}
install -d -m0755  %{buildroot}%{_datadir}/appdata
install -D -m0644 %{S:1} %{buildroot}%{_datadir}/appdata/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md
%dir %{_datadir}/appdata
%{_datadir}/appdata/adobe-sourcecodepro-fonts.metainfo.xml
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
