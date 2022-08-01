#
# spec file for package perl-Alien-Hunspell
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


%define cpan_name Alien-Hunspell
Name:           perl-Alien-Hunspell
Version:        0.17
Release:        0
Summary:        Install hunspell
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Base) >= 0.038
BuildRequires:  perl(Alien::Build) >= 0.51
BuildRequires:  perl(Alien::Build::MM) >= 0.40
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf) >= 0.41
BuildRequires:  perl(Alien::Build::Plugin::Probe::Vcpkg) >= 2.16
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::Require) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien::CPP)
Requires:       perl(Alien::Base) >= 0.038
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
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc alienfile author.yml Changes README
%license LICENSE

%changelog
