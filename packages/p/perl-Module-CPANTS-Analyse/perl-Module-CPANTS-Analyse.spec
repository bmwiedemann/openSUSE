#
# spec file for package perl-Module-CPANTS-Analyse
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


%define cpan_name Module-CPANTS-Analyse
Name:           perl-Module-CPANTS-Analyse
Version:        1.20.0
Release:        0
%define cpan_version 1.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Generate Kwalitee ratings for a distribution
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Any::Lite) >= 0.06
BuildRequires:  perl(Archive::Tar) >= 1.76
BuildRequires:  perl(Array::Diff) >= 0.04
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.133380
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  perl(Class::Accessor) >= 0.19
BuildRequires:  perl(Data::Binary)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.09
BuildRequires:  perl(File::Find::Object) >= 0.2.1
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Parse::Distname)
BuildRequires:  perl(Perl::PrereqScanner::NotQuiteLite) >= 0.9901
BuildRequires:  perl(Software::License) >= 0.103012
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.73
Requires:       perl(Archive::Any::Lite) >= 0.06
Requires:       perl(Archive::Tar) >= 1.76
Requires:       perl(Array::Diff) >= 0.04
Requires:       perl(CPAN::Meta::Validator) >= 2.133380
Requires:       perl(CPAN::Meta::YAML) >= 0.008
Requires:       perl(Class::Accessor) >= 0.19
Requires:       perl(Data::Binary)
Requires:       perl(File::Find::Object) >= 0.2.1
Requires:       perl(JSON::PP)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Find)
Requires:       perl(Parse::Distname)
Requires:       perl(Perl::PrereqScanner::NotQuiteLite) >= 0.9901
Requires:       perl(Software::License) >= 0.103012
Requires:       perl(version) >= 0.73
Provides:       perl(Module::CPANTS::Analyse) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::BrokenInstaller) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::CpantsErrors) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Distname) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Distros) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Files) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::FindModules) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::License) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Manifest) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::MetaYML) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::NeedsCompiler) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Pod) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Prereq) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Repackageable) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Signature) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Uses) = 1.20.0
Provides:       perl(Module::CPANTS::Kwalitee::Version) = 1.20.0
%define         __perllib_provides /bin/true
%{perl_requires}
# MANUAL BEGIN
Source99:       rpmlintrc
# MANUAL END

%description
Generate Kwalitee ratings for a distribution

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
