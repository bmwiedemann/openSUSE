#
# spec file
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%if 0%{?_build_in_place}
# Allow users to specify the version and the release when building the rpm in
# place. When not provided we look for the version in meson.version (introduced
# in v256).
%define systemd_version    %{?version_override}%{!?version_override:%(cat meson.version)}
%define systemd_release    %{?release_override}%{!?release_override:0}
%define archive_version    %{nil}
%else
%define systemd_version    255.7
%define systemd_release    0
%define archive_version    +suse.33.g603cd1d4d8
%endif

%define systemd_major      %{sub %systemd_version 1 3}

%define _testsuitedir %{_systemd_util_dir}/tests
%define xinitconfdir  %{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}/X11/xinit

# Similar to %%with but return true/false. The value when the condition is
# verified can be redefined when a second parameter is passed.
%define __when_1() %{expand:%%{?with_%{1}:true}%%{!?with_%{1}:false}}
%define __when_2() %{expand:%%{?with_%{1}:%{2}}%%{!?with_%{1}:false}}
%define when()     %{expand:%%__when_%# %{*}}

%define __when_not_1() %{expand:%%{?with_%{1}:false}%%{!?with_%{1}:true}}
%define __when_not_2() %{expand:%%{?with_%{1}:false}%%{!?with_%{1}:%{2}}}
%define when_not()     %{expand:%%__when_not_%# %{*}}

# Same as above but return enabled/disabled instead.
%define disabled_with()  %{expand:%%{?with_%{1}:disabled}%%{!?with_%{1}:enabled}}
%define enabled_with()   %{expand:%%{?with_%{1}:enabled}%%{!?with_%{1}:disabled}}

%if "%{flavor}" == "mini"
%global mini -mini
%global with_bootstrap 1
%else
%global mini %nil
%bcond_without  apparmor
%bcond_without  coredump
%bcond_without  homed
%bcond_without  importd
%bcond_without  journal_remote
%bcond_without  machined
%bcond_without  networkd
%bcond_without  portabled
%bcond_without  resolved
%ifarch %{ix86} x86_64 aarch64
%bcond_without  sd_boot
%else
%bcond_with     sd_boot
%endif
%bcond_without  selinux
%bcond_without  sysvcompat
%bcond_without  experimental
%bcond_without  testsuite
%endif

%bcond_with upstream

# The following features are kept to ease migrations toward SLE. Their default
# value is independent of the build flavor.
%bcond_without  filetriggers

# We stopped shipping main config files in /etc but we have to restore any
# config files that might have been backed up by rpm during the migration of the
# main config files from /etc to /usr. This needs to be done in %%posttrans
# because the .rpmsave files are created when the *old* package version is
# removed. This is not needed by ALP and will be dropped from Factory near the
# end of 2024.
%define restore_rpmsave() \
if [ -e %{_sysconfdir}/%{1}.rpmsave ] && [ ! -e %{_sysconfdir}/%{1} ]; then \
        echo >&2 "Restoring %{_sysconfdir}/%1. Please consider moving your customizations in a drop-in instead." \
        echo >&2 "For more details, visit https://en.opensuse.org/Systemd#Configuration." \
        mv -v %{_sysconfdir}/%{1}.rpmsave %{_sysconfdir}/%{1} || : \
fi \
%{nil}

Name:           systemd%{?mini}
URL:            http://www.freedesktop.org/wiki/Software/systemd
Version:        %systemd_version
Release:        %systemd_release
Summary:        A System and Session Manager
License:        LGPL-2.1-or-later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{without bootstrap}
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  docbook-xsl-stylesheets
%if %{with apparmor}
BuildRequires:  libapparmor-devel
%endif
BuildRequires:  libgcrypt-devel
BuildRequires:  libxslt-tools
BuildRequires:  polkit
# python is only required for generating systemd.directives.xml
BuildRequires:  python3-base
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libseccomp) >= 2.3.1
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux) >= 2.1.9
%endif
BuildRequires:  pkgconfig(libzstd)
%endif
BuildRequires:  fdupes
BuildRequires:  gperf
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libmount-devel >= 2.27.1
BuildRequires:  meson >= 0.53.2
BuildRequires:  pam-devel
BuildRequires:  python3-Jinja2
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(blkid) >= 2.26
# The following packages are only required by the execution of the unit tests during %%check
BuildRequires:  acl
BuildRequires:  distribution-release
BuildRequires:  python3-pefile
BuildRequires:  timezone

%if %{with bootstrap}
#!BuildIgnore:  dbus-1
Provides:       systemd = %{version}-%{release}
Conflicts:      systemd
# Don't consider the mini flavors when building kiwi medias. This conflict is
# automatically inherited by sub-packages requiring systemd (such as udev).
Conflicts:      kiwi
# This dependency is used to ensure that the mini flavors are selected only
# inside OBS builds (where this dependency is ignored) and don't get installed
# on real systems.
Requires:       this-is-only-for-build-envs
%else
# the buildignore is important for bootstrapping
#!BuildIgnore:  udev
Requires:       aaa_base >= 13.2
Requires:       dbus-1 >= 1.4.0
Requires:       kbd
Requires:       netcfg >= 11.5
Requires:       systemd-default-settings-branding
Requires:       systemd-presets-branding
Requires:       util-linux >= 2.27.1
Requires(post): coreutils
Requires(post): findutils
Requires(post): systemd-presets-branding
Requires(post): pam-config >= 0.79-5
# These weak dependencies because some features are optional and enabled at
# runtime with the presence of the relevant libs.
Recommends:     libpcre2-8-0
Recommends:     libbpf1
%endif
Provides:       group(systemd-journal)
Conflicts:      filesystem < 11.5
Provides:       sbin_init
Provides:       sysvinit:/sbin/init
Conflicts:      sbin_init
Conflicts:      sysvinit
Obsoletes:      nss-systemd < %{version}-%{release}
Provides:       nss-systemd = %{version}-%{release}
Obsoletes:      nss-myhostname < %{version}-%{release}
Provides:       nss-myhostname = %{version}-%{release}
Provides:       systemd-logger = %{version}-%{release}
Obsoletes:      systemd-logger < %{version}-%{release}
Provides:       systemd-sysvinit = %{version}-%{release}
Obsoletes:      systemd-sysvinit < %{version}-%{release}
Provides:       systemd-analyze = %{version}-%{release}
Obsoletes:      pm-utils <= 1.4.1
Obsoletes:      suspend <= 1.0
Obsoletes:      systemd-analyze < 201
Source0:        systemd-v%{version}%{archive_version}.tar.xz
Source1:        systemd-rpmlintrc
Source3:        systemd-update-helper
%if %{with sysvcompat}
Source4:        systemd-sysv-install
%endif
Source5:        tmpfiles-suse.conf
Source6:        baselibs.conf
Source7:        triggers.systemd
Source8:        pam.systemd-user
Source14:       kbd-model-map.legacy

