#
# spec file for package adobe-sourcecodepro-fonts
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         italic_version   1.062
%define         variable_version 1.026
Name:           adobe-sourcecodepro-fonts
Version:        2.042
Release:        0
Summary:        A set of OpenType fonts designed for coding environments
License:        OFL-1.1
URL:            https://adobe-fonts.github.io/source-code-pro/
Source:         https://github.com/adobe-fonts/source-code-pro/archive/%{version}R-u/%{italic_version}R-i/%{variable_version}R-vf.tar.gz#/source-code-pro-%{version}R-u-%{italic_version}R-i-%{variable_version}R-vf.tar.gz
Source1:        adobe-sourcecodepro-fonts.metainfo.xml
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
Obsoletes:      SourceCodePro-fonts < %{version}-%{release}
Provides:       SourceCodePro-fonts = %{version}-%{release}
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Source Code is a set of monospaced OpenType fonts that have been designed to
work well with coding environments. This family of fonts is a complementary
design to the Source Sans family.

%prep
%setup -q -n source-code-pro-%{version}R-u-%{italic_version}R-i-%{variable_version}R-vf

%build
chmod -x+X -R *
dos2unix *

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 OTF/*.otf %{buildroot}%{_ttfontsdir}
install -d -m0755  %{buildroot}%{_datadir}/metainfo
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/

%reconfigure_fonts_scriptlets

%files
%license LICENSE.md
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/adobe-sourcecodepro-fonts.metainfo.xml
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
