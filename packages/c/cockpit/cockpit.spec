#
# Copyright (C) 2014-2020 Red Hat, Inc.
#
# Cockpit is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# Cockpit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Cockpit; If not, see <https://www.gnu.org/licenses/>.
#

#
# This file is maintained at the following location:
# https://github.com/cockpit-project/cockpit/blob/main/tools/cockpit.spec
#
# If you are editing this file in another location, changes will likely
# be clobbered the next time an automated release is done.
#
# Check first cockpit-devel@lists.fedorahosted.org
#

# earliest base that the subpackages work on; this is still required as long as
# we maintain the basic/optional split, then it can be replaced with just %{version}.
%define required_base 266

# we generally want CentOS packages to be like RHEL; special cases need to check %{centos} explicitly
%if 0%{?centos}
%define rhel %{centos}
%endif

%define _hardened_build 1

%define __lib lib

%if %{defined _pamdir}
%define pamdir %{_pamdir}
%else
%define pamdir %{_libdir}/security
%endif

Name:           cockpit
Summary:        Web Console for Linux servers

License:        LGPL-2.1-or-later
URL:            https://cockpit-project.org/

Version:        332
Release:        0
Source0:        cockpit-%{version}.tar.gz
Source1:        cockpit.pam
Source2:        cockpit-rpmlintrc
Source3:        cockpit-suse-theme.tar
Source4:        cockpit-no-pamoath.pam
Source10:       update_version.sh
Source99:       README.packaging
Source98:       package-lock.json
Source97:       node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Patch1:         0001-selinux-allow-login-to-read-motd-file.patch
Patch2:         suse_docs.patch
Patch3:         suse-microos-branding.patch
Patch4:         css-overrides.patch
Patch5:         storage-btrfs.patch
# SLE Micro specific patches
Patch101:       hide-pcp.patch
Patch102:       0002-selinux-temporary-remove-setroubleshoot-section.patch
Patch107:       0006-totp-motd.patch
Patch108:       0007-Remove-DynamicUser-setting-as-these-conflict-with-re.patch
# For anything based on SLES 15 codebase (including Leap, SLE Micro)
Patch103:       0004-leap-gnu18-removal.patch
Patch104:       selinux_libdir.patch
Patch105:       fix-libexecdir.patch

Patch201:       remove_rh_links.patch

%define build_all 1
%if 0%{?rhel} == 8 && 0%{?epel} == 0 && !0%{?build_all}

%if "%{name}" == "cockpit"
%define build_basic 1
%define build_optional 0
%else
%define build_basic 0
%define build_optional 1
%endif

%else
%define build_basic 1
%define build_optional 1
%endif

%if 0%{?build_optional} && 0%{?suse_version} == 0
%define build_tests 1
%endif

# Allow root login in Cockpit on RHEL 8 and lower as it also allows password login over SSH.
%if 0%{?rhel} && 0%{?rhel} <= 8
%define disallow_root 0
%else
%define disallow_root 1
%endif

%if 0%{?fedora} >= 41 || 0%{?rhel}
ExcludeArch: %{ix86}
%endif

%define enable_multihost 1
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
%define enable_multihost 0
%endif

%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1500
# Ship custom SELinux policy
%define selinuxtype targeted
%define selinux_configure_arg --enable-selinux-policy=%{selinuxtype}
%define with_selinux 1
%else
%define selinux_configure_arg --enable-selinux-policy=no
%endif

BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(polkit-agent-1) >= 0.105
BuildRequires: pam-devel

BuildRequires: autoconf automake
BuildRequires: make
BuildRequires: /usr/bin/python3
BuildRequires: python3-devel
BuildRequires: gettext >= 0.21
BuildRequires: openssl-devel
BuildRequires: gnutls-devel >= 3.4.3
BuildRequires: zlib-devel
BuildRequires: pkgconfig(krb5) >= 1.11
BuildRequires: libxslt-devel
BuildRequires: glib-networking
BuildRequires: sed

