#
# spec file for package perl-BIND-Conf_Parser
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



Name:           perl-BIND-Conf_Parser
Version:        0.97
Release:        0
Group:          Development/Libraries/Perl
License:        ISC
Url:            ftp://ftp.gac.edu/pub/guenther
Summary:        Parser class for BIND configuration files
Source:         BIND-Conf_Parser-%{version}.tar.bz2
Patch:          BIND-Conf_Parser-%{version}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
This module implements a virtual base class for parsing BIND server
version 8 configuration files (named.conf).

%prep
%setup -n BIND-Conf_Parser-%{version}
%patch

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%doc %{_mandir}/man?/*
%doc Changes README verify_zones
%{perl_vendorlib}/BIND
%{perl_vendorarch}/auto/BIND-Conf_Parser

%changelog
