#
# spec file for package perl-SQL-ReservedWords
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


%define cpan_name SQL-ReservedWords
Name:           perl-SQL-ReservedWords
Version:        0.800.0
Release:        0
# 0.8 -> normalize -> 0.800.0
%define cpan_version 0.8
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Reserved SQL words by ANSI/ISO
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4
BuildRequires:  perl(Sub::Exporter)
Requires:       perl(Sub::Exporter)
Provides:       perl(SQL::ReservedWords) = %{version}
Provides:       perl(SQL::ReservedWords::DB2) = %{version}
Provides:       perl(SQL::ReservedWords::MySQL) = %{version}
Provides:       perl(SQL::ReservedWords::ODBC) = %{version}
Provides:       perl(SQL::ReservedWords::Oracle) = %{version}
Provides:       perl(SQL::ReservedWords::PostgreSQL) = %{version}
Provides:       perl(SQL::ReservedWords::SQLServer) = %{version}
Provides:       perl(SQL::ReservedWords::SQLite) = %{version}
Provides:       perl(SQL::ReservedWords::Sybase) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Determine if words are reserved by ANSI/ISO SQL standard.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
