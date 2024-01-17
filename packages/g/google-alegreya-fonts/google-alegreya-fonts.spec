#
# spec file for package google-alegreya-fonts
#
# Copyright (c) 2021 SUSE LLC
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


%define fontname alegreya

Name:           google-alegreya-fonts
Version:        2.008
Release:        0
Summary:        Serif family, part of the Alegreya “super family”
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/huertatipografica/Alegreya
Source0:        https://github.com/huertatipografica/Alegreya/archive/refs/tags/v%{version}.tar.gz#/Alegreya-%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Alegreya is a typeface originally intended for literature. Among its crowning
characteristics, it conveys a dynamic and varied rhythm which facilitates the
reading of long texts. Also, it provides freshness to the page while referring
to the calligraphic letter, not as a literal interpretation, but rather in a
contemporary typographic language.

The italic has just as much care and attention to detail in the design as the
roman. The bold weights are strong, and the Black weights are really
experimental for the genre. There is also a Small Caps sister family.

Not only does Alegreya provide great performance, but also achieves a strong
and harmonious text by means of elements designed in an atmosphere of
diversity.

The Alegreya type system is a “super family”, originally intended for
literature, and includes serif and sans serif sister families.

It supports expert latin, greek and cyrillic character sets and provides
advanced typography OpenType features such as small caps, dynamic ligatures and
fractions, four set of figures, super and subscript characters, ordinals,
localized accent forms for spanish, catalan, guaraní, dutch, turkish, romanian,
serbian among others.

Alegreya was chosen at the ATypI Letter2 competition in September 2011, and one
of the top 14 text type systems. It was also selected in the 2nd Bienal
Iberoamericana de Diseño, competition held in Madrid in 2010 and Tipos Latinos.

Designed by Juan Pablo del Peral for Huerta Tipográfica.

%prep
%setup -q -n Alegreya-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m0644 fonts/otf/*.otf %{buildroot}%{_ttfontsdir}
%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*.otf
%doc README.md AUTHORS.txt CONTRIBUTORS.txt
%license LICENSE.md OFL.txt

%changelog
