#
# spec file for package perl-Parse-Distname
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Parse-Distname
Name:           perl-Parse-Distname
Version:        0.05
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse a distribution name
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.08
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::UseAllModules) >= 0.17
%{perl_requires}

%description
Parse::Distname is yet another distribution name parser. It works almost
the same as CPAN::DistnameInfo, but Parse::Distname takes a different
approach. It tries to extract a version part of a distribution and treat
the rest as a distribution name, contrary to CPAN::DistnameInfo which tries
to define a name part and treat the rest as a version.

Because of this difference, when Parse::Distname parses a weird
distribution name such as "AUTHOR/v1.0.tar.gz", it says the name is empty
and the version is "v1.0", while CPAN::DistnameInfo says the name is "v"
and the version is "1.0". See test files in this distribution if you need
more details. As of this writing, Parse::Distname returns a different
result for about 200+ distributions among about 320000 BackPan
distributions.

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
