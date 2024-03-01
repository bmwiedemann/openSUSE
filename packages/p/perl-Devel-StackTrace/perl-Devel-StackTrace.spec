#
# spec file for package perl-Devel-StackTrace
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


%define cpan_name Devel-StackTrace
Name:           perl-Devel-StackTrace
Version:        2.50.0
Release:        0
%define cpan_version 2.05
License:        Artistic-2.0
Summary:        An object representing a stack trace
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
Provides:       perl(Devel::StackTrace) = %{version}
Provides:       perl(Devel::StackTrace::Frame) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The 'Devel::StackTrace' module contains two classes, 'Devel::StackTrace'
and Devel::StackTrace::Frame. These objects encapsulate the information
that can retrieved via Perl's 'caller' function, as well as providing a
simple interface to this data.

The 'Devel::StackTrace' object contains a set of 'Devel::StackTrace::Frame'
objects, one for each level of the stack. The frames contain all the data
available from 'caller'.

This code was created to support my Exception::Class::Base class (part of
Exception::Class) but may be useful in other contexts.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
