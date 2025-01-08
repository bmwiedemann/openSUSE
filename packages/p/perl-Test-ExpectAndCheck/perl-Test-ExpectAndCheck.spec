#
# spec file for package perl-Test-ExpectAndCheck
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


%define cpan_name Test-ExpectAndCheck
Name:           perl-Test-ExpectAndCheck
Version:        0.70.0
Release:        0
# 0.07 -> normalize -> 0.70.0
%define cpan_version 0.07
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Expect/check-style unit testing with object methods
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Builder) >= 1.302
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Future::Deferred)
Requires:       perl(Test::Builder) >= 1.302
Requires:       perl(Test::Deep)
Requires:       perl(Test::Future::Deferred)
Provides:       perl(Test::ExpectAndCheck) = %{version}
Provides:       perl(Test::ExpectAndCheck::Future) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This package creates objects that assist in writing unit tests with mocked
object instances. Each mock instance will expect to receive a given list of
method calls. Each method call is checked that it received the right
arguments, and will return a prescribed result. At the end of each test,
each object is checked to ensure all the expected methods were called.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
