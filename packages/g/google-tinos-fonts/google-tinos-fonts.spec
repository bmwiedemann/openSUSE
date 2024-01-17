#
# spec file for package google-tinos-fonts
#
# Copyright (c) 2024 SUSE LLC
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


Name:           google-tinos-fonts
Version:        20240101
Release:        0
Summary:        Times New Roman metric-compatible font
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            https://fonts.google.com/specimen/Tinos
Source0:        Tinos.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
Obsoletes:      noto-tinos < %{version}
Provides:       noto-tinos = %{version}
Obsoletes:      noto-tinos-fonts < %{version}
Provides:       noto-tinos-fonts = %{version}
%reconfigure_fonts_prereq

%description
Tinos is a serif design that is metrically compatible with Times New
Roman. Tinos offers improved on-screen readability characteristics
and the pan-European WGL character set and solves the needs of
developers looking for width-compatible fonts to address document
portability across platforms.

%prep
unzip %{SOURCE0}

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} *.ttf

%reconfigure_fonts_scriptlets

%files
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Tinos-*.ttf

%changelog
