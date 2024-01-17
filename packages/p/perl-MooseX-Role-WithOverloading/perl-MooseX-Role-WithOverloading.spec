#
# spec file for package perl-MooseX-Role-WithOverloading
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


Name:           perl-MooseX-Role-WithOverloading
Version:        0.17
Release:        0
%define cpan_name MooseX-Role-WithOverloading
Summary:        (DEPRECATED) Roles which support overloading
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Role-WithOverloading/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role) >= 1.15
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(aliased)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Moose) >= 0.94
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role) >= 1.15
Requires:       perl(aliased)
Requires:       perl(namespace::autoclean) >= 0.16
Requires:       perl(namespace::clean) >= 0.19
Recommends:     perl(Moose::Util::MetaRole)
%{perl_requires}

%description
MooseX::Role::WithOverloading allows you to write a the Moose::Role manpage
which defines overloaded operators and allows those overload methods to be
composed into the classes/roles/instances it's compiled to, where plain the
Moose::Role manpages would lose the overloading.

Starting with the Moose manpage version 2.1300, this module is no longer
necessary, as the functionality is available already. In that case, 'use
MooseX::Role::WithOverloading' behaves identically to 'use Moose::Role'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENCE README

%changelog
