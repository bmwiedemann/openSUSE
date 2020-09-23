#
# spec file for package openvpn
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} > 1210
%define with_systemd 1
%else
%define with_systemd 0
%endif
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           openvpn
Version:        2.4.9
Release:        0
Summary:        Full-featured SSL VPN solution using a TUN/TAP Interface
License:        SUSE-GPL-2.0-with-openssl-exception AND LGPL-2.1-only
Group:          Productivity/Networking/Security
URL:            http://openvpn.net/
Source:         https://swupdate.openvpn.org/community/releases/openvpn-%{version}.tar.xz
Source1:        https://swupdate.openvpn.org/community/releases/openvpn-%{version}.tar.xz.asc
Source2:        %{name}.init
Source3:        %{name}.README.SUSE
Source4:        client-netconfig.up
Source5:        client-netconfig.down
Source6:        %{name}.sysconfig
Source7:        %{name}.keyring
Source8:        %{name}.service
Source9:        %{name}.target
Source10:       %{name}-tmpfile.conf
Source11:       rc%{name}
Patch1:         %{name}-2.3-plugin-man.dif
Patch6:         %{name}-fips140-2.3.2.patch
Patch7:         openvpn-2.3.9-Fix-heap-overflow-on-getaddrinfo-result.patch
Patch8:         openvpn-2.3.x-fixed-multiple-low-severity-issues.patch
Patch9:         0001-preform-deferred-authentication-in-the-background.patch
BuildRequires:  iproute2
BuildRequires:  libselinux-devel
BuildRequires:  lzo-devel
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pam-devel
BuildRequires:  pkcs11-helper-devel >= 1.11
BuildRequires:  xz
Requires:       iproute2
Requires:       pkcs11-helper >= 1.11
Requires:       sysvinit-tools
%if %{with_systemd}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%systemd_ordering
%else
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
%endif

%description
OpenVPN is a full-featured SSL VPN solution which can accommodate a wide
range of configurations, including remote access, site-to-site VPNs,
WiFi security, and enterprise-scale remote access solutions with load
balancing, failover, and fine-grained access-controls.

OpenVPN implements OSI layer 2 or 3 secure network extension using the
industry standard SSL/TLS protocol, supports flexible client
authentication methods based on certificates, smart cards, and/or
2-factor authentication, and allows user or group-specific access
control policies using firewall rules applied to the VPN virtual
interface.

OpenVPN runs on: Linux, Windows 2000/XP and higher, OpenBSD, FreeBSD,
NetBSD, Mac OS X, and Solaris.

OpenVPN is not a web application proxy and does not operate through a
web browser.

%package down-root-plugin
Summary:        OpenVPN down-root plugin
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description down-root-plugin
The OpenVPN down-root plugin allows an OpenVPN configuration to call a
down script with root privileges, even when privileges have been
dropped using --user/--group/--chroot.

This module uses a split privilege execution model which will fork()
before OpenVPN drops root privileges, at the point where the --up
script is usually called.  The plugin will then remain in a wait state
until it receives a message from OpenVPN via pipe to execute the down
script.  Thus, the down script will be run in the same execution
environment as the up script.

%package auth-pam-plugin
Summary:        OpenVPN auth-pam plugin
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description auth-pam-plugin
The OpenVPN auth-pam plugin implements username/password authentication
via PAM, and essentially allows any authentication method supported by
PAM (such as LDAP, RADIUS, or Linux Shadow passwords) to be used with
OpenVPN.

While PAM supports username/password authentication, this can be
combined with X509 certificates to provide two indepedent levels of
authentication.

This plugin uses a split privilege execution model which will function
even if you drop openvpn daemon privileges using the user, group, or
chroot directives.

%package devel
Summary:        OpenVPN plugin header
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package provides the header file to build external plugins.

%prep
%setup -q
%patch1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

sed -e "s|\" __DATE__|$(date '+%b %e %Y' -r version.m4)\"|g" \
    -i src/openvpn/options.c
sed -e "s|@PLUGIN_LIBDIR@|%{_libdir}/openvpn/plugins|g" \
    -e "s|@PLUGIN_DOCDIR@|%{_defaultdocdir}/%{name}|g" \
    -i doc/openvpn.8
sed -e "s|%{_localstatedir}/run|%{_rundir}|g" < \
    $RPM_SOURCE_DIR/%{name}.service > %{name}.service

# %%doc items shouldn't be executable.
find contrib sample -type f -exec chmod a-x \{\} \;

%build
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS) -W -Wall -fno-strict-aliasing"
export LDFLAGS
%configure \
	--enable-iproute2		\
	--enable-x509-alt-username	\
	--enable-pkcs11			\
%if %{with_systemd}
	--enable-systemd		\
