#
# spec file for package perl-Params-Classify
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Params-Classify
Version:        0.015
Release:        0
%define cpan_name Params-Classify
Summary:        Argument Type Classification
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Params-Classify/
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
Requires:       perl(parent)
Recommends:     perl(Devel::CallChecker) >= 0.003
%{perl_requires}

%description
This module provides various type-testing functions. These are intended for
functions that, unlike most Perl code, care what type of data they are
operating on. For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions in
C++).

There are two flavours of function in this module. Functions of the first
flavour only provide type classification, to allow code to discriminate
between argument types. Functions of the second flavour package up the most
common type of type discrimination: checking that an argument is of an
expected type. The functions come in matched pairs, of the two flavours,
and so the type enforcement functions handle only the simplest requirements
for arguments of the types handled by the classification functions.
Enforcement of more complex types may, of course, be built using the
classification functions, or it may be more convenient to use a module
designed for the more complex job, such as Params::Validate.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
