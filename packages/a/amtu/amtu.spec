#
# spec file for package amtu
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           amtu
URL:            http://sourceforge.net/projects/amtueal/
Requires:       audit >= 1.2.9
Version:        1.0.8
Release:        0
Summary:        Abstract Machine Test Utility
License:        CPL-1.0
Group:          Productivity/Security
Source:         %{name}-%{version}.tar.gz
Patch0:         amtu-1.0.8_memsep_fclose_bnc523353.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  audit
BuildRequires:  audit-devel
BuildRequires:  audit-libs
ExclusiveArch:  %ix86 x86_64 ia64 ppc ppc64 s390 s390x

%description
Abstract Machine Test Utility (AMTU) is an administrative utility to
check whether the underlying protection mechanism of the hardware is
still being enforced. This is a requirement of the Controlled Access
Protection Profile (CAPP) FTP_AMT.1. See
http://www.radium.csc.mil/tpep/library/protection_profiles/CAPP-1.d.pdf
.

%prep
%setup -q amtu
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -Wall -pipe -fcommon"
    CC=gcc
export CC CFLAGS
  ./configure                           \
	--prefix=/usr			\
	--bindir=/usr/sbin		\
	--mandir=%{_mandir}		
  make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/amtu
make DESTDIR=$RPM_BUILD_ROOT install-strip
install -m 644 doc/amtu.8    $RPM_BUILD_ROOT/%{_mandir}/man8/amtu.8

%files
%defattr(-,root,root)
%attr(700,root,root)/usr/sbin/amtu
%doc %attr(444,root,root) %{_mandir}/man8/amtu.8*
%doc %attr(755,root,root) %{_defaultdocdir}/amtu

%changelog
