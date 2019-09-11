#
# spec file for package perl-Module-Build-Tiny
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Module-Build-Tiny
Version:        0.039
Release:        0
%define cpan_name Module-Build-Tiny
Summary:        A tiny replacement for Module::Build
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Build-Tiny/
Source:         http://www.cpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Config) >= 0.003
BuildRequires:  perl(ExtUtils::Helpers) >= 0.020
BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(CPAN::Meta)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::Config) >= 0.003
Requires:       perl(ExtUtils::Helpers) >= 0.020
Requires:       perl(ExtUtils::InstallPaths) >= 0.002
Requires:       perl(ExtUtils::ParseXS)
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(JSON::PP) >= 2
Requires:       perl(TAP::Harness::Env)
%{perl_requires}

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file
to drive distribution configuration, build, test and installation.
Traditionally, Build.PL uses Module::Build as the underlying build system.
This module provides a simple, lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has less
than 120, yet supports the features needed by most distributions.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README Todo

%changelog
