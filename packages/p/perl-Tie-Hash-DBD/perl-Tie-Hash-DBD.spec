#
# spec file for package perl-Tie-Hash-DBD
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Tie-Hash-DBD
Name:           perl-Tie-Hash-DBD
Version:        0.260.0
Release:        0
# 0.26 -> normalize -> 0.260.0
%define cpan_version 0.26
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tie plain hashes to DBI interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{cpan_version}.tgz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.613
BuildRequires:  perl(Test::More) >= 0.90
Requires:       perl(DBI) >= 1.613
Requires:       perl(Test::More) >= 0.9
Provides:       perl(Tie::Array::DBD) = %{version}
Provides:       perl(Tie::Hash::DBD) = %{version}
%undefine       __perllib_provides
Recommends:     perl(DBD::CSV) >= 0.620
Recommends:     perl(DBD::Pg) >= 3.18
Recommends:     perl(DBD::SQLite) >= 1.780
Recommends:     perl(DBI) >= 1.647
Recommends:     perl(Sereal) >= 5.4
Recommends:     perl(Storable) >= 3.25
%{perl_requires}

%description
This module has been created to act as a drop-in replacement for modules
that tie straight perl hashes to disk, like 'DB_File'. When the running
system does not have enough memory to hold large hashes, and disk-tieing
won't work because there is not enough space, it works quite well to tie
the hash to a database, which preferable runs on a different server.

This module ties a hash to a database table using *only* a 'key' and a
'value' field. If no tables specification is passed, this will create a
temporary table with 'h_key' for the key field and a 'h_value' for the
value field.

I think it would make sense to merge the functionality that this module
provides into 'Tie::DBI'.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md examples README SECURITY.md

%changelog
