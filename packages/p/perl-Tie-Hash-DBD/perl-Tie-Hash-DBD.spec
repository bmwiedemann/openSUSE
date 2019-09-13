#
# spec file for package perl-Tie-Hash-DBD
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


Name:           perl-Tie-Hash-DBD
Version:        0.20
Release:        0
%define cpan_name Tie-Hash-DBD
Summary:        Tie a plain hash to a database table
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.613
BuildRequires:  perl(Test::More) >= 0.9
Requires:       perl(DBI) >= 1.613
Requires:       perl(Test::More) >= 0.9
Recommends:     perl(DBD::CSV) >= 0.54
Recommends:     perl(DBD::Pg) >= v3.9.1
Recommends:     perl(DBD::SQLite) >= 1.64
Recommends:     perl(DBI) >= 1.642
Recommends:     perl(Test::More) >= 1.302167
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.md examples README

%changelog
