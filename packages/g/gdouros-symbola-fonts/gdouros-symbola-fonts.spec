#
# spec file for package gdouros-symbola-fonts
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


%define fontname  symbola-fonts

Name:           gdouros-symbola-fonts
Version:        10.23
Release:        0
Summary:        Font with Support for Symbol Blocks of the Unicode Standard
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://users.teilar.gr/~g1951d/
# Download URL
# http://users.teilar.gr/~g1951d/Symbola.zip
Source:         Symbola-%{version}.zip
# Download URL
# http://users.teilar.gr/~g1951d/Bibliography.pdf
Source1:        Bibliography-20170615.pdf
Source2:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      %{fontname} < 6.05
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Symbola covers the following scripts and symbols supported by Unicode: Basic Latin, IPA Extensions, Spacing Modifier Letters, Combining Diacritical Marks, Greek and Coptic, Cyrillic, Cyrillic Supplement, General Punctuation, Superscripts and Subscripts, Currency Symbols, Combining Diacritical Marks for Symbols, Letterlike Symbols, Number Forms, Arrows, Mathematical Operators, Miscellaneous Technical, Control Pictures, Optical Character Recognition, Box Drawing, Block Elements, Geometric Shapes, Miscellaneous Symbols, Dingbats, Miscellaneous Mathematical Symbols-A, Supplemental Arrows-A, Supplemental Arrows-B, Miscellaneous Mathematical Symbols-B, Supplemental Mathematical Operators, Miscellaneous Symbols and Arrows, Supplemental Punctuation, Yijing Hexagram Symbols, Combining Half Marks, Specials, Byzantine Musical Symbols, Musical Symbols, Ancient Greek Musical Notation, Tai Xuan Jing Symbols, Counting Rod Numerals, Mathematical Alphanumeric Symbols, Mahjong Tiles, Domino Tiles, Playing Cards, Miscellaneous Symbols And Pictographs, Emoticons, Transport And Map Symbols, Alchemical Symbols, et al.

%prep
%setup -q -cT -a0

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
# install docs
cp %{SOURCE1} %{SOURCE2} \
   -t .
for i in *-*.pdf; do
        IFS=-. read -r a b c <<< "$i"; mv "$i" "$a.$c"
done

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Bibliography.pdf Symbola.pdf
%{_ttfontsdir}

%changelog
