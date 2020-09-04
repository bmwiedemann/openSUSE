#
# spec file for package ebtables
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           ebtables
Version:        2.0.11
Release:        0
Summary:        Ethernet Bridge Tables
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://ebtables.sf.net/
#Git-Clone:	git://git.netfilter.org/ebtables
Source0:        http://ftp.netfilter.org/pub/ebtables/ebtables-%version.tar.gz
Source1:        http://ftp.netfilter.org/pub/ebtables/ebtables-%version.tar.gz.sig
Source2:        ebtables.keyring
Source3:        ebtables.service
Source4:        ebtables.systemd
BuildRequires:  linux-glibc-devel >= 2.6.20
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       netcfg >= 11.6
Requires(pre):  %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): update-alternatives
Requires(postun): update-alternatives
%{?systemd_ordering}

%description
A firewalling tool to transparently filter network traffic passing a
bridge. The filtering possibilities are limited to link layer filtering
and some basic filtering on higher network layers. The ebtables tool
can be used together with the other Linux filtering tools, like
iptables. There are no incompatibility issues.

%package -n libebtc0
Summary:        Library for the ebtables low-level ruleset generation and parsing
Group:          System/Libraries

%description -n libebtc0
libebtc ("ebtables cache") is used to retrieve from the kernel, parse,
construct, and load rulesets into the kernel.

%prep
%autosetup -p1

# delete all kernel headers, but keep ebt_ip6.h and ebt_nflog.h
mv include/linux/netfilter_bridge/ebt_ip6.{h,h.save}
mv include/linux/netfilter_bridge/ebt_nflog.{h,h.save}
mv include/linux/netfilter_bridge/ebt_ulog.{h,h.save}
rm -f include/linux/*.h
rm -f include/linux/netfilter_bridge/*.h
mv include/linux/netfilter_bridge/ebt_ip6.{h.save,h}
mv include/linux/netfilter_bridge/ebt_nflog.{h.save,h}
mv include/linux/netfilter_bridge/ebt_ulog.{h.save,h}

%build
# The way ebtables is built requires ASNEEDED=0 forever [bnc#567267]
export SUSE_ASNEEDED=0
%configure
make %{?_smp_mflags}

%install
# The way ebtables is built requires ASNEEDED=0 forever [bnc#567267]
export SUSE_ASNEEDED=0
mkdir -p "%{buildroot}/%{_sysconfdir}/init.d"
%make_install
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_unitdir}
install -p %_sourcedir/ebtables.service %{buildroot}%{_unitdir}/
sed -i "s|@LIBEXECDIR@|%{_libexecdir}|g" %{buildroot}%{_unitdir}/*.service
chmod -x %{buildroot}%{_unitdir}/*.service
mkdir -p %{buildroot}%{_libexecdir}
install -m0755 %_sourcedir/ebtables.systemd %{buildroot}%{_libexecdir}/%{name}-helper
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.filter
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.nat
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.broute
rm -rfv %{buildroot}%{_initrddir}
# not used
rm -f "%{buildroot}/%{_sysconfdir}/ebtables-config"
for i in ebtables ebtables-restore ebtables-save; do
	ln -fsv "/etc/alternatives/$i" "%{buildroot}/%{_sbindir}/$i"
done
echo ".so ebtables-legacy.8" >"%buildroot/%_mandir/man8/ebtables.8"
# no headers to make use of it
rm -f "%buildroot/%_libdir/libebtc.la" "%buildroot/%_libdir/libebtc.so"

%pre
%service_add_pre %{name}.service

%post
update-alternatives --force \
	--install "%{_sbindir}/ebtables" ebtables "%{_sbindir}/ebtables-legacy" 1 \
	--slave "%{_sbindir}/ebtables-restore" ebtables-restore "%{_sbindir}/ebtables-legacy-restore" \
	--slave "%{_sbindir}/ebtables-save" ebtables-save "%{_sbindir}/ebtables-legacy-save"
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
if test "$1" = 0; then
	update-alternatives --remove ebtables "%{_sbindir}/ebtables-legacy"
fi
%service_del_postun %{name}.service

%post   -n libebtc0 -p /sbin/ldconfig
%postun -n libebtc0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog
%{_mandir}/man8/ebtables*.8*
%{_libexecdir}/%{name}-helper
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/alternatives/ebtables
%ghost %{_sysconfdir}/alternatives/ebtables-restore
%ghost %{_sysconfdir}/alternatives/ebtables-save
%ghost %{_fillupdir}/sysconfig.%{name}.filter
%ghost %{_fillupdir}/sysconfig.%{name}.nat
%ghost %{_fillupdir}/sysconfig.%{name}.broute
# is provided by the netcfg package
%exclude %{_sysconfdir}/ethertypes
%{_sbindir}/ebtables*
%{_sbindir}/rcebtables

%files -n libebtc0
%_libdir/libebtc.so.0*

%changelog
