#
# spec file for package knot
#
# Copyright (c) 2024 SUSE LLC
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


%define libdnssec   libdnssec9
%define libknot     libknot14
%define libzscanner libzscanner4
%define pkg_name knot
%bcond_without  dnstap
%bcond_without  lto
%bcond_without systemd
%if 0%{?is_opensuse}
%bcond_without maxminddb
%else
%bcond_with    maxminddb
%endif
%bcond_without docs
%if %{with systemd}
%define has_systemd 1
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_requires}
%endif
Name:           knot
Version:        3.3.6
Release:        0
Summary:        An authoritative DNS daemon
License:        GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.knot-dns.cz/
Source0:        https://secure.nic.cz/files/knot-dns/%{pkg_name}-%{version}.tar.xz
Source2:        knot-tmp.conf
Source3:        https://secure.nic.cz/files/knot-dns/%{pkg_name}-%{version}.tar.xz.asc
Source4:        system-user-knot.conf
Source99:       knot.keyring
BuildRequires:  libcap-ng-devel
BuildRequires:  libedit-devel
BuildRequires:  liburcu-devel
BuildRequires:  lmdb-devel >= 0.9.15
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(gnutls) >= 3.3
BuildRequires:  pkgconfig(nettle)
Obsoletes:      knot2 < %{version}
%sysusers_requires
%if 0%{?suse_version} > 1320 || 0%{?leap_version} == 420300
BuildRequires:  libidn2-devel
%else
BuildRequires:  libidn-devel
%endif
%if %{with maxminddb}
BuildRequires:  pkgconfig(libmaxminddb)
%endif
%if %{with docs}
BuildRequires:  makeinfo
BuildRequires:  python3-Sphinx
%endif
%if %{with dnstap}
BuildRequires:  libfstrm-devel
BuildRequires:  libprotobuf-c-devel >= 1.0.0
%endif

%description
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

%package devel
#
Summary:        Development files for the knot libraries
Group:          Development/Libraries/C and C++
Requires:       %{libdnssec} = %{version}
Requires:       %{libknot} = %{version}
Requires:       %{libzscanner} = %{version}
Requires:       knot = %{version}

%description devel
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains headers for knot.

%package -n %{libdnssec}
#
Summary:        DNSSEC support functions for Knot DNS
Group:          System/Libraries

%description -n %{libdnssec}
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains a library for DNSSEC support functions.

%package -n %{libknot}
#
Summary:        Knot DNS support library
Group:          System/Libraries

%description -n %{libknot}
Knot DNS is a DNS server. It implements only the authoritative domain
name service. It uses a multi-threaded and mostly lock-free
implementation and can operate non-stop during zone addition or
removal.

This package contains the essential core library for Knot services.

%package -n %{libzscanner}
#
Summary:        Zone record parsing functions for Knot DNS
Group:          System/Libraries

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
  --with-bash-completions=%{_sysconfdir}/bash_completion.d \
  --disable-silent-rules
%make_build STRIP="/bin/true"
%sysusers_generate_pre %{SOURCE4} knot system-user-knot.conf

%install
%make_install STRIP="/bin/true"
find %{buildroot}
install -d %{buildroot}%{_docdir}/%{pkg_name}
install -d %{buildroot}%{_docdir}/%{pkg_name}/samples/
rm %{buildroot}%{_sysconfdir}/%{pkg_name}/*
install -p -m644 samples/knot.sample.conf %{buildroot}%{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%if %{with systemd}
install -d %{buildroot}%{_unitdir} %{buildroot}%{_tmpfilesdir}
install -p -m644 distro/common/knot.service %{buildroot}%{_unitdir}/%{pkg_name}.service
install -p -m644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/knot.conf
ln -s service %{buildroot}%{_sbindir}/rcknot
%endif
install -p -m644 COPYING NEWS README.md %{buildroot}%{_docdir}/%{pkg_name}
install -p -m644 samples/*.conf samples/*.zone* %{buildroot}%{_docdir}/%{pkg_name}/samples/
find %{buildroot} -type f -name "*.la" -delete -print
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/knot/
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/

%pre -f knot.pre
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
%dir %attr(750,knot,knot) %{_sysconfdir}/%{pkg_name}
%config(noreplace) %attr(640,knot,knot) %{_sysconfdir}/%{pkg_name}/%{pkg_name}.conf
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man?/*
%doc %{_docdir}/%{pkg_name}
%if %{with systemd}
%{_unitdir}/%{pkg_name}.service
%{_tmpfilesdir}/knot.conf
%{_sysusersdir}/system-user-knot.conf
%endif
%{_libdir}/knot/
%dir %attr(-,knot,knot) %{_localstatedir}/lib/knot/
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
