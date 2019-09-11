#
# spec file for package perl-Graphics-ColorUtils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Graphics-ColorUtils
Version:        0.17
Release:        0
%define cpan_name Graphics-ColorUtils
Summary:        Easy-to-use color space conversions and more
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Graphics-ColorUtils/
Source:         http://www.cpan.org/authors/id/J/JA/JANERT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Graphics::ColorUtils)
%{perl_requires}

%description
This modules provides some utility functions to handle colors and color
space conversions.

The interface has been kept simple, so that most functions can be called
"inline" when making calls to graphics libraries such as GD, Tk, or when
generating HTML/CSS. (E.g. for GD: '$c = $img->colorAllocate( hsv2rgb( 270,
0.5, 0.3 ) );'.)

Features:

* Color Space Conversions

  Color space conversions, in particular between the "intuitive" color
  spaces HSV (Hue/Saturation/Value) and HLS (Hue/Lightness/Saturation) to
  and from RGB (Red/Green/Blue).

* Color Lookup

  Color lookup by name for three standard sets of colors: WWW/CSS, SVG, and
  X11.

* Color Gradients

  Management of color gradients, which can be indexed by a floating point
  number in the range 0..1. (Mostly intended for false-color data
  visualization.)

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
