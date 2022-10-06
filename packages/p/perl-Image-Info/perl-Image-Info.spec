#
# spec file for package perl-Image-Info
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.43
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extract meta information from image files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Bundle::Image::Info::PNG)
Recommends:     perl(Bundle::Image::Info::SVG)
Recommends:     perl(Bundle::Image::Info::XBM)
Recommends:     perl(Bundle::Image::Info::XPM)
%{perl_requires}

%description
This module provides functions to extract various kinds of meta information
from image files.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
