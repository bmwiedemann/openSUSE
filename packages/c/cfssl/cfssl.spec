#
# spec file for package cfssl
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

%define configdir %{_sysconfdir}/cfssl
%define datadir   %{_localstatedir}/lib/cfssl
%define services cfssl-serve.service cfssl-ocspserve.service

Name:           cfssl
Version:        1.6.0
Release:        0
Summary:        CloudFlare's PKI/TLS toolkit
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://cfssl.org/
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-serve.service
Source2:        %{name}-ocspserve.service
Source3:        %{name}.sysconfig
Source4:        %{name}-serve
Source5:        %{name}-ocspserve
Source6:        configs.tar.xz
BuildRequires:  golang(API) >= 1.12
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
# There is a collision in /usr/bin/mkbundle
Conflicts:      mono-devel
Requires(pre):  %fillup_prereq
%systemd_ordering
%{go_nostrip}

%description
CFSSL is CloudFlare's PKI/TLS swiss army knife. It is both a command
line tool and an HTTP API server for signing, verifying, and bundling
TLS certificates. CFSSL consists of:

  * the cfssl program, which is the canonical command line utility
    using the CFSSL packages.
  * the multirootca program, which is a certificate authority server
    that can use multiple signing keys.
  * the mkbundle program for building certificate pool bundles.
  * the cfssljson program, which takes the JSON output from the cfssl
    and multirootca programs and writes certificates, keys, CSRs, and
    bundles to disk.

%prep
%autosetup -a 6

%build
sed --in-place "s/VERSION := .*/VERSION := %{version}/" Makefile
%ifnarch ppc64
sed --in-place --regexp-extended 's/LDFLAGS := "(.*)"/LDFLAGS := "\1 -buildmode=pie"/' Makefile
%endif
make

%install
for bin in %{name} %{name}-bundle %{name}-certinfo %{name}-newkey %{name}-scan %{name}json mkbundle multirootca; do
    install -D -m 0755 "bin/${bin}" "%{buildroot}/%{_bindir}/${bin}"
done
# Remove go.rice, as is a build requirement
rm bin/rice

install -m 0750 -d \
  %{buildroot}%{datadir} \
  %{buildroot}%{configdir} \
  %{buildroot}%{configdir}/certs \
  %{buildroot}%{configdir}/certs/ca \
  %{buildroot}%{configdir}/certs/users \
  %{buildroot}%{configdir}/certs/hosts \
  %{buildroot}%{configdir}/certs/intermediates \
  %{buildroot}%{_sbindir} \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_fillupdir}

install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-serve.service
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-ocspserve.service
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/%{name}-serve
install -m 0755 %{SOURCE5} %{buildroot}%{_sbindir}/%{name}-ocspserve

cp -av configs/* %{buildroot}%{configdir}/
chmod -R u=rwX,g=rX,o= %{buildroot}%{configdir}/

ln -sf /sbin/service %{buildroot}%{_sbindir}/rc%{name}-ocspserve
ln -sf /sbin/service %{buildroot}%{_sbindir}/rc%{name}-serve

rm -rv certdb/testdb/

%pre
getent group %{name} >/dev/null || \
	%{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -g %{name} -s /bin/false -r \
	-c "CloudFlare PKI/TLS toolkit" -d %{datadir} %{name}
%service_add_pre %{services}

%post
%fillup_only %{name}
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%config(noreplace) %attr(-,root,%{name}) %{configdir}
%dir %attr(-,%{name},%{name}) %{datadir}
%license LICENSE
%doc README.md configs/README.SUSE
%doc doc/
%doc certdb/
%{_bindir}/%{name}*
%{_bindir}/mkbundle
%{_bindir}/multirootca
%{_fillupdir}/sysconfig.%{name}
%{_unitdir}/%{name}*.service
%{_sbindir}/rc%{name}*
%{_sbindir}/%{name}*

%changelog
