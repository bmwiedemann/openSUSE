#
# spec file for package perl-Math-Geometry-Voronoi
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Math-Geometry-Voronoi
Version:        1.3
Release:        0
%define cpan_name Math-Geometry-Voronoi
Summary:        compute Voronoi diagrams from sets of points
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-Geometry-Voronoi/
Source:         http://www.cpan.org/authors/id/S/SA/SAMTREGAR/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Params::Validate)
Requires:       perl(Class::Accessor)
Requires:       perl(Params::Validate)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README

%changelog