Source100:      fixlet-container-post.sh
Source101:      fixlet-systemd-post.sh

Source200:      files.systemd
Source201:      files.udev
Source202:      files.container
Source203:      files.network
Source204:      files.devel
Source205:      files.sysvcompat
Source206:      files.uefi-boot
Source207:      files.experimental
Source208:      files.coredump
Source209:      files.homed
Source210:      files.lang
Source211:      files.journal-remote
Source212:      files.portable
Source213:      files.devel-doc

#
# All changes backported from upstream are tracked by the git repository, which
# can be found at:  https://github.com/openSUSE/systemd.
#
# Patches listed below are openSUSE specific ones and should be kept at its
# minimum. We try hard to push our changes to upstream but sometimes they are
# only relevant for SUSE distros. Special rewards for those who will manage to
# get rid of one of them !
#
Patch:          0001-Drop-support-for-efivar-SystemdOptions.patch
Patch:          0009-pid1-handle-console-specificities-weirdness-for-s390.patch
%if %{with sysvcompat}
Patch:          0002-rc-local-fix-ordering-startup-for-etc-init.d-boot.lo.patch
Patch:          0008-sysv-generator-translate-Required-Start-into-a-Wants.patch
%endif

%if %{without upstream}
# Patches listed below are put in quarantine. Normally all changes must go to
# upstream first and then are cherry-picked in the SUSE git repository. But for
# very few cases, some stuff might be broken in upstream and need to be fixed or
# worked around quickly. In these cases, the patches are added temporarily and
# will be removed as soon as a proper fix will be merged by upstream.
Patch:          5001-Revert-udev-update-devlink-with-the-newer-device-nod.patch
Patch:          5002-Revert-udev-revert-workarounds-for-issues-caused-by-.patch
Patch:          5003-Revert-run-pass-the-pty-slave-fd-to-transient-servic.patch
%endif

%description
Systemd is a system and service manager, compatible with SysV and LSB
init scripts for Linux. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system state,
maintains mount and automount points and implements an elaborate
transactional dependency-based service control logic. It can work as a
drop-in replacement for sysvinit.

%package devel
Summary:        Development files for libsystemd and libudev
License:        LGPL-2.1-or-later
Requires:       libsystemd0%{?mini} = %{version}-%{release}
Requires:       libudev%{?mini}1 = %{version}-%{release}
Requires:       systemd-rpm-macros
Provides:       libudev%{?mini}-devel = %{version}-%{release}
Obsoletes:      libudev%{?mini}-devel < %{version}-%{release}
%if %{with bootstrap}
Provides:       systemd-devel = %{version}-%{release}
Conflicts:      systemd-devel
Provides:       libudev-devel = %{version}-%{release}
Conflicts:      libudev-devel
%endif

%description devel
Development headers and files for libsystemd and libudev libraries for
developing and building applications linking to these libraries.

%if %{with sysvcompat}
%package sysvcompat
Summary:        SySV and LSB init script support for systemd (deprecated)
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
Provides:       systemd-sysvinit:%{_sbindir}/runlevel
Provides:       systemd-sysvinit:%{_sbindir}/telinit

%description sysvcompat
This package ships the necessary files that enable minimal SysV and LSB init
scripts support in systemd. It also contains the obsolete SysV init tools
telinit(8) and runlevel(8). You should consider using systemctl(1) instead.

Unless you have a 3rd party application installed on your system that still
relies on such scripts, this package should not be needed at all.

Please note that the content of this package is considered as deprecated.
%endif

%package -n libsystemd0%{?mini}
Summary:        Component library for systemd
License:        LGPL-2.1-or-later
%if %{with bootstrap}
Conflicts:      kiwi
Conflicts:      libsystemd0
Provides:       libsystemd0 = %{version}-%{release}
Requires:       this-is-only-for-build-envs
%endif

%description -n libsystemd0%{?mini}
This library provides several of the systemd C APIs:

* sd-bus implements an alternative D-Bus client library that is
  relatively easy to use, very efficient and supports both classic
  D-Bus as well as kdbus as transport backend.

* sd-daemon(3): for system services (daemons) to report their status
  to systemd and to make easy use of socket-based activation logic

* sd-event is a generic event loop abstraction that is built around
  Linux epoll, but adds features such as event prioritization or
  efficient timer handling.

* sd-id128(3): generation and processing of 128-bit IDs

* sd-journal(3): API to submit and query journal log entries

* sd-login(3): APIs to introspect and monitor seat, login session and
  user status information on the local system.

%package -n udev%{?mini}
Summary:        A rule-based device node and kernel event manager
License:        GPL-2.0-only
URL:            http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
Requires:       %{name} = %{version}-%{release}
%systemd_requires
Requires:       filesystem
%if %{without bootstrap}
# kmod executable is needed by kmod-static-nodes.service
Requires:       kmod
# By v256 libkmod will be dlopen()ed.
Requires:       libkmod2
%endif
Requires:       system-group-hardware
Requires:       group(kvm)
Requires:       group(lp)
# The next dependency is also needed with file-triggers enabled due to the way
# the libzypp default transaction backend works.
Requires(pre):  group(kvm)
Requires(post): sed
Requires(post): coreutils
Requires(postun):coreutils
# 'regenerate_initrd_post' macro is expanded during build, hence this BR.
BuildRequires:  suse-module-tools
%if %{without bootstrap}
# fdisk is a build requirement for repart
BuildRequires:  pkgconfig(fdisk)
BuildRequires:  pkgconfig(libcryptsetup) >= 1.6.0
BuildRequires:  pkgconfig(libkmod) >= 15
# Enable fido2 and tpm supports in systemd-cryptsetup, systemd-enroll. However
# these tools are not linked against the libs directly but instead are
# dlopen()ed at runtime to avoid hard dependencies. Hence the use of soft
# dependencies.
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
Recommends:     libfido2
Recommends:     libtss2-esys0
Recommends:     libtss2-mu0
Recommends:     libtss2-rc0
%endif
Conflicts:      ConsoleKit < 0.4.1
Conflicts:      dracut < 059
Conflicts:      filesystem < 11.5
Conflicts:      util-linux < 2.16
%if %{with bootstrap}
Conflicts:      udev
Provides:       udev = %{version}-%{release}
%endif
%if %{with upstream}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(xencontrol)
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     libarchive13
Recommends:     libxkbcommon0
%endif

