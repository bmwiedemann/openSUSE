#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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

%define min_kernel_version 4.5
%define archive_version +suse.29.g07bb12a282

%define _testsuitedir %{_systemd_util_dir}/tests
%define xinitconfdir %{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}/X11/xinit

# Similar to %%with but returns true/false. The 'true' value can be redefined
# when a second parameter is passed.
%define __when_1() %{expand:%%{?with_%{1}:true}%%{!?with_%{1}:false}}
%define __when_2() %{expand:%%{?with_%{1}:%{2}}%%{!?with_%{1}:false}}
%define when()     %{expand:%%__when_%# %{*}}

%define __when_not_1() %{expand:%%{?with_%{1}:false}%%{!?with_%{1}:true}}
%define __when_not_2() %{expand:%%{?with_%{1}:false}%%{!?with_%{1}:%{2}}}
%define when_not()     %{expand:%%__when_not_%# %{*}}

%if "%{flavor}" == "mini"
%define mini -mini
%bcond_without  bootstrap
%bcond_with     coredump
%bcond_with     importd
%bcond_with     journal_remote
%bcond_with     machined
%bcond_with     networkd
%bcond_with     portabled
%bcond_with     resolved
%bcond_with     sd_boot
%bcond_with     sysvcompat
%bcond_with     experimental
%bcond_with     testsuite
%else
%define mini %nil
%bcond_with     bootstrap
%bcond_without  coredump
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
%bcond_without  sysvcompat
%bcond_without  experimental
%bcond_without  testsuite
%endif
# Kept to ease migrations toward SLE
%bcond_without  filetriggers
%bcond_with     split_usr

Name:           systemd%{?mini}
URL:            http://www.freedesktop.org/wiki/Software/systemd
Version:        253.5
Release:        0
Summary:        A System and Session Manager
License:        LGPL-2.1-or-later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{without bootstrap}
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  kbd
BuildRequires:  libapparmor-devel
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
BuildRequires:  pkgconfig(libselinux) >= 2.1.9
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
# regenerate_initrd_post macro is expanded during build, hence this BR. Also
# this macro was introduced since version 12.4.
BuildRequires:  suse-module-tools >= 12.4
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(blkid) >= 2.26

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
Requires:       group(lock)
# This Recommends because some symbols of libpcre2 are dlopen()ed by journalctl
Recommends:     libpcre2-8-0
Recommends:     libbpf0

Requires(post): coreutils
Requires(post): findutils
Requires(post): systemd-presets-branding
Requires(post): pam-config >= 0.79-5
%endif
Conflicts:      filesystem < 11.5
Conflicts:      mkinitrd < 2.7.0
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
Source2:        systemd-user
Source3:        systemd-update-helper
%if %{with sysvcompat}
Source4:        systemd-sysv-install
%endif
Source5:        tmpfiles-suse.conf
Source6:        baselibs.conf
Source7:        triggers.systemd
Source11:       after-local.service
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

#
# All changes backported from upstream are tracked by the git repository, which
# can be found at:  https://github.com/openSUSE/systemd.
#
# Patches listed below are openSUSE specific and should be kept at its
# minimum. We try hard to push our changes to upstream but sometimes they are
# only relevant for SUSE distros. Special rewards for those who will manage to
# get rid of one of them !
#
Patch1:         0001-restore-var-run-and-var-lock-bind-mount-if-they-aren.patch
Patch2:         0002-rc-local-fix-ordering-startup-for-etc-init.d-boot.lo.patch
Patch3:         0003-strip-the-domain-part-from-etc-hostname-when-setting.patch
%if %{with sysvcompat}
Patch8:         0008-sysv-generator-translate-Required-Start-into-a-Wants.patch
%endif
Patch10:        0001-conf-parser-introduce-early-drop-ins.patch
Patch12:        0009-pid1-handle-console-specificities-weirdness-for-s390.patch

# Patches listed below are put in quarantine. Normally all changes must go to
# upstream first and then are cherry-picked in the SUSE git repository. But for
# very few cases, some stuff might be broken in upstream and need to be fixed or
# worked around quickly. In these cases, the patches are added temporarily and
# will be removed as soon as a proper fix will be merged by upstream.
Patch5000:      5000-core-manager-run-generators-directly-when-we-are-in-.patch
Patch5001:      5001-Revert-core-propagate-stop-too-if-restart-is-issued.patch

%description
Systemd is a system and service manager, compatible with SysV and LSB
init scripts for Linux. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system state,
maintains mount and automount points and implements an elaborate
transactional dependency-based service control logic. It can work as a
drop-in replacement for sysvinit.

%package doc
Summary:        HTML documentation for systemd
License:        LGPL-2.1-or-later
%if %{with bootstrap}
Conflicts:      systemd-doc
Requires:       this-is-only-for-build-envs
%else
Supplements:    (systemd and patterns-base-documentation)
%endif

%description doc
The HTML documentation for systemd.

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
%if %{with sd_boot}
BuildRequires:  gnu-efi
BuildRequires:  pesign-obs-integration
%endif
Requires:       %{name} = %{version}-%{release}
%systemd_requires
Requires:       filesystem
Requires:       kmod
Requires:       system-group-hardware
Requires:       group(kvm)
Requires(post): sed
Requires(post): coreutils
Requires(postun):coreutils
%if %{without bootstrap}
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
Conflicts:      dracut < 044.1
Conflicts:      filesystem < 11.5
Conflicts:      mkinitrd < 2.7.0
Conflicts:      util-linux < 2.16
%if %{with bootstrap}
Conflicts:      udev
Provides:       udev = %{version}-%{release}
%endif

%description -n udev%{?mini}
Udev creates and removes device nodes in /dev for devices discovered or
removed from the system. It receives events via kernel netlink messages
and dispatches them according to rules in %{_udevrulesdir}/. Matching
rules may name a device node, create additional symlinks to the node,
call tools to initialize a device, or load needed kernel modules.

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
Summary:        systemd network and Network Name Resolution managers
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

%if %{with portabled}
%package portable
Summary:        Systemd tools for portable services
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
%systemd_requires

%description portable
Systemd tools to manage portable services. The feature is still
considered experimental so the package might change  or vanish.
Use at own risk.

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
# Unit tests dependencies
License:        LGPL-2.1-or-later
Recommends:     python3
Recommends:     python3-colorama
# Optional dep for mkfs.vfat needed by test-loop-block (otherwise skipped)
Recommends:     dosfstools
# Optional deps needed by TEST-70-TPM2 (otherwise skipped)
Recommends:     swtpm
Recommends:     tpm2.0-tools
# The following deps on libs are for test-dlopen-so whereas the pkgconfig ones
# are used by test-funtions to find the libs on the host and install them in the
# image, see install_missing_libraries() for details.
%if %{with resolved}
# Optional dep for knot needed by TEST-75-RESOLVED
Recommends:     knot
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
Requires:       dosfstools
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
Requires:       qemu-kvm
Requires:       quota
Requires:       selinux-policy-devel
Requires:       socat
Requires:       squashfs
Requires:       systemd-container
Requires:       pkgconfig(libfido2)
Requires:       pkgconfig(tss2-esys)
Requires:       pkgconfig(tss2-mu)
Requires:       pkgconfig(tss2-rc)
%if %{with coredump}
Requires:       systemd-coredump
%endif
%if %{with experimental}
Requires:       systemd-experimental
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
# Needed by ukify
Requires:       python3-pefile
%systemd_requires
# These Recommends because some symbols of these libs are dlopen()ed by home stuff
Recommends:     libfido2
Recommends:     libpwquality1
Recommends:     libqrencode4
# libfido2, libpwquality1 and libqrencode4 are build requirements for home stuff
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(pwquality)
# fdisk and openssl are build requirements for home stuff and repart
BuildRequires:  pkgconfig(fdisk)
BuildRequires:  pkgconfig(openssl)

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

Currently this package contains: homed, repart, userdbd, oomd, measure,
pcrphase and ukify.

In case you want to create a user with systemd-homed quickly, here are the steps
you can follow:

 - Make sure the nss-systemd package is installed and added into
   /etc/nsswitch.conf, see nss-systemd(8) man page for details

 - Integrate pam_systemd_home.so in your PAM stack. You can do that either by
   following the instructions in pam_systemd_home(8) man page or by executing
   `pam-config --add --systemd_home` command

 - Enable and start systemd-homed with `systemctl enable --now systemd-homed`

 - Create a user with `homectl create <username>`

 - Verify the previous steps with `getent passwd <username>`

Have fun (at your own risk).
%endif

%if %{without bootstrap}
%lang_package
%endif

%prep
%autosetup -p1 -n systemd-v%{version}%{archive_version}

%build
# Disable _FORTIFY_SOURCE=3 as it get confused by the use of
# malloc_usable_size() (bsc#1200819). There used to be a workaround but it was
# reverted, see 2cfb790391958ada34284290af1f9ab863a515c7 for the details.
export CFLAGS="%{optflags} -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2"

%meson \
        -Dmode=release \
        -Dversion-tag=%{version}%{archive_version} \
        -Ddocdir=%{_docdir}/systemd \
%if %{with split_usr}
        -Drootprefix=/usr \
        -Dsplit-usr=true \
%endif
        -Dsplit-bin=true \
        -Dsystem-uid-max=499 \
        -Dsystem-gid-max=499 \
        -Dclock-valid-range-usec-max=946728000000000 \
        -Dadm-group=false \
        -Dwheel-group=false \
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
%endif
        -Drc-local=/etc/init.d/boot.local \
        -Dcreate-log-dirs=false \
        -Ddebug-shell=/bin/bash \
        \
        -Dbump-proc-sys-fs-nr-open=false \
        -Dgshadow=false \
        -Dldconfig=false \
        -Dsmack=false \
        \
        -Dpstore=true \
        \
        -Dapparmor=%{when_not bootstrap} \
        -Dbpf-framework=%{when_not bootstrap} \
        -Defi=%{when_not bootstrap} \
        -Delfutils=%{when_not bootstrap} \
        -Dhtml=%{when_not bootstrap} \
        -Dima=%{when_not bootstrap} \
        -Dlibcryptsetup-plugins=%{when_not bootstrap} \
        -Dman=%{when_not bootstrap} \
        -Dnss-myhostname=%{when_not bootstrap} \
        -Dnss-systemd=%{when_not bootstrap} \
        -Dseccomp=%{when_not bootstrap} \
        -Dselinux=%{when_not bootstrap} \
        -Dtpm=%{when_not bootstrap} \
        -Dtpm2=%{when_not bootstrap} \
        -Dtranslations=%{when_not bootstrap} \
        \
        -Dcoredump=%{when coredump} \
        -Dimportd=%{when importd} \
        -Dmachined=%{when machined} \
        -Dnetworkd=%{when networkd} \
        -Dportabled=%{when portabled} \
        -Dremote=%{when journal_remote} \
        \
        -Dgnu-efi=%{when sd_boot} \
        -Defi-color-highlight="black,green" \
        -Dkernel-install=%{when sd_boot} \
        \
        -Dsbat-distro="%{?sbat_distro}" \
        -Dsbat-distro-summary="%{?sbat_distro_summary}" \
        -Dsbat-distro-url="%{?sbat_distro_url}" \
        \
        -Dsbat-distro-pkgname="%{name}" \
        -Dsbat-distro-version="%{version}-%{release}" \
        \
        -Ddefault-dnssec=no \
        -Ddns-servers='' \
        -Ddns-over-tls=%{when resolved openssl} \
        -Dresolve=%{when resolved} \
        \
        -Dhomed=%{when experimental} \
        -Doomd=%{when experimental} \
        -Drepart=%{when experimental} \
        -Dsysupdate=%{when experimental} \
        -Duserdb=%{when experimental} \
        \
        -Dtests=%{when testsuite unsafe} \
        -Dinstall-tests=%{when testsuite}

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

mkdir -p % %{buildroot}%{_sysconfdir}/systemd/network
mkdir -p % %{buildroot}%{_sysconfdir}/systemd/nspawn

# Install the fixlets
mkdir -p %{buildroot}%{_systemd_util_dir}/rpm
%if %{with machined}
install -m0755 %{SOURCE100} %{buildroot}%{_systemd_util_dir}/rpm/
%endif
install -m0755 %{SOURCE101} %{buildroot}%{_systemd_util_dir}/rpm/

%if %{with split_usr}
mkdir -p %{buildroot}/{bin,sbin}
# Legacy paths
ln -s ../usr/bin/udevadm %{buildroot}/sbin/
ln -s ../usr/bin/systemctl %{buildroot}/bin/

ln -s ../usr/lib/systemd/systemd %{buildroot}/sbin/init
ln -s ../usr/bin/systemctl %{buildroot}/sbin/reboot
ln -s ../usr/bin/systemctl %{buildroot}/sbin/halt
ln -s ../usr/bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../usr/bin/systemctl %{buildroot}/sbin/poweroff
# Legacy sysvinit tools
%if %{with sysvcompat}
ln -s ../usr/bin/systemctl %{buildroot}/sbin/telinit
ln -s ../usr/bin/systemctl %{buildroot}/sbin/runlevel
%endif
# kmod keeps insisting on using /lib/modprobe.d only.
mkdir -p %{buildroot}%{_modprobedir}
mv %{buildroot}/usr/lib/modprobe.d/* %{buildroot}%{_modprobedir}/
%endif

# Make sure we don't ship static enablement symlinks in /etc during
# installation, presets should be honoured instead.
rm -rf %{buildroot}%{_sysconfdir}/systemd/system/*.target.{requires,wants}
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# Replace upstream systemd-user with the openSUSE one.
install -m0644 -D --target-directory=%{buildroot}%{_pam_vendordir} %{SOURCE2}

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

# Ensure after.local wrapper is called.
install -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/
ln -s ../after-local.service %{buildroot}%{_unitdir}/multi-user.target.wants/

# ghost directories with default permissions.
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/backlight

# ghost files with default permisssions.
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database

%fdupes -s %{buildroot}%{_mandir}

# Make sure to disable all services by default. The SUSE branding presets
# package takes care of defining the right policies.
rm -f %{buildroot}%{_presetdir}/*.preset
echo 'disable *' >%{buildroot}%{_presetdir}/99-default.preset
echo 'disable *' >%{buildroot}%{_userpresetdir}/99-default.preset

# The current situation with tmpfiles snippets dealing with the generic paths is
# pretty messy currently because:
#
#  1. filesystem package wants to define the generic paths and some of them
#     conflict with the definition given by systemd in var.conf, see
#     bsc#1078466.
#
#  2. /tmp and /var/tmp are not cleaned by default on SUSE distros (fate#314974)
#     which conflict with tmp.conf.
#
#  3. There're also legacy.conf which defines various legacy paths which either
#     don't match the SUSE defaults or don't look needed at all.
#
#  4. We don't want the part in etc.conf which imports default upstream files in
#     empty /etc, see below.
#
# To keep things simple, we remove all these tmpfiles config files but still
# keep the remaining paths that still don't have a better home in suse.conf.
rm -f %{buildroot}%{_tmpfilesdir}/{etc,home,legacy,tmp,var}.conf
install -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/suse.conf

# The content of the files shipped by systemd doesn't match the
# defaults used by SUSE. Don't ship those files but leave the decision
# to use the mechanism to the individual packages that actually
# consume those configs (like glibc or pam), see bsc#1170146.
rm -fr %{buildroot}%{_datadir}/factory/*

# Add entries for xkeyboard-config converted keymaps; mappings, which already
# exist in original systemd mapping table are being ignored though, i.e. not
# overwritten; needed as long as YaST uses console keymaps internally and calls
# localectl to convert from vconsole to X11 keymaps. Ideally YaST should switch
# to X11 layout names (the mapping table wouldn't be needed since each X11
# keymap has a generated xkbd keymap) and let localectl initialize
# /etc/vconsole.conf and /etc/X11/xorg.conf.d/00-keyboard.conf (FATE#319454).
if [ -f /usr/share/systemd/kbd-model-map.xkb-generated ]; then
        cat /usr/share/systemd/kbd-model-map.xkb-generated \
                >>%{buildroot}%{_datarootdir}/systemd/kbd-model-map
fi

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
%endif

# Don't drop %%pre section even if it becomes empty: the build process of
# installation images uses a hardcoded list of packages with a %%pre that needs
# to be run during the build and complains if it can't find one.
%pre
if [ $1 -gt 1 ]; then
        # We keep these just in case we're upgrading from an old version that
        # was missing one of these units. During package installation, these
        # macros are NOPs for the main package (the branding preset package
        # takes care of applying the presets in its %%posttrans in this case).
        %systemd_pre remote-fs.target
        %systemd_pre getty@.service
        %systemd_pre systemd-timesyncd.service
        %systemd_pre systemd-journald-audit.socket
fi

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

if [ $1 -gt 1 ]; then
        # See comments for %%systemd_pre in %%pre.
        %systemd_post remote-fs.target
        %systemd_post getty@.service
        %systemd_post systemd-timesyncd.service
        %systemd_post systemd-journald-audit.socket
fi

# Run the hacks/fixups to clean up old garbages left by (very) old versions of
# systemd.
%{_systemd_util_dir}/rpm/fixlet-systemd-post.sh $1 || :

%postun
%systemd_postun_with_restart systemd-journald.service
%systemd_postun_with_restart systemd-timesyncd.service
# Avoid restarting logind until fixed upstream (issue #1163)

%pre -n udev%{?mini}
# Units listed below can be enabled at installation accoding to their preset
# setting.
%systemd_pre remote-cryptsetup.target
%systemd_pre systemd-pstore.service

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
%endif
%systemd_post remote-cryptsetup.target
%systemd_post systemd-pstore.service

%preun -n udev%{?mini}
%systemd_preun systemd-udevd.service systemd-udevd-{control,kernel}.socket
%systemd_preun systemd-pstore.service

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
%systemd_postun systemd-pstore.service

%posttrans -n udev%{?mini}
%regenerate_initrd_posttrans

%post -n libudev%{?mini}1 -p %ldconfig
%post -n libsystemd0%{?mini} -p %ldconfig

%postun -n libudev%{?mini}1 -p %ldconfig
%postun -n libsystemd0%{?mini} -p %ldconfig

%if %{with machined}
%pre container
%systemd_pre machines.target

%preun container
%systemd_preun machines.target

%postun container
%systemd_postun machines.target
%ldconfig
%endif

%post container
%if %{without filetriggers}
%tmpfiles_create systemd-nspawn.conf
%endif
%if %{with machined}
%systemd_post machines.target
%ldconfig
%endif
%{_systemd_util_dir}/rpm/fixlet-container-post.sh $1 || :

%if %{with coredump}
%post coredump
%sysusers_create systemd-coredump.conf
%endif

%if %{with journal_remote}
%pre journal-remote
%systemd_pre systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_pre systemd-journal-remote.socket systemd-journal-remote.service
%systemd_pre systemd-journal-upload.service

%post journal-remote
# Assume that all files shipped by systemd-journal-remove are owned by root.
%sysusers_create systemd-remote.conf
%systemd_post systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_post systemd-journal-remote.socket systemd-journal-remote.service
%systemd_post systemd-journal-upload.service

%preun journal-remote
%systemd_preun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_preun systemd-journal-remote.socket systemd-journal-remote.service
%systemd_preun systemd-journal-upload.service

%postun journal-remote
%systemd_postun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_postun systemd-journal-remote.socket systemd-journal-remote.service
%systemd_postun systemd-journal-upload.service
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
%sysusers_create systemd-resolve.conf
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
%systemd_postun systemd-portabled.service
%endif

%if %{with experimental}
%pre experimental
%systemd_pre systemd-homed.service
%systemd_pre systemd-oomd.service systemd-oomd.socket
%systemd_pre systemd-userdbd.service systemd-userdbd.socket

%post experimental
%sysusers_create systemd-oom.conf
%systemd_post systemd-homed.service
%systemd_post systemd-oomd.service systemd-oomd.socket
%systemd_post systemd-userdbd.service systemd-userdbd.socket

%preun experimental
%systemd_preun systemd-homed.service
%systemd_preun systemd-oomd.service systemd-oomd.socket
%systemd_preun systemd-userdbd.service systemd-userdbd.socket

%postun experimental
%systemd_postun systemd-homed.service
%systemd_postun systemd-oomd.service systemd-oomd.socket
%systemd_postun systemd-userdbd.service systemd-userdbd.socket
%endif

# File trigger definitions
%if %{with filetriggers}
%include %{SOURCE7}
%endif

%files
%defattr(-,root,root)
%include %{SOURCE200}

%files -n udev%{?mini}
%defattr(-,root,root)
%include %{SOURCE201}
%include %{SOURCE206}

%files container
%defattr(-,root,root)
%include %{SOURCE202}

%if %{with networkd} || %{with resolved}
%files network
%defattr(-,root,root)
%include %{SOURCE203}
%endif

%files doc
%defattr(-,root,root,-)
%{_docdir}/systemd/

%files devel
%defattr(-,root,root,-)
%license LICENSE.LGPL2.1
%include %{SOURCE204}

%if %{with sysvcompat}
%files sysvcompat
%defattr(-,root,root,-)
%include %{SOURCE205}
%endif

%files -n libsystemd0%{?mini}
%defattr(-,root,root)
%license LICENSE.LGPL2.1
%{_libdir}/libsystemd.so.0
%{_libdir}/libsystemd.so.0.36.0

%files -n libudev%{?mini}1
%defattr(-,root,root)
%license LICENSE.LGPL2.1
%{_libdir}/libudev.so.1
%{_libdir}/libudev.so.1.7.6

%if %{with coredump}
%files coredump
%defattr(-,root,root)
%include %{SOURCE208}
%endif

%if %{without bootstrap}
%files lang -f systemd.lang
%endif

%if %{with journal_remote}
%files journal-remote
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/systemd/journal-remote.conf
%config(noreplace) %{_sysconfdir}/systemd/journal-upload.conf
%{_unitdir}/systemd-journal-gatewayd.*
%{_unitdir}/systemd-journal-remote.*
%{_unitdir}/systemd-journal-upload.*
%{_systemd_util_dir}/systemd-journal-gatewayd
%{_systemd_util_dir}/systemd-journal-remote
%{_systemd_util_dir}/systemd-journal-upload
%{_sysusersdir}/systemd-remote.conf
%{_mandir}/man5/journal-remote.conf*
%{_mandir}/man5/journal-upload.conf*
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/systemd-journal-remote.*
%{_mandir}/man8/systemd-journal-upload.*
%{_datadir}/systemd/gatewayd
%ghost %dir %{_localstatedir}/log/journal/remote
%endif

%if %{with portabled}
%files portable
%defattr(-,root,root)
%{_bindir}/portablectl
%{_systemd_util_dir}/systemd-portabled
%{_systemd_util_dir}/portable
%{_unitdir}/systemd-portabled.service
%{_unitdir}/dbus-org.freedesktop.portable1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.portable1.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.portable1.service
%{_datadir}/polkit-1/actions/org.freedesktop.portable1.policy
%{_tmpfilesdir}/portables.conf
%{_mandir}/man*/portablectl*
%{_mandir}/man*/systemd-portabled*
%endif

%if %{with testsuite}
%files testsuite
%defattr(-,root,root)
%doc %{_testsuitedir}/integration-tests/README.testsuite
%{_testsuitedir}
%endif

%if %{with experimental}
%files experimental
%defattr(-,root,root)
%include %{SOURCE207}
%endif

%changelog
