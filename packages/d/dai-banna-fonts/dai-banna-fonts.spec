#
# spec file for package dai-banna-fonts
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

%define fontname DaiBanna

Name:           dai-banna-fonts
Version:        2.200
Release:        0
Summary:        SIL New Tai Lue Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.sil.org/resources/software_fonts/dai-banna-sil
Source0:        %{fontname}-src-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Dai Banna SIL is a Unicode font package for rendering New Tai Lue 
(Xishuangbanna Dai) characters.

%prep
%setup -q -n ttf-sil-dai-banna-%{version}

%build
dos2unix OFL.txt README.txt FONTLOG.txt doc/OFL-FAQ.txt doc/sample.txt 
chmod 644  OFL.txt README.txt FONTLOG.txt doc/OFL-FAQ.txt doc/sample.txt doc/DaiBannaSIL.pdf

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 font-source/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL*.txt doc README.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