BuildRequires: glib2-devel >= 2.50.0
# this is for runtimedir in the tls proxy ace21c8879
BuildRequires: pkgconfig(libsystemd) >= 235
%if 0%{?suse_version}
BuildRequires: distribution-release
BuildRequires: openssh
BuildRequires: distribution-logos
BuildRequires: wallpaper-branding
# needed for /var/lib/pcp directory ownership
BuildRequires: pcp
%else
BuildRequires: openssh-clients
BuildRequires: docbook-style-xsl
%endif
BuildRequires: krb5-server
BuildRequires: gdb

# For documentation
BuildRequires: xmlto

%if 0%{?with_selinux}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%endif

# for rebuilding nodejs bits
BuildRequires: npm
BuildRequires: sassc
BuildRequires: local-npm-registry

# This is the "cockpit" metapackage. It should only
# Require, Suggest or Recommend other cockpit-xxx subpackages

Requires: cockpit-bridge
Requires: cockpit-ws
Requires: cockpit-system

# Optional components
Recommends: (cockpit-storaged if udisks2)
Recommends: (cockpit-packagekit if (dnf or zypper))
Suggests: python3-pcp

%if 0%{?rhel} == 0
Recommends: (cockpit-networkmanager if NetworkManager)
# c-ostree is not in RHEL 8/9
Recommends: (cockpit-ostree if rpm-ostree)
Suggests: cockpit-selinux
%endif
%if 0%{?rhel} && 0%{?centos} == 0
Requires: subscription-manager-cockpit
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pip
%if 0%{?rhel} == 0 && !0%{?suse_version}
# All of these are only required for running pytest (which we only do on Fedora)
BuildRequires:  procps-ng
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout
%endif

%prep
%setup -q -n cockpit-%{version} -a 3
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1


# SLE Micro specific patches
%if 0%{?is_smo}
%patch -P 101 -p1
%patch -P 107 -p1
# Patches for versions lower then SLE Micro 5.5
%if 0%{?sle_version} < 150500
%patch -P 102 -p1
%endif
%endif
# For anything based on SLES 15 codebase (including Leap, SLEM)
%if 0%{?suse_version} == 1500
%patch -P 103 -p1
%patch -P 104 -p1
%patch -P 105 -p1
%patch -P 108 -p1
%else
%patch -P 107 -p1
%endif

%patch -P 201 -p1

%if 0%{?suse_version} > 1500
cp %SOURCE1 tools/cockpit.pam
%else
cp %SOURCE4 tools/cockpit.pam
%endif
#
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts

%build
find node_modules -name \*.node -print -delete
touch node_modules/.stamp

exec 2>&1
PKG_NAME="Cockpit"
echo "m4_define(VERSION_NUMBER, %version)" > version.m4
autoreconf -fvi -I tools
#
%configure \
    %{?selinux_configure_arg} \
%if 0%{?suse_version}
    --docdir=%_defaultdocdir/%{name} \
    --libexecdir=%_libexecdir \
%endif
    --with-pamdir='%{pamdir}' \
%if %{enable_multihost}
    --enable-multihost \
%endif

%if 0%{?with_selinux}
make -f /usr/share/selinux/devel/Makefile cockpit.pp
bzip2 -9 cockpit.pp
%endif

%make_build

%check
make -j$(nproc) check

%if 0%{?rhel} == 0 && 0%{?suse_version} == 0
%tox
%endif

