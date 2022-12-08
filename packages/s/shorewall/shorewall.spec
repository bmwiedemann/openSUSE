#
# spec file for package shorewall
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


%define have_systemd 1
%define dmaj 5.2
%define dmin 5.2.8
# Warn users for upgrading configuration but only on major or minor version changes
%define conf_need_update 0
#2017+ New fillup location
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%{!?_distconfdir: %global _distconfdir %{_prefix}%{_sysconfdir}}
Name:           shorewall
Version:        5.2.8
Release:        0
Summary:        An iptables-based firewall for Linux systems
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            http://www.shorewall.net/
Source:         http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}-%version.tar.bz2
Source1:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}-core-%version.tar.bz2
Source2:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}-lite-%version.tar.bz2
Source3:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}-init-%version.tar.bz2
Source4:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}6-lite-%version.tar.bz2
Source5:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}6-%version.tar.bz2
Source6:        http://www.shorewall.net/pub/shorewall/%{dmaj}/shorewall-%{dmin}/%{name}-docs-html-%version.tar.bz2
Source7:        %{name}-5.2.rpmlintrc
Source8:        README.openSUSE
# PATCH-FIX-OPENSUSE Shorewall-init use of fillup template
Patch1:         shorewall-init-fillup-install.patch
# PATCH-FIX-OPENSUSE Shorewall (6) use of fillup template
Patch2:         shorewall-fillup-install.patch
# PATCH-FIX-OPENSUSE Shorewall-lite (6) use of fillup template
Patch3:         shorewall-lite-fillup-install.patch
# PATH-FIX-OPENSUSE invalid manpage boo#1203006
Patch4:         shorewall-fix-install-manpages.patch
BuildRequires:  bash >= 4
BuildRequires:  perl-base
BuildRequires:  pkgconfig
BuildRequires:  perl(Digest::SHA)
BuildRequires:  pkgconfig(systemd)
Requires:       %{_sbindir}/service
Requires:       %{name}-core = %{version}-%{release}
Requires:       bc
Requires:       iproute2
Requires:       iptables
Requires:       logrotate
Requires:       perl-base
PreReq:         %fillup_prereq
Suggests:       xtables-addons
Provides:       shoreline_firewall = %{version}-%{release}
BuildArch:      noarch
%{?systemd_ordering}
%{perl_requires}

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

%package lite
Summary:        Shoreline Firewall Lite is an iptables-based firewall for Linux systems
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Requires:       %{_sbindir}/service
Requires:       %{name}-core = %{version}-%{release}
Requires:       bc
Requires:       iproute2
Requires:       iptables
Requires:       logrotate
PreReq:         %fillup_prereq
Provides:       shoreline_firewall = %{version}-%{release}
%{?systemd_requires}

%description lite
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall Lite is a companion product to Shorewall that allows network
administrators to centralize the configuration of Shorewall-based firewalls.

%package -n %{name}6
Summary:        Shoreline Firewall 6 is an ip6tables-based firewall for Linux systems
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Requires:       %{_sbindir}/service
Requires:       %{name}-core = %{version}-%{release}
Requires:       bc
Requires:       iproute2
Requires:       iptables
Requires:       logrotate
Requires:       perl-base
PreReq:         %fillup_prereq
Provides:       shoreline_firewall = %{version}-%{release}
%{?systemd_requires}

%description -n %{name}6
The Shoreline Firewall 6, more commonly known as "Shorewall6", is a Netfilter
(ip6tables) based IPv6 firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

%package -n %{name}6-lite
Summary:        Shoreline Firewall 6 Lite is an ip6tables-based firewall for Linux systems
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Requires:       %{_sbindir}/service
Requires:       %{name}-core = %{version}-%{release}
Requires:       bc
Requires:       iproute2
Requires:       iptables
Requires:       logrotate
PreReq:         %fillup_prereq
Provides:       shoreline_firewall = %{version}-%{release}
%{?systemd_requires}

