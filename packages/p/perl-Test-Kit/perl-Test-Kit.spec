#
# spec file for package perl-Test-Kit
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


Name:           perl-Test-Kit
Version:        2.15
Release:        0
%define cpan_name Test-Kit
Summary:        Build custom test packages with only the features you want
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAORU/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Sub::Delete)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Warn)
Requires:       perl(Hook::LexWrap)
Requires:       perl(Import::Into)
Requires:       perl(Module::Runtime)
Requires:       perl(Sub::Delete)
%{perl_requires}

%description
Test::Kit allows you to create a single module in your project which gives
you access to all of the testing functions you want.

Its primary goal is to reduce boilerplate code that is currently littering
the top of all your test files.

It also allows your testing to be more consistent; for example it becomes a
trivial change to include Test::FailWarnings in all of your tests, and
there is no danger that you forget to include it in a new test.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
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
%license LICENSE

%changelog
