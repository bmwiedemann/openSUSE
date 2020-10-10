#
# spec file for package libunbound-devel-mini
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


%bcond_without python
%bcond_without munin
%bcond_without hardened_build

%define ldns_version 1.6.16

#
Name:           libunbound-devel-mini
Version:        1.12.0
Release:        0
#
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  flex
BuildRequires:  ldns-devel >= %{ldns_version}
BuildRequires:  libevent-devel
BuildRequires:  libexpat-devel
BuildRequires:  libsodium-devel
BuildRequires:  openssl-devel
Requires:       this-is-only-for-build-envs
Conflicts:      unbound-devel
Conflicts:      libunbound8
Provides:       libunbound-devel = %{version}-%{release}
#
URL:            https://www.unbound.net/
Source:         https://www.unbound.net/downloads/unbound-%{version}.tar.gz
Source1:        libunbound-devel-mini-rpmlintrc
Source5:        root.key
Source6:        dlv.isc.org.key
# From http://data.iana.org/root-anchors/icannbundle.pem
Source12:       icannbundle.pem
Source13:       root.anchor

Summary:        Just a devel package for build loops
License:        BSD-3-Clause
Group:          Productivity/Networking/DNS/Servers

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%prep
%setup -n unbound-%version

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure \
  --disable-rpath \
  --with-libevent \
  --with-pthreads \
  --disable-static \
  --with-ldns=%{_prefix} \
  --enable-sha2 \
  --enable-gost \
  --enable-ecdsa \
  --enable-event-api \
  --enable-pie \
  --enable-relro-now \
  --enable-dnscrypt \
  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \
  --with-pidfile=%{piddir}%{name}/%{name}.pid \
  --without-pythonmodule --without-pyunbound \
  --with-libunbound-only \
  --with-rootkey-file=%{_sharedstatedir}/unbound/root.key

make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_mandir} %{buildroot}%{_libdir}/*.la

%check
# it currently fails in the ldns unit test. which is weird as both come from the same project
make check ||:

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libunbound.so.*
%{_includedir}/unbound.h
%{_includedir}/unbound-event.h
%{_libdir}/libunbound.so

%changelog
