#
# spec file for package perl-Image-Info
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Image-Info
Name:           perl-Image-Info
Version:        1.440.0
Release:        0
%define cpan_version 1.44
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extract meta information from image files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Bundle::Image::Info::Everything) = 0.02
Provides:       perl(Bundle::Image::Info::PNG) = 0.02
Provides:       perl(Bundle::Image::Info::SVG) = 0.02
Provides:       perl(Bundle::Image::Info::XBM) = 0.02
Provides:       perl(Bundle::Image::Info::XPM) = 0.02
Provides:       perl(Image::Info) = 1.440.0
Provides:       perl(Image::Info::AVIF) = 0.10.0
Provides:       perl(Image::Info::BMP) = 1.04
Provides:       perl(Image::Info::GIF) = 1.02
Provides:       perl(Image::Info::ICO) = 0.02
Provides:       perl(Image::Info::JPEG) = 0.06
Provides:       perl(Image::Info::PNG) = 1.03
Provides:       perl(Image::Info::PPM) = 0.04
Provides:       perl(Image::Info::Result)
Provides:       perl(Image::Info::SVG) = 2.04
Provides:       perl(Image::Info::SVG::XMLLibXMLReader) = 1.05
Provides:       perl(Image::Info::SVG::XMLSimple) = 1.05
Provides:       perl(Image::Info::TIFF) = 0.05
Provides:       perl(Image::Info::WBMP) = 0.01
Provides:       perl(Image::Info::WEBP) = 0.01
Provides:       perl(Image::Info::XBM) = 1.08
Provides:       perl(Image::Info::XPM) = 1.09
Provides:       perl(Image::TIFF) = 1.11
Provides:       perl(Image::TIFF::Rational)
%define         __perllib_provides /bin/true
Recommends:     perl(Bundle::Image::Info::PNG)
Recommends:     perl(Bundle::Image::Info::SVG)
Recommends:     perl(Bundle::Image::Info::XBM)
Recommends:     perl(Bundle::Image::Info::XPM)
%{perl_requires}

%description
This module provides functions to extract various kinds of meta information
from image files.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES CREDITS exifdump imgdump README TODO

%changelog
