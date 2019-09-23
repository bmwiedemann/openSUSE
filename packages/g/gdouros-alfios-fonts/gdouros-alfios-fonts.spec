#
# spec file for package gdouros-alfios-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define fontname alfios-fonts

Name:           gdouros-alfios-fonts
Version:        1.01
Release:        0
Summary:        Fonts Based on the Work of Firmin Didot and Richard Porson
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://users.teilar.gr/~g1951d/
Source0:        Alfios_RBIJ.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      %{fontname} < 1.01
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Lowercase upright Greek were designed in 1805 by Firmin Didot (1764 – 1836) and cut by Walfard and Vibert. The typeface, together with a complete printing house, was donated in 1821 to the new Greek state by Didot’s son, Ambroise Firmin Didot (1790 – 1876). Lowercase italic Greek were designed in 1802 by Richard Porson (1757 – 1808) and cut by Richard Austin. They were first used by Cambridge University Press in 1810. Capitals, Latin and Cyrillic, as well as the complete bold weights, have been designed in an attempt to create a well-balanced font. The font covers the Windows Glyph List, Greek Extended, various typographic extras and some Open Type features (Numerators, Denominators, Fractions, Old Style Figures, Historical Forms, Stylistic Alternates, Ligatures); it is available in regular, italic, bold and bold italic.

%prep
%setup -q -cT -n %{fontname}-%{version} -a0
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE
%{_ttfontsdir}

%changelog