%description -n udev%{?mini}
This package provides systemd-udevd. The udev daemon receives device uevents
directly from the kernel whenever it adds or removes a device from the system in
/dev, or it changes its state. When udev receives a device event, it matches its
configured set of rules, located in %{_udevrulesdir}/, against various device
attributes to identify the device. Rules that match may adjust device node
permissions, create meaningful symlink names or provide additional device
information to be stored in the udev database.

The udev daemon may also rename network interfaces and perform various network
device configurations, see systemd.link(5) for more details.

This package also provides various tools and services that operate on devices
exclusively. For example it contains systemd-cryptsetup to manage encrypted
block devices as well as systemd-growfs to instruct the kernel to grow the
mounted filesystem to full size of the underlying block device.

This package shouldn't be necessary in containers.

%package -n libudev%{?mini}1
Summary:        Dynamic library to access udev device information
License:        LGPL-2.1-or-later
%if %{with bootstrap}
Conflicts:      kiwi
Conflicts:      libudev1
Provides:       libudev1 = %{version}-%{release}
Requires:       this-is-only-for-build-envs
%endif

%description -n libudev%{?mini}1
This package contains the dynamic library libudev, which provides
access to udev device information

%if %{with coredump}
%package coredump
Summary:        Systemd tools for coredump management
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires
Provides:       systemd:%{_bindir}/coredumpctl

%description coredump
Systemd tools to store and manage coredumps.

Visit https://systemd.io/COREDUMP for more details.
%endif

%if %{with sd_boot}
%package boot
Summary:        A simple UEFI boot manager
License:        LGPL-2.1-or-later
BuildRequires:  pesign-obs-integration
BuildRequires:  python3-pyelftools

%description boot
This package provides systemd-boot (short: sd-boot), which is a simple UEFI boot
manager. It provides a textual menu to select the entry to boot and an editor
for the kernel command line. systemd-boot supports systems with UEFI firmware
only.

This package also contains bootctl(1) and services to manage boot loaders that
implement the Boot Loader Specification[1] and the Boot Loader Interface[2] on
EFI systems, such as systemd-boot.

Note that systemd-boot is not fully integrated in openSUSE distributions yet
hence its installation requires special care and manual steps when used on
systems supporting secure boot or snapshots. For more details, visit:
https://en.opensuse.org/Systemd-boot

[1] https://uapi-group.org/specifications/specs/boot_loader_specification/
[2] https://systemd.io/BOOT_LOADER_INTERFACE/
%endif

%package container
Summary:        Systemd tools for container management
License:        LGPL-2.1-or-later
%if %{with importd}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
%endif
Requires:       %{name} = %{version}-%{release}
# import-tar needs tar and gpg
Requires:       /usr/bin/tar
Requires:       /usr/bin/gpg
%systemd_requires
Obsoletes:      nss-mymachines < %{version}-%{release}
Provides:       nss-mymachines = %{version}-%{release}
Provides:       systemd-container = %{version}-%{release}
Provides:       systemd:%{_bindir}/systemd-nspawn
%if %{with bootstrap}
Conflicts:      systemd-container
Provides:       systemd-container = %{version}-%{release}
%endif

%description container
Systemd tools to spawn and manage containers and virtual machines.

In addition, it also contains a plugin for the Name Service Switch (NSS),
providing host name resolution for all local containers and virtual machines
using network namespacing and registered with systemd-machined. It also maps
UID/GIDs ranges used by containers to useful names.

To activate this NSS module, you will need to include it in /etc/nsswitch.conf,
see nss-mymachines(8) manpage for more details.

%if %{with networkd} || %{with resolved}
%package network
Summary:        Systemd Network And Network Name Resolution Managers
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires
# This Recommends because some symbols of libidn2 are dlopen()ed by resolved
Recommends:     pkgconfig(libidn2)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(openssl)
Obsoletes:      nss-resolve < %{version}-%{release}
Provides:       nss-resolve = %{version}-%{release}
Provides:       systemd:/usr/lib/systemd/systemd-networkd
Provides:       systemd:/usr/lib/systemd/systemd-resolved

%description network
systemd-networkd is a system service that manages networks. It detects and
configures network devices as they appear, as well as manages network addresses
and routes for any link for which it finds a .network file, see
systemd.network(5). It can also create virtual network devices based on their
description given by systemd.netdev(5) files. It may be controlle by
networkctl(1).

systemd-resolved is a system service that provides network name resolution to
local applications. It implements a caching and validating DNS/DNSSEC stub
resolver, as well as an LLMNR and MulticastDNS resolver and responder. It may be
controlled by resolvectl(1).

Addtionally, this package also contains a plug-in module for the Name Service
Switch (NSS), which enables hostname resolutions by contacting
systemd-resolved(8). It replaces the nss-dns plug-in module that traditionally
resolves hostnames via DNS.

To activate this NSS module, you will need to include it in /etc/nsswitch.conf,
see nss-resolve(8) manpage for more details.
%endif

%if %{with homed}
%package homed
Summary:        Home Area/User Account Manager
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires
BuildRequires:  pkgconfig(fdisk)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pwquality)
# These Recommends because some symbols of these libs are dlopen()ed by homed
Recommends:     libfido2
Recommends:     libpwquality1
Recommends:     libqrencode4

%description homed
This package contains systemd-homed.service, a system service that manages home
directories of users. The home directories managed are self-contained, and thus
include the user's full metadata record in the home's data storage itself,
making them easy to migrate between machines; the user account and home
directory becoming the same concept.

This package also includes homectl(1), a tool to interact with systemd-homed and
PAM module to automatically mount home directories on user login.

