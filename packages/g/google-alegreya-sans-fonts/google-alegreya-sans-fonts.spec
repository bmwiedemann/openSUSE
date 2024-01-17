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

Name:           google-alegreya-sans-fonts
Version:        2.008
Release:        0
Summary:        Humanist sans serif family, part of Alegreya “super family”
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/huertatipografica/Alegreya-Sans
Source0:        https://github.com/huertatipografica/Alegreya-Sans/archive/refs/tags/v%{version}.tar.gz#/Alegreya-Sans-%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRequires:  dos2unix
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
Alegreya Sans is a humanist sans serif family with a calligraphic feeling that
conveys a dynamic and varied rhythm. This gives a pleasant feeling to readers
of long texts.

The family follows humanist proportions and principles, just like the serif
version of the family, Alegreya. It achieves a ludic and harmonious paragraph
through elements carefully designed in an atmosphere of diversity. The italics
bring a strong emphasis to the roman styles, and each have seven weights to
bring you a wide typographic palette.

Alegreya Sans supports expert latin, greek and cyrillic character sets and
provides advanced typography OpenType features such as small caps, dynamic
ligatures and fractions, four set of figures, super and subscript characters,
ordinals, localized accent forms for spanish, catalan, guaraní, dutch, turkish,
romanian, serbian among others.

The Alegreya type system is a “super family”, originally intended for
literature, and includes sans and serif sister families.

%prep
%setup -q -n Alegreya-Sans-%{version}
chmod -x OFL.txt
dos2unix OFL.txt

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m0644 fonts/otf/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*.otf
%doc README.md CONTRIBUTORS.txt
%license LICENSE.md OFL.txt

%changelog
