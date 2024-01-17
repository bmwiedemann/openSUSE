#
# spec file for package perl-Menlo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Menlo
Version:        1.9019
Release:        0
%define cpan_name Menlo
Summary:        CPAN client
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         dropwindows.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Common::Index) >= 0.006
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(ExtUtils::Config) >= 0.003
BuildRequires:  perl(ExtUtils::Helpers) >= 0.020
BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(HTTP::Tiny) >= 0.054
BuildRequires:  perl(HTTP::Tinyish) >= 0.04
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Parse::PMFile) >= 0.26
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(version)
#BuildRequires:  perl(Win32::ShellQuote)
Requires:       perl(CPAN::Common::Index) >= 0.006
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta) >= 2.132830
Requires:       perl(CPAN::Meta::Check)
Requires:       perl(CPAN::Meta::Requirements)
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Capture::Tiny)
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(ExtUtils::Config) >= 0.003
Requires:       perl(ExtUtils::Helpers) >= 0.020
Requires:       perl(ExtUtils::InstallPaths) >= 0.002
Requires:       perl(File::Which)
Requires:       perl(File::pushd)
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(HTTP::Tiny) >= 0.054
Requires:       perl(HTTP::Tinyish) >= 0.04
Requires:       perl(JSON::PP) >= 2
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::CoreList)
Requires:       perl(Module::Metadata)
Requires:       perl(Parse::CPAN::Meta)
Requires:       perl(Parse::PMFile) >= 0.26
Requires:       perl(String::ShellQuote)
Requires:       perl(URI)
Requires:       perl(local::lib)
Requires:       perl(parent)
Requires:       perl(version)
#Requires:       perl(Win32::ShellQuote)
%{perl_requires}

%description
Menlo is a backend for _cpanm 2.0_, developed with the goal to replace
cpanm internals with a set of modules that are more flexible, extensible
and easier to use.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
