#
# spec file for package perl-DateTime-Format-Pg
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name DateTime-Format-Pg
Name:           perl-DateTime-Format-Pg
Version:        0.16014
Release:        0
Summary:        Parse and format PostgreSQL dates and times
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 0.10
BuildRequires:  perl(DateTime::Format::Builder) >= 0.72
BuildRequires:  perl(DateTime::TimeZone) >= 0.05
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
Requires:       perl(DateTime) >= 0.10
Requires:       perl(DateTime::Format::Builder) >= 0.72
Requires:       perl(DateTime::TimeZone) >= 0.05
%{perl_requires}

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create 'DateTime' or 'DateTime::Duration' objects, and it can
take a 'DateTime' or 'DateTime::Duration' object and produce a string
representing it in a format accepted by PostgreSQL.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Makefile minil.toml README.md
%license LICENSE

%changelog
