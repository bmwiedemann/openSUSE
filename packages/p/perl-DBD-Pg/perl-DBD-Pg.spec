#
# spec file for package perl-DBD-Pg
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


%define cpan_name DBD-Pg
Name:           perl-DBD-Pg
Version:        3.18.0
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        DBI PostgreSQL interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.614
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version)
Requires:       perl(DBI) >= 1.614
Requires:       perl(version)
Recommends:     perl(Module::Signature) >= 0.50
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel >= 8.1
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif
# For the Testsuite
BuildRequires:  postgresql-server
# MANUAL END

%description
DBD::Pg is a Perl module that works with the DBI module to provide access
to PostgreSQL databases.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
HARNESS_TIMER=1 HARNESS_VERBOSE=1 make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README README.dev README.win32 TODO win32.mak

%changelog
