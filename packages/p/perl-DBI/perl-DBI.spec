#
# spec file for package perl-DBI
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name DBI
Name:           perl-DBI
Version:        1.653.0
Release:        0
# 1.653 -> normalize -> 1.653.0
%define cpan_version 1.653
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Database independent interface for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{cpan_version}.tgz
Source1:        perl-DBI.rpmlintrc
Source2:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(Module::Load) >= 0.22
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Simple) >= 0.96
Requires:       perl(Module::Load) >= 0.22
Provides:       perl(DBI) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Encode) >= 3.24
%{perl_requires}

%description
The DBI is a database access module for the Perl programming language. It
defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database being
used.

It is important to remember that the DBI is just an interface. The DBI is a
layer of "glue" between an application and one or more database _driver_
modules. It is the driver modules which do most of the real work. The DBI
provides a standard interface and framework for the drivers to operate
within.

This document often uses terms like _references_, _objects_, _methods_. If
you're not familiar with those terms then it would be a good idea to read
at least the following perl manuals first: perlreftut, perldsc, perllol,
and perlboot.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc ChangeLog CONTRIBUTING.md Driver.xst README.md SECURITY.md
%license LICENSE

%changelog
