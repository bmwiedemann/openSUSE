#
# spec file for package perl-Module-Build-Tiny
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


%define cpan_name Module-Build-Tiny
Name:           perl-Module-Build-Tiny
Version:        0.52.0
Release:        0
# 0.052 -> normalize -> 0.52.0
%define cpan_version 0.052
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tiny replacement for Module::Build
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Config) >= 0.3
BuildRequires:  perl(ExtUtils::Helpers) >= 0.20
BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.2
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(CPAN::Meta)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::Config) >= 0.3
Requires:       perl(ExtUtils::Helpers) >= 0.20
Requires:       perl(ExtUtils::InstallPaths) >= 0.2
Requires:       perl(ExtUtils::ParseXS)
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(JSON::PP) >= 2
Requires:       perl(TAP::Harness::Env)
Provides:       perl(Module::Build::Tiny) = %{version}
%undefine       __perllib_provides
Recommends:     perl(CPAN::Requirements::Dynamic)
%{perl_requires}

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file
to drive distribution configuration, build, test and installation.
Traditionally, Build.PL uses Module::Build as the underlying build system.
This module provides a simple, lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has less
than 200, yet supports the features needed by most distributions.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README Todo
%license LICENSE

%changelog
