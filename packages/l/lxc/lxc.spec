#
# spec file for package lxc
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


%define         shlib_version 1
Name:           lxc
Version:        6.0.3
Release:        0
URL:            http://linuxcontainers.org/
Summary:        Userspace tools for Linux kernel containers
License:        LGPL-2.1-or-later
Group:          System/Management
Source:         https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        lxc-createconfig.in
Source90:       openSUSE-apparmor.conf
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  docbook2x
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libapparmor-devel
BuildRequires:  libcap-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  meson >= 0.61
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  dbus-1-devel
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
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package ja-doc
Summary:        Japanese documentation for %{name}
License:        LGPL-2.1-or-later
Group:          System/Management
Requires:       %{name} = %{version}
BuildArch:      noarch

%description ja-doc
Japanese language man pages for %{name}.

%package ko-doc
Summary:        Korean documentation for %{name}
License:        LGPL-2.1-or-later
Group:          System/Management
Requires:       %{name} = %{version}
BuildArch:      noarch

%description ko-doc
Korean language man pages for %{name}.

%prep
%autosetup -p1

%build
%meson \
	-D examples=false \
	-D tests=false \
	-D init-script=systemd \
	-D systemd-unitdir=%{_unitdir} \
	-D distrosysconfdir=default \
	-D pam-cgroup=true \
	-D runtime-path=%{_rundir} \
	%{nil}
%meson_build

# openSUSE-specific templated files.
# TODO: Switch this be done properly with meson (unfortunately meson doesn't
# have an equivalent to "config.status --file" (which lets you do variable
# replacement on arbitray files not included in the project config).
sed -i 's|@LXCTEMPLATEDIR@|%{_datadir}/lxc/templates|g' %{S:3}

%install
%meson_install
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}

# openSUSE-specific helpers and configuration.
install -D -m 0755 %{S:3} %{buildroot}%{_bindir}/lxc-createconfig
install -D -m 0644 %{S:90} %{buildroot}%{_datadir}/%{name}/config/common.conf.d/30-openSUSE-apparmor.conf

# sysv-init compat wrappers.
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-net

# Clean up.
find %{buildroot} -type f -name '*.la' -delete
find %{buildroot} -type f -name '*.a' -delete
%fdupes %{buildroot}

%pre
%service_add_pre lxc@.service lxc.service lxc-net.service lxc-monitord.service

%post
#restart_on_update apparmor - but non-broken (bnc#853019)
systemctl is-active -q apparmor && systemctl reload apparmor ||:
%service_add_post lxc@.service lxc.service lxc-net.service lxc-monitord.service

%preun
%service_del_preun lxc@.service lxc.service lxc-net.service lxc-monitord.service

%postun
%service_del_postun lxc@.service lxc.service lxc-net.service lxc-monitord.service

%post -n liblxc%{shlib_version}
/sbin/ldconfig
%set_permissions %{_libexecdir}/%{name}/lxc-user-nic

%postun -n liblxc%{shlib_version} -p /sbin/ldconfig

%verifyscript -n liblxc%{shlib_version}
%verify_permissions -e %{_libexecdir}/%{name}/lxc-user-nic

%check

%files
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
%{_unitdir}/%{name}*.service

# AppArmor profiles specifically for the lxc binaries.
%config %{_sysconfdir}/apparmor.d/usr.bin.lxc-*

%files -n pam_cgfs
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1699
%{_pam_moduledir}/pam_cgfs.so
%else
%dir /%{_libdir}/security/
/%{_libdir}/security/pam_cgfs.so
%endif

%files -n liblxc%{shlib_version}
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
%attr(04750,root,kvm) %{_libexecdir}/%{name}/lxc-user-nic

# AppArmor profiles and templates related to LXC.
%dir %{_sysconfdir}/apparmor.d/lxc
%dir %{_sysconfdir}/apparmor.d/abstractions/lxc
%config %{_sysconfdir}/apparmor.d/abstractions/lxc/*
%config %{_sysconfdir}/apparmor.d/lxc-*
%config %{_sysconfdir}/apparmor.d/lxc/*

%files -n liblxc-devel
%{_libdir}/lib%{name}.so
%{_includedir}/%name/
%{_libdir}/pkgconfig/%{name}.pc

%files bash-completion
%{_datadir}/bash-completion/

%files ja-doc
%{_mandir}/ja/

%files ko-doc
%{_mandir}/ko/

%changelog
