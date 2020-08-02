#
# spec file for package mplus-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mplus-fonts
Version:        1.0.63
Release:        0
%define mplusname mplus-TESTFLIGHT-063
Summary:        Font set incorporating all Kanji until level 2, and latin glyphs
License:        SUSE-mplus
Group:          System/X11/Fonts
Url:            https://mplus-fonts.osdn.jp/

Source0:        %{mplusname}.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The M+ outline fonts are distributed with proportional Latin (4 variations),
fixed-halfwidth Latin (3 variations) and fixed-fullwidth Japanese (2 Kana variations)
character sets. 7 weights from Thin to Black are included, but fixed-halfwidth
Latin with just 5 weights from Thin to Bold.

%prep
%setup -q -n %{mplusname}

%build

%install
mkdir -p  %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc LICENSE_?  README_?
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
