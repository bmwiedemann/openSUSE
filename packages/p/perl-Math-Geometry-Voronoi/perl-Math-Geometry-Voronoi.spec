#
# spec file for package perl-Math-Geometry-Voronoi
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Math-Geometry-Voronoi
Name:           perl-Math-Geometry-Voronoi
Version:        1.300.0
Release:        0
# 1.3 -> normalize -> 1.300.0
%define cpan_version 1.3
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Compute Voronoi diagrams from sets of points
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Params::Validate)
Requires:       perl(Class::Accessor)
Requires:       perl(Params::Validate)
Provides:       perl(Math::Geometry::Voronoi) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module computes Voronoi diagrams from a set of input points. Info on
Voronoi diagrams can be found here:

  http://en.wikipedia.org/wiki/Voronoi_diagram

This module is a wrapper around a C implementation found here:

  http://www.derekbradley.ca/voronoi.html

Which is itself a modification of code by Steve Fortune, the inventor of
the algorithm used (Fortune's algorithm):

  http://cm.bell-labs.com/who/sjf/

I made changes to the C code to allow reading input and writing output
to/from Perl data-structures. I also modified the memory allocation code to
use Perl's memory allocator. Finally, I changed all floats to doubles to
provide better precision and to match Perl's NVs.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README

%changelog
