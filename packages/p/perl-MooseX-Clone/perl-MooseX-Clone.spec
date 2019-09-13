#
# spec file for package perl-MooseX-Clone
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-Clone
Version:        0.06
Release:        0
%define cpan_name MooseX-Clone
Summary:        Fine-grained cloning support for Moose objects
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Clone/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Visitor) >= 0.24
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Data::Visitor) >= 0.24
Requires:       perl(Data::Visitor::Callback)
Requires:       perl(Hash::Util::FieldHash::Compat)
Requires:       perl(Moose::Role)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Out of the box the Moose manpage only provides very barebones cloning
support in order to maximize flexibility.

This role provides a 'clone' method that makes use of the low level cloning
support already in the Moose manpage and adds selective deep cloning based
on introspection on top of that. Attributes with the 'Clone' trait will
handle cloning of data within the object, typically delegating to the
attribute value's own 'clone' method.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
