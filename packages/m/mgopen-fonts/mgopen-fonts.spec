#
# spec file for package mgopen-fonts
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           mgopen-fonts
Version:        0.20050518
Release:        0
Summary:        Greek serif/sans-serif fonts
License:        SUSE-MgOpen
Group:          System/X11/Fonts
URL:            https://ellak-gr.translate.goog/2005/05/mgopen-fonts-are-available/
Source:         MgOpen.tar.bz2
# The file README contains the license and was created with
# w3m -dump http://www.ellak.gr/fonts/mgopen/index.en > README
Source1:        README
Source2:        LICENSE
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-el
BuildArch:      noarch

%description
The MgOpen typefaces contain glyphs for viewing texts in Greek
(written in the monotoniko system).

The package contains a serif typeface and two sans-serif ones, based
on the designs of Times Roman, Optima and Helvetica, respectively.

%prep
%setup -c %{name} -n %{name}
cp %{SOURCE1} %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%doc README
%license LICENSE
%{_ttfontsdir}

%changelog
