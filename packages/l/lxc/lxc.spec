#
# spec file for package lxc
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


# On pre-15 SLE versions, _sharedstatedir was /usr/com -- which is just wrong.
%if 0%{?suse_version} < 1500
%define _sharedstatedir /var/lib
%endif

# In later versions of openSUSE's permissions config, lxc-user-nic was
# whitelisted with a setuid bit enabled -- but in order to allow building on
# old distros we must not make it setuid on pre-15.1 distros. See bsc#988348.
%if 0%{suse_version} <= 1500 && 0%{?sle_version} < 150100
%define old_permissions 1
%endif
%define setuid_mode 0%{!?old_permissions:4}750

# XXX: Really should be included (in some form) in standard openSUSE macros.
#      suse_install_update_message is useless for subpackages.
%define _updatemessagedir      /var/adm/update-messages

%define         shlib_version 1
Name:           lxc
Version:        4.0.2
Release:        0
URL:            http://linuxcontainers.org/
Summary:        Userspace tools for Linux kernel containers
License:        LGPL-2.1-or-later
Group:          System/Management
Source:         https://linuxcontainers.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://linuxcontainers.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        lxc-createconfig.in
Source90:       openSUSE-apparmor.conf
Source91:       missing_setuid.txt.in
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libapparmor-devel
BuildRequires:  libcap-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkg-config
%ifarch %ix86 x86_64
BuildRequires:  libseccomp-devel
%endif
BuildRequires:  bash-completion
BuildRequires:  docbook-utils
BuildRequires:  docbook2x
BuildRequires:  fdupes
BuildRequires:  libxslt
BuildRequires:  pkgconfig(systemd)
Requires:       libcap-progs
Requires:       lxcfs
Requires:       lxcfs-hooks-lxc
Requires:       rsync
%{?systemd_ordering}
# Needed to create openSUSE containers using template.
Recommends:     build
Recommends:     criu >= 2.0

%description
LXC is the well-known and heavily tested low-level Linux container runtime.

%package -n pam_cgfs
Summary:        PAM module to provide unprivileged cgroupfs
License:        LGPL-2.1-only
Group:          System/Libraries
Supplements:    lxc

%description -n pam_cgfs
When a user logs in, this PAM module will create cgroups which the user may
administer, either for all controllers or for any controllers listed on the
command line.

%package -n liblxc%{shlib_version}
Summary:        LXC container runtime library
License:        LGPL-2.1-only
Group:          System/Libraries
Requires(pre):  permissions
Requires(post): permissions
Requires(post): findutils
# Older SLE versions didn't have -abstractions but instead had -profiles
# (though Leap has -abstractions regardless of it being based on SLE). We only
# need them to not have to own /etc/apparmor.d/abstractions.
%if 0%{?is_opensuse} || 0%{?suse_version} >= 1500
BuildRequires:  apparmor-abstractions
%else
BuildRequires:  apparmor-profiles
%endif

%description -n liblxc%{shlib_version}
This package provides the LXC container runtime library.

%package -n liblxc-devel
Summary:        LXC container runtime library development files
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       liblxc%{shlib_version} = %version

%description -n liblxc-devel
This package provides the LXC container runtime library development files.

%package bash-completion
Summary:        Bash Completion for %{name}
License:        LGPL-2.1-or-later
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%prep
%setup

%build
./autogen.sh
%configure \
	--enable-pam \
	--disable-static \
	--disable-examples \
	--disable-rpath \
	--with-init-script=systemd \
	--with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}

# Ensure that shlib_version was correct.
lxc_api_version="$(echo "@LXC_ABI_MAJOR@" | ./config.status --file -)"
[ "$lxc_api_version" = "%{shlib_version}" ]

# openSUSE-specific templated files.
./config.status --file=lxc-createconfig:%{S:3}
./config.status --file=missing_setuid.txt:%{S:91}

# Add an additional warning header if the distro is old enough that
# /etc/permissions should already be whitelisting lxc-user-nic.
%if ! 0%{?old_permissions}
patch missing_setuid.txt <<EOF
--- a/missing_setuid.txt
+++ b/missing_setuid.txt
@@ -0,0 +1,4 @@
+NOTE: It appears you are running on a new-enough distribution that this warning
+      should not have appeared. If you are not using a "paranoid" profile,
+      please report this as a bug using <https://bugs.opensuse.org/>.
+
EOF
%endif

%install
%make_install
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}

# openSUSE-specific helpers and configuration.
install -D -m 0755 lxc-createconfig %{buildroot}%{_bindir}/lxc-createconfig
install -D -m 0644 %{S:90} %{buildroot}%{_datadir}/%{name}/config/common.conf.d/30-openSUSE-apparmor.conf

