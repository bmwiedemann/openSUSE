#
# spec file for package csync2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           csync2
Version:        2.0+git.1542296533.b974921
Release:        0
Summary:        Cluster synchronization tool
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
Url:            http://oss.linbit.com/csync2/
#Source0:       http://oss.linbit.com/csync2/%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.bz2
Source1:        csync2-README.quickstart
Source2:        csync2-rm-ssl-cert
Source3:        csync2.socket
Source4:        csync2@.service
# PATCH-FIX-UPSTREAM -- tserong@suse.com -- fix ugly ./configure warnings about missing headers
Patch10:        0003-Set-AC_PROG_CPP-in-configure.ac.patch
# PATCH-FIX-UPSTREAM -- tserong@suse.com -- use properly versioned sonames in dlopen()
Patch12:        0002-Patch-sonames.patch
# PATCH-FIX-UPSTREAM -- tserong@suse.com -- ensure COPYING is present in docfiles and thus %doc
Patch13:        0001-Add-COPYING-as-docfile.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libgnutls-devel
BuildRequires:  librsync-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-rpm-macros
Requires:       sqlite3
Requires(post): openssl
%if 0%{?suse_version} > 1320
# Conflicts with net-tools in Leap
Requires(post): hostname
%endif

%description
Csync2 is a cluster synchronization tool. It can be used to keep files on
multiple hosts in a cluster in sync. Csync2 can handle complex setups with
much more than just 2 hosts, handle file deletions and can detect conflicts.
It is expedient for HA-clusters, HPC-clusters, COWs and server farms.

%prep
%setup -q
%patch10 -p1
%patch12 -p1
%patch13 -p1

%build
autoreconf -fvi
%configure \
    --enable-sqlite3 \
    --sysconfdir=%{_sysconfdir}/csync2 \
    --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/lib/csync2
install -p -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.quickstart
install -p -m 755 %{SOURCE2} %{buildroot}%{_sbindir}/csync2-rm-ssl-cert
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/
# We need these empty files to be able to %%ghost them
touch %{buildroot}%{_sysconfdir}/csync2/csync2_ssl_key.pem
touch %{buildroot}%{_sysconfdir}/csync2/csync2_ssl_cert.pem

%pre
%service_add_pre csync2.socket

%post
%service_add_post csync2.socket
umask 077
if [ ! -f %{_sysconfdir}/csync2/csync2_ssl_key.pem ]; then
  %{_bindir}/openssl genrsa -out %{_sysconfdir}/csync2/csync2_ssl_key.pem 1024
fi
FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
   FQDN=localhost.localdomain
fi
if [ ! -f %{_sysconfdir}/csync2/csync2_ssl_cert.pem ]; then
  yes '' | %{_bindir}/openssl req -new -key %{_sysconfdir}/csync2/csync2_ssl_key.pem -out %{_sysconfdir}/csync2/csync2_ssl_cert.csr
  %{_bindir}/openssl x509 -req -days 3000 -in %{_sysconfdir}/csync2/csync2_ssl_cert.csr -signkey %{_sysconfdir}/csync2/csync2_ssl_key.pem \
    -out %{_sysconfdir}/csync2/csync2_ssl_cert.pem
  rm %{_sysconfdir}/csync2/csync2_ssl_cert.csr
fi

%preun
%service_del_preun csync2.socket
# Cleanup all databases upon last removal
if [ $1 -eq 0 ]; then
  rm -f %{_localstatedir}/lib/csync2/*
fi

%postun
%service_del_postun csync2.socket

%files
%{_sbindir}/csync2
%{_sbindir}/csync2-compare
%{_unitdir}/csync2.socket
%{_unitdir}/csync2@.service
%dir %{_localstatedir}/lib/csync2/
# Using docdir here ensures correct doc file tagging
%{_docdir}/%{name}
%dir %{_sysconfdir}/csync2/
%config(noreplace) %{_sysconfdir}/csync2/csync2.cfg
%ghost %config %{_sysconfdir}/csync2/csync2_ssl_key.pem
%ghost %config %{_sysconfdir}/csync2/csync2_ssl_cert.pem
%{_sbindir}/csync2-rm-ssl-cert
%{_mandir}/man1/csync2.1*

%changelog
