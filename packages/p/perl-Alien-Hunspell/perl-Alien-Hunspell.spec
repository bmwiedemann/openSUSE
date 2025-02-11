#
# spec file for package perl-Alien-Hunspell
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


%define cpan_name Alien-Hunspell
Name:           perl-Alien-Hunspell
Version:        0.170.0
Release:        0
# 0.17 -> normalize -> 0.170.0
%define cpan_version 0.17
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Install hunspell
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Base) >= 0.38.0
BuildRequires:  perl(Alien::Build) >= 0.510
BuildRequires:  perl(Alien::Build::MM) >= 0.400
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf) >= 0.410
BuildRequires:  perl(Alien::Build::Plugin::Probe::Vcpkg) >= 2.160
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::Require) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien::CPP)
Requires:       perl(Alien::Base) >= 0.38.0
Provides:       perl(Alien::Hunspell) = %{version}
Provides:       perl(Test2::Require::Dev)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(PkgConfig)
BuildRequires:  pkgconfig(hunspell)
Requires:       pkgconfig(hunspell)
# MANUAL END

%description
This module provides the spelling library Hunspell. It will either detect
it as provided by the operating system, or download the source from the
Internet and install it for you. It uses Alien::Base.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc alienfile Changes README
%license LICENSE

%changelog
