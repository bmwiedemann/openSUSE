#
# spec file for package adobe-sourcecodepro-fonts
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           adobe-sourcecodepro-fonts
Version:        2.038
Release:        0
%define         italic_version   1.058
%define         variable_version 1.018
Summary:        A set of OpenType fonts designed for coding environments
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://adobe-fonts.github.io/source-code-pro/
Source:         https://github.com/adobe-fonts/source-code-pro/archive/%{version}R-ro/%{italic_version}R-it/%{variable_version}R-VAR.tar.gz#/source-code-pro-%{version}R-ro-%{italic_version}R-it-%{variable_version}R-VAR.tar.gz
Source1:        adobe-sourcecodepro-fonts.metainfo.xml
Obsoletes:      SourceCodePro-fonts < %version-%release
Provides:       SourceCodePro-fonts = %version-%release
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Source Code is a set of monospaced OpenType fonts that have been designed to
work well with coding environments. This family of fonts is a complementary
design to the Source Sans family.

%prep
%setup -q -n source-code-pro-%{version}R-ro-%{italic_version}R-it-%{variable_version}R-VAR

%build
chmod -x+X -R *
dos2unix *

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 OTF/*.otf %{buildroot}%{_ttfontsdir}
install -d -m0755  %{buildroot}%{_datadir}/metainfo
install -D -m0644 %{S:1} %{buildroot}%{_datadir}/metainfo/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%license LICENSE.md
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/adobe-sourcecodepro-fonts.metainfo.xml
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