%description -n %{name}6-lite
The Shoreline Firewall 6, more commonly known as "Shorewall6", is a Netfilter
(ip6tables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall6 Lite is a companion product to Shorewall6 that allows network
administrators to centralize the configuration of Shorewall6-based firewalls.

%package  init
Summary:        Adds functionality during boot to Shoreline Firewall (Shorewall)
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Requires:       %{_sbindir}/service
Requires:       logrotate
Requires:       shoreline_firewall = %{version}-%{release}
PreReq:         %fillup_prereq
%{?systemd_requires}

%description init
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall Init is a companion product to Shorewall that allows for tigher
control of connections during boot and that integrates Shorewall with
ifup/ifdown and NetworkManager.

%package  docs
Summary:        HTML documentation for shorewall configuration
License:        GFDL-1.1-only
Group:          Documentation/Other

%description  docs
HTML documentation for the Shoreline Firewall. Highly recommend to read before
starting to configure shorewall

%package core
Summary:        Core libraries for Shorewall
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Requires:       iptables
Requires:       perl-base

%description core
This package contains the core libraries for Shorewall.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6
#PATCH-FIX-OPENSUSE geo_ip has no LE
#We keep it with this dynamic form to avoid maintaining manual patch
find . \( -name shorewall*.conf -or -name shorewall*.conf.annotated \) -exec sed -i "s,GEOIPDIR=%{_datadir}/xt_geoip/LE,GEOIPDIR=%{_datadir}/xt_geoip,g" {} \;
#PATCH-FIX-OPENSUSUSE for fillup
pushd %{name}-init-%{version}
%patch1 -p1
popd
pushd %{name}-%{version}
%patch2 -p1
%patch4 -p1
popd
pushd %{name}6-%{version}
%patch2 -p1
%patch4 -p1
popd
pushd %{name}-lite-%{version}
%patch3 -p1
popd
pushd %{name}6-lite-%{version}
%patch3 -p1
popd

chmod -x %{name}-docs-html-%{version}/images/*.png
chmod -x %{name}6-%{version}/tunnel
chmod -x %{name}6-%{version}/ipv6
chmod -x %{name}-%{version}/Contrib/swping.init
chmod -x %{name}-%{version}/Contrib/tunnel

cp %{SOURCE8} %{name}-%{version}/.

# We don't have /sbin /bin merged on /usr so symlinks can't work.
# so we dynamically patch last /sbin calls in lib.cli-std
# and make shorewall remote working without hacks
sed -i 's#/sbin/shorewall#%{_sbindir}/shorewall#g' %{name}-%{version}/lib.cli-std

# On 20201108 Upstream decide to remove StandardOutput=syslog from service on future version
find . -iname "*.service" -exec sed -i '/StandardOutput=syslog/d' {} \;

%build

%install

# find the systemd version in order to install correct service files
%define systemd_version \
systemd --version | awk '/^systemd/ {print $2}'

# NOTE For REVIEWERS
#
# configure is used to set the installation parameters to shorewall.
# The default shorewallrc is not what we want and every distro needs
# to set it differently. Please see the disccussion in
# http://lists.opensuse.org/opensuse-packaging/2012-08/msg00050.html

targets="shorewall shorewall-core shorewall-lite shorewall6 shorewall6-lite shorewall-init"

for i in $targets; do
    pushd ${i}-%{version}
    ./configure \
        vendor=%{_vendor} \
        host=%{_vendor} \
        prefix=%{_prefix} \
        perllibdir=%{perl_vendorlib} \
        libexecdir=%{_libexecdir} \
        sbindir=%{_sbindir} \
        %if 0%{?have_systemd}
            servicedir=%{_unitdir} \
            initdir= \
        %endif
       sharedir=%{_datadir}

    if [ $i != shorewall-init ];
    then
        BUILD=suse DESTDIR=%{buildroot} FILLUPDIR=%{_fillupdir} ./install.sh shorewallrc
    else
        install -d %buildroot/%{_sysconfdir}/NetworkManager/dispatcher.d
        BUILD=suse DESTDIR=%{buildroot} FILLUPDIR=%{_fillupdir} ./install.sh shorewallrc

        if [ -f ${DESTDIR}%{_sysconfdir}/ppp ]; then
            for directory in ip-up.d ip-down.d ipv6-up.d ipv6-down.d; do
                mkdir -p ${DESTDIR}%{_sysconfdir}/ppp/$directory #SuSE doesn't create the IPv6 directories
                cp -fp ${DESTDIR}${LIBEXEC}/shorewall-init/ifupdown ${DESTDIR}%{_sysconfdir}/ppp/$directory/shorewall
            done
        fi
        # Move Networkmanager to _prefix
        if [ -d "%buildroot/%{_sysconfdir}/NetworkManager/dispatcher.d" ]; then
            install -d "%buildroot/%{_prefix}/lib/NetworkManager/"
            mv -v "%buildroot/%{_sysconfdir}/NetworkManager/dispatcher.d" "%buildroot/%{_prefix}/lib/NetworkManager/dispatcher.d"
        fi
        # Move logrotate.d files to _prefix
        if [ -d "%{buildroot}%{_sysconfdir}/logrotate.d" ]; then
            install -d "%{buildroot}%{_distconfdir}"
            mv -v "%{buildroot}%{_sysconfdir}/logrotate.d" "%{buildroot}%{_distconfdir}/logrotate.d"
        fi
    fi
    popd
done

rctargets="shorewall shorewall-lite shorewall6 shorewall6-lite shorewall-init"
mkdir -p %buildroot/%{_sbindir}
for i in $rctargets; do
  ln -sf %{_sbindir}/service %buildroot%{_sbindir}/rc${i}
done

# starting with 12.3 drop sysv-init support fedora already did
rm -rf %buildroot%_initddir

# Since 5.12 we need to remove them again
rm -f %{buildroot}/%{_sysconfdir}/sysconfig/%{name}*

# Move
%pre
%service_add_pre shorewall.service
%if %conf_need_update
echo "upgrade configuration" > /run/%{name}_upgrade
%endif

%post
%service_add_post shorewall.service

%preun
rm -f %{_sysconfdir}/%{name}/startup_disabled
%service_del_preun shorewall.service

%postun
%service_del_postun shorewall.service

%posttrans
if [ -f /run/%{name}_upgrade ]; then
cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-something << EOF
Warning: Shorewall %{dmaj} has just been installed
Warning: You have to check and upgrade your configuration
%{name} update -a %{_sysconfdir}/%{name}
Warning: Adjust changes and try the new configuration
%{name} try %{_sysconfdir}/%{name}
Warning: If everything work run
systemctl try-reload-or-restart %{name}
EOF
rm -f /run/%{name}_upgrade
fi

%pre -n %{name}6
%service_add_pre shorewall6.service
%if %conf_need_update
echo "upgrade configuration" > /run/%{name}6_upgrade
%endif

%post -n %{name}6
%service_add_post shorewall6.service

%preun -n %{name}6
rm -f %{_sysconfdir}/%{name}/startup_disabled
%service_del_preun shorewall6.service

%postun -n %{name}6
%service_del_postun shorewall6.service

%posttrans -n %{name}6
if [ -f /run/%{name}6_upgrade ]; then
cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-something << EOF
Warning: Shorewall6 %{dmaj} has just been installed
Warning: You have to check and upgrade your configuration
%{name}6 update -a %{_sysconfdir}/%{name}6
Warning: Adjust changes and try the new configuration
%{name}6 try %{_sysconfdir}/%{name}6
Warning: If everything work run
systemctl try-reload-or-restart %{name}6
EOF
rm -f /run/%{name}6_upgrade
fi

%pre -n %{name}-lite
%service_add_pre shorewall-lite.service

%post -n %{name}-lite
%service_add_post shorewall-lite.service

%preun -n %{name}-lite
rm -f %{_sysconfdir}/%{name}/startup_disabled
%service_del_preun shorewall-lite.service

%postun -n %{name}-lite
%service_del_postun shorewall-lite.service

%pre -n %{name}6-lite
%service_add_pre shorewall6-lite.service

%post -n %{name}6-lite
%service_add_post shorewall6-lite.service

%preun -n %{name}6-lite
rm -f %{_sysconfdir}/%{name}/startup_disabled
%service_del_preun shorewall6-lite.service

%postun -n %{name}6-lite
%service_del_postun shorewall6-lite.service

%pre init
%service_add_pre shorewall-init.service

%post init
%{fillup_only}
%service_add_post shorewall-init.service

%preun init
%service_del_preun shorewall-init.service

%postun init
# boo#1166114 Never try to restart shorewall-init
# You can lock down the system so never use
#%%service_del_postun shorewall-init.service macro
%systemd_postun

%files
%defattr(-,root,root,-)
%doc %{name}-%version/{COPYING,changelog.txt,releasenotes.txt,README.openSUSE}
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%dir %{_sysconfdir}/%{name}
%ghost %{_sysconfdir}/%{name}/isusable
%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%dir %{_libexecdir}/%{name}
%dir %{_datadir}/%{name}/configfiles
%dir %{_datadir}/%{name}/deprecated
%dir %{_datadir}/%{name}/Shorewall
%attr(0700,root,root) %dir %{_localstatedir}/lib/%{name}
%dir %{_distconfdir}
%dir %{_distconfdir}/logrotate.d/
%{_distconfdir}/logrotate.d/%{name}
%{_datadir}/%{name}/version
%{_datadir}/%{name}/actions.std
%{_datadir}/%{name}/action.*
%{_datadir}/%{name}/lib.base
%{_datadir}/%{name}/macro.*
%{_datadir}/%{name}/prog.*
%{_datadir}/%{name}/helpers
%{_datadir}/%{name}/configpath
%{_datadir}/%{name}/configfiles/*
%attr(755,root,root) %{_libexecdir}/%{name}/getparams
%attr(755,root,root) %{_libexecdir}/%{name}/compiler.pl
%dir %{perl_vendorlib}/Shorewall
%{perl_vendorlib}/Shorewall/*.pm
%{_mandir}/man5/%{name}-[a-k,m-z]*.5*
%{_mandir}/man5/%{name}-logging.5*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%attr(644,root,root) %{_unitdir}/%{name}.service

%files lite
%defattr(-,root,root,-)
%doc %{name}-lite-%version/{COPYING,changelog.txt,releasenotes.txt}
%{_fillupdir}/sysconfig.%{name}-lite
%dir %{_sysconfdir}/%{name}-lite
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}-lite/%{name}-lite.conf
%{_sbindir}/rc%{name}-lite
%{_sbindir}/%{name}-lite
%dir %{_datadir}/%{name}-lite
%dir %{_libexecdir}/%{name}-lite
%attr(0700,root,root) %dir %{_localstatedir}/lib/%{name}-lite
%dir %{_distconfdir}
%dir %{_distconfdir}/logrotate.d/
%{_distconfdir}/logrotate.d/%{name}-lite
%{_datadir}/%{name}-lite/version
%{_datadir}/%{name}-lite/configpath
%attr(- ,root,root) %{_datadir}/%{name}-lite/functions
%{_datadir}/%{name}-lite/lib.base
%{_datadir}/%{name}-lite/helpers
%attr(0544,root,root) %{_libexecdir}/%{name}-lite/shorecap
%{_mandir}/man5/%{name}-lite*.5*
%{_mandir}/man8/%{name}-lite.8.*
%attr(644,root,root) %{_unitdir}/%{name}-lite.service

%files -n %{name}6
%defattr(-,root,root,-)
%doc %{name}6-%version/{COPYING,changelog.txt,releasenotes.txt,tunnel,ipv6,ipsecvpn}
%{_sbindir}/rc%{name}6
%{_sbindir}/%{name}6
%{_fillupdir}/sysconfig.%{name}6
%dir %{_sysconfdir}/%{name}6
%ghost %{_sysconfdir}/%{name}6/isusable
%config(noreplace) %{_sysconfdir}/%{name}6/*
%dir %{_datadir}/%{name}6
%dir %{_libexecdir}/%{name}6
%dir %{_datadir}/%{name}6/configfiles
%dir %{_datadir}/%{name}6/deprecated
%attr(0700,root,root) %dir %{_localstatedir}/lib/%{name}6
%dir %{_distconfdir}
%dir %{_distconfdir}/logrotate.d/
%{_distconfdir}/logrotate.d/%{name}6
%{_datadir}/%{name}6/version
%{_datadir}/%{name}6/actions.std
%{_datadir}/%{name}6/action.*
%{_datadir}/%{name}6/functions
%{_datadir}/%{name}6/lib.base
%{_datadir}/%{name}6/macro.*
%{_datadir}/%{name}6/helpers
%{_datadir}/%{name}6/configpath
%{_datadir}/%{name}6/configfiles/*
%{_mandir}/man5/%{name}6-[a-k,m-z]*.5*
%{_mandir}/man5/%{name}6.conf.5*
%{_mandir}/man8/%{name}6.8*
%attr(644,root,root) %{_unitdir}/%{name}6.service

%files -n %{name}6-lite
%defattr(-,root,root,-)
%{_mandir}/man5/%{name}6-lite*.5*
%{_mandir}/man8/%{name}6-lite.8*
%doc %{name}6-lite-%version/{COPYING,changelog.txt,releasenotes.txt}
%{_fillupdir}/sysconfig.%{name}6-lite
%dir %{_sysconfdir}/%{name}6-lite
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}6-lite/%{name}6-lite.conf
%{_sbindir}/rc%{name}6-lite
%{_sbindir}/%{name}6-lite
%dir %{_datadir}/%{name}6-lite
%dir %{_libexecdir}/%{name}6-lite
%attr(0700,root,root) %dir %{_localstatedir}/lib/%{name}6-lite
%dir %{_distconfdir}
%dir %{_distconfdir}/logrotate.d/
%{_distconfdir}/logrotate.d/%{name}6-lite
%{_datadir}/%{name}6-lite/version
%{_datadir}/%{name}6-lite/configpath
%attr(- ,root,root) %{_datadir}/%{name}6-lite/functions
%{_datadir}/%{name}6-lite/lib.base
%{_datadir}/%{name}6-lite/helpers
%attr(0544,root,root) %{_libexecdir}/%{name}6-lite/shorecap
%attr(644,root,root) %{_unitdir}/%{name}6-lite.service

%files init
%defattr(-,root,root,-)
%doc %{name}-init-%version/{COPYING,changelog.txt,releasenotes.txt}
%{_sbindir}/rc%{name}-init
%{_fillupdir}/sysconfig.%{name}-init
%attr(0755,root,root) %{_sbindir}/shorewall-init
%dir %{_datadir}/%{name}-init
%dir %{_libexecdir}/%{name}-init
%dir %attr(0755,root,root) %{_prefix}/lib//NetworkManager
%dir %attr(0755,root,root) %{_prefix}/lib//NetworkManager/dispatcher.d
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/01-%{name}
%{_datadir}/%{name}-init/version
%attr(0544,root,root) %{_libexecdir}/%{name}-init/ifupdown
%dir %{_sysconfdir}/sysconfig/network
%dir %{_sysconfdir}/sysconfig/network/if-down.d
%attr(0544,root,root) %{_sysconfdir}/sysconfig/network/if-down.d/%{name}
%dir %{_sysconfdir}/sysconfig/network/if-up.d
%attr(0755,root,root) %{_sysconfdir}/sysconfig/network/if-up.d/%{name}
%{_mandir}/man8/%{name}-init.8*
%dir %{_distconfdir}
%dir %{_distconfdir}/logrotate.d/
%{_distconfdir}/logrotate.d/%{name}-init
%attr(644,root,root) %{_unitdir}/%{name}-init.service

%files core
%defattr(-,root,root,-)
%doc shorewall-core-%{version}/{COPYING,changelog.txt,releasenotes.txt}
%{_sbindir}/%{name}
%dir %{_datadir}/shorewall/
%{_datadir}/shorewall/coreversion
%{_datadir}/shorewall/functions
%{_datadir}/shorewall/lib.cli
%{_datadir}/shorewall/lib.cli-std
%{_datadir}/shorewall/lib.common
%{_datadir}/shorewall/lib.core
%{_datadir}/shorewall/lib.runtime
%dir %{_libexecdir}/shorewall
%{_libexecdir}/shorewall/wait4ifup
%{_datadir}/shorewall/shorewallrc

%files docs
%defattr(-,root,root,-)
%doc %{name}-docs-html-%version/*
%doc %{name}-%version/{Contrib,Samples}

%changelog
