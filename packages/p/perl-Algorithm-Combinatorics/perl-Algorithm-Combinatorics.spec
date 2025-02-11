#
# spec file for package perl-Algorithm-Combinatorics
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


%define cpan_name Algorithm-Combinatorics
Name:           perl-Algorithm-Combinatorics
Version:        0.270.0
Release:        0
# 0.27 -> normalize -> 0.270.0
%define cpan_version 0.27
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Efficient generation of combinatorial sequences
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FX/FXN/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Algorithm::Combinatorics) = %{version}
Provides:       perl(Algorithm::Combinatorics::Iterator)
Provides:       perl(Algorithm::Combinatorics::JustCoderef)
%undefine       __perllib_provides
%{perl_requires}

%description
Algorithm::Combinatorics is an efficient generator of combinatorial
sequences. Algorithms are selected from the literature (work in progress,
see REFERENCES). Iterators do not use recursion, nor stacks, and are
written in C.

Tuples are generated in lexicographic order, except in 'subsets()'.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