# sysv-init compat wrappers.
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-net

# Install bash-completion. Note that we have to install a symlink for every
# lxc-* command because bash-completion relies on the binary name to pick the
# bash-completion script.
install -D -m 0644 config/bash/lxc %{buildroot}%{_datadir}/bash-completion/completions/_%{name}
for bin in $(find src/lxc/lxc-* -executable -print0 | xargs -n1 -0 basename)
do
	ln -s "_%{name}" "%{buildroot}%{_datadir}/bash-completion/completions/$bin"
done
# lxc installs bash-completion to the wrong location.
rm -f %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

# Clean up.
find %{buildroot} -type f -name '*.la' -delete
%fdupes %{buildroot}

%pre
%service_add_pre lxc@.service lxc.service lxc-net.service

%post
#restart_on_update apparmor - but non-broken (bnc#853019)
systemctl is-active -q apparmor && systemctl reload apparmor ||:
%service_add_post lxc@.service lxc.service lxc-net.service

%preun
%service_del_preun lxc@.service lxc.service lxc-net.service

%postun
%service_del_postun lxc@.service lxc.service lxc-net.service

%post -n liblxc%{shlib_version}
/sbin/ldconfig
%set_permissions %{_libexecdir}/%{name}/lxc-user-nic

# Remove any existing update messages if we're reinstalling. I'm a bit
# surprised this isn't done automatically. We don't do this on postun because
# we should keep around past package update messages.
[ "$1" -gt 1 ] && \
	find %{_updatemessagedir} -xtype f \
		-name 'liblxc%{shlib_version}-%{version}-%{release}-*.txt' -delete

# If lxc-user-nic doesn't have setuid we need to copy the update-message.
[ -u %{_libexecdir}/%{name}/lxc-user-nic ] ||
	cp %{_defaultdocdir}/liblxc%{shlib_version}/missing_setuid.txt \
	   %{_updatemessagedir}/liblxc%{shlib_version}-%{version}-%{release}-missing_setuid.txt

%postun -n liblxc%{shlib_version} -p /sbin/ldconfig

%verifyscript -n liblxc%{shlib_version}
%verify_permissions -e %{_libexecdir}/%{name}/lxc-user-nic

%files
%defattr(-,root,root)
%doc doc/FAQ.txt

# Configuration for LXC.
%dir %{_sysconfdir}/%{name}/
%config %{_sysconfdir}/%{name}/default.conf
%config(noreplace) %{_sysconfdir}/default/%{name}
%{_datadir}/%{name}/

# Binaries, man pages, and service files.
%{_bindir}/lxc-*
%{_sbindir}/init.lxc
%{_sbindir}/rclxc
%{_sbindir}/rclxc-net
%{_mandir}/man[^3]/*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-net.service
%{_unitdir}/%{name}@.service

# AppArmor profiles specifically for the lxc binaries.
%config %{_sysconfdir}/apparmor.d/usr.bin.lxc-*

%files -n pam_cgfs
%defattr(-,root,root)
/%{_lib}/security/pam_cgfs.so

%files -n liblxc%{shlib_version}
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS
%license COPYING
%{_libdir}/lib%{name}.so.*

# In addition to liblxc, there are a bunch of configuration and runtime
# directories that are implicitly required by liblxc. We have to expose these
# here, as opposed to the lxc package so that LXD (and others) can make use of
# it.

# Runtime-related directories.
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/rootfs/
%dir %{_sharedstatedir}/%{name}
%{_libexecdir}/%{name}/
# Make sure lxc-user-nic has the right mode.
%attr(%{setuid_mode},root,kvm) %{_libexecdir}/%{name}/lxc-user-nic

# AppArmor profiles and templates related to LXC.
%dir %{_sysconfdir}/apparmor.d/lxc
%dir %{_sysconfdir}/apparmor.d/abstractions/lxc
%config %{_sysconfdir}/apparmor.d/abstractions/lxc/*
%config %{_sysconfdir}/apparmor.d/lxc-*
%config %{_sysconfdir}/apparmor.d/lxc/*

# In order to avoid fun issues with update-messages we store update-messages in
# docdir and then copy them in post to /var/adm/update-messages if it makes
# sense.
%doc missing_setuid.txt

%files -n liblxc-devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_includedir}/%name/
%{_libdir}/pkgconfig/%{name}.pc

%files bash-completion
%defattr(-,root,root)
%{_datadir}/bash-completion/

%changelog
