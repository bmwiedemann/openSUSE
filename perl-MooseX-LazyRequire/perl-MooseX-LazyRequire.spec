#
# spec file for package perl-MooseX-LazyRequire
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-LazyRequire
Version:        0.11
Release:        0
%define cpan_name MooseX-LazyRequire
Summary:        Required attributes which fail only when trying to use them
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-LazyRequire/
Source:         http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::CheckDeps) >= 0.002
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(aliased) >= 0.30
BuildRequires:  perl(namespace::autoclean)
#BuildRequires: perl(Account)
#BuildRequires: perl(MooseX::LazyRequire)
#BuildRequires: perl(MooseX::LazyRequire::Meta::Attribute::Trait::LazyRequire)
#BuildRequires: perl(Role)
Requires:       perl(Moose) >= 0.94
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role)
Requires:       perl(aliased) >= 0.30
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
This module adds a 'lazy_required' option to Moose attribute declarations.

The reader methods for all attributes with that option will throw an
exception unless a value for the attributes was provided earlier by a
constructor parameter or through a writer method.

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
