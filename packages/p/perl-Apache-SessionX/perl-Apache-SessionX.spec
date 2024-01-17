#
# spec file for package perl-Apache-SessionX
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Apache-SessionX
BuildRequires:  apache2-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  mysql-client
BuildRequires:  pcre-devel
BuildRequires:  perl-Apache-Session
BuildRequires:  perl-DBD-mysql
BuildRequires:  perl-MLDBM
BuildRequires:  perl-macros
Version:        2.01
Release:        0
Provides:       Apache-SessionX
Requires:       apache2-mod_perl
Requires:       perl-DBI
Requires:       perl-URI
Conflicts:      perlmod
Summary:        Persistent Storage for Arbitrary Data (for Embperl)
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://cpan.org/modules/by-module/Apache/
Source:         Apache-SessionX-%{version}.tar.gz
Source1:        get-apache-version.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
Apache::SessionX extends Apache::Session. It was initially written to
use Apache::Session from inside of HTML::Embperl, but is seems to be
useful outside of Embperl as well, so here is it as standalone module.

%prep 
%setup -n Apache-SessionX-%{version}

%build
PERL_HASH_SEED=42 perl Makefile.PL
make all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Apache/testcount.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README MANIFEST 
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Apache
%dir %{perl_vendorarch}/auto
%{perl_vendorarch}/auto/Apache

%changelog
