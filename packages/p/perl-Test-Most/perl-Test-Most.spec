#
# spec file for package perl-Test-Most
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


%define cpan_name Test-Most
Name:           perl-Test-Most
Version:        0.38
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Most commonly needed test functions and features
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exception::Class) >= 1.14
BuildRequires:  perl(Test::Deep) >= 0.119
BuildRequires:  perl(Test::Differences) >= 0.64
BuildRequires:  perl(Test::Exception) >= 0.430000
BuildRequires:  perl(Test::Harness) >= 3.35
BuildRequires:  perl(Test::More) >= 1.302047
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Exception::Class) >= 1.14
Requires:       perl(Test::Deep) >= 0.119
Requires:       perl(Test::Differences) >= 0.64
Requires:       perl(Test::Exception) >= 0.430000
Requires:       perl(Test::Harness) >= 3.35
Requires:       perl(Test::More) >= 1.302047
Requires:       perl(Test::Warn) >= 0.30
%{perl_requires}

%description
Test::Most exists to reduce boilerplate and to make your testing life
easier. We provide "one stop shopping" for most commonly used testing
modules. In fact, we often require the latest versions so that you get bug
fixes through Test::Most and don't have to keep upgrading these modules
separately.

This module provides you with the most commonly used testing functions,
along with automatically turning on strict and warning and gives you a bit
more fine-grained control over your test suite.

    use Test::Most tests => 4, 'die';

    ok 1, 'Normal calls to ok() should succeed';
    is 2, 2, '... as should all passing tests';
    eq_or_diff [3], [4], '... but failing tests should die';
    ok 4, '... will never get to here';

As you can see, the 'eq_or_diff' test will fail. Because 'die' is in the
import list, the test program will halt at that point.

If you do not want strict and warnings enabled, you must explicitly disable
them. Thus, you must be explicit about what you want and no longer need to
worry about accidentally forgetting them.

    use Test::Most tests => 4;
    no strict;
    no warnings;

%prep
%autosetup  -n %{cpan_name}-%{version}

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

%changelog
