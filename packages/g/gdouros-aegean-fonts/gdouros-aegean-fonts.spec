#
# spec file for package gdouros-aegean-fonts
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


Name:           gdouros-aegean-fonts
Version:        9.78
Release:        0
Summary:        Font with Support for Ancient Aegean and Eastern Mediterranean Scripts
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://users.teilar.gr/~g1951d
# download url:
# http://users.teilar.gr/~g1951d/Aegean.zip
# http://users.teilar.gr/~g1951d/Cretan%20Hieroglyphs.zip
# http://users.teilar.gr/~g1951d/Cypro-Minoan%20Inscriptions.zip
# http://users.teilar.gr/~g1951d/Alphabetics.pdf
# http://users.teilar.gr/~g1951d/Bibliography.pdf
# http://users.teilar.gr/~g1951d/Linear%20A%20and%20B%20Signs.pdf
# http://users.teilar.gr/~g1951d/Linear%20A%20Inscriptions.pdf
Source0:        Aegean-%{version}.zip
Source1:        Cretan_Hieroglyphs-9.17.zip
Source2:        Cypro-Minoan_Inscriptions-9.17.zip
Source3:        Alphabetics-20170213.pdf
Source4:        Bibliography-20170213.pdf
Source5:        Linear_A_and_B_Signs-20170220.pdf
Source6:        Linear_A_Inscriptions-20171217.pdf
Source7:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      aegean-fonts < 7.12
Provides:       aegean-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Aegean covers the following scripts and symbols supported by Unicode: Basic Latin, Greek and Coptic, Greek Extended, some Punctuation and other Symbols, Linear B Syllabary, Linear B Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols, Phaistos Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian, Cypriot Syllabary, Phoenician, Lydian, and Archaic Greek Musical Notation. Aegean allocates in Plane 15 of the UCS the following scripts and symbols, as yet unsupported by Unicode: Cretan Hieroglyphs, Cypro-Minoan, Linear A, the Arkalochori Axe, signs on Troy vessels and the Dispilio tablet. In this version Linear A and B have been expanded with variant glyphs. The Tsepis stele variant of the Cypriot Syllabary has been added as its Open Type Stylistic Set VI.

%prep
%setup -q -cT -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
# install docs
cp %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
   %{SOURCE7} \
   -t .
# we don't like spaces
for f in *\ *.pdf; do mv -- "$f" "${f// /_}"; done
# or dates
for f in *-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].pdf; do
    mv -- "$f" "${f//-*[0-9].pdf/.pdf}"
done

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE *.pdf
%{_ttfontsdir}

%changelog
