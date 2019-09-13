#
# spec file for package perl-Devel-Declare
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-Declare
Version:        0.006019
Release:        0
%define cpan_name Devel-Declare
Summary:        Adding keywords to perl, in perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-Declare/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.05
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
Requires:       perl(B::Hooks::EndOfScope) >= 0.05
Requires:       perl(B::Hooks::OP::Check) >= 0.19
Requires:       perl(Sub::Name)
%{perl_requires}

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

This document describes how to create a simple declarator.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