%install
# In obs we get  write error: stdout
%make_install | tee make_install.log
make install-tests DESTDIR=%{buildroot}
%if 0%{?suse_version} > 1500
mkdir -p $RPM_BUILD_ROOT%{_pam_vendordir}
install -p -m 644 tools/cockpit.pam $RPM_BUILD_ROOT%{_pam_vendordir}/cockpit
%else
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m 644 tools/cockpit.pam $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/cockpit
%endif
rm -f %{buildroot}/%{_libdir}/cockpit/*.so
install -D -p -m 644 AUTHORS COPYING README.md %{buildroot}%{_docdir}/cockpit/

# selinux
%if 0%{?with_selinux}
install -D -m 644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -m 644 -t %{buildroot}%{_mandir}/man8 selinux/%{name}_session_selinux.8cockpit
install -D -m 644 -t %{buildroot}%{_mandir}/man8 selinux/%{name}_ws_selinux.8cockpit
# create this directory in the build root so that %ghost sees the desired mode
install -d -m 700 %{buildroot}%{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

# SUSE branding
mkdir -p %{buildroot}%{_datadir}/cockpit/branding/suse
pushd cockpit-suse-theme
cp src/css-overrides.css %{buildroot}%{_datadir}/cockpit/branding/suse
cp src/fonts.css %{buildroot}%{_datadir}/cockpit/branding/suse
cp -a src/fonts %{buildroot}%{_datadir}/cockpit/branding/suse
popd

%if 0%{?suse_version} == 1500
sed -i -e 's#"/lib/systemd/system#"%{_unitdir}#' \
  %{buildroot}%{_datadir}/cockpit/packagekit/manifest.json
%endif

# Build the package lists for resource packages
# cockpit-bridge is the basic dependency for all cockpit-* packages, so centrally own the page directory
echo '%dir %{_datadir}/cockpit' > base.list
echo '%dir %{_datadir}/cockpit/base1' >> base.list
find %{buildroot}%{_datadir}/cockpit/base1 -type f -o -type l >> base.list
echo '%{_sysconfdir}/cockpit/machines.d' >> base.list
echo %{buildroot}%{_datadir}/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy >> base.list

echo '%dir %{_datadir}/cockpit/shell' >> system.list
find %{buildroot}%{_datadir}/cockpit/shell -type f >> system.list

echo '%dir %{_datadir}/cockpit/systemd' >> system.list
find %{buildroot}%{_datadir}/cockpit/systemd -type f >> system.list

echo '%dir %{_datadir}/cockpit/users' >> system.list
find %{buildroot}%{_datadir}/cockpit/users -type f >> system.list

echo '%dir %{_datadir}/cockpit/metrics' >> system.list
find %{buildroot}%{_datadir}/cockpit/metrics -type f >> system.list

echo '%dir %{_datadir}/cockpit/kdump' > kdump.list
find %{buildroot}%{_datadir}/cockpit/kdump -type f >> kdump.list

echo '%dir %{_datadir}/cockpit/sosreport' > sosreport.list
find %{buildroot}%{_datadir}/cockpit/sosreport -type f >> sosreport.list

echo '%dir %{_datadir}/cockpit/storaged' > storaged.list
find %{buildroot}%{_datadir}/cockpit/storaged -type f >> storaged.list

echo '%dir %{_datadir}/cockpit/networkmanager' > networkmanager.list
find %{buildroot}%{_datadir}/cockpit/networkmanager -type f >> networkmanager.list

echo '%dir %{_datadir}/cockpit/packagekit' > packagekit.list
find %{buildroot}%{_datadir}/cockpit/packagekit -type f >> packagekit.list

echo '%dir %{_datadir}/cockpit/apps' >> packagekit.list
find %{buildroot}%{_datadir}/cockpit/apps -type f >> packagekit.list

echo '%dir %{_datadir}/cockpit/selinux' > selinux.list
find %{buildroot}%{_datadir}/cockpit/selinux -type f >> selinux.list

echo '%dir %{_datadir}/cockpit/static' > static.list
echo '%dir %{_datadir}/cockpit/static/fonts' >> static.list
find %{buildroot}%{_datadir}/cockpit/static -type f >> static.list

# when not building basic packages, remove their files
%if 0%{?build_basic} == 0
for pkg in base1 branding motd kdump networkmanager selinux shell sosreport static systemd users metrics; do
    rm -r %{buildroot}/%{_datadir}/cockpit/$pkg
    rm -f %{buildroot}/%{_datadir}/metainfo/org.cockpit-project.cockpit-${pkg}.metainfo.xml
done
for data in doc man pixmaps polkit-1; do
    rm -r %{buildroot}/%{_datadir}/$data
done
rm -r %{buildroot}/%{_prefix}/%{__lib}/tmpfiles.d
for libexec in cockpit-askpass cockpit-session cockpit-ws cockpit-tls cockpit-wsinstance-factory cockpit-client cockpit-client.ui cockpit-desktop cockpit-certificate-helper cockpit-certificate-ensure; do
    rm -f %{buildroot}/%{_libexecdir}/$libexec
done
rm -rf %{buildroot}/%{_sysconfdir}/pam.d %{buildroot}/%{_sysconfdir}/motd.d %{buildroot}/%{_sysconfdir}/issue.d
%if 0%{?suse_version} > 1500
rm -rf %{buildroot}/%{_pam_vendordir}
%else
rm -rf %{buildroot}/%{_sysconfdir}/pam.d
%endif
rm -f %{buildroot}/%{_libdir}/security/pam_*
rm -f %{buildroot}/usr/bin/cockpit-bridge
rm -f %{buildroot}%{_libexecdir}/cockpit-ssh
rm -f %{buildroot}%{_datadir}/metainfo/cockpit.appdata.xml
rm -rf %{buildroot}%{python3_sitelib}/cockpit*
%endif

# when not building optional packages, remove their files
%if 0%{?build_optional} == 0
for pkg in apps packagekit playground storaged; do
    rm -rf %{buildroot}/%{_datadir}/cockpit/$pkg
done
# files from -storaged
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml
%endif

%if 0%{?build_tests} == 0
rm -rf %{buildroot}%{_datadir}/cockpit/playground
rm -f %{buildroot}/%{pamdir}/mock-pam-conv-mod.so
%endif

sed -i "s|%{buildroot}||" *.list

%if 0%{?suse_version}
# remove brandings with stale symlinks. Means they don't match
# the distro.
pushd %{buildroot}/%{_datadir}/cockpit/branding
ls --hide={default,kubernetes,opensuse,registry,suse} | xargs rm -rv
popd
# need this in SUSE as post build checks dislike stale symlinks
install -m 644 -D /dev/null %{buildroot}/run/cockpit/issue

test -e %{buildroot}/usr/share/cockpit/branding/opensuse/default-1920x1200.jpg  || install -m 644 -D /dev/null %{buildroot}/usr/share/cockpit/branding/opensuse/default-1920x1200.jpg
test -e %{buildroot}/usr/share/cockpit/branding/suse/apple-touch-icon.png  || install -m 644 -D /dev/null %{buildroot}/usr/share/cockpit/branding/suse/apple-touch-icon.png
test -e %{buildroot}/usr/share/cockpit/branding/suse/default-1920x1200.png || install -m 644 -D /dev/null %{buildroot}/usr/share/cockpit/branding/suse/default-1920x1200.png

# remove files of not installable packages
rm -r %{buildroot}%{_datadir}/cockpit/sosreport
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit_project.cockpit_sosreport.metainfo.xml
rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/cockpit-sosreport.png
%else
%global _debugsource_packages 1
%global _debuginfo_subpackages 0

%define find_debug_info %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_include_minidebuginfo:-m} %{?_find_debuginfo_dwz_opts} %{?_find_debuginfo_opts} %{?_debugsource_packages:-S debugsourcefiles.list} "%{_builddir}/%{?buildsubdir}"

%endif
# /suse_version
rm -rf %{buildroot}/usr/src/debug

# On RHEL kdump, networkmanager, selinux, and sosreport are part of the system package
%if 0%{?rhel}
cat kdump.list sosreport.list networkmanager.list selinux.list >> system.list
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-networkmanager.metainfo.xml
rm -f %{buildroot}%{_datadir}/pixmaps/cockpit-sosreport.png
%endif

mkdir -p %{buildroot}%{_datadir}/cockpit/devel
cp -a pkg/lib %{buildroot}%{_datadir}/cockpit/devel

# -------------------------------------------------------------------------------
# Sub-packages

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

%files
%{_docdir}/cockpit/AUTHORS
%{_docdir}/cockpit/COPYING
%{_docdir}/cockpit/README.md
%{_datadir}/metainfo/org.cockpit_project.cockpit.appdata.xml
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/128x128/apps/cockpit.png
%doc %{_mandir}/man1/cockpit.1.gz


%package bridge
Summary: Cockpit bridge server-side component

%description bridge
The Cockpit bridge component installed server side and runs commands on the
system on behalf of the web based user interface.

%files bridge -f base.list
%doc %{_mandir}/man1/cockpit-bridge.1.gz
%{_bindir}/cockpit-bridge
%{_libexecdir}/cockpit-askpass
%{python3_sitelib}/%{name}*

%package doc
Summary: Cockpit deployment and developer guide
BuildArch: noarch

%description doc
The Cockpit Deployment and Developer Guide shows sysadmins how to
deploy Cockpit on their machines as well as helps developers who want to
embed or extend Cockpit.

%files doc
%exclude %{_docdir}/cockpit/AUTHORS
%exclude %{_docdir}/cockpit/COPYING
%exclude %{_docdir}/cockpit/README.md
%{_docdir}/cockpit

%package system
Summary: Cockpit admin interface package for configuring and troubleshooting a system
BuildArch: noarch
Requires: cockpit-bridge >= %{version}-%{release}
%if !0%{?suse_version}
Requires: shadow-utils
%endif
Requires: grep
Requires: jeos-firstboot
Requires: /usr/bin/pwscore
Requires: /usr/bin/date
Provides: cockpit-shell = %{version}-%{release}
Provides: cockpit-systemd = %{version}-%{release}
Provides: cockpit-tuned = %{version}-%{release}
Provides: cockpit-users = %{version}-%{release}
%if 0%{?rhel}
Requires: NetworkManager >= 1.6
Requires: sos
Requires: sudo
Recommends: PackageKit
Recommends: setroubleshoot-server >= 3.3.3
Recommends: kexec-tools
Suggests: NetworkManager-team
Suggests: python3-pcp
Provides: cockpit-kdump = %{version}-%{release}
Provides: cockpit-networkmanager = %{version}-%{release}
Provides: cockpit-selinux = %{version}-%{release}
Provides: cockpit-sosreport = %{version}-%{release}
%endif
Obsoletes: cockpit-tests <  %{version}
%if 0%{?fedora}
Recommends: (reportd if abrt)
%endif

#NPM_PROVIDES

%description system
This package contains the Cockpit shell and system configuration interfaces.

%files system -f system.list
%dir %{_datadir}/cockpit/shell/images

%package ws
Summary: Cockpit Web Service
Requires: glib-networking
Requires: openssl
Requires: glib2 >= 2.50.0
%if 0%{?with_selinux}
Requires: (selinux-policy >= %{_selinux_policy_version} if selinux-policy-%{selinuxtype})
Requires(post): (policycoreutils if selinux-policy-%{selinuxtype})
%endif
Conflicts: firewalld < 0.6.0-1
Recommends: sscg >= 2.3
Recommends: system-logos
Suggests: sssd-dbus
%if 0%{?suse_version}
Requires(pre): permissions
Requires: distribution-logos
%if 0%{?suse_version} > 1500
Requires: pam_oath >= 2.6.11.12
%endif
Requires: wallpaper-branding
%endif
# for cockpit-desktop
Suggests: python3
Obsoletes: cockpit-tests < 331
Provides:       group(cockpit-wsinstance-socket)
Provides:       group(cockpit-session-socket)
Provides:       user(cockpit-wsinstance-socket)
Provides:       user(cockpit-session-socket)
Provides:       user(cockpit-systemd-service)

# prevent hard python3 dependency for cockpit-desktop, it falls back to other browsers
%global __requires_exclude_from ^%{_libexecdir}/cockpit-client$

%description ws
The Cockpit Web Service listens on the network, and authenticates users.

If sssd-dbus is installed, you can enable client certificate/smart card
authentication via sssd/FreeIPA.

%files ws -f static.list
%doc %{_mandir}/man1/cockpit-desktop.1.gz
%doc %{_mandir}/man5/cockpit.conf.5.gz
%doc %{_mandir}/man8/cockpit-ws.8.gz
%doc %{_mandir}/man8/cockpit-tls.8.gz
%doc %{_mandir}/man8/pam_ssh_add.8.gz
%dir %{_sysconfdir}/cockpit
%config(noreplace) %{_sysconfdir}/cockpit/ws-certs.d
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/cockpit
%else
%config(noreplace) %{_sysconfdir}/pam.d/cockpit
%endif
# dir is not owned by pam in openSUSE
%dir %{_sysconfdir}/motd.d
# created in %post, so that users can rm the files
%ghost %{_sysconfdir}/issue.d/cockpit.issue
%ghost %{_sysconfdir}/motd.d/cockpit
%ghost %attr(0644, root, root) %{_sysconfdir}/cockpit/disallowed-users
%ghost %dir /run/cockpit
%ghost /run/cockpit/issue
%dir %{_datadir}/cockpit/issue
%{_datadir}/cockpit/issue/update-issue
%{_datadir}/cockpit/issue/inactive.issue
%{_unitdir}/cockpit.service
%{_unitdir}/cockpit-issue.service
%{_unitdir}/cockpit.socket
%{_unitdir}/cockpit-session-socket-user.service
%{_unitdir}/cockpit-session.socket
%{_unitdir}/cockpit-session@.service
%{_unitdir}/cockpit-wsinstance-http.socket
%{_unitdir}/cockpit-wsinstance-http.service
%{_unitdir}/cockpit-wsinstance-https-factory.socket
%{_unitdir}/cockpit-wsinstance-https-factory@.service
%{_unitdir}/cockpit-wsinstance-https@.socket
%{_unitdir}/cockpit-wsinstance-https@.service
%{_unitdir}/cockpit-wsinstance-socket-user.service
%{_unitdir}/system-cockpithttps.slice
%{_prefix}/%{__lib}/tmpfiles.d/cockpit-ws.conf
%{pamdir}/pam_ssh_add.so
%{pamdir}/pam_cockpit_cert.so
%{_libexecdir}/cockpit-ws
%{_libexecdir}/cockpit-wsinstance-factory
%{_libexecdir}/cockpit-tls
%{_libexecdir}/cockpit-client
%{_libexecdir}/cockpit-client.ui
%{_libexecdir}/cockpit-desktop
%{_libexecdir}/cockpit-certificate-ensure
%{_libexecdir}/cockpit-certificate-helper
%{?suse_version:%verify(not mode) }%attr(4750, root, cockpit-wsinstance-socket) %{_libexecdir}/cockpit-session
%{_datadir}/cockpit/branding
%if 0%{?with_selinux}
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%{_mandir}/man8/%{name}_session_selinux.8cockpit.*
%{_mandir}/man8/%{name}_ws_selinux.8cockpit.*
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%pre ws
# HACK: old RPM and even Fedora's current RPM don't properly support sysusers
# https://github.com/rpm-software-management/rpm/issues/3073
getent group cockpit-wsinstance-socket >/dev/null || groupadd -r cockpit-wsinstance-socket
getent group cockpit-session-socket >/dev/null || groupadd -r cockpit-session-socket
getent passwd cockpit-wsinstance-socket >/dev/null || useradd -r -g cockpit-wsinstance-socket -d /nonexisting -s /sbin/nologin -c "User for cockpit-ws instances" cockpit-wsinstance-socket
getent passwd cockpit-session-socket >/dev/null || useradd -r -g cockpit-session-socket -d /nonexisting -s /sbin/nologin -c "User for cockpit-session instances" cockpit-session-socket
getent passwd cockpit-systemd-service >/dev/null || useradd -r -g cockpit-wsinstance-socket -d /nonexisting -s /sbin/nologin -c "User for cockpit.service" cockpit-systemd-service

if %{_sbindir}/selinuxenabled 2>/dev/null; then
    %selinux_relabel_pre -s %{selinuxtype}
fi
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/cockpit ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%post ws
if [ -x %{_sbindir}/selinuxenabled ]; then
    %selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
    %selinux_relabel_post -s %{selinuxtype}
fi

# set up dynamic motd/issue symlinks on first-time install; don't bring them back on upgrades if admin removed them
# disable root login on first-time install; so existing installations aren't changed
if [ "$1" = 1 ]; then
    mkdir -p /etc/motd.d /etc/issue.d
    ln -s ../../run/cockpit/issue /etc/motd.d/cockpit
    ln -s ../../run/cockpit/issue /etc/issue.d/cockpit.issue
    printf "# List of users which are not allowed to login to Cockpit\n" > /etc/cockpit/disallowed-users
    printf "root\n" >> /etc/cockpit/disallowed-users
    chmod 644 /etc/cockpit/disallowed-users
fi

if [ "$1" = 2 ]; then
    # switch old self-signed cert group from cockpit-wsintance to cockpit-ws on upgrade
    certfile=/etc/cockpit/ws-certs.d/0-self-signed.cert
    test -f $certfile && stat -c '%G' $certfile | grep -q cockpit-wsinstance && chgrp cockpit-ws $certfile

    # on upgrades, adjust motd/issue links to changed target if they still exist (changed in 331)
    if [ "$(readlink /etc/motd.d/cockpit 2>/dev/null)" = "../../run/cockpit/motd" ]; then
        ln -sfn ../../run/cockpit/issue /etc/motd.d/cockpit
    fi
    if [ "$(readlink /etc/issue.d/cockpit.issue 2>/dev/null)" = "../../run/cockpit/motd" ]; then
        ln -sfn ../../run/cockpit/issue /etc/issue.d/cockpit.issue
    fi
fi

%if 0%{?suse_version}
%set_permissions %{_libexecdir}/cockpit-session
%endif
%tmpfiles_create cockpit-ws.conf
%systemd_post cockpit.socket cockpit.service
# firewalld only partially picks up changes to its services files without this
test -f %{_bindir}/firewall-cmd && firewall-cmd --reload --quiet || true

# check for deprecated PAM config
if test -f %{_sysconfdir}/pam.d/cockpit &&  grep -q pam_cockpit_cert %{_sysconfdir}/pam.d/cockpit; then
    echo '**** WARNING:'
    echo '**** WARNING: pam_cockpit_cert is a no-op and will be removed in a'
    echo '**** WARNING: future release; remove it from your /etc/pam.d/cockpit.'
    echo '**** WARNING:'
fi

# remove obsolete system user on upgrade (replaced with DynamicUser in version 330)
if getent passwd cockpit-wsinstance >/dev/null; then
    userdel cockpit-wsinstance
fi

%preun ws
%systemd_preun cockpit.socket cockpit.service

%postun ws
if [ -x %{_sbindir}/selinuxenabled ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%systemd_postun_with_restart cockpit.socket cockpit.service

%if 0%{?suse_version}
%verifyscript ws
%verify_permissions -e %{_libexecdir}/cockpit-session
%endif

%if 0%{?suse_version} > 1500
%posttrans ws
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/cockpit ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

# -------------------------------------------------------------------------------
# Sub-packages that are part of cockpit-system in RHEL/CentOS, but separate in Fedora

%if 0%{?rhel} == 0

%package kdump
Summary: Cockpit user interface for kernel crash dumping
Requires: cockpit-bridge >= %{required_base}
Requires: cockpit-shell >= %{required_base}
Requires: kexec-tools
BuildArch: noarch

%description kdump
The Cockpit component for configuring kernel crash dumping.

%files kdump -f kdump.list
%{_datadir}/metainfo/org.cockpit_project.cockpit_kdump.metainfo.xml

%if !0%{?suse_version}
%package sosreport
Summary: Cockpit user interface for diagnostic reports
Requires: cockpit-bridge >= %{required_base}
Requires: cockpit-shell >= %{required_base}
Requires: sos
BuildArch: noarch

%description sosreport
The Cockpit component for creating diagnostic reports with the
sosreport tool.

%files sosreport -f sosreport.list
%{_datadir}/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
%{_datadir}/pixmaps/cockpit-sosreport.png
%endif

%package networkmanager
Summary: Cockpit user interface for networking, using NetworkManager
Requires: cockpit-bridge >= %{required_base}
Requires: cockpit-shell >= %{required_base}
Requires: NetworkManager >= 1.6
Conflicts: cockpit-wicked
# Optional components
Recommends: NetworkManager-team
BuildArch: noarch

%description networkmanager
The Cockpit component for managing networking.  This package uses NetworkManager.

%files networkmanager -f networkmanager.list
%{_datadir}/metainfo/org.cockpit_project.cockpit_networkmanager.metainfo.xml

%endif

%if 0%{?rhel} == 0 && ( 0%{?suse_version} >= 1500 || 0%{?is_smo} )

%package selinux
Summary: Cockpit SELinux package
Requires: cockpit-bridge >= %{required_base}
Requires: cockpit-shell >= %{required_base}
Requires:       policycoreutils-python-utils >= 3.1
# setroubleshoot is available on SLE Micro starting with 5.5)
%if !0%{?suse_version}  || ( 0%{?is_smo} && 0%{?sle_version} >= 150500 ) || 0%{?suse_version} >= 1600
Requires:       setroubleshoot-server >= 3.3.3
%endif
BuildArch:      noarch

%description selinux
This package contains the Cockpit user interface integration with the
utility setroubleshoot to diagnose and resolve SELinux issues.

%files selinux -f selinux.list
%{_datadir}/metainfo/org.cockpit_project.cockpit_selinux.metainfo.xml

%endif

%package -n cockpit-storaged
Summary: Cockpit user interface for storage, using udisks
Requires: cockpit-shell >= %{required_base}
Requires: udisks2 >= 2.9
Requires: %{__python3}
%if 0%{?suse_version}
Requires: libudisks2-0_lvm2 >= 2.9
Requires: libudisks2-0_btrfs >= 2.9
Recommends: multipath-tools
Requires: python3-dbus-python
%else
Recommends: udisks2-lvm2 >= 2.9
Recommends: udisks2-iscsi >= 2.9
%if ! 0%{?rhel}
Recommends: udisks2-btrfs >= 2.9
%endif
Recommends: device-mapper-multipath
Recommends: clevis-luks
Requires: python3-dbus
%endif
BuildArch: noarch

%description -n cockpit-storaged
The Cockpit component for managing storage.  This package uses udisks.

%files -n cockpit-storaged -f storaged.list
%{_datadir}/metainfo/org.cockpit_project.cockpit_storaged.metainfo.xml

%post storaged
# version 332 moved the btrfs temp mounts db to /run
if [ "$1" = 2 ] && [ -d /var/lib/cockpit/btrfs ]; then
    rm -rf --one-file-system  /var/lib/cockpit/btrfs || true
fi

%package devel
Summary: Development files for for Cockpit

%description devel
This package contains files used to develop cockpit modules

%files devel
%{_datadir}/cockpit/devel

%package -n cockpit-packagekit
Summary: Cockpit user interface for packages
BuildArch: noarch
Requires: cockpit-bridge >= %{required_base}
Requires: PackageKit
Recommends: python3-tracer
# HACK: https://bugzilla.redhat.com/show_bug.cgi?id=1800468
Requires: polkit

%description -n cockpit-packagekit
The Cockpit components for installing OS updates and Cockpit add-ons,
via PackageKit.

%files -n cockpit-packagekit -f packagekit.list

# The changelog is automatically generated and merged
%changelog
