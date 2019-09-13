#
# spec file for package gdouros-text-fonts
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


Name:           gdouros-text-fonts
Version:        8.01
Release:        0
Summary:        Text fonts from George Douros
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download URL
# http://users.teilar.gr/~g1951d/Textfonts.zip
Source0:        Textfonts-%{version}.zip
Source2:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      gdouros-aroania-fonts <= 6.31
Provides:       gdouros-aroania-fonts = %{version}
Obsoletes:      gdouros-anaktoria-fonts <= 6.31
Provides:       gdouros-anaktoria-fonts = %{version}
Obsoletes:      gdouros-alexander-fonts <= 6.31
Provides:       gdouros-alexander-fonts = %{version}
Obsoletes:      gdouros-avdira-fonts <= 6.31
Provides:       gdouros-avdira-fonts = %{version}
Obsoletes:      gdouros-asea-fonts <= 6.31
Provides:       gdouros-asea-fonts = %{version}
Obsoletes:      aroania-fonts <= 1.0
Provides:       aroania-fonts = %{version}
Obsoletes:      anaktoria-fonts <= 1.01
Provides:       anaktoria-fonts = %{version}
Obsoletes:      alexander-fonts < 3.01
Provides:       alexander-fonts = %{version}
Obsoletes:      avdira-fonts < 1.01
Provides:       avdira-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Greek typefaces:

- Aroania, based on the ‘New Hellenic’ font by Victor Julius Scholderer
  (1880-1971).
- Anaktoria, grecs du roi was designed by Claude Garamond (1480 – 1561)
  between 1541 and 1544, commissioned by king Francis I of France, for the
  exclusive use by the Imprimerie Nationale in Paris. Greek in Akaktoria is
  based on a modern version of Grecs du roi prepared by Mindaugas Strockis in
  2001. Lowercase Latin stems from the titles in the 1623 First Folio Edition
  of Shakespeare. Scott Mann & Peter Guither prepared a modern version for The
  Illinois Shakespeare Festival in 1995. Cyrillic has been designed to match
  the above Greek and Latin. The font covers the Windows Glyph List, Greek
  Extended, various typographic extras and some Open Type features
  (Numerators, Denominators, Fractions, Old Style Figures, Historical Forms,
  Stylistic Alternates, Ligatures, Swash Capitals).
- Alexander, a text typeface using the Greek letters designed by Alexander
  Wilson (1714-1786), a Scottish doctor, astronomer, and typefounder. The type
  was especially designed for an edition of Homer’s epics, published in 1756-8
  by Andrew and Robert Foulis, printers to the University of Glasgow. A modern
  revival, Wilson Greek, has been designed by Matthew Carter in 1995. Peter S.
  Baker is also using Wilson’s Greek type in his Junicode font for medieval
  scholars (2007). Latin and Cyrillic are based on a Garamond typeface. The
  font covers the Windows Glyph List, Greek Extended, IPA Extensions, Ancient
  Greek Numbers, Byzantine and Ancient Greek Musical Notation, various
  typographic extras and several Open Type features (Case-Sensitive Forms,
  Small Capitals, Subscript, Superscript, Numerators, Denominators, Fractions,
  Old Style Figures, Historical Forms, Stylistic Alternates, Ligatures).
- Avdira, based on the lowercase Greek letters in the typeface used
  by Demetrios Damilas for the edition of Isocrates, published in Milan in
  1493. A digital revival, was prepared by Ralph P. Hancock, in his Milan
  (Mediolanum) font. Italic Greek were designed in 1802 by Richard Porson
  (1757 – 1808) and cut by Richard Austin. They were first used by Cambridge
  University Press in 1810. Capitals, Latin and Cyrillic, as well as the
  complete bold weights, have been designed in an attempt to create a
  well-balanced font. The font covers the Windows Glyph List, Greek Extended,
  various typographic extras and is available in regular, italic, bold and
  bold italic. The regular style of the font also covers IPA Extensions,
  Ancient Greek Numbers, Byzantine and Ancient Greek Musical Notation and
  several Open Type features (Case-Sensitive Forms, Small Capitals, Subscript,
  Superscript, Numerators, Denominators, Fractions, Old Style Figures,
  Historical Forms, Stylistic Alternates, Ligatures).
- Asea, typeface with four styles covering almost the whole Greek script as
  defined by unicode, by Firmin Didot (1764-1836).

%prep
%setup -q -cT -a0

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 fonts/*.ttf fonts/hinted/*.ttf -t %{buildroot}%{_ttfontsdir}/
# install docs
cp %{SOURCE2} .

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Textfonts.pdf
%{_ttfontsdir}

%changelog
