#
# spec file for package perl-Class-C3-XS
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


Name:           perl-Class-C3-XS
Version:        0.14
Release:        0
%define cpan_name Class-C3-XS
Summary:        XS speedups for Class::C3
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-C3-XS/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Metadata)
%{perl_requires}

%description
This contains XS performance enhancers for Class::C3 version 0.16 and
higher. The main Class::C3 package will use this package automatically if
it can find it. Do not use this package directly, use Class::C3 instead.

The test suite here is not complete, although it does verify a few basic
things. The best testing comes from running the Class::C3 test suite
*after* this module is installed.

This module won't do anything for you if you're running a version of
Class::C3 older than 0.16. (It's not a dependency because it would be
circular with the optional dependency from that package to this one).

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