See homectl(1) man page for instructions to create a new user account.

A description of the various storage mechanisms implemented by systemd-homed can
be found at https://systemd.io/HOME_DIRECTORY/.

Note that nss-systemd has still not been integrated into nsswitch and therefore
needs to be added manually into /etc/nsswitch.conf, see nss-systemd(8) man page
for an example on how to do that.
%endif

%if %{with portabled}
%package portable
Summary:        Systemd tools for portable services
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires

%description portable
Systemd tools to manage portable services. The feature is still considered
experimental so the package might change or vanish.  Use at own risk.

More information can be found online:

http://0pointer.net/blog/walkthrough-for-portable-services.html
https://systemd.io/PORTABLE_SERVICES
%endif

%if %{with journal_remote}
%package journal-remote
Summary:        Gateway for serving journal events over the network using HTTP
License:        LGPL-2.1-or-later
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.33
Requires:       %{name} = %{version}-%{release}
%systemd_requires

%description journal-remote
This extends the journal functionality to keep a copy of logs on a
remote server by providing programs to forward journal entries over
the network, using encrypted HTTP, and to write journal files from
serialized journal contents.

This package contains systemd-journal-gatewayd,
systemd-journal-remote, and systemd-journal-upload.
%endif

%if %{with testsuite}
%package testsuite
Summary:        Testsuite for systemd
License:        LGPL-2.1-or-later
Recommends:     python3
Recommends:     python3-colorama
# Optional dep for mkfs.vfat needed by test-loop-block (otherwise skipped)
Recommends:     dosfstools
# Optional deps needed by TEST-70-TPM2 (otherwise skipped)
Recommends:     swtpm
Recommends:     tpm2.0-tools
%if %{with resolved}
# Optional dep for knot needed by TEST-75-RESOLVED
Recommends:     knot
%if %{with selinux}
# Optional deps needed by TEST-06-SELINUX (otherwise skipped)
Recommends:     selinux-policy-devel
Recommends:     selinux-policy-targeted
%endif
# System users/groups that some tests rely on.
Requires:       group(bin)
Requires:       group(daemon)
Requires:       group(games)
Requires:       group(nobody)
Requires:       user(bin)
Requires:       user(daemon)
Requires:       user(games)
Requires:       user(nobody)
# The following deps on libs are for test-dlopen-so whereas the pkgconfig ones
# are used by test-funtions to find the libs on the host and install them in the
# image, see install_missing_libraries() for details.
Requires:       libidn2
Requires:       pkgconfig(libidn2)
%endif
%if %{with experimental}
Requires:       libpwquality1
Requires:       libqrencode4
Requires:       pkgconfig(libqrencode)
Requires:       pkgconfig(pwquality)
%endif
Requires:       %{name} = %{version}-%{release}
Requires:       attr
Requires:       binutils
Requires:       busybox-static
Requires:       cryptsetup
Requires:       dhcp-client
Requires:       dosfstools
Requires:       iproute2
Requires:       jq
Requires:       libcap-progs
Requires:       libfido2
Requires:       libtss2-esys0
Requires:       libtss2-mu0
Requires:       libtss2-rc0
Requires:       lz4
Requires:       make
Requires:       mtools
Requires:       netcat
Requires:       python3-pexpect
Requires:       qemu
Requires:       quota
Requires:       socat
Requires:       squashfs
Requires:       systemd-container
Requires:       pkgconfig(libfido2)
Requires:       pkgconfig(tss2-esys)
Requires:       pkgconfig(tss2-mu)
Requires:       pkgconfig(tss2-rc)
%if %{with sd_boot}
Requires:       systemd-boot
%endif
%if %{with coredump}
Requires:       systemd-coredump
%endif
%if %{with experimental}
Requires:       systemd-experimental
%endif
%if %{with homed}
Requires:       systemd-homed
%endif
%if %{with journal_remote}
Requires:       systemd-journal-remote
%endif
%if %{with networkd}
Requires:       systemd-network
%endif
%if %{with portabled}
Requires:       systemd-portable
%endif
Requires:       xz

%description testsuite
This package contains the unit tests as well as the extended testsuite. The unit
tests are used to check various internal functions used by systemd whereas the
extended testsuite is used to test various functionalities of systemd and all
its components.

Note that you need root privileges to run the extended testsuite.

Run the following python script to run all unit tests at once:
$ %{_testsuitedir}/run-unit-tests.py

To run the full extended testsuite do the following:
$ NO_BUILD=1 TEST_NESTED_VM=1 %{_testsuitedir}/integration-tests/run-integration-tests.sh

Or to run one specific integration test:
$ NO_BUILD=1 TEST_NESTED_VM=1 make -C %{_testsuitedir}/integration-tests/TEST-01-BASIC clean setup run

For more details on the available options to run the extended testsuite, please
refer to %{_testsuitedir}/integration-tests/README.testsuite.
%endif

%if %{with experimental}
%package experimental
Summary:        Experimental systemd features
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires

%description experimental
This package contains optional extra services that are considered as previews
and are provided so users can do early experiments with the new features or
technologies without waiting for them to be fully supported by both upstream
and openSUSE.

Please note that all services should be considered in development phase and as
such their behaviors details, unit files, option names, etc... are subject to
change without the usual backwards-compatibility promises.

Components that turn out to be stable and considered as fully supported will be
merged into the main package or moved into a dedicated package.

Currently this package contains: bsod, oomd, measure, pcrextend, pcrlock,
storagetm, sysupdate, tpm2-setup, userwork and ukify.

Have fun (at your own risk).
%endif

%if %{without bootstrap}
%lang_package

%package doc
Summary:        Additional documentation or doc formats for systemd
License:        LGPL-2.1-or-later
BuildArch:      noarch

%description doc
A HTML version of the systemd documentation, plus the manual pages
for the C APIs.
%endif

%prep
%autosetup -p1 -n systemd-v%{version}%{archive_version}

