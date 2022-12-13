#
# spec file for package bird
#
# Copyright (c) 2022 SUSE LLC
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


%define bird_user bird
%define bird_group bird
%define bird_home %{_localstatedir}/lib/bird
%define bird_runtimedir %{_rundir}/%{name}
Name:           bird
Version:        2.0.11
Release:        0
Summary:        The BIRD Internet Routing Daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Routing
URL:            https://bird.network.cz/
Source:         ftp://bird.network.cz/pub/bird/bird-%{version}.tar.gz
Source1:        bird.service
Source3:        bird.tmpfiles.d
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(systemd)
Provides:       bird6 = %{version}
Provides:       bird6:%{_sbindir}/bird6
Obsoletes:      bird6 < %{version}
Provides:       bird-common = %{version}
Obsoletes:      bird-common < %{version}

%description
BIRD is an implementation for routing Internet Protocol packets. IPv4
and IPv6 are supported by running separate daemons. It establishes
multiple routing tables, and uses BGP, RIP, and OSPF routing
protocols, as well as statically defined routes.

This package holds the IPv4+IPv6 binaries.

This package holds common files and directories.

%package doc
Summary:        Documentation for the BIRD Internet Routing Daemon
Group:          Documentation/HTML
BuildRequires:  perl-FindBin-Real

%description doc
BIRD is an implementation for routing Internet Protocol packets.

This package holds the HTML documentation.

%prep
%setup -q

%build
export CFLAGS="${RPM_OPT_FLAGS} -fpic -DPIC -fno-strict-aliasing -Wno-parentheses -Wno-pointer-sign"
export LDFLAGS="-Wl,-z,relro -pie"
%configure \
	--with-runtimedir=%{bird_runtimedir}
%make_build all
# requires linuxdoctools
# make docs

%install
%make_install

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/bird.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcbird
install -D -d -m 0750 %{buildroot}%{bird_home}
install -D -d -m 0750 %{buildroot}%{_docdir}/%{name}/

%check
make test

%pre
# Create bird user/group
getent group %{bird_group} >/dev/null || groupadd -r %{bird_group}
getent passwd %{bird_user} >/dev/null || useradd -r -g %{bird_group} -d %{bird_home} -s /sbin/nologin -c "Bird routing daemon" %{bird_user}
%service_add_pre bird.service

%preun
%service_del_preun bird.service

%post
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || true
%service_add_post bird.service

%postun
%service_del_postun bird.service

%files
%config(noreplace) %attr(0640,root,%{bird_group}) %{_sysconfdir}/bird.conf
%{_sbindir}/bird
%{_sbindir}/birdc
%{_sbindir}/birdcl
%{_sbindir}/rcbird
%{_unitdir}/bird.service
%dir %attr(750,%{bird_user},%{bird_group}) %{bird_home}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(-,%{bird_user},%{bird_group}) %ghost %{bird_runtimedir}

%files doc
%doc NEWS README
%doc doc/bird.conf.*

%changelog
