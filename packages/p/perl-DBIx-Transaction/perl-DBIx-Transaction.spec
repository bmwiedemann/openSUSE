#
# spec file for package perl-DBIx-Transaction
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


Name:           perl-DBIx-Transaction
BuildRequires:  perl-DBI
BuildRequires:  perl-Module-Build
BuildRequires:  perl-macros
Url:            http://cpan.org/modules/by-module/DBIx/
Requires:       perl-DBI
Summary:        Allow transactions to be nested in DBI
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        1.100
Release:        0
Source:         DBIx-Transaction-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
DBIx::Transaction is a wrapper around DBI that helps you manage your
database transactions.



Authors:
--------
    Tyler "Crackerjack" MacDonald <japh@crackerjack.net>

%prep
%setup -n DBIx-Transaction-%{version} -q

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
%dir %{perl_vendorlib}/DBIx
%dir %{perl_vendorlib}/DBIx/Transaction
%{perl_vendorlib}/DBIx/Transaction.*
%{perl_vendorlib}/DBIx/Transaction/*.pm
%dir %{perl_vendorarch}/auto/DBIx
%dir %{perl_vendorarch}/auto/DBIx/Transaction
%{_mandir}/man3/*

%changelog
