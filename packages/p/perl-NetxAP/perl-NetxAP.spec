#
# spec file for package perl-NetxAP
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


Name:           perl-NetxAP
Version:        0.02
Release:        0
Summary:        Interface to the protocol family IMAP, IMSP, ACAP, and ICAP
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/~kjohnson/NetxAP-0.02/
Source:         http://search.cpan.org/CPAN/authors/id/K/KJ/KJOHNSON/NetxAP-%{version}.tar.gz
Patch0:         NetxAP-%{version}.dif
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       perl-Digest-HMAC
%define cpan_name NetxAP
Provides:       p_netxap
Obsoletes:      p_netxap
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This module provides an interface to the protocol family represented by
IMAP, IMSP, ACAP, and ICAP.  A usable IMAP module is also provide.

%prep
%autosetup -p0 -n %{cpan_name}-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%defattr(-, root, root)
%dir %{perl_vendorlib}/Net
%{perl_vendorarch}/auto/Net
%{perl_vendorlib}/Net/IMAP.pm
%{perl_vendorlib}/Net/xAP.pm
%doc %{_mandir}/man3/Net::IMAP.3pm.gz
%doc %{_mandir}/man3/Net::xAP.3pm.gz
%doc ANNOUNCE BUGS CREDITS MANIFEST NEWS README TODO examples

%changelog
