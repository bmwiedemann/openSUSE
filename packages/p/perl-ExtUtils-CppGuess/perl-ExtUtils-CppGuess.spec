#
# spec file for package perl-ExtUtils-CppGuess
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name ExtUtils-CppGuess
Name:           perl-ExtUtils-CppGuess
Version:        0.26
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Guess C++ compiler and flags
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280231
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.35
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Capture::Tiny)
Requires:       perl(ExtUtils::ParseXS) >= 3.35
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
# MANUAL END

%description
'ExtUtils::CppGuess' attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

It can generate the necessary options to the Module::Build constructor or
to ExtUtils::MakeMaker's 'WriteMakefile' function.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
