#
# spec file for package perl-Module-Install
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


%define cpan_name Module-Install
Name:           perl-Module-Install
Version:        1.21
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Standalone, extensible Perl module installer
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::PPPort) >= 3.16
BuildRequires:  perl(ExtUtils::Install) >= 1.52
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.19
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::Spec) >= 3.28
BuildRequires:  perl(Module::Build) >= 0.290000
BuildRequires:  perl(Module::CoreList) >= 2.17
BuildRequires:  perl(Module::ScanDeps) >= 1.09
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4413
BuildRequires:  perl(Test::Harness) >= 3.13
BuildRequires:  perl(Test::More) >= 0.86
BuildRequires:  perl(YAML::Tiny) >= 1.33
BuildRequires:  perl(autodie)
Requires:       perl(Devel::PPPort) >= 3.16
Requires:       perl(ExtUtils::Install) >= 1.52
Requires:       perl(ExtUtils::MakeMaker) >= 6.59
Requires:       perl(ExtUtils::ParseXS) >= 2.19
Requires:       perl(File::Remove) >= 1.42
Requires:       perl(File::Spec) >= 3.28
Requires:       perl(Module::Build) >= 0.290000
Requires:       perl(Module::CoreList) >= 2.17
Requires:       perl(Module::ScanDeps) >= 1.09
Requires:       perl(Parse::CPAN::Meta) >= 1.4413
Requires:       perl(YAML::Tiny) >= 1.38
Recommends:     perl(Archive::Zip) >= 1.37
Recommends:     perl(File::HomeDir) >= 1
Recommends:     perl(JSON) >= 2.9
Recommends:     perl(LWP::Simple) >= 6.00
Recommends:     perl(LWP::UserAgent) >= 6.05
Recommends:     perl(PAR::Dist) >= 0.29
%{perl_requires}

%description
*Module::Install* is a package for writing installers for CPAN (or
CPAN-like) distributions that are clean, simple, minimalist, act in a
strictly correct manner with ExtUtils::MakeMaker, and will run on any Perl
installation version 5.005 or newer.

The intent is to make it as easy as possible for CPAN authors (and
especially for first-time CPAN authors) to have installers that follow all
the best practices for distribution installation, but involve as much DWIM
(Do What I Mean) as possible when writing them.

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
%doc Changes README TODO

%changelog
