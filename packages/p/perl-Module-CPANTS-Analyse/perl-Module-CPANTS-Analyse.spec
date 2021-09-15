#
# spec file for package perl-Module-CPANTS-Analyse
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


%define cpan_name Module-CPANTS-Analyse
Name:           perl-Module-CPANTS-Analyse
Version:        1.01
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Generate Kwalitee ratings for a distribution
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Any::Lite) >= 0.06
BuildRequires:  perl(Archive::Tar) >= 1.76
BuildRequires:  perl(Array::Diff) >= 0.04
BuildRequires:  perl(CPAN::DistnameInfo) >= 0.06
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.133380
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  perl(Class::Accessor) >= 0.19
BuildRequires:  perl(Data::Binary)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.08
BuildRequires:  perl(File::Find::Object) >= v0.2.1
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Perl::PrereqScanner::NotQuiteLite) >= 0.9901
BuildRequires:  perl(Software::License) >= 0.103012
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.73
Requires:       perl(Archive::Any::Lite) >= 0.06
Requires:       perl(Archive::Tar) >= 1.76
Requires:       perl(Array::Diff) >= 0.04
Requires:       perl(CPAN::DistnameInfo) >= 0.06
Requires:       perl(CPAN::Meta::Validator) >= 2.133380
Requires:       perl(CPAN::Meta::YAML) >= 0.008
Requires:       perl(Class::Accessor) >= 0.19
Requires:       perl(Data::Binary)
Requires:       perl(File::Find::Object) >= v0.2.1
Requires:       perl(JSON::PP)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Find)
Requires:       perl(Perl::PrereqScanner::NotQuiteLite) >= 0.9901
Requires:       perl(Software::License) >= 0.103012
Requires:       perl(version) >= 0.73
%{perl_requires}
# MANUAL BEGIN
Source99:       rpmlintrc
# MANUAL END

%description
Generate Kwalitee ratings for a distribution

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
%doc AUTHORS Changes README.md TODO

%changelog
