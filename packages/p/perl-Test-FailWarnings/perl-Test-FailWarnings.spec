#
# spec file for package perl-Test-FailWarnings
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-FailWarnings
Version:        0.008
Release:        0
%define cpan_name Test-FailWarnings
Summary:        Add test failures if warnings are caught
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-FailWarnings/
Source:         http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Test::More) >= 0.96
#BuildRequires: perl(Noisy)
#BuildRequires: perl(Pod::Wordlist)
#BuildRequires: perl(Test::FailWarnings)
#BuildRequires: perl(Test::Spelling) >= 0.12
Requires:       perl(Test::More) >= 0.86
%{perl_requires}

%description
This module hooks '$SIG{__WARN__}' and converts warnings to the Test::More
manpage 'fail()' calls. It is designed to be used with 'done_testing', when
you don't need to know the test count in advance.

Just as with the Test::NoWarnings manpage, this does not catch warnings if
other things localize '$SIG{__WARN__}', as this is designed to catch
_unhandled_ warnings.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING cpanfile LICENSE perlcritic.rc README tidyall.ini

%changelog
