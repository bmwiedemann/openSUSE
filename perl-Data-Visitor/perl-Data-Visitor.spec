#
# spec file for package perl-Data-Visitor
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Visitor
Version:        0.30
Release:        0
%define cpan_name Data-Visitor
Summary:        Visitor style traversal of Perl data structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Visitor/
Source:         http://www.cpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::ToObject) >= 0.01
BuildRequires:  perl(namespace::clean) >= 0.19
#BuildRequires: perl(Data::Visitor)
#BuildRequires: perl(Data::Visitor::Callback)
#BuildRequires: perl(Sub::Name)
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Moose) >= 0.89
Requires:       perl(Task::Weaken)
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

the Data::Visitor manpage is meant to be subclassed, but also ships with a
callback driven subclass, the Data::Visitor::Callback manpage.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
