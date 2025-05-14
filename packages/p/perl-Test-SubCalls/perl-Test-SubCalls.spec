#
# spec file for package perl-Test-SubCalls
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Test-SubCalls
Name:           perl-Test-SubCalls
Version:        1.100.0
Release:        0
# 1.10 -> normalize -> 1.100.0
%define cpan_version 1.10
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Track the number of times subs are called
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hook::LexWrap) >= 0.200
Requires:       perl(Hook::LexWrap) >= 0.200
Provides:       perl(Test::SubCalls) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that some
underlying subroutine deep within the code was called a specific number of
times.

This module provides a number of functions for doing testing in this way in
association with your normal Test::More (or similar) test scripts.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
