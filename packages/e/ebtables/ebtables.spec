#
# spec file for package ebtables
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.0.10.4
Release:        0
Summary:        Ethernet Bridge Tables
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            http://ebtables.sf.net/
#Git-Clone:	git://git.netfilter.org/ebtables
Source:         ebtables-v2.0.10-4.tar.xz
Source1:        ebtables.service
Source2:        ebtables.systemd
Patch0:         ebtables-v2.0.8-makefile.diff
Patch1:         ebtables-v2.0.8-initscript.diff
# PATCH-FIX-UPSTREAM bnc#934680 kstreitova@suse.com -- audit patch for CC certification
Patch2:         ebtables-v2.0.10-4-audit.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-fix-compilation-warning.patch
# PATCH-FIX-SUSE-ONLY
Patch4:         include-linux-if.patch
# PATCH-FIX-UPSTREAM boo#1126094
Patch5:         0001-Use-flock-for-concurrent-option.patch
Patch6:         0002-Fix-locking-if-LOCKDIR-does-not-exist.patch
BuildRequires:  linux-glibc-devel >= 2.6.20
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       netcfg >= 11.6
Requires(pre):  %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): update-alternatives
Requires(postun): update-alternatives
%{?systemd_requires}

%description
A firewalling tool to transparently filter network traffic passing a
bridge. The filtering possibilities are limited to link layer filtering
and some basic filtering on higher network layers. The ebtables tool
can be used together with the other Linux filtering tools, like
iptables. There are no incompatibility issues.

%prep
%setup -q -n %{name}-v2.0.10-4
%patch -P 0 -P 1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
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
make \
    CFLAGS="%{optflags}" \
    CXXFLAGS="%{optflags}" \
    LIBDIR="%{_libdir}/%{name}" \
    MANDIR="%{_mandir}" \
    BINDIR="%{_sbindir}" \
    ETCDIR="%{_sysconfdir}" \
    INITDIR="%{_sysconfdir}/init.d" \
    SYSCONFIGDIR="%{_sysconfdir}"

%install
# The way ebtables is built requires ASNEEDED=0 forever [bnc#567267]
export SUSE_ASNEEDED=0
mkdir -p "%{buildroot}/%{_sysconfdir}/init.d"
make \
    DESTDIR=%{buildroot} \
    LIBDIR="%{_libdir}/%{name}" \
    MANDIR="%{_mandir}" \
    BINDIR="%{_sbindir}" \
    ETCDIR="%{_sysconfdir}" \
    INITDIR="%{_sysconfdir}/init.d" \
    SYSCONFIGDIR="%{_sysconfdir}" \
    install
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_unitdir}
install -p %{SOURCE1} %{buildroot}%{_unitdir}/
chmod -x %{buildroot}%{_unitdir}/*.service
mkdir -p %{buildroot}%{_libexecdir}
install -m0755 %{SOURCE2} %{buildroot}%{_libexecdir}/ebtables
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.filter
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.nat
touch %{buildroot}%{_fillupdir}/sysconfig.%{name}.broute
rm -rf %{buildroot}%{_initrddir}
# not used
rm -f "%{buildroot}/%{_sysconfdir}/ebtables-config"
mv "%{buildroot}/%{_sbindir}/ebtables" "%{buildroot}/%{_sbindir}/ebtables-legacy"
mv "%{buildroot}/%{_sbindir}/ebtables-restore" "%{buildroot}/%{_sbindir}/ebtables-legacy-restore"
mv "%{buildroot}/%{_sbindir}/ebtables-save" "%{buildroot}/%{_sbindir}/ebtables-legacy-save"
for i in ebtables ebtables-restore ebtables-save; do
	ln -fsv "/etc/alternatives/$i" "%{buildroot}/%{_sbindir}/$i"
done

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

%files
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_mandir}/man8/ebtables.8*
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/alternatives/ebtables
%ghost %{_sysconfdir}/alternatives/ebtables-restore
%ghost %{_sysconfdir}/alternatives/ebtables-save
%ghost %{_fillupdir}/sysconfig.%{name}.filter
%ghost %{_fillupdir}/sysconfig.%{name}.nat
%ghost %{_fillupdir}/sysconfig.%{name}.broute
# is provided by the netcfg package
%exclude %{_sysconfdir}/ethertypes
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_sbindir}/ebtables*
%{_sbindir}/rcebtables

%changelog
