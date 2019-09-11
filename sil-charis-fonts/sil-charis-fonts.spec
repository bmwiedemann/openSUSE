#
# spec file for package sil-charis-fonts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sil-charis-fonts
Version:        5.000
Release:        0
Summary:        Smart Unicode Font for Latin and Cyrillic Scripts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            c
Source0:        CharisSIL-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       locale(vi;ru;bg)
Obsoletes:      sil-charis < %{version}
Provides:       sil-charis = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Charis is similar to Bitstream Charter, one of the first fonts designed
specifically for laser printers. It is highly readable and holds up
well in less-than-ideal reproduction environments. It also has a full
set of styles - regular, italic, bold, bold italic - and so is more
useful in general publishing than Doulos SIL. Charis is a serif,
proportionally-spaced font optimized for readability in long printed
documents.

The goal for this product was to provide a single Unicode-based font
family that would contain a comprehensive inventory of glyphs needed
for almost any Roman- or Cyrillic-based writing system, whether used
for phonetic or orthographic needs. In addition, there is provision for
other characters and symbols useful to linguists. This font makes use
of state-of-the-art font technologies to support complex typographic
issues, such as the need to position arbitrary combinations of base
glyphs and diacritics optimally.

%prep
%setup -q -n CharisSIL-%{version}
rm -f documentation/DOCUMENTATION.txt
find . -name \*.txt -print0 | xargs chmod 644
# Fix rpmlint warnings:
find . -name \*.txt -print0 | xargs -0 dos2unix

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

#
# This is unfortunately necessary to support old
# filename naming
# The following expression removes any "-" characters
# in the filename:
cd %{buildroot}%{_ttfontsdir}
for font in *.ttf; do
  ln -s "$font" "${font/-}"
done
cd -

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.txt
%{_ttfontsdir}

%changelog
