#
# spec file for package perl-JSON-XS
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


%define cpan_name JSON-XS
Name:           perl-JSON-XS
Version:        4.40.0
Release:        0
# 4.04 -> normalize -> 4.40.0
%define cpan_version 4.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        JSON serialising/deserialising, done correctly and fast
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(common::sense)
Requires:       perl(Types::Serialiser)
Requires:       perl(common::sense)
Provides:       perl(JSON::XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be _correct_ and its secondary goal is to be _fast_. To
reach the latter goal it was written in C.

See MAPPING, below, on how JSON::XS maps perl values to JSON values and
vice versa.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%license COPYING

%changelog
