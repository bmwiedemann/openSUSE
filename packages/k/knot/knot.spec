#
# spec file for package knot
#
# Copyright (c) 2021 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        3.0.4
Release:        1
%define pkg_name knot
Summary:        An authoritative DNS daemon
License:        GPL-3.0+
Group:          Productivity/Networking/DNS/Servers
Url:            http://www.knot-dns.cz/
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
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildRequires:  lmdb-devel >= 0.9.15
%if %{with docs}
BuildRequires:  makeinfo
BuildRequires:  python3-Sphinx
%endif
%if %{with dnstap}
BuildRequires:  protobuf-c >= 1.0.0
BuildRequires:  libprotobuf-c-devel >= 1.0.0
BuildRequires:  libfstrm-devel
%endif
%if %{with systemd}
%define has_systemd 1
BuildRequires:  systemd-devel
%{?systemd_requires}
%endif
Obsoletes:      knot2 < %{version}

%description
Knot DNS is a high-performance authoritative DNS server implementation.

%package devel
Group:          Development/Libraries/C and C++
Requires:       knot = %{version}
#
Summary:        Development files for the knot libraries
%description devel
Knot DNS is a high-performance authoritative DNS server implementation.

Development files for knot.

%package -n %{libdnssec}
Group:          System/Libraries
#
Summary:        Shared library from knot: libdnssec
%description -n %{libdnssec}
Knot DNS is a high-performance authoritative DNS server implementation.

This package holds the shared library libdnssec from knot.

%package -n %{libknot}
Group:          System/Libraries
#
Summary:        Shared library from knot: libknot
%description -n %{libknot}
Knot DNS is a high-performance authoritative DNS server implementation.

This package holds the shared library libknot from knot.

%package -n %{libzscanner}
Group:          System/Libraries
#
Summary:        Shared library from knot 2: libzscanner
%description -n %{libzscanner}
Knot DNS is a high-performance authoritative DNS server implementation.

This package holds the shared library libzscanner from knot.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%configure \
  --sysconfdir=%{_sysconfdir} \
  --libexecdir=%{_libexecdir}/%{pkg_name} \
  --localstatedir=%{_localstatedir} \
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
make %{?_smp_mflags} STRIP="/bin/true"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} STRIP="/bin/true"
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
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_libdir}/libdnssec.so.*

%files -n %{libknot}
%defattr(-,root,root)
%{_libdir}/libknot.so.*

%files -n %{libzscanner}
%defattr(-,root,root)
%{_libdir}/libzscanner.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/knot/
%{_libdir}/libdnssec.so
%{_libdir}/libknot.so
%{_libdir}/libzscanner.so
%{_libdir}/pkgconfig/knotd.pc
%{_libdir}/pkgconfig/libdnssec.pc
%{_libdir}/pkgconfig/libknot.pc
%{_libdir}/pkgconfig/libzscanner.pc

%changelog
