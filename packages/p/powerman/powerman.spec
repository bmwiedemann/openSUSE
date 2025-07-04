#
# spec file for package powerman
#
# Copyright (c) 2025 SUSE LLC
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


#
%define _with_snmppower 1
%define _with_tcp_wrappers 1
%undefine _with_genders

%if 0%{?suse_version} >= 1500
%define powerman_g %name
%define powerman_u %name
%define have_sysuser 1
%else
%define powerman_g daemon
%define powerman_u root
%endif

Name:           powerman
Version:        2.4.4
Release:        0
Summary:        Centralized Power Control for Clusters
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/chaos/powerman
Source:         https://github.com/chaos/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:         harden_powerman.service.patch
Patch2:         Replace-deprecated-usmHMACMD5AuthProtocol-Protocol-by-SNMP_DEFAULT_AUTH_PROTO.patch
Patch3:         httppower-redfishpower-Curl_easy_setopt-Expects-long-int.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
%{?have_sysuser:BuildRequires:  sysuser-tools}
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
%autosetup -p1

%build

# Use gnu17 on SLES16 and higher
%if 0%{?suse_version} >= 1600
%global optflags %{optflags} -std=gnu17
%endif

%configure \
	--disable-static\
	--with-httppower \
	--with-user=%{powerman_u} \
	--with-group=%{powerman_g} \
    --with-systemdsystemunitdir=%{_unitdir} \
%{?_with_snmppower:--with-snmppower} \
%{?_with_genders:--with-genders} \
%{?_with_tcp_wrappers:--with-tcp-wrappers} \

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%{__mkdir} -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %_rundir/powerman 0755 %{powerman_u} %{powerman_g} -
EOF
mv %{buildroot}%{_sysconfdir}/powerman/powerman.conf.example %{buildroot}%{_sysconfdir}/powerman/powerman.conf
rm -r %{buildroot}%{_libdir}/stonith
%if 0%{?have_sysuser}
echo "u %{powerman_u} - \"Power Manager service\" %_rundir/powerman" > system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf powerman system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
%endif

%fdupes -s  %{buildroot}

%pre %{?have_sysuser:-f %{name}.pre}
%service_add_pre %{name}.service

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
%doc DISCLAIMER NEWS.md
%license COPYING
%{_bindir}/*
%{_mandir}/man?/*.*
%exclude %{_mandir}/man3/*.*
%{_sbindir}/*
%config %{_sysconfdir}/powerman/
%attr(0644,root,root) %{_unitdir}/%{name}.service
%attr(0644,root,root) %{_tmpfilesdir}/powerman.conf
%ghost %{_rundir}/powerman
%{?have_sysuser:%{_sysusersdir}/system-user-%{name}.conf}

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
