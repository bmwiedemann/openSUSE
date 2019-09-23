#
# spec file for package perl-Class-Inner
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Class-Inner
Version:        0.200001
Release:        1
# MANUAL
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Class-Inner
Summary:        A perlish implementation of Java like inner classes
Url:            http://search.cpan.org/dist/Class-Inner/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/A/AR/ARUNBEAR/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
%{perl_requires}

%description
Yet another implementation of an anonymous class with per object
overrideable methods, but with the added attraction of sort of working
dispatch to the parent class's method.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
