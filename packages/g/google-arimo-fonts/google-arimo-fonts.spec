#
# spec file for package google-arimo-fonts
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


Name:           google-arimo-fonts
Version:        20240101
Release:        0
Summary:        Arial metric-compatible font
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            https://fonts.google.com/specimen/Arimo
Source0:        Arimo.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
Obsoletes:      noto-arimo < %{version}
Provides:       noto-arimo = %{version}
Obsoletes:      noto-arimo-fonts < %{version}
Provides:       noto-arimo-fonts = %{version}
%reconfigure_fonts_prereq

%description
Arimo is a sans serif design that is metrically compatible with
Arial. Arimo offers improved on-screen readability characteristics
and the pan-European WGL character set and solves the needs of
developers looking for width-compatible fonts to address document
portability across platforms.

%prep
unzip %{SOURCE0}

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} static/*

%reconfigure_fonts_scriptlets

%files
%license LICENSE.txt
%doc README.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Arimo-*.ttf

%changelog