%endif
	--enable-plugins		\
	--enable-plugin-down-root	\
	--enable-plugin-auth-pam	\
	CFLAGS="$CFLAGS $(getconf LFS_CFLAGS) -fPIE $PLUGIN_DEFS"	\
	LDFLAGS="$LDFLAGS -pie -lpam -rdynamic -Wl,-rpath,%{_libdir}/%{name}/plugins"
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}/%{_sysconfdir}/openvpn
mkdir -p %{buildroot}/%{_rundir}/openvpn
mkdir -p %{buildroot}/%{_datadir}/openvpn
%if %{with_systemd}
rm %{buildroot}%{_libdir}/systemd/system/openvpn-client@.service
rm %{buildroot}%{_libdir}/systemd/system/openvpn-server@.service
#use one proveded by suse
rm %{buildroot}%{_libdir}/tmpfiles.d/openvpn.conf
install -D -m 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}@.service
install -D -m 644 $RPM_SOURCE_DIR/%{name}.target %{buildroot}/%{_unitdir}/%{name}.target
install -D -m 755 $RPM_SOURCE_DIR/rc%{name} %{buildroot}%{_sbindir}/rc%{name}
# tmpfiles.d
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 $RPM_SOURCE_DIR/%{name}-tmpfile.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
install -D -m 755 $RPM_SOURCE_DIR/openvpn.init %{buildroot}/%{_sysconfdir}/init.d/openvpn
ln -sv %{_sysconfdir}/init.d/openvpn %{buildroot}/%{_sbindir}/rcopenvpn
# the /etc/sysconfig/openvpn template only with sysvinit, no needed with systemd
install -d -m0755 %{buildroot}%{_fillupdir}
install    -m0600 $RPM_SOURCE_DIR/openvpn.sysconfig \
                  %{buildroot}%{_fillupdir}/sysconfig.openvpn
%endif
cp -p $RPM_SOURCE_DIR/openvpn.README.SUSE README.SUSE
install -m 755 $RPM_SOURCE_DIR/client-netconfig.up sample/sample-scripts/client-netconfig.up
install -m 755 $RPM_SOURCE_DIR/client-netconfig.down sample/sample-scripts/client-netconfig.down

# we install docs via spec into _defaultdocdir/name/management-notes.txt
rm -rf %{buildroot}%{_datadir}/doc/{OpenVPN,%{name}}
find sample -name .gitignore | xargs rm -f

%pre
%if %{with_systemd}
%service_add_pre %{name}.target
%endif

%post
%if %{with_systemd}
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.target
# try to migrate openvpn.service autostart to openvpn@<CONF>.service
if test $1 -ge 1 -a \
	-x /bin/systemctl -a \
	-f %{_sysconfdir}/sysconfig/openvpn -a \
	-f %{_fillupdir}/sysconfig.openvpn && \
	/bin/systemctl --quiet is-enabled openvpn.service &>/dev/null ;
then
	. %{_sysconfdir}/sysconfig/openvpn
	try_service_cgroup_join()
	{
		local p="%{_localstatedir}/run/openvpn/${1}.pid"
		local t="/sys/fs/cgroup/systemd/system/openvpn@.service/${1}"
		/sbin/checkproc -p "$p" "%{_sbindir}/openvpn" &>/dev/null || return 0
		test -d "$t" || mkdir -p "$t" 2>/dev/null || return 1
		cat "$p" > "$t/tasks" 2>/dev/null || return 1
	}
	if test "X$OPENVPN_AUTOSTART" != "X" ; then
		for conf in $OPENVPN_AUTOSTART ; do
			test -f "%{_sysconfdir}/openvpn/${conf}.conf" && \
			/bin/systemctl enable "openvpn@${conf}.service" && \
			try_service_cgroup_join "$conf" || continue
		done
	else
		shopt -s nullglob || :
		for conf in %{_sysconfdir}/openvpn/*.conf ; do
			conf=${conf##*/}
			conf=${conf%.conf}
			test -f "%{_sysconfdir}/openvpn/${conf}.conf" && \
			/bin/systemctl enable "openvpn@${conf}.service" && \
			try_service_cgroup_join "$conf" || continue
		done
	fi
fi
rm -f %{_sysconfdir}/sysconfig/openvpn || :
%else
%{?fillup_and_insserv:%fillup_and_insserv}
%endif

%preun
%if %{with_systemd}
%service_del_preun %{name}.target
%else
%{?stop_on_removal:%stop_on_removal openvpn}
%endif

%postun
%if %{with_systemd}
%service_del_postun %{name}.target
%else
%{?insserv_cleanup:%insserv_cleanup}
%endif

%files
%license COPYING
%doc AUTHORS COPYRIGHT.GPL ChangeLog PORTS README
%doc src/plugins/{auth-pam/README.auth-pam,down-root/README.down-root}
%doc README.*
%doc contrib
%doc sample/sample-config-files
%doc sample/sample-keys
%doc sample/sample-scripts
%doc doc/management-notes.txt
%{_mandir}/man8/openvpn.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/openvpn/
%if %{with_systemd}
%dir %{_tmpfilesdir}
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0750,root,root) %ghost %{_rundir}/openvpn/
%else
%config %{_sysconfdir}/init.d/openvpn
%{_fillupdir}/sysconfig.openvpn
%dir %attr(750,root,root) %{_rundir}/openvpn/
%endif
%{_sbindir}/rcopenvpn
%{_sbindir}/openvpn

%files down-root-plugin
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/%{name}-plugin-down-root.so

%files auth-pam-plugin
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/%{name}-plugin-auth-pam.so

%files devel
%{_includedir}/%{name}-plugin.h
%{_includedir}/%{name}-msg.h

%changelog