%build
%meson \
        -Dmode=release \
        -Dversion-tag=%{version}%{archive_version} \
        -Ddocdir=%{_docdir}/systemd \
        -Dconfigfiledir=/usr/lib \
        -Dsplit-bin=true \
        -Dsystem-uid-max=499 \
        -Dsystem-gid-max=499 \
        -Dclock-valid-range-usec-max=946728000000000 \
        -Dadm-group=false \
        -Dwheel-group=false \
        -Dgroup-render-mode=0660 \
        -Dutmp=false \
        -Ddefault-hierarchy=unified \
        -Ddefault-kill-user-processes=false \
        -Dpamconfdir=no \
        -Dpamlibdir=%{_pam_moduledir} \
        -Dxinitrcdir=%{xinitconfdir}/xinitrc.d \
        -Drpmmacrosdir=no \
        -Dcertificate-root=%{_sysconfdir}/pki/systemd \
%if %{with bootstrap}
        -Dbashcompletiondir=no \
        -Dzshcompletiondir=no \
%endif
%if %{without sysvcompat}
        -Dsysvinit-path= \
        -Dsysvrcnd-path= \
%else
        -Drc-local=/etc/init.d/boot.local \
%endif
        -Dcreate-log-dirs=false \
        -Ddebug-shell=/bin/bash \
        \
        -Dbump-proc-sys-fs-nr-open=false \
        -Ddbus=disabled \
        -Ddefault-network=false \
        -Dglib=disabled \
        -Dgshadow=false \
        -Dldconfig=false \
        -Dlibidn=disabled \
        -Dsmack=false \
        -Dxenctrl=disabled \
        -Dxkbcommon=disabled \
        \
        -Dpstore=true \
        \
        -Daudit=%{disabled_with bootstrap} \
        -Dbpf-framework=%{disabled_with bootstrap} \
        -Dbzip2=%{enabled_with importd} \
        -Defi=%{when_not bootstrap} \
        -Delfutils=%{disabled_with bootstrap} \
        -Dfdisk=%{disabled_with bootstrap} \
        -Dgcrypt=%{disabled_with bootstrap} \
        -Dgnutls=%{disabled_with bootstrap} \
        -Dhtml=%{disabled_with bootstrap} \
        -Dima=%{when_not bootstrap} \
        -Dkernel-install=%{when_not bootstrap} \
        -Dlibfido2=%{disabled_with bootstrap} \
        -Dlibidn2=%{enabled_with resolved} \
        -Dlibiptc=%{disabled_with bootstrap} \
        -Dlz4=%{disabled_with bootstrap} \
        -Dqrencode=%{disabled_with bootstrap} \
        -Dkmod=%{disabled_with bootstrap} \
        -Dlibcryptsetup=%{disabled_with bootstrap} \
        -Dlibcryptsetup-plugins=%{disabled_with bootstrap} \
        -Dlibcurl=%{disabled_with bootstrap} \
        -Dman=%{disabled_with bootstrap} \
        -Dmicrohttpd=%{enabled_with journal_remote} \
        -Dnss-myhostname=%{when_not bootstrap} \
        -Dnss-mymachines=%{enabled_with machined} \
        -Dnss-resolve=%{enabled_with resolved} \
        -Dnss-systemd=%{when_not bootstrap} \
        -Dopenssl=%{disabled_with bootstrap} \
        -Dp11kit=%{disabled_with bootstrap} \
        -Dpasswdqc=%{disabled_with bootstrap} \
        -Dpwquality=%{disabled_with bootstrap} \
        -Dseccomp=%{disabled_with bootstrap} \
        -Drepart=%{disabled_with bootstrap} \
        -Dstoragetm=%{when_not bootstrap} \
        -Dtpm=%{when_not bootstrap} \
        -Dtpm2=%{disabled_with bootstrap} \
        -Dtranslations=%{when_not bootstrap} \
        -Duserdb=%{when_not bootstrap} \
        -Dxz=%{disabled_with bootstrap} \
        -Dzlib=%{enabled_with importd} \
        -Dzstd=%{disabled_with bootstrap} \
        \
        -Dapparmor=%{enabled_with apparmor} \
        -Dcoredump=%{when coredump} \
        -Dhomed=%{enabled_with homed} \
        -Dimportd=%{enabled_with importd} \
        -Dmachined=%{when machined} \
        -Dnetworkd=%{when networkd} \
        -Dportabled=%{when portabled} \
        -Dremote=%{enabled_with journal_remote} \
        -Dselinux=%{enabled_with selinux} \
        \
        -Dbootloader=%{enabled_with sd_boot} \
        -Defi-color-highlight="black,green" \
        \
        -Dsbat-distro="%{?sbat_distro}" \
        -Dsbat-distro-summary="%{?sbat_distro_summary}" \
        -Dsbat-distro-url="%{?sbat_distro_url}" \
        \
        -Dsbat-distro-pkgname="%{name}" \
        -Dsbat-distro-version="%{version}%[%{without upstream}?"-%{release}":""]" \
        \
        -Ddefault-dnssec=no \
        -Ddns-servers='' \
        -Ddns-over-tls=%{when resolved openssl} \
        -Dresolve=%{when resolved} \
        \
        -Doomd=%{when experimental} \
        -Dsysupdate=%{enabled_with experimental} \
%if %{with sd_boot}
        -Dukify=%{enabled_with experimental} \
%else
        -Dukify=disabled \
%endif
        -Dvmspawn=%{enabled_with experimental} \
        \
        -Dtests=%{when testsuite unsafe} \
        -Dinstall-tests=%{when testsuite} \
        \
        %{?meson_extra_configure_options}

%meson_build

%install
%meson_install

%if %{with sd_boot}
%ifarch x86_64
export BRP_PESIGN_FILES="%{_systemd_util_dir}/boot/efi/systemd-bootx64.efi"
%endif
%endif

# Don't ship resolvconf symlink for now as it conflicts with the binary shipped
# by openresolv and provides limited compatibility only.
%if %{with resolved}
rm %{buildroot}%{_sbindir}/resolvconf
rm %{buildroot}%{_mandir}/man1/resolvconf.1*
%endif

install -m0755 -D %{SOURCE3} %{buildroot}/%{_systemd_util_dir}/systemd-update-helper
%if %{with sysvcompat}
install -m0755 -D %{SOURCE4} %{buildroot}/%{_systemd_util_dir}/systemd-sysv-install
%endif

# Drop-ins are currently not supported by udev.
mv %{buildroot}%{_prefix}/lib/udev/udev.conf %{buildroot}%{_sysconfdir}/udev/

