#
# spec file for package perl-MooseX-MarkAsMethods
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-MarkAsMethods
Version:        0.15
Release:        0
%define cpan_name MooseX-MarkAsMethods
Summary:        Mark overload code symbols as methods
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-MarkAsMethods/
Source:         http://www.cpan.org/authors/id/R/RS/RSRCHBOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(namespace::autoclean) >= 0.12
#BuildRequires: perl(funcs)
#BuildRequires: perl(MooseX::MarkAsMethods)
#BuildRequires: perl(TestClass)
#BuildRequires: perl(TestClass::Funky)
#BuildRequires: perl(TestRole)
Requires:       perl(B::Hooks::EndOfScope)
Requires:       perl(Moose) >= 0.94
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::MetaRole)
Requires:       perl(namespace::autoclean) >= 0.12
%{perl_requires}

%description
MooseX::MarkAsMethods allows one to easily mark certain functions as Moose
methods. This will allow other packages such as the namespace::autoclean
manpage to operate without blowing away your overloads. After using
MooseX::MarkAsMethods your overloads will be recognized by the Class::MOP
manpage as being methods, and class extension as well as composition from
roles with overloads will "just work".

By default we check for overloads, and mark those functions as methods.

If 'autoclean =&gt; 1' is passed to import on using this module, we will
invoke namespace::autoclean to clear out non-methods.

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
%doc Changes README

%changelog
