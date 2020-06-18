#
# spec file for package bird
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


%define bird_user bird
%define bird_group bird
%define bird_home %{_localstatedir}/lib/bird
%define bird_runtimedir %{_rundir}/%{name}
Name:           bird
Version:        1.6.8
Release:        0
Summary:        The BIRD Internet Routing Daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Routing
URL:            https://bird.network.cz/
Source:         ftp://bird.network.cz/pub/bird/bird-%{version}.tar.gz
Source1:        bird.service
Source2:        bird6.service
Source3:        bird.tmpfiles.d
Patch0:         bird-1.6.3_verbose.build.patch
Patch1:         bufferoverflow.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(systemd)
Requires:       bird-common

%description
BIRD is an implementation for routing Internet Protocol packets. IPv4
and IPv6 are supported by running separate daemons. It establishes
multiple routing tables, and uses BGP, RIP, and OSPF routing
protocols, as well as statically defined routes.

This package holds the IPv4 binaries.

%package -n bird6
Summary:        The BIRD Internet Routing Daemon for IPv6
Group:          Productivity/Networking/Routing
Requires:       bird-common

%description -n bird6
BIRD is an implementation for routing Internet Protocol packets. IPv4
and IPv6 are supported by running separate daemons. It establishes
multiple routing tables, and uses BGP, RIP, and OSPF routing
protocols, as well as statically defined routes.

This package holds the IPv6 binaries.

%package common
Summary:        Common files for the BIRD Internet Routing Daemon
Group:          Productivity/Networking/Routing
Requires(pre):  shadow
%{?systemd_requires}

%description common
BIRD is an implementation for routing Internet Protocol packets.

This package holds common files and directories.

%package doc
Summary:        Documentation for the BIRD Internet Routing Daemon
Group:          Documentation/HTML

%description doc
BIRD is an implementation for routing Internet Protocol packets.

This package holds the HTML documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# gcc detects overflow in strncpy at proto/rip/packets.c:215:5
# but it's false alarm, relax gcc (-D_FORTIFY_SOURCE=1)
# see http://bird.network.cz/pipermail/bird-users/2016-May/010380.html
export CFLAGS="${RPM_OPT_FLAGS//-D_FORTIFY_SOURCE=2/-D_FORTIFY_SOURCE=0} -fpic -DPIC -fno-strict-aliasing -Wno-parentheses -Wno-pointer-sign -fcommon"
export LDFLAGS="-Wl,-z,relro -pie"
%define _configure ../configure
mkdir 4 6
pushd 4
%configure \
	--with-runtimedir=%{bird_runtimedir}
make %{?_smp_mflags}
popd
pushd 6
%configure --enable-ipv6 \
	--with-runtimedir=%{bird_runtimedir}
make %{?_smp_mflags}
popd

%install
%make_install -C 4
%make_install -C 6

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/bird.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/bird6.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcbird
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcbird6
install -D -d -m 0750 %{buildroot}%{bird_home}
install -D -d -m 0750 %{buildroot}%{_docdir}/%{name}/
cp -av NEWS README doc/bird*.html %{buildroot}%{_docdir}/%{name}/

%pre common
# Create bird user/group
getent group %{bird_group} >/dev/null || groupadd -r %{bird_group}
getent passwd %{bird_user} >/dev/null || useradd -r -g %{bird_group} -d %{bird_home} -s /sbin/nologin -c "Bird routing daemon" %{bird_user}
exit 0

%post common
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || true

%pre
%service_add_pre bird.service

%pre -n bird6
%service_add_pre bird6.service

%preun
%service_del_preun bird.service

%preun -n bird6
%service_del_preun bird6.service

%post
%service_add_post bird.service

%post -n bird6
%service_add_post bird6.service

%postun
%service_del_postun bird.service

%postun -n bird6
%service_del_postun bird6.service

%files
%config(noreplace) %attr(0640,root,%{bird_group}) %{_sysconfdir}/bird.conf
%{_sbindir}/bird
%{_sbindir}/birdc
%{_sbindir}/birdcl
%{_sbindir}/rcbird
%{_unitdir}/bird.service

%files -n bird6
%config(noreplace) %attr(0640,root,%{bird_group}) %{_sysconfdir}/bird6.conf
%{_sbindir}/bird6
%{_sbindir}/birdc6
%{_sbindir}/birdcl6
%{_sbindir}/rcbird6
%{_unitdir}/bird6.service

%files common
%dir %attr(750,%{bird_user},%{bird_group}) %{bird_home}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(-,%{bird_user},%{bird_group}) %ghost %{bird_runtimedir}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/NEWS

%files doc
%doc %{_docdir}/%{name}/bird*.html

%changelog
