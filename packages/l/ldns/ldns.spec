#
# spec file for package ldns
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libname libldns3
Name:           ldns
Version:        1.8.4
Release:        0
Summary:        A library for developing the Domain Name System
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.nlnetlabs.nl/projects/ldns/
Source:         https://www.nlnetlabs.nl/downloads/ldns/ldns-%{version}.tar.gz
Source1:        https://www.nlnetlabs.nl/downloads/ldns/ldns-%{version}.tar.gz.asc
Source2:        ldns.keyring
Patch2:         ldns-1.8.4-swig-3.4.0.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  libpcap-devel
BuildRequires:  perl-Devel-CheckLib
BuildRequires:  python3-devel
BuildRequires:  swig

%description
ldns is a C library that can be used for domain name system (DNS)
development. It supports RFCs like the DNSSEC documents, and allows
developers to create software conforming to RFCs, as well as
experimental software for current Internet Drafts.

This package holds the tools/examples from ldns.

%package -n %{libname}
Summary:        A library for developing the Domain Name System
Group:          System/Libraries

%description -n %{libname}
ldns is a C library that can be used for domain name system (DNS)
development. It supports RFCs like the DNSSEC documents, and allows
developers to create software conforming to RFCs, as well as
experimental software for current Internet Drafts.

%package devel
Summary:        Development files for ldns
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       openssl-devel

%description devel
ldns is a C library that can be used for domain name system (DNS)
development. It supports RFCs like the DNSSEC documents, and allows
developers to create software conforming to RFCs, as well as
experimental software for current Internet Drafts.

This package holds the development files.

%package -n python3-ldns
Summary:        Python3 bindings for ldns
Group:          Development/Languages/Python
Requires:       %{libname} >= %{version}

%description -n python3-ldns
Python bindings for the ldns library

%package -n perl-DNS-LDNS
Summary:        Perl bindings for ldns
Group:          Development/Languages/Perl
Requires:       %{libname} >= %{version}
%{libperl_requires}

%description -n perl-DNS-LDNS
Perl bindings for the ldns library.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
if pkg-config --max-version=1.1.0 openssl; then
  DISABLE_DANE="--disable-dane-verify"
fi
export PYTHON=%{_bindir}/python3
%configure                \
  --disable-rpath         \
  --disable-static        \
  --enable-rrtype-ninfo   \
  --enable-rrtype-rkey    \
  --enable-rrtype-cds     \
  --enable-rrtype-uri     \
  --enable-rrtype-ta      \
  --with-pyldns           \
  --with-pyldnsx          \
  --with-drill            \
  --with-examples         \
  --with-ca-path=%{_sysconfdir}/ssl/certs/ \
  $DISABLE_DANE
%make_build

# We cannot use the built-in --with-p5-dns-ldns
pushd contrib/DNS-LDNS
LD_LIBRARY_PATH="../../lib:$LD_LIBRARY_PATH" perl \
    Makefile.PL INSTALLDIRS=vendor  INC="-I. -I../.." LIBS="-L../../lib"
%make_build
popd

%install
make DESTDIR=%{buildroot} \
  install \
  install-drill \
  install-examples

make DESTDIR=%{buildroot} \
  install-pyldns \
  install-pyldnsx
rm -v %{buildroot}%{python3_sitearch}/*.la

make -C contrib/DNS-LDNS DESTDIR=%{buildroot} pure_install
chmod 755 %{buildroot}%{perl_vendorarch}/auto/DNS/LDNS/LDNS.so
rm -f %{buildroot}%{perl_vendorarch}/auto/DNS/LDNS/{.packlist,LDNS.bs}

rm -v %{buildroot}%{_libdir}/libldns.*a
%fdupes %{buildroot}%{_mandir}

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%{_bindir}/drill
%{_bindir}/ldns-chaos
%{_bindir}/ldns-compare-zones
%{_bindir}/ldns-dpa
%{_bindir}/ldns-gen-zone
%{_bindir}/ldns-key2ds
%{_bindir}/ldns-keyfetcher
%{_bindir}/ldns-keygen
%{_bindir}/ldns-mx
%{_bindir}/ldns-notify
%{_bindir}/ldns-nsec3-hash
%{_bindir}/ldns-read-zone
%{_bindir}/ldns-resolver
%{_bindir}/ldns-revoke
%{_bindir}/ldns-rrsig
%{_bindir}/ldns-signzone
%{_bindir}/ldns-test-edns
%{_bindir}/ldns-testns
%{_bindir}/ldns-update
%{_bindir}/ldns-verify-zone
%{_bindir}/ldns-version
%{_bindir}/ldns-walk
%{_bindir}/ldns-zcat
%{_bindir}/ldns-zsplit
%{_bindir}/ldnsd
%{_bindir}/ldns-dane
%{_mandir}/man1/drill.1%{?ext_man}
%{_mandir}/man1/ldns*.1%{?ext_man}

%files -n %{libname}
%license LICENSE
%{_libdir}/libldns.so.*

%files devel
%license LICENSE
%{_bindir}/ldns-config
%{_includedir}/ldns/
%{_libdir}/libldns.so
%{_libdir}/pkgconfig/ldns.pc
%{_mandir}/man3/ldns*.3%{?ext_man}
%doc libdns.vim README*

%files -n perl-DNS-LDNS
%license LICENSE
%{perl_vendorarch}/DNS/LDNS.pm
%dir %{perl_vendorarch}/DNS/
%{perl_vendorarch}/DNS/LDNS/
%dir %{perl_vendorarch}/auto/DNS/
%{perl_vendorarch}/auto/DNS/LDNS/
%{_mandir}/man3/DNS::LDNS*3pm*

%files -n python3-ldns
%license LICENSE
%{python3_sitearch}/*ldns*

%changelog
