#
# spec file for package perl-MooseX-Types-Perl
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name MooseX-Types-Perl
Name:           perl-MooseX-Types-Perl
Version:        0.101344
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Moose types that check against Perl syntax
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(version) >= 0.82
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(Params::Util)
Requires:       perl(version) >= 0.82
%{perl_requires}

%description
This library provides Moose types for checking things (mostly strings)
against syntax that is, or is a reasonable subset of, Perl syntax.

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
