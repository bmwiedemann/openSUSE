#
# spec file for package perl-Test-MockObject
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-MockObject
Version:        1.20180705
Release:        0
%define cpan_name Test-MockObject
Summary:        Perl extension for emulating troublesome interfaces
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-MockObject/
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI) >= 4.15
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(UNIVERSAL::can) >= 1.20110617
BuildRequires:  perl(UNIVERSAL::isa) >= 1.20110614
Requires:       perl(UNIVERSAL::can) >= 1.20110617
Requires:       perl(UNIVERSAL::isa) >= 1.20110614
%{perl_requires}

%description
It's a simple program that doesn't use any other modules, and those are
easy to test. More often, testing a program completely means faking up
input to another module, trying to coax the right output from something
you're not supposed to be testing anyway.

Testing is a lot easier when you can control the entire environment. With
Test::MockObject, you can get a lot closer.

Test::MockObject allows you to create objects that conform to particular
interfaces with very little code. You don't have to reimplement the
behavior, just the input and the output.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes README
%license LICENSE

%changelog
