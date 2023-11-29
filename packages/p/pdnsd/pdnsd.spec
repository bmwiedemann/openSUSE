#
# spec file for package pdnsd
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


%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif
%endif

Name:           pdnsd

%define _cache_dir  %{_localstatedir}/cache/%{name}
%define _cache_file %{_cache_dir}/%{name}.cache

Version:        1.2.9a
Release:        0
Summary:        A caching DNS proxy for small networks or dialin accounts
License:        GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Servers
URL:            http://members.home.nl/p.a.rombouts/pdnsd.html

#Source0:        http://members.home.nl/p.a.rombouts/pdnsd/releases/pdnsd-1.2.9a-par.tar.gz
Source0:        %{name}-%{version}-par.tar.gz
Source1:        %{name}.sysconfig
Source2:        %{name}.service.in
# PATCH-FIX-OPENSUSE -- fix UDP response packet for large responses being incorrectly truncated -- seife@novell.slipkontur.de
Patch0:         %{name}-fix-udppacketsize.diff
# borrowed from debian's 1.2.9a-par-3 release
Patch1:         %{name}-06_reproducible_build.patch
# PATCH-FIX-OPENSUSE -- compile fix with newer glibc(?)/kernel-headers(?) where ordering matters -- seife+obs@b1-systems.com
Patch2:         %{name}-net_if_h-vs-linux_if_h.patch
# without this, --with-query-method=udptcp is ignored and "-muo" is default
# PATCH-FIX-OPENSUSE -- make compile-time preset selection work -- seife+obs@b1-systems.com
Patch3:         %{name}-fix-preproc-errors.patch
# PATCH-FIX-OPENSUSE -- the default nodaemon option adds a useless timestamp, remove that -- seife+obs@b1-systems.com
Patch4:         %{name}-nodaemon-logfix.patch
# PATCH-FIX-OPENSUSE -- cleanup default config
Patch100:       %{name}_conf.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros
Recommends:     %{name}-doc
%{?systemd_ordering}

%description
pdnsd is a proxy DNS daemon with permanent (disk-)cache and the ability
to serve local records. It is designed to detect network outages or hangups
and to prevent DNS-dependent applications like Netscape Navigator from hanging.

The original author of pdnsd is Thomas Moestl, but pdnsd is no longer maintained
by him. This is an extensively revised version by Paul A. Rombouts.
For a description of the changes see http://www.phys.uu.nl/~rombouts/pdnsd.html
and the file README.par in %{_docdir}/%{name}-doc.

%package doc
Summary:        Docs for pdnsd
Group:          Productivity/Networking/DNS/Servers
BuildArch:      noarch
Requires:       %{name}

%description doc
This package provides various text files for pdnsd

%prep
%setup -q
%autopatch -p1

%build
%configure \
  --enable-ipv6 \
  --enable-specbuild \
  --with-cachedir="%{_cache_dir}" \
  --with-default-id=pdns \
  --with-query-method=udptcp \
  --with-par-queries=3

make %{?_smp_mflags}

%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
# sles12 does not know the hardening stuff...
sed '/^# BEGIN_NOT_IN_SLES12/,/^# END_NOT_IN_SLES12/d' %{S:2} > %{name}.service
%else
sed '/^# BEGIN_NOT_IN_SLES12/d;/^# END_NOT_IN_SLES12/d' %{S:2} > %{name}.service
%endif
touch -r %{S:2} %{name}.service

%install
%make_install
install -D -m 0644 %{S:1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
cp -a %{buildroot}%{_sysconfdir}/%{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}.conf
install -d -m 0755 %{buildroot}/%{_docdir}/%{name}
mv %{buildroot}%{_sysconfdir}/%{name}.conf.sample .
install -D -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
# add group
%{_sbindir}/groupadd -r pdns 2>/dev/null || :
# add user
%{_sbindir}/useradd -c "DNS proxy account" -d %{_cache_dir} -G pdns -g pdns \
  -r -s /sbin/nologin pdns 2>/dev/null || :
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n pdnsd}

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%config(noreplace) %attr(0640,root,pdns) %{_sysconfdir}/%{name}.conf
%{_sbindir}/*%{name}*
%{_mandir}/man*/%{name}*
%dir %attr(0750,pdns,root) %{_cache_dir}
%ghost %attr(0600,pdns,root) %{_cache_file}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%license COPYING*
%doc %{name}.conf.sample

%files doc
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO

%changelog
