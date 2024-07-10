#
# spec file for package perl-Test-Kit
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Test-Kit
Name:           perl-Test-Kit
Version:        2.160.0
Release:        0
%define cpan_version 2.16
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Build custom test packages with only the features you want
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAORU/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
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
Provides:       perl(Test::Kit) = 2.160.0
%undefine       __perllib_provides
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
%autosetup  -n %{cpan_name}-%{cpan_version}

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
