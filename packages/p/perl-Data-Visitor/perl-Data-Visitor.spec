#
# spec file for package perl-Data-Visitor
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Data-Visitor
Version:        0.31
Release:        0
%define cpan_name Data-Visitor
Summary:        Visitor style traversal of Perl data structures
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Tie::ToObject) >= 0.01
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Moose) >= 0.89
Requires:       perl(Sub::Name)
Requires:       perl(Tie::ToObject) >= 0.01
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
This module is a simple visitor implementation for Perl values.

It has a main dispatcher method, 'visit', which takes a single perl value
and then calls the methods appropriate for that value.

It can recursively map (cloning as necessary) or just traverse most
structures, with support for per object behavior, circular structures,
visiting tied structures, and all ref types (hashes, arrays, scalars, code,
globs).

Data::Visitor is meant to be subclassed, but also ships with a callback
driven subclass, Data::Visitor::Callback.

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
