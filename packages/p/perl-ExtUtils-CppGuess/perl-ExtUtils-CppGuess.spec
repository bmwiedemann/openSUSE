#
# spec file for package perl-ExtUtils-CppGuess
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-ExtUtils-CppGuess
Version:        0.21
Release:        0
%define cpan_name ExtUtils-CppGuess
Summary:        Guess C++ compiler and flags
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%doc Changes README

%changelog
