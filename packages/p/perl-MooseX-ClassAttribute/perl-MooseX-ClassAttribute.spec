#
# spec file for package perl-MooseX-ClassAttribute
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-ClassAttribute
Version:        0.29
Release:        0
%define cpan_name MooseX-ClassAttribute
Summary:        Declare class attributes Moose-style
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-ClassAttribute/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.05
BuildRequires:  perl(namespace::autoclean) >= 0.11
BuildRequires:  perl(namespace::clean) >= 0.20
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Moose) >= 2.00
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Meta::Role::Attribute)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util)
Requires:       perl(Moose::Util::MetaRole)
Requires:       perl(namespace::autoclean) >= 0.11
Requires:       perl(namespace::clean) >= 0.20
%{perl_requires}

%description
This module allows you to declare class attributes in exactly the same way
as object attributes, using 'class_has()' instead of 'has()'.

You can use any feature of Moose's attribute declarations, including
overriding a parent's attributes, delegation ('handles'), attribute traits,
etc. All features should just work. The one exception is the "required"
flag, which is not allowed for class attributes.

The accessor methods for class attribute may be called on the class
directly, or on objects of that class. Passing a class attribute to the
constructor will not set that attribute.

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
%doc Changes CONTRIBUTING.md LICENSE README.md

%changelog
