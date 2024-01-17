#
# spec file for package perl-MooseX-SemiAffordanceAccessor
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


Name:           perl-MooseX-SemiAffordanceAccessor
Version:        0.10
Release:        0
%define cpan_name MooseX-SemiAffordanceAccessor
Summary:        Name your accessors foo() and set_foo()
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-SemiAffordanceAccessor/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Moose) >= 0.94
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::MetaRole)
%{perl_requires}

%description
This module does not provide any methods. Simply loading it changes the
default naming policy for the loading class so that accessors are separated
into get and set methods. The get methods have the same name as the
accessor, while set methods are prefixed with "set_".

If you define an attribute with a leading underscore, then the set method
will start with "_set_".

If you explicitly set a "reader" or "writer" name when creating an
attribute, then that attribute's naming scheme is left unchanged.

The name "semi-affordance" comes from David Wheeler's Class::Meta module.

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
%doc Changes LICENSE README.md

%changelog
