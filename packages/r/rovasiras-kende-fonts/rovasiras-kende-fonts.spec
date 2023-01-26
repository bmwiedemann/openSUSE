#
# spec file for package rovasiras-kende-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           rovasiras-kende-fonts
Version:        20221015
Release:        0
Summary:        A ligatured font for the Old Hungarian script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/rovasiras/kende-font
# https://github.com/rovasiras/kende-font/archive/refs/tags/Font.tar.gz
Source0:        kende-font-Font.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Kende is a ligatured font for the Old Hungarian script.

%prep
%autosetup -n kende-font-Font

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} Kende.ttf

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Kende.ttf

%changelog
