#
# spec file for package google-poppins-fonts
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

Name:           google-poppins-fonts
License:        OFL-1.1
Group:          System/X11/Fonts
PreReq:         %suseconfig_fonts_prereq
Version:        4.003
Release:        1
URL:            https://fonts.google.com/specimen/Poppins
Source0:        https://github.com/itfoundry/Poppins/archive/v%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
Summary:        Geometric sans serif typefaces

%description
Geometric sans serif typefaces have been a popular design tool ever since these actors took to the world’s stage. Poppins is one of the new comers to this long tradition. With support for the Devanagari and Latin writing systems, it is an internationalist take on the genre.

Many of the Latin glyphs (such as the ampersand) are more constructed and rationalist than is typical. The Devanagari design is particularly new, and is the first ever Devanagari typeface with a range of weights in this genre. Just like the Latin, the Devanagari is based on pure geometry, particularly circles.

Each letterform is nearly monolinear, with optical corrections applied to stroke joints where necessary to maintain an even typographic color. The Devanagari base character height and the Latin ascender height are equal; Latin capital letters are shorter than the Devanagari characters, and the Latin x-height is set rather high.

The Devanagari is designed by Ninad Kale. The Latin is by Jonny Pinhorn.


%prep
%setup -q -n Poppins-%{version}

%build
# -- nothing to do --
ls -l

%install
install -d %{buildroot}%{_ttfontsdir}
unzip -d %{buildroot}%{_ttfontsdir} \
    products/Poppins-%{version}-GoogleFonts-TTF.zip

%reconfigure_fonts_scriptlets

%files
%doc README.md
%license OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog

