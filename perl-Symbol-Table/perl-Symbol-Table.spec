#
# spec file for package perl-Symbol-Table
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

# norootforbuild


Name:           perl-Symbol-Table
Url:            http://cpan.org/modules/by-module/Symbol/
License:        Artistic-1.0
Group:          Development/Languages/Perl
AutoReqProv:    on
Summary:        An easy interface to symbol tables
Version:        1.01
Release:        47
Source:         Symbol-Table-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Symbol::Table allows the user to manipulate Perl's symbol table



Authors:
--------
    Greg London

%prep
%setup -n Symbol-Table-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%dir %{perl_vendorlib}/Symbol
%{perl_vendorlib}/Symbol/Table.pm
%dir %{perl_vendorarch}/auto/Symbol
%dir %{perl_vendorarch}/auto/Symbol/Table
%{_mandir}/man3/*

%changelog
