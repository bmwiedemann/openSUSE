#
# spec file for package perl-Net-IPv4Addr
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


Name:           perl-Net-IPv4Addr
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Provides:       Net
AutoReqProv:    on
Version:        0.10
Release:        148
Summary:        Net::IPv4Addr Module for Perl
Url:            http://search.cpan.org/~frajulac/Net-IPv4Addr-0.10
Source:         Net-IPv4Addr-%{version}.tar.gz
Patch0:         Net-IPv4Addr-%{version}.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl perl-macros

%description
Net::IPv4Addr provides functions for parsing IPv4 addresses both in
traditional address/netmask format and in the new CIDR format. There
are also methods for calculating the network and broadcast address and
also to see check if a given address is in a specific network.

Authors:
--------
    Francis J. Lacoste <francis.lacoste@iNsu.COM>

%prep
%setup -n Net-IPv4Addr-%{version}
%patch0

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL 
make %{?_smp_mflags}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%doc ChangeLog README
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorarch}/auto/Net
%dir %{perl_vendorarch}/auto/Net/IPv4Addr
%dir %{perl_vendorlib}/auto/Net
%dir %{perl_vendorlib}/auto/Net/IPv4Addr
%{perl_vendorlib}/Net/IPv4Addr.pm
%{perl_vendorlib}/auto/Net/IPv4Addr/autosplit.ix
/usr/bin/ipv4calc
%doc %{_mandir}/man?/ipv4calc.1.gz
%doc %{_mandir}/man?/Net::IPv4Addr.3pm.gz

%changelog