# Install the fixlets
mkdir -p %{buildroot}%{_systemd_util_dir}/rpm
%if %{with machined}
install -m0755 %{SOURCE100} %{buildroot}%{_systemd_util_dir}/rpm/
%endif
install -m0755 %{SOURCE101} %{buildroot}%{_systemd_util_dir}/rpm/

# Make sure /usr/lib/modules-load.d exists in udev(-mini)?, so other
# packages can install modules without worry
mkdir -p %{buildroot}%{_modulesloaddir}

# Make sure we don't ship static enablement symlinks in /etc during
# installation, presets should be honoured instead.
rm -rf %{buildroot}%{_sysconfdir}/systemd/system/*.target.{requires,wants}
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# Replace upstream PAM configuration files with openSUSE ones.
install -m0644 -D %{SOURCE8} %{buildroot}%{_pam_vendordir}/systemd-user

# Don't enable wall ask password service, it spams every console (bnc#747783).
rm %{buildroot}%{_unitdir}/multi-user.target.wants/systemd-ask-password-wall.path

# do not ship sysctl defaults in systemd package, will be part of aaa_base (in
# procps for now).
rm -f %{buildroot}%{_sysctldir}/50-default.conf
rm -f %{buildroot}%{_sysctldir}/50-pid-max.conf

# Make sure systemd-network polkit rules file starts with a suitable number
# prefix so it takes precedence over our polkit-default-privs.
%if %{with networkd}
mv %{buildroot}%{_datadir}/polkit-1/rules.d/systemd-networkd.rules \
        %{buildroot}%{_datadir}/polkit-1/rules.d/60-systemd-networkd.rules
%endif

# Since v207 /etc/sysctl.conf is no longer parsed (commit 04bf3c1a60d82791),
# however backward compatibility is provided by the following symlink.
ln -s ../../../etc/sysctl.conf %{buildroot}%{_sysctldir}/99-sysctl.conf
touch %{buildroot}%{_sysconfdir}/sysctl.conf

# The definitions of the basic users/groups are given by system-user package on
# SUSE (bsc#1006978).
rm -f %{buildroot}%{_sysusersdir}/basic.conf

# systemd-user PAM module relies on pam_env(8) to import the environment defined
# in /etc/environment (which is part of the environment configuration files of
# pam_env(8) anyways).
rm -f %{buildroot}%{_environmentdir}/99-environment.conf

# Remove README file in init.d as (SUSE) rpm requires executable files in this
# directory... oh well.
rm -f %{buildroot}%{_sysconfdir}/init.d/README

# Create *.conf.d/ directories to encourage users to create drop-ins when they
# need to customize some setting defaults.
mkdir -p %{buildroot}%{_sysconfdir}/systemd/coredump.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/journald.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/journal-remote.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/journal-upload.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/logind.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/networkd.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/oomd.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/pstore.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/resolved.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/sleep.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/timesyncd.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/user.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/udev/iocost.conf.d

mkdir -p %{buildroot}%{_sysconfdir}/systemd/network
mkdir -p %{buildroot}%{_sysconfdir}/systemd/nspawn

mkdir -p %{buildroot}%{_sysconfdir}/sysusers.d/

# This dir must be owned (and thus created) by systemd otherwise the build
# system will complain. This is odd since we simply own a ghost file in it...
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d

# Make sure directories in /var exist.
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/rpm

# Make sure the NTP units dir exists.
mkdir -p %{buildroot}%{_ntpunitsdir}

# Make sure the shutdown/sleep drop-in dirs exist.
mkdir -p %{buildroot}%{_systemd_util_dir}/system-shutdown/
mkdir -p %{buildroot}%{_systemd_util_dir}/system-sleep/

# Make sure these directories are properly owned.
mkdir -p %{buildroot}%{_unitdir}/basic.target.wants
mkdir -p %{buildroot}%{_unitdir}/default.target.wants
mkdir -p %{buildroot}%{_unitdir}/dbus.target.wants
mkdir -p %{buildroot}%{_unitdir}/graphical.target.wants
mkdir -p %{buildroot}%{_unitdir}/halt.target.wants
mkdir -p %{buildroot}%{_unitdir}/initrd-root-device.target.wants
mkdir -p %{buildroot}%{_unitdir}/initrd-root-fs.target.wants
mkdir -p %{buildroot}%{_unitdir}/kexec.target.wants
mkdir -p %{buildroot}%{_unitdir}/poweroff.target.wants
mkdir -p %{buildroot}%{_unitdir}/reboot.target.wants
mkdir -p %{buildroot}%{_unitdir}/remote-fs.target.wants
mkdir -p %{buildroot}%{_unitdir}/rescue.target.wants
mkdir -p %{buildroot}%{_unitdir}/shutdown.target.wants

# Make sure the generator directories are created and properly owned.
mkdir -p %{buildroot}%{_systemdgeneratordir}
mkdir -p %{buildroot}%{_systemdusergeneratordir}
mkdir -p %{buildroot}%{_presetdir}
mkdir -p %{buildroot}%{_userpresetdir}
mkdir -p %{buildroot}%{_systemd_system_env_generator_dir}
mkdir -p %{buildroot}%{_systemd_user_env_generator_dir}

# ghost directories with default permissions.
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/backlight

# ghost files with default permisssions.
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database

%fdupes -s %{buildroot}%{_mandir}

# Make sure to disable all services by default. The branding presets package
# takes care of defining the SUSE policies.
rm -f %{buildroot}%{_presetdir}/*.preset
echo 'disable *' >%{buildroot}%{_presetdir}/99-default.preset
echo 'disable *' >%{buildroot}%{_userpresetdir}/99-default.preset

# Most of the entries for the generic paths are defined by filesystem package as
# the definitions used by SUSE distros diverged from the ones defined by
# systemd. For lack of a better place some (deprecated) paths are still shipped
# along with the systemd package.
rm -f %{buildroot}%{_tmpfilesdir}/{etc,home,legacy,tmp,var}.conf
install -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/systemd-suse.conf

# The content of the files shipped by systemd doesn't match the
# defaults used by SUSE. Don't ship those files but leave the decision
# to use the mechanism to the individual packages that actually
# consume those configs (like glibc or pam), see bsc#1170146.
rm -fr %{buildroot}%{_datadir}/factory/*

# kbd-model-map.legacy is used to provide mapping for legacy keymaps, which may
# still be used by yast.
cat %{SOURCE14} >>%{buildroot}%{_datarootdir}/systemd/kbd-model-map

%if %{with testsuite}
# -Dinstall_test took care of installing the unit tests only (those in
# src/tests) and testdata directory. Here we copy the integration tests
# including also all related scripts used to prepare and run the integration
# tests in dedicated VMs. During the copy, all symlinks are replaced by the
# files they point to making sure we won't try to embed dangling symlinks.
mkdir -p %{buildroot}%{_testsuitedir}/integration-tests
tar -cO \
    --dereference \
    --exclude=testdata \
    --exclude-vcs  \
    --exclude-vcs-ignores \
    -C test/ . | tar -xC %{buildroot}%{_testsuitedir}/integration-tests
%endif

%if %{without bootstrap}
%find_lang systemd
%else
rm -f  %{buildroot}%{_bindir}/varlinkctl
rm -f  %{buildroot}%{_journalcatalogdir}/*
rm -fr %{buildroot}%{_docdir}/systemd
%endif

# Don't drop %%pre section even if it becomes empty: the build process of
# installation images uses a hardcoded list of packages with a %%pre that needs
# to be run during the build and complains if it can't find one.
%pre
# We don't really need to enable these units explicitely since during
# installation `systemctl preset-all` is executed at the end of the install
# transaction by the branding preset package. However it might be needed when
# upgrading from a previous version of systemd that didn't ship one of these
# units.
%systemd_pre remote-fs.target
%systemd_pre getty@.service
%systemd_pre systemd-journald-audit.socket
%systemd_pre systemd-userdbd.service

%check
# Run the unit tests.
%meson_test

%post
if [ $1 -eq 1 ]; then
        # Make /etc/machine-id an empty file during package installation. On the
        # first boot, machine-id is initialized and either committed (if /etc/
        # is writable) or the system/image runs with a transient machine ID,
        # that changes on each boot (if the image is read-only). This is
        # important for appliance builds to avoid an identical machine ID in all
        # images.
        touch     %{_sysconfdir}/machine-id
        chmod 444 %{_sysconfdir}/machine-id

        # Persistent journal is the default
        mkdir -p %{_localstatedir}/log/journal
fi

%if %{without bootstrap}
pam-config --add --systemd || :
# Run ldconfig for nss-systemd and nss-myhostname NSS modules.
%ldconfig
%endif

systemctl daemon-reexec || :
# Reexecute the user managers (if any)
%{_systemd_util_dir}/systemd-update-helper user-reexec || :

%if %{without filetriggers}
# During package installation, the followings are for config files shipped by
# packages that got installed before systemd and by the systemd main package
# itself. During update they deal with files that could have been introduced by
# new versions of systemd.
systemd-sysusers || :
systemd-tmpfiles --create || :
journalctl --update-catalog || :
%endif

# See the comment in %%pre about why we need to call %%systemd_pre.
%systemd_post remote-fs.target
%systemd_post getty@.service
%systemd_post systemd-journald-audit.socket
%systemd_post systemd-userdbd.service

# Run the hacks/fixups to clean up the old stuff left by (very) old versions of
# systemd.
%{_systemd_util_dir}/rpm/fixlet-systemd-post.sh $1 || :

%postun
# Avoid restarting logind until fixed upstream (issue #1163)
%systemd_postun_with_restart systemd-hostnamed.service
%systemd_postun_with_restart systemd-journald.service
%systemd_postun_with_restart systemd-localed.service
%systemd_postun_with_restart systemd-timedated.service
%systemd_postun_with_restart systemd-userdbd.service

%posttrans
%restore_rpmsave systemd/journald.conf
%restore_rpmsave systemd/logind.conf
%restore_rpmsave systemd/system.conf
%restore_rpmsave systemd/user.conf

%pre -n udev%{?mini}
# Units listed below can be enabled at installation accoding to their preset
# setting.
%systemd_pre remote-cryptsetup.target
%systemd_pre systemd-pstore.service
%systemd_pre systemd-timesyncd.service

# New installations uses the last compat symlink generation number (currently at
# 2), which basically disables all compat symlinks. On old systems, the file
# doesn't exist. This is equivalent to generation #1, which enables the creation
# of all compat symlinks.
if [ $1 -eq 1 ]; then
        echo "COMPAT_SYMLINK_GENERATION=2" >/usr/lib/udev/compat-symlink-generation
fi

%post -n udev%{?mini}
%regenerate_initrd_post
%if %{without filetriggers}
%udev_hwdb_update
%tmpfiles_create systemd-pstore.conf
%sysusers_create systemd-timesync.conf
%endif
%systemd_post remote-cryptsetup.target
%systemd_post systemd-pstore.service
%systemd_post systemd-timesyncd.service

%preun -n udev%{?mini}
%systemd_preun systemd-udevd.service systemd-udevd-{control,kernel}.socket
%systemd_preun systemd-pstore.service
%systemd_preun systemd-timesyncd.service

%postun -n udev%{?mini}
%regenerate_initrd_post

# The order of the units being restarted is important here because there's
# currently no way to queue multiple jobs into a single transaction
# atomically. Therefore systemctl will create 3 restart jobs that can be handled
# by PID1 separately and if the jobs for the sockets are being handled first
# then starting them again will fail as the service is still active hence the
# sockets held by udevd. However if the restart job for udevd is handled first,
# there should be enough time to queue the socket jobs before the stop job for
# udevd is processed. Hence PID1 will automatically sort the restart jobs
# correctly by stopping the service then the sockets and then by starting the
# sockets and the unit.
#
# Note that when systemd-udevd is restarted, there will always be a short time
# frame where no socket will be listening to the events sent by the kernel, no
# matter if the socket unit is restarted in first or not.
%systemd_postun_with_restart systemd-udevd.service systemd-udevd-{control,kernel}.socket
%systemd_postun_with_restart systemd-timesyncd.service
%systemd_postun systemd-pstore.service

%posttrans -n udev%{?mini}
%regenerate_initrd_posttrans
%restore_rpmsave systemd/pstore.conf
%restore_rpmsave systemd/sleep.conf
%restore_rpmsave systemd/timesyncd.conf
%restore_rpmsave udev/iocost.conf

%ldconfig_scriptlets -n libsystemd0%{?mini}
%ldconfig_scriptlets -n libudev%{?mini}1

%if %{with machined}
%pre container
%systemd_pre machines.target

%preun container
%systemd_preun machines.target

%postun container
%ldconfig
%systemd_postun machines.target
%endif

%post container
%if %{with machined}
%ldconfig
%if %{without filetriggers}
%tmpfiles_create systemd-nspawn.conf
%endif
%systemd_post machines.target
%{_systemd_util_dir}/rpm/fixlet-container-post.sh $1 || :
%endif

%if %{with coredump}
%post coredump
%if %{without filetriggers}
%sysusers_create systemd-coredump.conf

%posttrans coredump
%restore_rpmsave systemd/coredump.conf
%endif
%endif

%if %{with journal_remote}
%pre journal-remote
%systemd_pre systemd-journal-gatewayd.service
%systemd_pre systemd-journal-remote.service
%systemd_pre systemd-journal-upload.service

%post journal-remote
# Assume that all files shipped by systemd-journal-remove are owned by root.
%if %{without filetriggers}
%sysusers_create systemd-remote.conf
%endif
%systemd_post systemd-journal-gatewayd.service
%systemd_post systemd-journal-remote.service
%systemd_post systemd-journal-upload.service

%preun journal-remote
%systemd_preun systemd-journal-gatewayd.service
%systemd_preun systemd-journal-remote.service
%systemd_preun systemd-journal-upload.service

%postun journal-remote
%systemd_postun_with_restart systemd-journal-gatewayd.service
%systemd_postun_with_restart systemd-journal-remote.service
%systemd_postun_with_restart systemd-journal-upload.service

%posttrans journal-remote
%restore_rpmsave systemd/journal-remote.conf
%restore_rpmsave systemd/journal-upload.conf
%endif

%if %{with networkd} || %{with resolved}
%pre network
%if %{with networkd}
%systemd_pre systemd-networkd.service
%systemd_pre systemd-networkd-wait-online.service
%endif
%if %{with resolved}
%systemd_pre systemd-resolved.service
%endif

%post network
%if %{with networkd}
%if %{without filetriggers}
%sysusers_create systemd-network.conf
%tmpfiles_create systemd-network.conf
%endif
%systemd_post systemd-networkd.service
%systemd_post systemd-networkd-wait-online.service
%endif
%if %{with resolved}
%ldconfig
%if %{without filetriggers}
%sysusers_create systemd-resolve.conf
%tmpfiles_create systemd-resolve.conf
%endif
%systemd_post systemd-resolved.service
%endif

%preun network
%if %{with networkd}
%systemd_preun systemd-networkd.service
%systemd_preun systemd-networkd-wait-online.service
%endif
%if %{with resolved}
%systemd_preun systemd-resolved.service
%endif

%postun network
%if %{with networkd}
%systemd_postun systemd-networkd.service
%systemd_postun systemd-networkd-wait-online.service
%endif
%if %{with resolved}
%ldconfig
%systemd_postun systemd-resolved.service
%endif

%posttrans network
%restore_rpmsave systemd/networkd.conf
%restore_rpmsave systemd/resolved.conf
%endif

%if %{with homed}
%pre homed
%systemd_pre systemd-homed.service

%post homed
if [ $1 -eq 1 ]; then
        pam-config --add --systemd_home || :
fi
%systemd_post systemd-homed.service

%preun homed
%systemd_preun systemd-homed.service
if [ $1 -eq 0 ]; then
        pam-config --delete --systemd_home || :
fi

%postun homed
%systemd_postun_with_restart systemd-homed.service
%endif

%if %{with portabled}
%pre portable
%systemd_pre systemd-portabled.service

%post portable
%if %{without filetriggers}
%tmpfiles_create portables.conf
%endif
%systemd_post systemd-portabled.service

%preun portable
%systemd_preun systemd-portabled.service

%postun portable
%systemd_postun_with_restart systemd-portabled.service
%endif

%if %{with experimental}
%pre experimental
%systemd_pre systemd-homed.service
%systemd_pre systemd-oomd.service systemd-oomd.socket

%post experimental
%if %{without filetriggers}
%sysusers_create systemd-oom.conf
%endif
%systemd_post systemd-homed.service
%systemd_post systemd-oomd.service systemd-oomd.socket

%preun experimental
%systemd_preun systemd-homed.service
%systemd_preun systemd-oomd.service systemd-oomd.socket

%postun experimental
%systemd_postun systemd-homed.service
%systemd_postun systemd-oomd.service systemd-oomd.socket

%posttrans experimental
%restore_rpmsave systemd/oomd.conf
%endif

# File trigger definitions
%if %{with filetriggers}
%include %{SOURCE7}
%endif

%files
%include %{SOURCE200}

%files -n udev%{?mini}
%include %{SOURCE201}

%if %{with sd_boot}
%files boot
%include %{SOURCE206}
%endif

%files container
%include %{SOURCE202}

%if %{with networkd} || %{with resolved}
%files network
%include %{SOURCE203}
%endif

%files devel
%license LICENSE.LGPL2.1
%include %{SOURCE204}

%if %{with sysvcompat}
%files sysvcompat
%include %{SOURCE205}
%endif

%files -n libsystemd0%{?mini}
%license LICENSE.LGPL2.1
%{_libdir}/libsystemd.so.0
%{_libdir}/libsystemd.so.0.*.0

%files -n libudev%{?mini}1
%license LICENSE.LGPL2.1
%{_libdir}/libudev.so.1
%{_libdir}/libudev.so.1.7.*

%if %{with coredump}
%files coredump
%include %{SOURCE208}
%endif

%if %{without bootstrap}
%files lang -f systemd.lang
%include %{SOURCE210}

%files doc
%{_docdir}/systemd/
%include %{SOURCE213}
%endif

%if %{with journal_remote}
%files journal-remote
%include %{SOURCE211}
%endif

%if %{with homed}
%files homed
%include %{SOURCE209}
%endif

%if %{with portabled}
%files portable
%include %{SOURCE212}
%endif

%if %{with testsuite}
%files testsuite
%doc %{_testsuitedir}/integration-tests/README.testsuite
%{_testsuitedir}
%endif

%if %{with experimental}
%files experimental
%include %{SOURCE207}
%endif

%changelog
