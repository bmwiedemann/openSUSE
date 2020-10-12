#
# spec file for package stunnel
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


%define VENDORAFFIX openSUSE

%if 0%{?suse_version} >= 1210

%define has_systemd 1
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%else

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(pre):  %insserv_prereq
Requires(pre):  /usr/sbin/useradd
# %{_sbindir} does not work here!

%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           stunnel
Version:        5.57
Release:        0
Summary:        Universal TLS Tunnel
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Recommends:     stunnel-doc = %version
URL:            http://www.stunnel.org/
Source:         https://www.stunnel.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.stunnel.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        stunnel.keyring
Source3:        sysconfig.syslog-stunnel
Source4:        stunnel.rc
Source5:        stunnel.service
Source7:        stunnel.README
BuildRequires:  libopenssl-devel
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel
Requires(pre):         %fillup_prereq
Requires(pre):         %{_sbindir}/useradd
Requires(pre):         fileutils
Requires(pre):         textutils
%if 0%{?suse_version} >= 1500
Requires(pre):  group(nogroup)
%endif

%description
Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without
any changes in the programs' code. Its architecture is optimized for security, portability, and 
scalability (including load-balancing), making it suitable for large deployments.

%package doc
Summary:        Documentation for the universal TLS Tunnel
Group:          Documentation/Other
Requires:       stunnel = %{version}
%if 0%{?suse_version} >= 1210
BuildArch:      noarch
%endif

%description doc
This package contains additional documentation for the stunnel program.

%prep
%setup -q -n stunnel-%{version}
chmod -x %{_builddir}/stunnel-%{version}/tools/ca.*
chmod -x %{_builddir}/stunnel-%{version}/tools/importCA.*

%build
sed -i 's/-m 1770//g' tools/Makefile.in
%configure \
%if 0%{?suse_version} == 1110
	--disable-fips \
%endif
	--disable-static \
	--bindir=%{_sbindir}
make %{?_smp_mflags} LDADD="-pie -Wl,-z,defs,-z,relro,-z,now"

# connot do checks with 5.49, checks depend on ncat and network interaction
#%check
#make %{?_smp_mflags} check

%install
%if 0%{?suse_version} >= 1210
  %make_install
%else
  make install DESTDIR=$RPM_BUILD_ROOT
%endif

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/stunnel %{buildroot}%{_docdir}/
mkdir -p %{buildroot}%{_docdir}/stunnel/tools
mkdir -p %{buildroot}%{_fillupdir}
cp -p %{SOURCE3} %{buildroot}%{_fillupdir}/
%if 0%{?has_systemd}
install -D -m 0644 %{_sourcedir}/stunnel.service %{buildroot}/%{_unitdir}/stunnel.service
ln -s service %{buildroot}%{_sbindir}/rcstunnel
%else
mkdir -p %{buildroot}%{_initddir}/
install -m 744 %{_sourcedir}/stunnel.rc %{buildroot}/%{_initddir}/stunnel
ln -s ../..%{_initddir}/stunnel %{buildroot}%{_sbindir}/rcstunnel
%endif
sed -i "s/^;setuid = nobody/setuid = stunnel/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;setgid =/setgid =/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;include =/include =/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i '/gmail-pop3/,+25 s/^./;&/' %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/; Sample stunnel/# Sample stunnel/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;/#/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample 
mv %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL.WCE
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL.W32
rm -rf %{buildroot}%{_docdir}/stunnel/ca-certs.pem
rm -rf %{buildroot}%{_docdir}/stunnel/plugins/

mkdir -p %{buildroot}%{_localstatedir}/lib/stunnel/{bin,etc,dev,%{_lib},sbin,var/run}
install -d %{buildroot}%{_sysconfdir}/%{name}/conf.d

%pre
if ! %{_bindir}/getent passwd stunnel >/dev/null; then
   %{_sbindir}/useradd -r -c "Daemon user for stunnel (universal SSL tunnel)" -g nogroup -s /bin/false \
   -d %{_localstatedir}/lib/stunnel stunnel
fi

%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%post
%if 0%{?has_systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv -f}
%endif
%{fillup_only -ans syslog stunnel}

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal stunnel
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update stunnel
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_libdir}/%{name}/
%{_mandir}/man8/*
%dir %attr(700,root,root) %{_sysconfdir}/%{name}/
%dir %attr(700,root,root) %{_sysconfdir}/%{name}//conf.d
%config %{_sysconfdir}/%{name}/stunnel.conf
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/bin
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel%{_sysconfdir}
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/dev
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/%{_lib}
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/sbin
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel%{_localstatedir}
%dir %attr(755,stunnel,root) %{_localstatedir}/lib/stunnel%{_localstatedir}/run
%{_fillupdir}/sysconfig.syslog-stunnel
%if 0%{?has_systemd}
%{_unitdir}/stunnel.service
%else
%config %{_initddir}/*
%endif

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
