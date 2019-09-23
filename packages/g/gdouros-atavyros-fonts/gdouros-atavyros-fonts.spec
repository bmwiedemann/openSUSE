#
# spec file for package gdouros-atavyros-fonts
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


%define fontname atavyros-fonts

Name:           gdouros-atavyros-fonts
Version:        1.01
Release:        0
Summary:        Parangonne Greque Typeface
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://users.teilar.gr/~g1951d/
Source:         %{fontname}-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Obsoletes:      %{fontname} < 1.01
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define _ttfontsdir     /usr/share/fonts/truetype

%description
Robert Granjon (1513 – 1589) produced his Parangonne Greque typeface (Garmond size) at the instigation of Plantin as a counterpart to Garamond’s Grec du roi, in Antwerp Holland, between 1560 - 1565. A version of the font was used (a century later!) for the 1692 edition of Diogenes Laertius by Aegidius Menagius (Gilles Ménage of Angers, 1613 – 92), published by Henric Wetstenium in Amsterdam. A second variant, at Kolonel size, was cut by Nikolaas Kis for the Greek-Dutch edition of the New Testament in 1698, again by Henric Wetstenium. A digital revival, was prepared by Ralph P. Hancock, in his Vusillus font. Latin and Cyrillic are based on a Goudy typeface. The font covers the Windows Glyph List, Greek Extended, various typographic extras and some Open Type features (Numerators, Denominators, Fractions, Old Style Figures, Historical Forms, Stylistic Alternates, Ligatures).

%prep
%setup -q -n %{fontname}-%{version}

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
