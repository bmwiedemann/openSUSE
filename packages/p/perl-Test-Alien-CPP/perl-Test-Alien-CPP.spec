#
# spec file for package perl-Test-Alien-CPP
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


%define cpan_name Test-Alien-CPP
Name:           perl-Test-Alien-CPP
Version:        1.40.0
Release:        0
# 1.04 -> normalize -> 1.40.0
%define cpan_version 1.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Testing tools for Alien modules for projects that use C++
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(Test2::Require) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 1.88
BuildRequires:  perl(Test::Alien::Build) >= 1.21
Requires:       perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::CppGuess)
Requires:       perl(Test2::Require) >= 0.000121
Requires:       perl(Test::Alien) >= 1.88
Requires:       perl(Test::Alien::Build) >= 1.21
Provides:       perl(Test::Alien::CPP) = %{version}
Provides:       perl(Test::Alien::CanCompileCpp) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module works exactly like Test::Alien except that it supports C++. All
functions like 'alien_ok', etc that are exported by Test::Alien are
exported by this module. The only difference is that 'xs_ok' injects C++
support before delegating to Test::Alien.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
