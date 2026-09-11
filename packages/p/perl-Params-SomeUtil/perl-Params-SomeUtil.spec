#
# spec file for package perl-Params-SomeUtil
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


%define cpan_name Params-SomeUtil
Name:           perl-Params-SomeUtil
Version:        1.110.0
Release:        0
# 1.11 -> normalize -> 1.110.0
%define cpan_version 1.11
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple, compact and correct param-checking functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(Test::More) >= 0.87
Provides:       perl(Params::SomeUtil) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Params::SomeUtil' provides a basic set of importable functions that makes
checking parameters a hell of a lot easier. This module is a fork of
version 1.07 of Params::Util with some additional bug fixes, see WHY below.

While they can be (and are) used in other contexts, the main point behind
this module is that the functions *both* Do What You Mean, and Do The Right
Thing, so they are most useful when you are getting params passed into your
code from someone and/or somewhere else and you can't really trust the
quality.

Thus, 'Params::SomeUtil' is of most use at the edges of your API, where
params and data are coming in from outside your code.

The functions provided by 'Params::SomeUtil' check in the most strictly
correct manner known, are documented as thoroughly as possible so their
exact behaviour is clear, and heavily tested so make sure they are not
fooled by weird data and Really Bad Things.

To use, simply load the module providing the functions you want to use as
arguments (as shown in the SYNOPSIS).

To aid in maintainability, 'Params::SomeUtil' will *never* export by
default.

You must explicitly name the functions you want to export, or use the
':ALL' param to just have it export everything (although this is not
recommended if you have any _FOO functions yourself with which future
additions to 'Params::SomeUtil' may clash)

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
%doc Changes README README.md
%license LICENSE

%changelog
