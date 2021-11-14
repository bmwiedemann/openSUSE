#
# spec file for package ebtables
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           ebtables
Version:        2.0.11
Release:        0
Summary:        Ethernet Bridge Tables
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://ebtables.sf.net/
#Git-Clone:	git://git.netfilter.org/ebtables
Source0:        http://ftp.netfilter.org/pub/ebtables/ebtables-%{version}.tar.gz
Source1:        http://ftp.netfilter.org/pub/ebtables/ebtables-%{version}.tar.gz.sig
Source2:        ebtables.keyring
Source3:        ebtables.service
Source4:        ebtables.systemd
BuildRequires:  linux-glibc-devel >= 2.6.20
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       netcfg >= 11.6
Requires(pre):  %fillup_prereq
%{?systemd_ordering}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif

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
%make_build

%install
# The way ebtables is built requires ASNEEDED=0 forever [bnc#567267]
export SUSE_ASNEEDED=0
mkdir -p "%{buildroot}/%{_sysconfdir}/init.d"
%make_install
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_unitdir}
install -p %{_sourcedir}/ebtables.service %{buildroot}%{_unitdir}/
sed -i "s|@LIBEXECDIR@|%{_libexecdir}|g" %{buildroot}%{_unitdir}/*.service
chmod -x %{buildroot}%{_unitdir}/*.service
mkdir -p %{buildroot}%{_libexecdir}
install -m0755 %{_sourcedir}/ebtables.systemd %{buildroot}%{_libexecdir}/%{name}-helper
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.filter
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.nat
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.broute
rm -rfv %{buildroot}%{_initddir}
# not used
rm -f "%{buildroot}/%{_sysconfdir}/ebtables-config"
for i in ebtables ebtables-restore ebtables-save; do
%if ! %{with libalternatives}
        ln -fsv "%{_sysconfdir}/alternatives/$i" "%{buildroot}/%{_sbindir}/$i"
%else
        ln -fsv  %{_bindir}/alts "%{buildroot}/%{_sbindir}/$i"
%endif
done
echo ".so ebtables-legacy.8" >"%{buildroot}/%{_mandir}/man8/ebtables.8"
# no headers to make use of it
rm -f "%{buildroot}/%{_libdir}/libebtc.la" "%{buildroot}/%{_libdir}/libebtc.so"

%if %{with libalternatives}
mkdir -p %{buildroot}%{_datadir}/libalternatives/ebtables
cat > %{buildroot}%{_datadir}/libalternatives/ebtables/1.conf <<EOF
binary=%{_sbindir}/ebtables-legacy
group=ebtables, ebtables-restore, ebtables-save
EOF
mkdir -p %{buildroot}%{_datadir}/libalternatives/ebtables-restore
cat > %{buildroot}%{_datadir}/libalternatives/ebtables-restore/1.conf <<EOF
binary=%{_sbindir}/ebtables-legacy-restore
group=ebtables, ebtables-restore, ebtables-save
EOF
mkdir -p %{buildroot}%{_datadir}/libalternatives/ebtables-save
cat > %{buildroot}%{_datadir}/libalternatives/ebtables-save/1.conf <<EOF
binary=%{_sbindir}/ebtables-legacy-save
group=ebtables, ebtables-restore, ebtables-save
EOF
%endif

%pre
%if %{with libalternatives}
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
         update-alternatives --remove ebtables "%{_sbindir}/ebtables-legacy"
fi
%endif
%service_add_pre %{name}.service

%post
%if ! %{with libalternatives}
update-alternatives --force \
	--install "%{_sbindir}/ebtables" ebtables "%{_sbindir}/ebtables-legacy" 1 \
	--slave "%{_sbindir}/ebtables-restore" ebtables-restore "%{_sbindir}/ebtables-legacy-restore" \
	--slave "%{_sbindir}/ebtables-save" ebtables-save "%{_sbindir}/ebtables-legacy-save"
%endif
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%if ! %{with libalternatives}
if test "$1" = 0; then
	update-alternatives --remove ebtables "%{_sbindir}/ebtables-legacy"
fi
%endif
%service_del_postun %{name}.service

%post   -n libebtc0 -p /sbin/ldconfig
%postun -n libebtc0 -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog
%{_mandir}/man8/ebtables*.8%{?ext_man}
%{_libexecdir}/%{name}-helper
%{_unitdir}/%{name}.service
%if ! %{with libalternatives}
%ghost %{_sysconfdir}/alternatives/ebtables
%ghost %{_sysconfdir}/alternatives/ebtables-restore
%ghost %{_sysconfdir}/alternatives/ebtables-save
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/ebtables
%dir %{_datadir}/libalternatives/ebtables-restore
%dir %{_datadir}/libalternatives/ebtables-save
%{_datadir}/libalternatives/ebtables/1.conf
%{_datadir}/libalternatives/ebtables-restore/1.conf
%{_datadir}/libalternatives/ebtables-save/1.conf
%endif
%ghost %{_fillupdir}/sysconfig.%{name}.filter
%ghost %{_fillupdir}/sysconfig.%{name}.nat
%ghost %{_fillupdir}/sysconfig.%{name}.broute
# is provided by the netcfg package
%exclude %{_sysconfdir}/ethertypes
%{_sbindir}/ebtables*
%{_sbindir}/rcebtables

%files -n libebtc0
%{_libdir}/libebtc.so.0*

%changelog
