#
# spec file for package openvpn
#
# Copyright (c) 2025 SUSE LLC
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


%define _buildshell /bin/bash
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           openvpn
Version:        2.6.14
Release:        0
Summary:        Full-featured SSL VPN solution using a TUN/TAP Interface
License:        GPL-2.0-only WITH openvpn-openssl-exception
Group:          Productivity/Networking/Security
URL:            https://openvpn.net/
Source:         https://swupdate.openvpn.org/community/releases/openvpn-%{version}.tar.gz
Source1:        https://swupdate.openvpn.org/community/releases/openvpn-%{version}.tar.gz.asc
Source3:        %{name}.README.SUSE
Source4:        client-netconfig.up
Source5:        client-netconfig.down
Source7:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf554a3687412cffebdefe0a312f5f7b42f2b01e7#/%{name}.keyring
Source8:        %{name}.service
Source9:        %{name}.target
Source10:       %{name}-tmpfile.conf
Source11:       rc%{name}
Patch1:         %{name}-2.3-plugin-man.dif
BuildRequires:  iproute2
BuildRequires:  libcap-ng-devel
BuildRequires:  liblz4-devel
BuildRequires:  libselinux-devel
BuildRequires:  lz4
BuildRequires:  lzo-devel
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pam-devel
BuildRequires:  pkcs11-helper-devel >= 1.11
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Requires:       iproute2
Requires:       pkcs11-helper >= 1.11
Recommends:     ovpn-dco-kmp
%systemd_ordering

%description
OpenVPN is an SSL VPN solution which can accommodate a wide
range of configurations, including remote access, site-to-site VPNs,
WiFi security, and remote access solutions with load
balancing, failover, and fine-grained access-controls.

OpenVPN implements OSI layer 2 or 3 secure network extension using the
SSL/TLS protocol, supports flexible client
authentication methods based on certificates, smart cards, and/or
2-factor authentication, and allows user or group-specific access
control policies using firewall rules applied to the VPN virtual
interface.

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
%autosetup -p0

sed -e "s|\" __DATE__|$(date '+%%b %%e %%Y' -r version.m4)\"|g" \
    -i src/openvpn/options.c
sed -e "s|@PLUGIN_LIBDIR@|%{_libdir}/openvpn/plugins|g" \
    -e "s|@PLUGIN_DOCDIR@|%{_defaultdocdir}/%{name}|g" \
    -i doc/openvpn.8
sed -e "s|%{_localstatedir}/run|%{_rundir}|g" < %{SOURCE8} > %{name}.service

# %%doc items shouldn't be executable.
find contrib sample -type f -exec chmod a-x \{\} +

%build
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS) -W -Wall -fno-strict-aliasing"
export LDFLAGS
%if 0%{?suse_version} >= 1550
# usrmerge
export IPROUTE="%{_sbindir}/ip"
%endif
libnlversion=$(rpm -q --qf "%%{version}" libnl3-devel)
if [[ $libnlversion == 3.[0-3].* ]] ; then
  confopt=--enable-iproute2
else
  confopt=--enable-dco
fi
%configure \
	$confopt			\
	--enable-x509-alt-username	\
	--enable-pkcs11			\
	--enable-systemd		\
	--enable-plugins		\
	--enable-plugin-down-root	\
	--enable-plugin-auth-pam	\
	CFLAGS="$CFLAGS $(getconf LFS_CFLAGS) -fPIE $PLUGIN_DEFS"	\
	LDFLAGS="$LDFLAGS -pie -lpam -rdynamic -Wl,-rpath,%{_libdir}/%{name}/plugins"
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -print -delete
mkdir -p %{buildroot}/%{_sysconfdir}/openvpn
mkdir -p %{buildroot}/%{_rundir}/openvpn
mkdir -p %{buildroot}/%{_datadir}/openvpn
rm %{buildroot}%{_libdir}/systemd/system/openvpn-client@.service
rm %{buildroot}%{_libdir}/systemd/system/openvpn-server@.service
#use one proveded by suse
rm %{buildroot}%{_libdir}/tmpfiles.d/openvpn.conf
install -D -m 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}@.service
install -D -m 644 %{SOURCE9} %{buildroot}/%{_unitdir}/%{name}.target
%if 0%{?suse_version} < 1600
install -D -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/rc%{name}
%endif
# tmpfiles.d
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE10} %{buildroot}%{_tmpfilesdir}/%{name}.conf
cp -p %{SOURCE3} README.SUSE
install -m 755 %{SOURCE4} sample/sample-scripts/client-netconfig.up
install -m 755 %{SOURCE5} sample/sample-scripts/client-netconfig.down

# we install docs via spec into _defaultdocdir/name/management-notes.txt
rm -rf %{buildroot}%{_datadir}/doc/{OpenVPN,%{name}}
find sample -name .gitignore -delete

%pre
%service_add_pre %{name}.target

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.target

%preun
%service_del_preun %{name}.target

%postun
%service_del_postun %{name}.target

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
%{_mandir}/man5/openvpn-examples.5%{?ext_man}
%{_mandir}/man8/openvpn.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/openvpn/
%dir %{_tmpfilesdir}
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0750,root,root) %ghost %{_rundir}/openvpn/
%if 0%{?suse_version} < 1600
%{_sbindir}/rcopenvpn
%endif
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
