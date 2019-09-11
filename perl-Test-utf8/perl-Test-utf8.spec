#
# spec file for package perl-Test-utf8
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-utf8
Version:        1.01
Release:        0
%define cpan_name Test-utf8
Summary:        Handy utf8 tests
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/pod/Test::utf8
Source:         http://www.cpan.org/authors/id/M/MA/MARKF/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(inc::Module::Install)
%{perl_requires}

%description
This module is a collection of tests useful for dealing with utf8 strings
in Perl.

This module has two types of tests: The validity tests check if a string is
valid and not corrupt, whereas the characteristics tests will check that
string has a given set of characteristics.

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
%doc CHANGES README

%changelog
