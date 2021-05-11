#
# spec file for package knot
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{?suse_version} > 1320
%bcond_without  dnstap
%bcond_without  lto
%else
%bcond_with     dnstap
%bcond_with     lto
%endif
%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%if 0%{?is_opensuse}
%bcond_without maxminddb
%else
%bcond_with    maxminddb
%endif

%if 0%{?suse_version} > 1140 && ( 0%{?suse_version} != 1315 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ))
%bcond_without docs
%else
%bcond_with    docs
%endif

%define libdnssec   libdnssec8
%define libknot     libknot11
%define libzscanner libzscanner3

Name:           knot
Version:        3.0.5
Release:        0
%define pkg_name knot
Summary:        An authoritative DNS daemon
License:        GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Servers
URL:            http://www.knot-dns.cz/
Source0:        https://secure.nic.cz/files/knot-dns/%{pkg_name}-%{version}.tar.xz
Source1:        knot.service
Source2:        knot-tmp.conf
Source3:        https://secure.nic.cz/files/knot-dns/%{pkg_name}-%{version}.tar.xz.asc
BuildRequires:  libedit-devel
%if 0%{?suse_version} > 1320 || 0%{?leap_version} == 420300
BuildRequires:  libidn2-devel
%else
BuildRequires:  libidn-devel
%endif
BuildRequires:  liburcu-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gnutls) >= 3.3
BuildRequires:  pkgconfig(nettle)
%if %{with maxminddb}
BuildRequires:  pkgconfig(libmaxminddb)
%endif
BuildRequires:  libcap-ng-devel
BuildRequires:  xz
Requires(pre):  pwdutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  lmdb-devel >= 0.9.15
%if %{with docs}
BuildRequires:  makeinfo
BuildRequires:  python3-Sphinx
%endif
%if %{with dnstap}
BuildRequires:  libfstrm-devel
BuildRequires:  libprotobuf-c-devel >= 1.0.0
BuildRequires:  protobuf-c >= 1.0.0
%endif
%if %{with systemd}
%define has_systemd 1
BuildRequires:  systemd-devel
%{?systemd_requires}
%endif
Obsoletes:      knot2 < %{version}

%description
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

%package devel
Group:          Development/Libraries/C and C++
Requires:       knot = %{version}
#
Summary:        Development files for the knot libraries

%description devel
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains headers for knot.

%package -n %{libdnssec}
Group:          System/Libraries
#
Summary:        DNSSEC support functions for Knot DNS

%description -n %{libdnssec}
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains a library for DNSSEC support functions.

%package -n %{libknot}
Group:          System/Libraries
#
Summary:        Knot DNS support library

%description -n %{libknot}
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains the essential core library for Knot services.

%package -n %{libzscanner}
Group:          System/Libraries
#
Summary:        Zone record parsing functions for Knot DNS

%description -n %{libzscanner}
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains a library for a zone record scanner.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%configure \
  --libexecdir=%{_libexecdir}/%{pkg_name} \
  --includedir=%{_includedir}/knot/ \
  --disable-static \
  --enable-recvmmsg=yes \
%if %{with lto}
  --enable-lto=yes \
%endif
%if %{with dnstap}
  --enable-dnstap=yes \
  --with-module-dnstap=shared \
%endif
  --enable-rosedb \
  --with-module-rosedb=shared \
%if %{with systemd}
  --with-rundir=/run/knot/ \
  --enable-systemd=yes \
%endif
  --with-module-cookies=shared \
  --with-module-dnsproxy=yes \
%if %{with maxminddb}
  --with-module-geoip=shared \
%endif
  --with-module-noudp=shared \
  --with-module-onlinesign=yes \
  --with-module-queryacl=shared \
  --with-module-rrl=shared \
  --with-module-stats=shared \
  --with-module-synthrecord=shared \
  --with-module-whoami=shared \
  --with-bash-completions=/etc/bash_completion.d \
  --disable-silent-rules
%make_build STRIP="/bin/true"

%install
%make_install STRIP="/bin/true"
install -d %{buildroot}%{_docdir}/%{pkg_name}
install -d %{buildroot}%{_docdir}/%{pkg_name}/samples/
rm %{buildroot}%{_sysconfdir}/%{pkg_name}/*
install -p -m644 samples/knot.sample.conf %{buildroot}%{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%if %{with systemd}
install -d %{buildroot}%{_unitdir} %{buildroot}%{_tmpfilesdir}
install -p -m644 %{SOURCE1} %{buildroot}%{_unitdir}/%{pkg_name}.service
install -p -m644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/knot.conf
ln -s service %{buildroot}%{_sbindir}/rcknot
%endif
install -p -m644 COPYING NEWS README.md %{buildroot}%{_docdir}/%{pkg_name}
install -p -m644 samples/*.conf samples/*.zone* %{buildroot}%{_docdir}/%{pkg_name}/samples/
find %{buildroot} -type f -name "*.la" -delete -print
install -d -m 0750 %{buildroot}/var/lib/knot/

%pre
getent group knot >/dev/null || groupadd -r knot
getent passwd knot >/dev/null || \
  useradd -r -g knot -d %{_sysconfdir}/knot -s /sbin/nologin \
  -c "Knot DNS server" knot
%if %{with systemd}
%service_add_pre %{pkg_name}.service
%preun
%service_del_preun %{pkg_name}.service

%post
systemd-tmpfiles --create  %{_tmpfilesdir}/knot.conf  || :
%service_add_post %{pkg_name}.service
# Incompatibility warning
if grep -q '{' %{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf; then
cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release} << EOF
WARNING: You are upgrading from incompatible version of Knot DNS

Your configuration file looks like you are upgrading from ancient version of Knot DNS.
Knot 1.6.x was deprecated quite some time ago:

https://lists.nic.cz/pipermail/knot-dns-users/2017-April/001099.html

Unfortunately, it used completely different format of configuration file and
you have to migrate your configuration manually.

Please, see examples in %{_docdir}/%{pkg_name}/samples/ directory.
EOF
fi

%postun
%service_del_postun %{pkg_name}.service
%endif

%post   -n %{libdnssec}   -p /sbin/ldconfig
%post   -n %{libknot}     -p /sbin/ldconfig
%post   -n %{libzscanner} -p /sbin/ldconfig
%postun -n %{libdnssec}   -p /sbin/ldconfig
%postun -n %{libknot}     -p /sbin/ldconfig
%postun -n %{libzscanner} -p /sbin/ldconfig

%files
%dir %attr(750,root,root) %{_sysconfdir}/%{pkg_name}
%config(noreplace) %{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man?/*
%doc %{_docdir}/%{pkg_name}
%if %{with systemd}
%{_unitdir}/%{pkg_name}.service
%{_tmpfilesdir}/knot.conf
%endif
%{_libdir}/knot/
%dir %attr(-,knot,knot) /var/lib/knot/
%ghost %dir %(751,knot,knot) /run/knot

%files -n %{libdnssec}
%{_libdir}/libdnssec.so.*

%files -n %{libknot}
%{_libdir}/libknot.so.*

%files -n %{libzscanner}
%{_libdir}/libzscanner.so.*

%files devel
%{_includedir}/knot/
%{_libdir}/libdnssec.so
%{_libdir}/libknot.so
%{_libdir}/libzscanner.so
%{_libdir}/pkgconfig/knotd.pc
%{_libdir}/pkgconfig/libdnssec.pc
%{_libdir}/pkgconfig/libknot.pc
%{_libdir}/pkgconfig/libzscanner.pc

%changelog
