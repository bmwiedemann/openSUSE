#
# spec file for package perl-SQL-Abstract-Pg
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


%define cpan_name SQL-Abstract-Pg
Name:           perl-SQL-Abstract-Pg
Version:        1.0.0
Release:        0
# 1.0 -> normalize -> 1.0.0
%define cpan_version 1.0
License:        Artistic-2.0
Summary:        PostgreSQL features for SQL::Abstract
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(SQL::Abstract) >= 2.0
Requires:       perl(SQL::Abstract) >= 2.0
Provides:       perl(SQL::Abstract::Pg) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
SQL::Abstract::Pg extends SQL::Abstract with a few PostgreSQL features used
by Mojo::Pg.

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
%doc Changes README.md
%license LICENSE

%changelog
