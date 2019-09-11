#
# spec file for package perl-Module-Install
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Module-Install
Version:        1.19
Release:        0
%define cpan_name Module-Install
Summary:        Standalone, extensible Perl module installer
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Install/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README TODO

%changelog
