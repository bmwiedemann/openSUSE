#
# spec file for package perl-CPAN-Changes
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


%define cpan_name CPAN-Changes
Name:           perl-CPAN-Changes
Version:        0.500004
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parser for CPAN style change logs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006000
BuildRequires:  perl(Sub::Quote) >= 1.005000
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Types::Standard)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 1.006000
Requires:       perl(Sub::Quote) >= 1.005000
Requires:       perl(Types::Standard)
%{perl_requires}

%description
It is standard practice to include a Changes file in your distribution. The
purpose the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

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
%doc Changes README
%license LICENSE

%changelog
