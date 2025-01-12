#
# spec file for package perl-Term-Table
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Term-Table
Name:           perl-Term-Table
Version:        0.024
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Format a header and rows into a table
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Term::Size::Any) >= 0.002
Recommends:     perl(Unicode::GCString) >= 2013.10
Recommends:     perl(Unicode::LineBreak) >= 2015.06
%{perl_requires}

%description
This is used by some failing tests to provide diagnostics about what has
gone wrong. This module is able to format rows of data into tables.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README README.md
%license LICENSE

%changelog
