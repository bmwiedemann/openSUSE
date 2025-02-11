#
# spec file for package perl-Algorithm-Annotate
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


%define cpan_name Algorithm-Annotate
Name:           perl-Algorithm-Annotate
Version:        0.100.0
Release:        0
# 0.10 -> normalize -> 0.100.0
%define cpan_version 0.10
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Represent a series of changes in annotation list
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLKAO/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff) >= 1.150
Requires:       perl(Algorithm::Diff) >= 1.150
Provides:       perl(Algorithm::Annotate) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Algorithm::Annotate generates a list that is useful for generating output
simliar to 'cvs annotate'.

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

%changelog
