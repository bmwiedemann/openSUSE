#
# spec file for package powerman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define _with_snmppower 1
%define _with_tcp_wrappers 1
%undefine _with_genders

%if 0%{?suse_version} >= 1500
%define powerman_g %name
%define powerman_u %name
%else
%define powerman_g daemon
%define powerman_u root
%endif

Name:           powerman
Version:        2.3.24
Release:        0
Summary:        Centralized Power Control for Clusters
License:        GPL-2.0+
Group:          Productivity/Clustering/HA
Url:            https://github.com/chaos/powerman
Source0:        https://github.com/chaos/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch1:         service-dynamic-user-autofiles.patch
Patch2:         service-dynamic-user-configure.patch
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libcurl)
%if 0%{?_with_snmppower}
BuildRequires:  net-snmp-devel
%endif
%if 0%{?_with_genders}
BuildRequires:  genders
%endif
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

Requires(pre):  shadow

%description
PowerMan is a tool for manipulating remote power control (RPC) devices from a
central location. Several RPC varieties are supported natively by PowerMan and
Expect-like configurability simplifies the addition of new devices.

%package -n libpowerman0
Summary:        Libraries for applications using PowerMan
Group:          System/Libraries

%description -n libpowerman0
A shared library for applications using PowerMan.

%package devel
Summary:        Headers and libraries for developing applications using PowerMan
Group:          Development/Libraries/C and C++
Requires:       libpowerman0 = %{version}

%description devel
Header files, pkg-config file and man pages for developing applications using PowerMan.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure \
	--disable-static\
	--with-httppower \
	--with-user=%{powerman_u} \
	--with-group=%{powerman_g} \
%{?_with_snmppower:--with-snmppower} \
%{?_with_genders:--with-genders} \
%{?_with_tcp_wrappers:--with-tcp-wrappers} \

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%{__mkdir} -p %{buildroot}%{_tmpfilesdir}
cat >> %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d /var/run/powerman 0755 %{powerman_u} %{powerman_g} -
EOF
mv %{buildroot}%{_sysconfdir}/powerman/powerman.conf.example %{buildroot}%{_sysconfdir}/powerman/powerman.conf
rm -r %{buildroot}%{_libdir}/stonith
%fdupes -s  %{buildroot}

%pre
%service_add_pre %{name}.service
%define powerman_descr "Power Manager service"
getent group %powerman_g >/dev/null || groupadd -r %powerman_g
getent passwd %powerman_u >/dev/null || useradd -r -g %powerman_g -M -s /bin/false -c %powerman_descr %powerman_u
exit 0

%post
systemd-tmpfiles --create %{_tmpfilesdir}/powerman.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post -n libpowerman0 -p /sbin/ldconfig

%postun -n libpowerman0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS DISCLAIMER COPYING NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/*.*
%exclude %{_mandir}/man3/*.*
%{_sbindir}/*
%config %{_sysconfdir}/powerman/
%attr(0644,root,root) %{_unitdir}/%{name}.service
%{_tmpfilesdir}/powerman.conf

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.*

%files -n libpowerman0
%defattr(-,root,root)
%{_libdir}/*.so.*

%changelog
