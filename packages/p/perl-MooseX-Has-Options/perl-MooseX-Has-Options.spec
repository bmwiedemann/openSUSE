#
# spec file for package perl-MooseX-Has-Options
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


Name:           perl-MooseX-Has-Options
Version:        0.003
Release:        0
%define cpan_name MooseX-Has-Options
Summary:        Succinct options for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Has-Options/
Source:         http://www.cpan.org/authors/id/P/PS/PSHANGOV/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Package::Stash) >= 0.18
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(namespace::autoclean)
#BuildRequires: perl(MooseX::Has::Options)
Requires:       perl(Class::Load)
Requires:       perl(List::MoreUtils)
Requires:       perl(Package::Stash) >= 0.18
Requires:       perl(String::RewritePrefix)
%{perl_requires}

%description
This module provides a succinct syntax for declaring options for the Moose
manpage attributes.

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
%doc Changes LICENSE README weaver.ini

%changelog
