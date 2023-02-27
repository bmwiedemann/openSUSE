#
# spec file for package stunnel
#
# Copyright (c) 2023 SUSE LLC
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
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           stunnel
Version:        5.68
Release:        0
Summary:        Universal TLS Tunnel
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.stunnel.org/
Source:         https://www.stunnel.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.stunnel.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        https://www.stunnel.org/pgp.asc#/%{name}.keyring
Source3:        sysconfig.syslog-stunnel
Source4:        stunnel.rc
Source7:        stunnel.README
# PATCH-FIX-UPSTREAM Fix service file, so it ensure we are starting after network is really up!
Patch1:         stunnel-5.59_service_always_after_network.patch
Patch2:         harden_stunnel.service.patch
BuildRequires:  libopenssl-devel
# test dependencies
BuildRequires:  netcat
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
#
Requires(pre):  %fillup_prereq
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  fileutils
Requires(pre):  textutils
Recommends:     stunnel-doc = %{version}
%{?systemd_ordering}
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
BuildArch:      noarch

%description doc
This package contains additional documentation for the stunnel program.

%prep
%setup -q -n stunnel-%{version}
%patch1 -p1
chmod -x %{_builddir}/stunnel-%{version}/tools/ca.*
chmod -x %{_builddir}/stunnel-%{version}/tools/importCA.*
%patch2 -p1

%build
sed -i 's/-m 1770//g' tools/Makefile.in
%configure \
	--disable-static \
	--bindir=%{_sbindir}
%make_build LDADD="-pie -Wl,-z,defs,-z,relro,-z,now"

%install
  %make_install

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/stunnel %{buildroot}%{_docdir}/
mkdir -p %{buildroot}%{_docdir}/stunnel/tools
mkdir -p %{buildroot}%{_fillupdir}
cp -p %{SOURCE3} %{buildroot}%{_fillupdir}/
install -D -m 0644 %{buildroot}%{_docdir}/stunnel/examples/stunnel.service %{buildroot}/%{_unitdir}/stunnel.service
ln -s service %{buildroot}%{_sbindir}/rcstunnel
sed -i "s/^;setuid = nobody/setuid = stunnel/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;setgid =/setgid =/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;include =/include =/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i '/gmail-pop3/,+25 s/^./;&/' %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/; Sample stunnel/# Sample stunnel/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
sed -i "s/^;/#/" %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample
mv %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf-sample %{buildroot}/%{_sysconfdir}/stunnel/stunnel.conf

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL.WCE.md
rm -rf %{buildroot}%{_docdir}/stunnel/INSTALL.W32.md
rm -rf %{buildroot}%{_docdir}/stunnel/ca-certs.pem
rm -rf %{buildroot}%{_docdir}/stunnel/plugins/

mkdir -p %{buildroot}%{_localstatedir}/lib/stunnel/{bin,etc,dev,%{_lib},sbin,var/run}
install -d %{buildroot}%{_sysconfdir}/%{name}/conf.d

%check
# only works in Tumbleweed as of 2021-04-08
%if 0%{?suse_version} > 1500
  rm tests/plugins/*fips*.py
  %make_build test
%endif

%pre
if ! %{_bindir}/getent passwd stunnel >/dev/null; then
   %{_sbindir}/useradd -r -c "Daemon user for stunnel (universal SSL tunnel)" -g nogroup -s /bin/false \
   -d %{_localstatedir}/lib/stunnel stunnel
fi

%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -ans syslog stunnel}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING.md
%{_sbindir}/rcstunnel
%{_sbindir}/stunnel
%{_sbindir}/stunnel3
%{_libdir}/%{name}/
%{_mandir}/man8/stunnel*8%{?ext_man}
%dir %attr(700,root,root) %{_sysconfdir}/%{name}/
%dir %attr(700,root,root) %{_sysconfdir}/%{name}//conf.d
%config(noreplace) %{_sysconfdir}/%{name}/stunnel.conf
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/bin
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel%{_sysconfdir}
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/dev
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/%{_lib}
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel/sbin
%dir %attr(755,root,root) %{_localstatedir}/lib/stunnel%{_localstatedir}
%dir %attr(755,stunnel,root) %{_localstatedir}/lib/stunnel%{_localstatedir}/run
%{_fillupdir}/sysconfig.syslog-stunnel
%{_unitdir}/stunnel.service

%files doc
%doc %{_docdir}/%{name}

%changelog
