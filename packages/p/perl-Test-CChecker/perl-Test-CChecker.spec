#
# spec file for package perl-Test-CChecker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-CChecker
Version:        0.10
Release:        0
%define cpan_name Test-CChecker
Summary:        Test-time utilities for checking C headers, libraries, or OS features (D[cut]
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::CChecker) >= 0.09
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Capture::Tiny)
Requires:       perl(ExtUtils::CChecker) >= 0.09
%{perl_requires}

%description
*DEPRECATED*: The intention of this module was always to test Alien modules
(both Alien::Base based and non-Alien::Base based modules). It has a number
of shortcomings that I believe to be better addressed by Test::Alien, so
please consider using that for new projects, or even migrating existing
code.

This module is a very thin convenience wrapper around ExtUtils::CChecker to
make it useful for use in a test context. It is intended for use with Alien
modules which need to verify that libraries work as intended with the
Compiler and flags used by Perl to build XS modules.

By default this module is very quiet, hiding all output using Capture::Tiny
unless there is a failure, in which case you will see the commands, flags
and output used.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc author.yml Changes README
%license LICENSE

%changelog
