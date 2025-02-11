#
# spec file for package perl-Algorithm-C3
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


%define cpan_name Algorithm-C3
Name:           perl-Algorithm-C3
Version:        0.110.0
Release:        0
# 0.11 -> normalize -> 0.110.0
%define cpan_version 0.11
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module for merging hierarchies using the C3 algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Algorithm::C3) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements the C3 algorithm. I have broken this out into it's
own module because I found myself copying and pasting it way too often for
various needs. Most of the uses I have for C3 revolve around class building
and metamodels, but it could also be used for things like dependency
resolution as well since it tends to do such a nice job of preserving local
precedence orderings.

Below is a brief explanation of C3 taken from the Class::C3 module. For
more detailed information, see the SEE ALSO section and the links there.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
