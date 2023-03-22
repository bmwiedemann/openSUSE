#
# spec file for package dnsdist
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


%if 0%{?suse_version}
%bcond_without  apparmor
%else
%bcond_with     apparmor
%endif
#
# this should only be needed if we have to patch the ragel files
# in which case it might be faster to just run it locally and put the regenerated file into the tarball
%bcond_with     dnsdist_ragel

# requires h2o http server
%bcond_with  dnsdist_doh

%if 0%{?%is_backports} || 0%{?suse_version} >= 1599
%bcond_without  dnsdist_re2
%else
%bcond_with     dnsdist_re2
%endif

%define file_version 1.8.0-rc3

Name:           dnsdist
Version:        1.8.0~rc3
Release:        0
License:        GPL-2.0-only
Summary:        A highly DNS-, DoS- and abuse-aware loadbalancer
URL:            http://www.powerdns.com/
Group:          Productivity/Networking/DNS/Servers
Source0:        https://downloads.powerdns.com/releases/dnsdist-%{file_version}.tar.bz2
Source1:        https://downloads.powerdns.com/releases/dnsdist-%{file_version}.tar.bz2.sig
Source2:        https://dnsdist.org/_static/dnsdist-keyblock.asc#/dnsdist.keyring
Source10:       dnsdist.user
Source11:       dnsdist.lua
Source12:       usr.sbin.dnsdist
Source13:       local.usr.sbin.dnsdist
%if %{with apparmor}
BuildRequires:  apparmor-profiles
%endif
%if %{with dnsdist_ragel}
BuildRequires:  ragel
%endif
%if %{with dnsdist_re2}
BuildRequires:  re2-devel
%endif
%if %{with dnsdist_doh}
BuildRequires:  pkgconfig(libh2o-evloop)
%endif
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libedit-devel
BuildRequires:  libfstrm-devel
BuildRequires:  libsodium-devel
BuildRequires:  lmdb-devel
BuildRequires:  luajit-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libsystemd)
%{systemd_ordering}
%{sysusers_requires}

%define home           %{_var}/lib/%{name}

%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.

dnsdist is dynamic, in the sense that its configuration can be changed at
runtime, and that its statistics can be queried from a console-like interface.

%prep
%autosetup -p1 -n %name-%file_version

%build
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%ifarch %arm %ix86
export CFLAGS="$CFLAGS -D__USE_TIME_BITS64"
%endif
export CXXFLAGS="$CFLAGS"

%configure \
  --enable-dnstap \
  --enable-dns-over-tls \
  --enable-systemd \
  --enable-lto \
  --enable-dnscrypt \
%if %{with dnsdist_doh}
  --enable-dns-over-https \
%endif
%if %{with dnsdist_re2}
  --with-re2 \
%endif
  --with-ebpf \
  --with-net-snmp \
  --with-libcap \
  --with-lua=luajit \
  --with-lmdb \
  --disable-silent-rules \
  --bindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir}/%{name}/

make %{?_smp_mflags}
%sysusers_generate_pre %{SOURCE10} %{name}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
#
%if 0%{?suse_version}
  ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
%if %{with apparmor}
install -D -m 0644 %{S:12} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.dnsdist
install -D -m 0644 %{S:13} %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.dnsdist
%endif

install -Dd -m 0750    %{buildroot}%{_sysconfdir}/%{name}/ %{buildroot}%{home}/
install -m 0640 %{S:11} %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf

%pre -f %{name}.pre
%service_add_pre %{name}.service %{name}@.service

%preun
%service_del_preun %{name}.service %{name}@.service

%post
%service_add_post %{name}.service %{name}@.service

%postun
%service_del_postun %{name}.service %{name}@.service

%files
%doc README.md
%{_sbindir}/dnsdist
%{_mandir}/man1/dnsdist.1*
%{_unitdir}/%{name}*.service
%if 0%{?suse_version}
%{_sbindir}/rc%{name}
%endif
%if %{with apparmor}
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.dnsdist
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.sbin.dnsdist
%endif
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/%{name}/
%dir %attr(700,%{name},%{name}) %{home}

%changelog
