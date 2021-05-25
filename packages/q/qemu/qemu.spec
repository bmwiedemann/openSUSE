#
# spec file for package qemu
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


# !! IMPORTANT !! See README.PACKAGING before modifying package in any way

#!ForceMultiversion

%define _buildshell /bin/bash

%define build_x86_firmware_from_source 0
%define build_skiboot_from_source 0
%define build_slof_from_source 0
%define build_opensbi_from_source 0
%define kvm_available 0
%define legacy_qemu_kvm 0
%define force_fit_virtio_pxe_rom 1

%define build_rom_arch %ix86 x86_64 aarch64

%if "%{?distribution}" == ""
%define distro private-build
%else
%define distro %{distribution}
%endif

%ifarch %{build_rom_arch}
# choice of building all from source or using provided binary x86 blobs
%define build_x86_firmware_from_source 1
%endif

%ifarch ppc64
%define build_skiboot_from_source 1
%define build_slof_from_source 1
%endif

%ifarch ppc64le
%define build_skiboot_from_source 1
%define build_slof_from_source 1
%endif

%ifarch riscv64
%define build_opensbi_from_source 1
%endif

%ifarch %ix86 x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
%define kvm_available 1
%endif

%ifarch %ix86 x86_64 s390x
%define legacy_qemu_kvm 1
%endif

%ifarch x86_64 aarch64 ppc64le s390x
%define with_rbd 1
%endif

%ifarch x86_64 ppc64le
%define with_daxctl 1
%endif

%ifarch %ix86 x86_64
%define with_uring 1
%define liburing_min_version 0.3
%endif

# qemu, qemu-linux-user, and qemu-testsuite "flavors" are enabled via OBS Multibuild
%global flavor @BUILD_FLAVOR@%{nil}
%define name_suffix %{nil}
%if "%flavor" == "testsuite"
%define name_suffix -testsuite
%endif
%if "%flavor" == "linux-user"
%define name_suffix -linux-user
%define summary_string CPU emulator for user space
%else
%define summary_string Machine emulator and virtualizer
%endif

%bcond_with system_membarrier

%define qemuver 6.0.0
%define srcver  6.0.0
%define sbver   1.14.0_0_g155821a
%define srcname qemu
Name:           qemu%{name_suffix}
URL:            https://www.qemu.org/
Summary:        %{summary_string}
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
Version:        %qemuver
Release:        0
Source:         https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz
Source99:       https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz.sig
Source100:      %{srcname}.keyring
Source1:        80-kvm.rules
Source2:        kvm.conf
Source3:        qemu-ifup
Source4:        bridge.conf
Source5:        qemu-kvm.1.gz
Source6:        ksm.service
Source7:        qemu-ga@.service
Source8:        80-qemu-ga.rules
Source9:        qemu-supportconfig
Source10:       supported.arm.txt
Source11:       supported.ppc.txt
Source12:       supported.x86.txt
Source13:       supported.s390.txt
Source14:       50-seabios-256k.json
Source15:       60-seabios-128k.json
Source200:      qemu-rpmlintrc
Source201:      pkg-split.txt
Source300:      bundles.tar.xz
Source301:      update_git.sh
Source302:      config.sh
Source303:      README.PACKAGING
# Upstream First -- https://wiki.qemu.org/Contribute/SubmitAPatch
# This patch queue is auto-generated - see README.PACKAGING for process

# Patches applied in base project:
Patch00000:     net-vmxnet3-validate-configuration-value.patch
Patch00001:     XXX-dont-dump-core-on-sigabort.patch
Patch00002:     qemu-binfmt-conf-Modify-default-path.patch
Patch00003:     qemu-cvs-gettimeofday.patch
Patch00004:     qemu-cvs-ioctl_debug.patch
Patch00005:     qemu-cvs-ioctl_nodirection.patch
Patch00006:     linux-user-add-binfmt-wrapper-for-argv-0.patch
Patch00007:     PPC-KVM-Disable-mmu-notifier-check.patch
Patch00008:     linux-user-binfmt-support-host-binaries.patch
Patch00009:     linux-user-Fake-proc-cpuinfo.patch
Patch00010:     linux-user-use-target_ulong.patch
Patch00011:     Make-char-muxer-more-robust-wrt-small-FI.patch
Patch00012:     linux-user-lseek-explicitly-cast-non-set.patch
Patch00013:     AIO-Reduce-number-of-threads-for-32bit-h.patch
Patch00014:     xen_disk-Add-suse-specific-flush-disable.patch
Patch00015:     qemu-bridge-helper-reduce-security-profi.patch
Patch00016:     qemu-binfmt-conf-use-qemu-ARCH-binfmt.patch
Patch00017:     roms-Makefile-pass-a-packaging-timestamp.patch
Patch00018:     Raise-soft-address-space-limit-to-hard-l.patch
Patch00019:     increase-x86_64-physical-bits-to-42.patch
Patch00020:     i8254-Fix-migration-from-SLE11-SP2.patch
Patch00021:     acpi_piix4-Fix-migration-from-SLE11-SP2.patch
Patch00022:     Make-installed-scripts-explicitly-python.patch
Patch00023:     hw-smbios-handle-both-file-formats-regar.patch
Patch00024:     xen-add-block-resize-support-for-xen-dis.patch
Patch00025:     tests-qemu-iotests-Triple-timeout-of-i-o.patch
Patch00026:     tests-Fix-block-tests-to-be-compatible-w.patch
Patch00027:     xen-ignore-live-parameter-from-xen-save-.patch
Patch00028:     tests-change-error-message-in-test-162.patch
Patch00029:     hw-intc-exynos4210_gic-provide-more-room.patch
Patch00030:     configure-only-populate-roms-if-softmmu.patch
Patch00031:     pc-bios-s390-ccw-net-avoid-warning-about.patch
Patch00032:     roms-change-cross-compiler-naming-to-be-.patch
Patch00033:     test-add-mapping-from-arch-of-i686-to-qe.patch
Patch00034:     configure-remove-pkgversion-from-CONFIG_.patch
Patch00035:     Revert-qht-constify-qht_statistics_init.patch
Patch00036:     qht-Revert-some-constification-in-qht.c.patch
Patch00037:     meson-install-ivshmem-client-and-ivshmem.patch
Patch00038:     Revert-roms-efirom-tests-uefi-test-tools.patch
Patch00039:     Makefile-Don-t-check-pc-bios-as-pre-requ.patch
Patch00040:     roms-Makefile-add-cross-file-to-qboot-me.patch
Patch00041:     usb-Help-compiler-out-to-avoid-a-warning.patch
Patch00042:     module-for-virtio-gpu-pre-load-module-to.patch
Patch00043:     qom-handle-case-of-chardev-spice-module-.patch
Patch00044:     doc-add-our-support-doc-to-the-main-proj.patch
Patch00045:     ui-Fix-memory-leak-in-qemu_xkeymap_mappi.patch
Patch00046:     hw-rx-rx-gdbsim-Do-not-accept-invalid-me.patch
Patch00047:     monitor-qmp-fix-race-on-CHR_EVENT_CLOSED.patch
Patch00048:     vhost-user-blk-Fail-gracefully-on-too-la.patch
Patch00049:     usb-redir-avoid-dynamic-stack-allocation.patch
Patch00050:     virtiofsd-Fix-side-effect-in-assert.patch
Patch00051:     sockets-update-SOCKET_ADDRESS_TYPE_FD-li.patch
Patch00052:     virtio-blk-Fix-rollback-path-in-virtio_b.patch
Patch00053:     hw-block-nvme-consider-metadata-read-aio.patch
Patch00054:     vhost-user-blk-Make-sure-to-set-Error-on.patch
Patch00055:     vhost-user-blk-Don-t-reconnect-during-in.patch
Patch00056:     vhost-user-blk-Get-more-feature-flags-fr.patch
Patch00057:     virtio-Fail-if-iommu_platform-is-request.patch
Patch00058:     vhost-user-blk-Check-that-num-queues-is-.patch
Patch00059:     vfio-ccw-Permit-missing-IRQs.patch
# Patches applied in roms/seabios/:
Patch01000:     seabios-use-python2-explicitly-as-needed.patch
Patch01001:     seabios-switch-to-python3-as-needed.patch
Patch01002:     enable-cross-compilation-on-ARM.patch
Patch01003:     build-be-explicit-about-mx86-used-note-n.patch
# Patches applied in roms/ipxe/:
Patch02000:     ath5k-Add-missing-AR5K_EEPROM_READ-in-at.patch
Patch02001:     stub-out-the-SAN-req-s-in-int13.patch
Patch02002:     ipxe-Makefile-fix-issues-of-build-reprod.patch
Patch02003:     help-compiler-out-by-initializing-array.patch
# Patches applied in roms/sgabios/:
Patch03000:     sgabios-Makefile-fix-issues-of-build-rep.patch
Patch03001:     roms-sgabios-Fix-csum8-to-be-built-by-ho.patch
# Patches applied in roms/qboot/:
Patch11000:     qboot-add-cross.ini-file-to-handle-aarch.patch
# Patches applied in roms/edk2/BaseTools/Source/C/BrotliCompress/brotli/:
Patch27000:     brotli-fix-actual-variable-array-paramet.patch

# Please do not add patches manually here.

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Common BuildRequires listed here:
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja >= 1.7
BuildRequires:  python3-base >= 3.6
BuildRequires:  python3-setuptools
%if "%{name}" == "qemu-linux-user"
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  pcre-devel-static
BuildRequires:  zlib-devel-static
# we must not install the qemu-linux-user package when under QEMU build
%if 0%{?qemu_user_space_build:1}
#!BuildIgnore:  post-build-checks
%endif

%description
QEMU provides CPU emulation along with other related capabilities. This package
provides programs to run user space binaries and libraries meant for another
architecture. The syscall interface is intercepted and execution below the
syscall layer occurs on the native hardware and operating system.

# above section is for qemu-linux-user
# ------------------------------------------------------------------------
%else
%if %{build_x86_firmware_from_source}
BuildRequires:  acpica
%endif
BuildRequires:  pkgconfig(alsa)
%if %{build_x86_firmware_from_source}
BuildRequires:  binutils-devel
%endif
BuildRequires:  bison
BuildRequires:  brlapi-devel
%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
# We must cross-compile on non-x86*
BuildRequires:  cross-i386-binutils
BuildRequires:  cross-i386-gcc%gcc_version
BuildRequires:  cross-x86_64-binutils
BuildRequires:  cross-x86_64-gcc%gcc_version
%endif
%endif
BuildRequires:  pkgconfig(libcurl) >= 7.29
BuildRequires:  pkgconfig(libsasl2)
%if %{build_x86_firmware_from_source}
BuildRequires:  dos2unix
%endif
BuildRequires:  flex
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
%if %{build_x86_firmware_from_source}
BuildRequires:  glibc-devel-32bit
%endif
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbz2-devel
BuildRequires:  libfdt-devel >= 1.4.2
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glusterfs-api) >= 3
BuildRequires:  pkgconfig(gnutls) >= 3.1.18
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libcacard) >= 2.5.1
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libiscsi) >= 1.9.0
BuildRequires:  pkgconfig(libjpeg)
%if 0%{?with_daxctl}
BuildRequires:  pkgconfig(libndctl)
%endif
BuildRequires:  pkgconfig(libnfs) >= 1.9.3
%ifnarch %arm s390x
BuildRequires:  libnuma-devel
%endif
BuildRequires:  pkgconfig(pixman-1) >= 0.21.8
%ifarch x86_64
BuildRequires:  pkgconfig(libpmem)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
%if 0%{?with_rbd}
BuildRequires:  librbd-devel
%endif
BuildRequires:  Mesa-devel
BuildRequires:  pkgconfig(libseccomp) >= 2.3.0
BuildRequires:  pkgconfig(libssh) >= 0.8
BuildRequires:  pkgconfig(slirp) >= 4.2.0
BuildRequires:  pkgconfig(spice-server) >= 0.12.5
%if 0%{?with_uring}
BuildRequires:  pkgconfig(liburing) >= %liburing_min_version
%endif
BuildRequires:  lzfse-devel
BuildRequires:  multipath-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rdma-core-devel
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.13
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.3
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vdeplug)
BuildRequires:  pkgconfig(xkbcommon)
%{?systemd_ordering}
%if %{kvm_available}
BuildRequires:  pkgconfig(udev)
%endif
BuildRequires:  update-desktop-files
BuildRequires:  usbredir-devel >= 0.6
BuildRequires:  pkgconfig(virglrenderer) >= 0.4.1
BuildRequires:  pkgconfig(vte-2.91)
%ifarch x86_64
BuildRequires:  xen-devel >= 4.2
%endif
BuildRequires:  xfsprogs-devel
%if %{build_x86_firmware_from_source}
BuildRequires:  pkgconfig(liblzma)
%endif
BuildRequires:  pkgconfig(zlib)
%if "%{name}" == "qemu"
Requires:       group(kvm)
Requires:       group(qemu)
Requires:       user(qemu)
Requires(post): coreutils
%if %{kvm_available}
Requires(post): acl
Requires(post): udev
%ifarch s390x
Requires(post): procps
%endif
Recommends:     kvm_stat
%endif
Recommends:     qemu-block-curl
Recommends:     qemu-ksm = %{qemuver}
Recommends:     qemu-tools
Recommends:     qemu-ui-curses
%ifarch s390x
Recommends:     qemu-hw-s390x-virtio-gpu-ccw
%else
Recommends:     qemu-hw-display-qxl
Recommends:     qemu-hw-display-virtio-gpu
Recommends:     qemu-hw-display-virtio-gpu-pci
Recommends:     qemu-hw-display-virtio-vga
Recommends:     qemu-hw-usb-redirect
Recommends:     qemu-hw-usb-smartcard
Recommends:     qemu-ui-gtk
Recommends:     qemu-ui-spice-app
%endif
%ifarch %{ix86} x86_64
Recommends:     qemu-x86
%else
Suggests:       qemu-x86
%endif
%ifarch ppc ppc64 ppc64le
Recommends:     qemu-ppc
%else
Suggests:       qemu-ppc
%endif
%ifarch s390x
Recommends:     qemu-s390x
%else
Suggests:       qemu-s390x
%endif
%ifarch %arm aarch64
Recommends:     qemu-arm
%else
Suggests:       qemu-arm
%endif
Suggests:       qemu-block-dmg
Suggests:       qemu-block-gluster
Suggests:       qemu-block-iscsi
Suggests:       qemu-block-nfs
%if 0%{?with_rbd}
Suggests:       qemu-block-rbd
%endif
Suggests:       qemu-block-ssh
Suggests:       qemu-chardev-baum
Suggests:       qemu-extra
Suggests:       qemu-skiboot
Suggests:       qemu-lang
Suggests:       qemu-microvm
Suggests:       qemu-vhost-user-gpu
Obsoletes:      qemu-audio-oss < %{qemuver}
Obsoletes:      qemu-audio-sdl < %{qemuver}
Obsoletes:      qemu-ui-sdl < %{qemuver}

%define generic_qemu_description QEMU provides full machine emulation and cross architecture usage. It closely\
integrates with KVM and Xen virtualization, allowing for excellent performance.\
Many options are available for defining the emulated environment, including\
traditional devices, direct host device access, and interfaces specific to\
virtualization.

%description
%{generic_qemu_description}

This package acts as an umbrella package to the other QEMU sub-packages.

%package x86
Summary:        Machine emulator and virtualizer for x86 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Requires:       qemu-ipxe
Requires:       qemu-seabios
Requires:       qemu-sgabios
Requires:       qemu-vgabios
Recommends:     ovmf
Recommends:     qemu-microvm
Recommends:     qemu-ovmf-x86_64

%description x86
%{generic_qemu_description}

This package provides i386 and x86_64 emulation.

%package ppc
Summary:        Machine emulator and virtualizer for Power architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios

%description ppc
%{generic_qemu_description}

This package provides ppc and ppc64 emulation.

%package s390x
Summary:        Machine emulator and virtualizer for S/390 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Provides:       qemu-s390 = %{qemuver}
Obsoletes:      qemu-s390 < %{qemuver}

%description s390x
%{generic_qemu_description}

This package provides s390x emulation.

%package arm
Summary:        Machine emulator and virtualizer for ARM architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     ovmf
Recommends:     qemu-ipxe
Recommends:     qemu-uefi-aarch64
Recommends:     qemu-vgabios

%description arm
%{generic_qemu_description}

This package provides arm emulation.

%package extra
Summary:        Machine emulator and virtualizer for "extra" architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-skiboot
Recommends:     qemu-vgabios

%description extra
%{generic_qemu_description}

This package provides some lesser used emulations, including alpha, m68k,
mips, moxie, sparc, and xtensa. (The term "extra" is juxtapositioned against
more popular QEMU packages which are dedicated to a single architecture.)

%if %{legacy_qemu_kvm}
%package kvm
Summary:        Wrapper to enable KVM acceleration under QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%ifarch %ix86 x86_64
Requires:       qemu-x86 = %{qemuver}
%endif
%ifarch s390x
Requires:       qemu-s390x = %{qemuver}
%endif
Provides:       kvm = %{qemuver}
Obsoletes:      kvm < %{qemuver}

%description kvm
%{generic_qemu_description}

This package provides a symlink to the main QEMU emulator used for KVM
virtualization. The symlink is named qemu-kvm, which causes the QEMU program
to enable the KVM accelerator, due to the name reference ending with 'kvm'.
This package is an artifact of the early origins of QEMU, and is deprecated.
%endif

%package lang
Summary:        Translations for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0

%description lang
This package contains a few language translations, particularly for the
graphical user interface components that come with QEMU. The bulk of strings
in QEMU are not localized.

# Modules need to match {qemu-system-*,qemu-img} version.
# We cannot have qemu and qemu-tools require them in the right version,
# as that would drag in the dependencies the modules are supposed to avoid.
# Nor can we have modules require the right version of qemu and qemu-tools
# as Xen reuses our qemu-tools but does not want our qemu and qemu-x86.
%define qemu_module_conflicts \
Conflicts:      %name < %{qemuver}-%{release} \
Conflicts:      %name > %{qemuver}-%{release} \
Conflicts:      qemu-tools < %{qemuver}-%{release} \
Conflicts:      qemu-tools > %{qemuver}-%{release}

%package audio-alsa
Summary:        ALSA based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-alsa
This package contains a module for ALSA based audio support for QEMU.

%package audio-pa
Summary:        Pulse Audio based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-pa
This package contains a module for Pulse Audio based audio support for QEMU.

%package audio-spice
Summary:        Spice based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/05
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description audio-spice
This package contains a module for Spice based audio support for QEMU.

%package block-curl
Summary:        cURL block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-curl
This package contains a module for accessing network-based image files over
a network connection from qemu-img tool and QEMU system emulation.

%package block-dmg
Summary:        DMG block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-dmg
This package contains a module for accessing Mac OS X image files from
qemu-img tool and QEMU system emulation.

%package block-gluster
Summary:        GlusterFS block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-gluster
This package contains a module for accessing network-based image files over a
GlusterFS network connection from qemu-img tool and QEMU system emulation.

%package block-iscsi
Summary:        iSCSI block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-iscsi
This package contains a module for accessing network-based image files over an
iSCSI network connection from qemu-img tool and QEMU system emulation.

%package block-nfs
Summary:        direct Network File System support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-nfs
This package contains a module for directly accessing nfs based image files
for QEMU.

%if 0%{?with_rbd}
%package block-rbd
Summary:        Rados Block Device (Ceph) support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-rbd
This package contains a module for accessing ceph (rbd,rados) image files
for QEMU.
%endif

%package block-ssh
Summary:        SSH (SFTP) block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-ssh
This package contains a module for accessing network-based image files over an
SSH network connection from qemu-img tool and QEMU system emulation.

%package chardev-baum
Summary:        Baum braille chardev support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/00
%{qemu_module_conflicts}

%description chardev-baum
This package contains a module for baum braille chardev support for QEMU.

%package chardev-spice
Summary:        Spice vmc and port chardev support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/08
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description chardev-spice
This package contains a module for Spice chardev support for QEMU.

%package hw-display-qxl
Summary:        QXL display support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/01
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description hw-display-qxl
This package contains a module for QXL display support for QEMU.

%package hw-display-virtio-gpu
Summary:        Virtio GPU display support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/04
%{qemu_module_conflicts}

%description hw-display-virtio-gpu
This package contains a module for Virtio GPU display support for QEMU.

%package hw-display-virtio-gpu-pci
Summary:        Virtio-gpu pci device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-hw-display-virtio-gpu
Provides:       %name:%_datadir/%name/forsplits/11
%{qemu_module_conflicts}

%description hw-display-virtio-gpu-pci
This package contains a module providing the virtio gpu pci device for QEMU.

%package hw-display-virtio-vga
Summary:        Virtio vga device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/12
%{qemu_module_conflicts}

%description hw-display-virtio-vga
This package contains a module providing the virtio vga device for QEMU.

%package hw-s390x-virtio-gpu-ccw
Summary:        S390x virtio-gpu ccw device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-hw-display-virtio-gpu
Provides:       %name:%_datadir/%name/forsplits/13
%{qemu_module_conflicts}

%description hw-s390x-virtio-gpu-ccw
This package contains a module providing the s390x virtio gpu ccw device for
QEMU.

%package hw-usb-redirect
Summary:        USB redirection support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/02
%{qemu_module_conflicts}

%description hw-usb-redirect
This package contains a module for USB redirection support for QEMU.

%package hw-usb-smartcard
Summary:        USB smartcard support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/03
%{qemu_module_conflicts}

%description hw-usb-smartcard
This package contains a modules for USB smartcard support for QEMU.

%package ui-curses
Summary:        Curses based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-curses
This package contains a module for doing curses based UI for QEMU.

%package ui-gtk
Summary:        GTK based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-opengl
%{qemu_module_conflicts}

%description ui-gtk
This package contains a module for doing GTK based UI for QEMU.

%package ui-opengl
Summary:        OpenGL based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/10
%{qemu_module_conflicts}

%description ui-opengl
This package contains a module for doing OpenGL based UI for QEMU.

%package ui-spice-app
Summary:        Spice UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-chardev-spice
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description ui-spice-app
This package contains a module for doing Spice based UI for QEMU.

%package ui-spice-core
Summary:        Core Spice support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/09
Requires:       qemu-ui-opengl
# This next Requires is only since virt-manager expects audio support
Requires:       qemu-audio-spice
%{qemu_module_conflicts}

%description ui-spice-core
This package contains a module with core Spice support for QEMU.

%package vhost-user-gpu
Summary:        Vhost user mode virtio-gpu 2D/3D rendering backend for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description vhost-user-gpu
This package contains a vhost user mode virtio-gpu 2D/3D rendering backend for
QEMU.

%package tools
Summary:        Tools for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires(pre):  permissions
Requires:       group(kvm)
Recommends:     multipath-tools
Recommends:     qemu-block-curl
%if 0%{?with_rbd}
Recommends:     qemu-block-rbd
%endif

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper, ivshmem, disk utilities and scripts for various purposes.

%package ivshmem-tools
Summary:        Inter-VM Shared Memory Tools for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_datadir/%name/forsplits/07

%description ivshmem-tools
This package contains a sample shared memory client and server which utilize
QEMU's Inter-VM shared memory device as specified by the ivshmem client-server
protocol specification documented in docs/specs/ivshmem-spec.txt in QEMU source
code.

%package guest-agent
Summary:        Guest agent for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       group(kvm)
Requires(post): udev
Supplements:    modalias(acpi*:QEMU0002%3A*)
Supplements:    modalias(pci:v00005853d00000001sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000FFFDd00000101sv*sd*bc*sc*i*)
%{?systemd_ordering}

%description guest-agent
This package contains the QEMU guest agent. It is installed in the linux guest
to provide information and control at the guest OS level.

%ifarch %{build_rom_arch}
%package microvm
Summary:        x86 MicroVM firmware for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
BuildArch:      noarch

%description microvm
This package provides minimal x86 firmware for booting certain guests under
QEMU. qboot provides the minimum resources needed to boot PVH and bzImages.
bios-microvm, created from a minimal seabios configuration, provides slightly
wider support than qboot, but still focuses on quick boot up.

%package seabios
Summary:        x86 Legacy BIOS for QEMU
Group:          System/Emulators/PC
Version:        %{sbver}
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description seabios
SeaBIOS is an open source implementation of a 16bit x86 BIOS. SeaBIOS
is the default and legacy BIOS for QEMU.

%package vgabios
Summary:        VGA BIOSes for QEMU
Group:          System/Emulators/PC
Version:        %{sbver}
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description vgabios
VGABIOS provides the video ROM BIOSes for the following variants of VGA
emulated devices: Std VGA, QXL, Cirrus CLGD 5446 and VMware emulated
video card. For use with QEMU.

%package sgabios
Summary:        Serial Graphics Adapter BIOS for QEMU
Group:          System/Emulators/PC
Version:        8
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description sgabios
The Google Serial Graphics Adapter BIOS or SGABIOS provides a means for legacy
x86 software to communicate with an attached serial console as if a video card
were attached. For use with QEMU.

%package ipxe
Summary:        PXE ROMs for QEMU NICs
Group:          System/Emulators/PC
Version:        1.0.0+
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description ipxe
Provides Preboot Execution Environment (PXE) ROM support for various emulated
network adapters available with QEMU.
%endif

%package skiboot
Summary:        OPAL firmware (aka skiboot), used in booting OpenPOWER systems
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       %name:%_datadir/%name/forsplits/06

%description skiboot
Provides OPAL (OpenPower Abstraction Layer) firmware, aka skiboot, as
traditionally packaged with QEMU.

%package ksm
Summary:        Kernel Samepage Merging services
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires(pre):  coreutils
Requires(post): coreutils

%description ksm
Kernel Samepage Merging (KSM) is a memory-saving de-duplication feature, that
merges anonymous (private) pages (not pagecache ones).

This package provides a service file for starting and stopping KSM.

# above section is for qemu
%else
BuildRequires:  bc
BuildRequires:  qemu-arm = %{qemuver}
BuildRequires:  qemu-audio-alsa = %{qemuver}
BuildRequires:  qemu-audio-pa = %{qemuver}
BuildRequires:  qemu-audio-spice = %{qemuver}
BuildRequires:  qemu-block-curl = %{qemuver}
BuildRequires:  qemu-block-dmg = %{qemuver}
BuildRequires:  qemu-block-gluster = %{qemuver}
BuildRequires:  qemu-block-iscsi = %{qemuver}
BuildRequires:  qemu-block-nfs = %{qemuver}
%if 0%{?with_rbd}
BuildRequires:  qemu-block-rbd = %{qemuver}
%endif
BuildRequires:  qemu-block-ssh = %{qemuver}
BuildRequires:  qemu-chardev-baum = %{qemuver}
BuildRequires:  qemu-chardev-spice = %{qemuver}
BuildRequires:  qemu-extra = %{qemuver}
BuildRequires:  qemu-guest-agent = %{qemuver}
BuildRequires:  qemu-hw-display-qxl = %{qemuver}
BuildRequires:  qemu-hw-display-virtio-gpu = %{qemuver}
BuildRequires:  qemu-hw-usb-redirect = %{qemuver}
BuildRequires:  qemu-hw-usb-smartcard = %{qemuver}
BuildRequires:  qemu-ipxe = 1.0.0+
BuildRequires:  qemu-ivshmem-tools = %{qemuver}
BuildRequires:  qemu-ksm = %{qemuver}
BuildRequires:  qemu-lang = %{qemuver}
BuildRequires:  qemu-ppc = %{qemuver}
BuildRequires:  qemu-s390x = %{qemuver}
BuildRequires:  qemu-seabios = %{sbver}
BuildRequires:  qemu-sgabios = 8
BuildRequires:  qemu-skiboot = %{qemuver}
BuildRequires:  qemu-tools = %{qemuver}
BuildRequires:  qemu-ui-curses = %{qemuver}
BuildRequires:  qemu-ui-gtk = %{qemuver}
BuildRequires:  qemu-ui-opengl = %{qemuver}
BuildRequires:  qemu-ui-spice-app = %{qemuver}
BuildRequires:  qemu-ui-spice-core = %{qemuver}
BuildRequires:  qemu-vgabios = %{sbver}
BuildRequires:  qemu-x86 = %{qemuver}

%description
This package records qemu testsuite results and represents successful testing.

# above section is for qemu-testsuite
%endif
# above section is for qemu and qemu-testsuite
%endif

# ========================================================================

%prep
%setup -q -n %{srcname}-%{expand:%%(SV=%{srcver};echo ${SV%%%%+git*})}
%patch00000 -p1
%patch00001 -p1
%patch00002 -p1
%patch00003 -p1
%patch00004 -p1
%patch00005 -p1
%patch00006 -p1
%patch00007 -p1
%patch00008 -p1
%patch00009 -p1
%patch00010 -p1
%patch00011 -p1
%patch00012 -p1
%patch00013 -p1
%patch00014 -p1
%patch00015 -p1
%patch00016 -p1
%patch00017 -p1
%patch00018 -p1
%patch00019 -p1
%patch00020 -p1
%patch00021 -p1
%patch00022 -p1
%patch00023 -p1
%patch00024 -p1
%patch00025 -p1
%patch00026 -p1
%patch00027 -p1
%patch00028 -p1
%patch00029 -p1
%patch00030 -p1
%patch00031 -p1
%patch00032 -p1
%patch00033 -p1
%patch00034 -p1
%patch00035 -p1
%patch00036 -p1
%patch00037 -p1
%patch00038 -p1
%patch00039 -p1
%ifarch aarch64
%patch00040 -p1
%endif
%ifarch %arm %ix86 ppc
%patch00041 -p1
%endif
%patch00042 -p1
%patch00043 -p1
%if %{legacy_qemu_kvm}
%patch00044 -p1
%endif
%patch00045 -p1
%patch00046 -p1
%patch00047 -p1
%patch00048 -p1
%patch00049 -p1
%patch00050 -p1
%patch00051 -p1
%patch00052 -p1
%patch00053 -p1
%patch00054 -p1
%patch00055 -p1
%patch00056 -p1
%patch00057 -p1
%patch00058 -p1
%patch00059 -p1
%patch01000 -p1
%patch01001 -p1
%patch01002 -p1
%patch01003 -p1
%patch02000 -p1
%if 0%{?patch-possibly-applied-elsewhere}
%patch02001 -p1
%endif
%patch02002 -p1
%patch02003 -p1
%patch03000 -p1
%patch03001 -p1
%patch11000 -p1
%patch27000 -p1

%if "%{name}" != "qemu-linux-user"
# for the record, this set of firmware files is installed, but we don't
# build (yet): bamboo.dtb canyonlands.dtb hppa-firmware.img openbios-ppc
# openbios-sparc32 openbios-sparc64 palcode-clipper petalogix-ml605.dtb
# petalogix-s3adsp1800.dtb QEMU,cgthree.bin QEMU,tcx.bin qemu_vga.ndrv
# u-boot.e500 u-boot-sam460-20100605.bin opensbi-riscv32-generic-fw_dynamic.bin
# opensbi-riscv32-generic-fw_dynamic.elf npcm7xx_bootrom.bin

# This first list group isn't specific to what this instance builds
%define ppc_default_firmware {%nil}
%define ppc_extra_firmware {skiboot.lid slof.bin}
%define ppc64_only_default_firmware {%nil}
%define ppc64_only_extra_firmware {%nil}
%define riscv64_default_firmware {opensbi-riscv64-generic-fw_dynamic.bin \
opensbi-riscv64-generic-fw_dynamic.elf}
%define riscv64_extra_firmware {%nil}
%define s390x_default_firmware {s390-ccw.img s390-netboot.img}
%define s390x_extra_firmware {%nil}
%define x86_default_firmware {linuxboot.bin linuxboot_dma.bin multiboot.bin \
kvmvapic.bin pvh.bin}
%define x86_extra_firmware {bios.bin bios-256k.bin bios-microvm.bin qboot.rom \
pxe-e1000.rom pxe-eepro100.rom pxe-ne2k_pci.rom pxe-pcnet.rom pxe-rtl8139.rom \
pxe-virtio.rom sgabios.bin vgabios-ati.bin vgabios-bochs-display.bin \
vgabios.bin vgabios-cirrus.bin vgabios-qxl.bin vgabios-ramfb.bin \
vgabios-stdvga.bin vgabios-virtio.bin vgabios-vmware.bin}
%define x86_64_only_default_firmware {%nil}
%define x86_64_only_extra_firmware {efi-e1000.rom efi-e1000e.rom \
efi-eepro100.rom efi-ne2k_pci.rom efi-pcnet.rom efi-rtl8139.rom efi-virtio.rom \
efi-vmxnet3.rom}

%define firmware { \
%{?ppc_default_firmware} %{?ppc_extra_firmware} \
%{?ppc64_only_default_firmware} %{?ppc64_only_extra_firmware} \
%{?riscv64_default_firmware} %{?riscv64_extra_firmware} \
%{?s390x_default_firmware} %{?s390x_extra_firmware} \
%{?x86_default_firmware} %{?x86_extra_firmware} \
%{?x86_64_only_default_firmware} %{?x86_64_only_extra_firmware} }

# This second list group is specific to what this instance builds
%define ppc_default_built_firmware %{ppc_default_firmware}
%if %{build_skiboot_from_source} && %{build_slof_from_source}
%define ppc_extra_built_firmware %{ppc_extra_firmware}
%else
%if %{build_skiboot_from_source}
%define ppc_extra_built_firmware {skiboot.lid}
%endif
%if %{build_slof_from_source}
%define ppc_extra_built_firmware {slof.bin}
%endif
%endif

%ifarch ppc64
%define ppc64_only_default_built_firmware %{ppc64_only_default_firmware}
%define ppc64_only_extra_built_firmware %{ppc64_only_extra_firmware}
%endif

%ifarch riscv64
%define riscv64_default_built_firmware %{riscv64_default_firmware}
%define riscv64_extra_built_firmware %{riscv64_extra_firmware}
%endif

%ifarch s390x
%define s390x_default_built_firmware %{s390x_default_firmware}
%define s390x_extra_built_firmware %{s390x_extra_firmware}
%endif

%ifarch %ix86 x86_64
%define x86_default_built_firmware %{x86_default_firmware}
%ifarch x86_64
%define x86_64_only_default_built_firmware %{x86_64_only_default_firmware}
%endif
%endif

%if %{build_x86_firmware_from_source}
%define x86_extra_built_firmware %{x86_extra_firmware}
%ifarch x86_64
%define x86_64_only_extra_built_firmware %{x86_64_only_extra_firmware}
%endif
%endif

%define built_firmware { \
%{?ppc_default_built_firmware} %{?ppc_extra_built_firmware} \
%{?ppc64_only_default_built_firmware} %{?ppc64_only_extra_built_firmware} \
%{?riscv64_default_built_firmware} %{?riscv64_extra_built_firmware} \
%{?s390x_default_built_firmware} %{?s390x_extra_built_firmware} \
%{?x86_default_built_firmware} %{?x86_extra_built_firmware} \
%{?x86_64_only_default_built_firmware} %{?x86_64_only_extra_built_firmware} }

# above section is for qemu and qemu-testsuite
%endif

# ========================================================================

%build

# non-x86 archs still seem to have some issues with Link Time Optimization
%ifnarch %ix86 x86_64
%define _lto_cflags %{nil}
%endif

%if %{legacy_qemu_kvm}
%ifarch s390x
cp %{SOURCE13} docs/supported.rst
%else
cp %{SOURCE13} docs/supported.rst
%endif
%endif

%define srcdir %{_builddir}/%buildsubdir
%define blddir %srcdir/build
mkdir -p %blddir
cd %blddir

%srcdir/configure \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--docdir=%_docdir \
	--firmwarepath=%_datadir/%name \
        --python=%_bindir/python3 \
	--extra-cflags="%{optflags}" \
	--with-git-submodules=ignore \
	--disable-fuzzing \
	--disable-multiprocess \
	--disable-stack-protector \
	--disable-strip \
	--disable-tcg-interpreter \
	--with-git-submodules=ignore \
%if "%{name}" != "qemu-linux-user"
	--with-pkgversion="%(echo '%{distro}' | sed 's/ (.*)//')" \
	--with-default-devices \
	--enable-system --disable-linux-user \
	--enable-tools --enable-guest-agent \
	--enable-modules \
	--disable-module-upgrades \
	--enable-slirp=system \
	--enable-pie \
	--enable-docs \
	--audio-drv-list="pa alsa" \
	--enable-attr \
	--disable-auth-pam \
	--enable-bochs \
	--enable-brlapi \
	--enable-bzip2 \
	--enable-cap-ng \
	--disable-capstone \
	--enable-cloop \
	--enable-coroutine-pool \
	--disable-crypto-afalg \
	--enable-curl \
	--enable-curses \
	--enable-dmg \
	--enable-fdt \
	--enable-gio \
	--enable-gcrypt \
	--enable-glusterfs \
	--enable-gnutls \
	--enable-gtk \
	--disable-hax \
	--disable-hvf \
	--enable-iconv \
	--disable-jemalloc \
%if %{kvm_available}
	--enable-kvm \
%else
	--disable-kvm \
%endif
%if 0%{?with_daxctl}
	--enable-libdaxctl \
%else
	--disable-libdaxctl \
%endif
	--enable-libiscsi \
	--enable-libnfs \
%ifarch x86_64
	--enable-libpmem \
%else
	--disable-libpmem \
%endif
	--enable-libssh \
	--enable-libusb \
	--disable-libxml2 \
	--enable-linux-aio \
%if 0%{?with_uring}
        --enable-linux-io-uring \
%else
        --disable-linux-io-uring \
%endif
	--enable-lzfse \
	--enable-lzo \
	--disable-malloc-trim \
%if %{with system_membarrier}
	--enable-membarrier \
%else
	--disable-membarrier \
%endif
	--enable-mpath \
	--disable-netmap \
	--disable-nettle \
%ifarch %arm s390x
	--disable-numa \
%else
	--enable-numa \
%endif
	--enable-opengl \
	--enable-parallels \
	--disable-plugins \
	--enable-pvrdma \
	--enable-qcow1 \
	--enable-qed \
%if 0%{?with_rbd}
	--enable-rbd \
%else
	--disable-rbd \
%endif
	--enable-rdma \
	--enable-replication \
	--disable-safe-stack \
	--disable-sanitizers \
	--disable-sdl \
	--disable-sdl-image \
	--enable-seccomp \
	--enable-sheepdog \
	--enable-smartcard \
	--enable-snappy \
	--enable-spice \
	--disable-tcmalloc \
	--enable-tpm \
	--enable-usb-redir \
	--enable-vde \
	--enable-vdi \
	--enable-vhost-crypto \
	--enable-vhost-kernel \
	--enable-vhost-net \
	--enable-vhost-scsi \
	--enable-vhost-user \
	--enable-vhost-user-blk-server \
        --enable-vhost-user-fs \
	--enable-vhost-vdpa \
	--enable-vhost-vsock \
	--enable-virglrenderer \
	--enable-virtfs \
	--enable-vnc \
	--enable-vnc-jpeg \
	--enable-vnc-png \
	--enable-vnc-sasl \
	--enable-vte \
	--enable-vvfat \
	--enable-werror \
	--disable-whpx \
%ifarch x86_64
	--enable-xen \
	--enable-xen-pci-passthrough \
%else
	--disable-xen \
%endif
	--enable-xfsctl \
        --enable-xkbcommon \
# above section is for qemu and qemu-testsuite
# ------------------------------------------------------------------------
%else
	--without-default-devices \
	--disable-system --enable-linux-user \
	--disable-tools --disable-guest-agent \
	--static \
	--disable-modules \
	--disable-pie \
	--disable-docs \
	--audio-drv-list="" \
	--disable-blobs \
	--disable-bochs \
	--disable-capstone \
	--disable-cloop \
	--enable-coroutine-pool \
	--disable-dmg \
	--disable-fdt \
	--disable-gio \
	--disable-iconv \
	--disable-kvm \
	--disable-libdaxctl \
        --disable-linux-io-uring \
	--disable-malloc-trim \
%if %{with system_membarrier}
	--enable-membarrier \
%else
	--disable-membarrier \
%endif
	--disable-parallels \
	--disable-plugins \
	--disable-qcow1 \
	--disable-qed \
	--disable-replication \
	--disable-sheepdog \
	--disable-safe-stack \
	--disable-slirp \
	--disable-tpm \
	--disable-vdi \
	--disable-vhost-crypto \
	--disable-vhost-kernel \
	--disable-vhost-net \
	--disable-vhost-scsi \
	--disable-vhost-user \
	--disable-vhost-user-blk-server \
        --disable-vhost-user-fs \
	--disable-vhost-vsock \
	--disable-vnc \
	--disable-vvfat \
        --disable-xkbcommon \

# above section is for qemu-linux-user
%endif

%if "%{name}" == "qemu"

# delete the firmware files that we intend to build
for i in %built_firmware
do
  unlink %srcdir/pc-bios/$i
done

make %{?_smp_mflags} V=1

# Firmware

%ifarch s390x
for i in %s390x_default_built_firmware
do
  cp pc-bios/s390-ccw/$i %srcdir/pc-bios/
done
%endif

%ifarch ppc64
for i in %ppc64_only_default_built_firmware
do
  cp pc-bios/spapr-rtas/$i %srcdir/pc-bios/
done
%endif

%ifarch %ix86 x86_64
for i in %x86_default_built_firmware
do
  cp pc-bios/optionrom/$i %srcdir/pc-bios/
done
%ifarch x86_64
for i in %x86_64_only_default_built_firmware
do
  cp pc-bios/optionrom/$i %srcdir/pc-bios/
done
%endif
%endif

%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
export CC=x86_64-suse-linux-gcc
export LD=x86_64-suse-linux-ld
%endif

make %{?_smp_mflags} -C %srcdir/roms bios \
  SEABIOS_EXTRAVERSION="-rebuilt.opensuse.org" \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %srcdir/roms qboot

make %{?_smp_mflags} -C %srcdir/roms seavgabios \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %srcdir/roms seavgabios-ati \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %srcdir/roms pxerom

%ifnarch %ix86
make %{?_smp_mflags} -C %srcdir/roms efirom \
  EDK2_BASETOOLS_OPTFLAGS='-fPIE'
%endif

make                 -C %srcdir/roms sgabios \
  HOSTCC=cc

%if %{force_fit_virtio_pxe_rom}
pushd %srcdir
patch -p1 < %_sourcedir/stub-out-the-SAN-req-s-in-int13.patch
popd
make %{?_smp_mflags} -C %srcdir/roms pxerom_variants=virtio pxerom_targets=1af41000 pxerom
%endif

# enforce pxe rom sizes for migration compatability from SLE 11 SP3 forward
# the following need to be > 64K
%define supported_nics_large {e1000 rtl8139}
# the following need to be <= 64K
%define supported_nics_small {virtio}
# Though not required, make unsupported pxe roms migration compatable as well
%define unsupported_nics {eepro100 ne2k_pci pcnet}

for i in %supported_nics_large %unsupported_nics
  do
    if test "`stat -c '%s' %srcdir/pc-bios/pxe-$i.rom`" -gt "131072" ; then
    echo "pxe rom is too large"
    exit 1
  fi
  if test "`stat -c '%s' %srcdir/pc-bios/pxe-$i.rom`" -le "65536" ; then
    ./%srcdir/roms/ipxe/src/util/padimg.pl %srcdir/pc-bios/pxe-$i.rom -s 65536 -b 255
    echo -ne "SEGMENT OVERAGE\0" >> %srcdir/pc-bios/pxe-$i.rom
  fi
done
for i in %supported_nics_small
  do
    if test "`stat -c '%s' %srcdir/pc-bios/pxe-$i.rom`" -gt "65536" ; then
    echo "pxe rom is too large"
    exit 1
  fi
done
%ifnarch %{ix86} x86_64
unset CC
unset LD
%endif
%endif

%if %{build_skiboot_from_source}
make %{?_smp_mflags} -C %srcdir/roms skiboot CROSS=
%endif

%if %{build_slof_from_source}
make %{?_smp_mflags} -C %srcdir/roms slof
%endif

%if %{build_opensbi_from_source}
make %{?_smp_mflags} -C %srcdir/roms opensbi64-generic CROSS_COMPILE=
%endif

# above section is for qemu
%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-testsuite"

# TODO: Some of these are actually overwritten during the following make's
ln -s %_bindir/qemu-img qemu-img
ln -s %_bindir/qemu-ga qemu-ga
ln -s %_bindir/qemu-io qemu-io
ln -s %_bindir/elf2map elf2map
ln -s %_bindir/qemu-nbd qemu-nbd
ln -s %_bindir/qemu-edid qemu-edid
ln -s %_bindir/qemu-keymap qemu-keymap
ln -s %_bindir/ivshmem-client ivshmem-client
ln -s %_bindir/ivshmem-server ivshmem-server
ln -s %_bindir/qemu-pr-helper qemu-pr-helper
ln -s %_libexecdir/virtfs-proxy-helper fsdev/virtfs-proxy-helper

for i in %firmware
do
  unlink pc-bios/$i
  ln -s %_datadir/qemu/$i pc-bios/$i
done

for conf in %{_builddir}/%buildsubdir/default-configs/targets/*-softmmu.mak; do
  arch=`echo "$conf" | sed -e 's|%{_builddir}/%buildsubdir/default-configs/targets/\(.*\)-softmmu.mak|\1|g'`
  if $(unlink $arch-softmmu/qemu-system-$arch); then
    ln -s %_bindir/qemu-system-$arch $arch-softmmu/qemu-system-$arch
  fi
done

# Compile the QOM test binary first, so that ...
make %{?_smp_mflags} tests/qtest/qom-test V=1
# ... make comes in fresh and has lots of address space (needed for 32bit, bsc#957379)
make %{?_smp_mflags} check-report.tap V=1

%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

make %{?_smp_mflags} V=1

%ifarch %ix86
%define qemu_arch i386
%endif
%ifarch x86_64
%define qemu_arch x86_64
%endif
%ifarch %arm
%define qemu_arch arm
%endif
%ifarch aarch64
%define qemu_arch aarch64
%endif
%ifarch ppc
%define qemu_arch ppc
%endif
%ifarch ppc64
%define qemu_arch ppc64
%endif
%ifarch ppc64le
%define qemu_arch ppc64le
%endif
%ifarch s390x
%define qemu_arch s390x
%endif

%endif

# ========================================================================

%check
cd %blddir
%if "%{name}" == "qemu-testsuite"

export QEMU_PROG=%_bindir/qemu-system-x86_64
export QEMU_IMG_PROG=%_bindir/qemu-img
export QEMU_IO_PROG=%_bindir/qemu-io
export QEMU_NBD_PROG=%_bindir/qemu-nbd
make %{?_smp_mflags} check-block V=1

%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

%ifarch %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le s390x
%ifnarch %arm
%{qemu_arch}-linux-user/qemu-%{qemu_arch} %_bindir/ls > /dev/null
%endif
make %{?_smp_mflags} check-softfloat
%endif

%endif

# ========================================================================

%install
cd %blddir

%if "%{name}" == "qemu-testsuite"

install -D -m 0644 check-report.tap %{buildroot}%_datadir/qemu/check-report.tap

%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

make %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}%_datadir/qemu/keymaps
unlink %{buildroot}%_datadir/qemu/trace-events-all
install -d -m 755 %{buildroot}%_sbindir
install -m 755 scripts/qemu-binfmt-conf.sh %{buildroot}%_sbindir
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-aarch64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-aarch64_be-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-alpha-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-arm-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-armeb-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-cris-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-hexagon-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-hppa-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-i386-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-m68k-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-microblaze-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-microblazeel-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mips-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mips64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mips64el-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mipsel-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mipsn32-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-mipsn32el-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-nios2-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-or1k-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-ppc-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-ppc64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-ppc64le-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-riscv32-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-riscv64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-s390x-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-sh4-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-sh4eb-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-sparc-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-sparc32plus-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-sparc64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-x86_64-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-xtensa-binfmt
ln -s qemu-binfmt %{buildroot}%_bindir/qemu-xtensaeb-binfmt
%fdupes -s %{buildroot}

%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu"

make %{?_smp_mflags} install DESTDIR=%{buildroot}
%ifarch %{build_rom_arch}
install -D -m 0644 %{SOURCE14} %{buildroot}%_datadir/%name/firmware/50-seabios-256k.json
install -D -m 0644 %{SOURCE15} %{buildroot}%_datadir/%name/firmware/60-seabios-128k.json
%else
for f in %{x86_extra_firmware} \
         %{x86_64_only_extra_firmware}; do
  unlink %{buildroot}%_datadir/%name/$f
done
%endif
%find_lang %name
install -d -m 0755 %{buildroot}%_datadir/%name/firmware
install -d -m 0755 %{buildroot}%_libexecdir/supportconfig/plugins
install -d -m 0755 %{buildroot}%_sysconfdir/%name/firmware
install -D -m 0644 %{SOURCE4} %{buildroot}%_sysconfdir/%name/bridge.conf
install -D -m 0755 %{SOURCE3} %{buildroot}%_datadir/%name/qemu-ifup
install -D -p -m 0644 %{SOURCE8} %{buildroot}/usr/lib/udev/rules.d/80-qemu-ga.rules
install -D -m 0755 scripts/analyze-migration.py  %{buildroot}%_bindir/analyze-migration.py
install -D -m 0755 scripts/vmstate-static-checker.py  %{buildroot}%_bindir/vmstate-static-checker.py
install -D -m 0755 %{SOURCE9} %{buildroot}%_libexecdir/supportconfig/plugins/%name
install -D -m 0644 %{SOURCE10} %{buildroot}%_docdir/qemu-arm/supported.txt
install -D -m 0644 %{SOURCE11} %{buildroot}%_docdir/qemu-ppc/supported.txt
install -D -m 0644 %{SOURCE12} %{buildroot}%_docdir/qemu-x86/supported.txt
install -D -m 0644 %{SOURCE13} %{buildroot}%_docdir/qemu-s390x/supported.txt
%if %{legacy_qemu_kvm}
install -D -m 0644 %{SOURCE5} %{buildroot}%_mandir/man1/qemu-kvm.1.gz
install -d %{buildroot}%_docdir/qemu-kvm
%ifarch s390x
ln -s qemu-system-s390x %{buildroot}%_bindir/qemu-kvm
ln -s ../qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
%else
ln -s qemu-system-x86_64 %{buildroot}%_bindir/qemu-kvm
ln -s ../qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
%endif
%endif
%if %{kvm_available}
install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d/80-kvm.rules
%endif
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/qemu-ga@.service
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/ksm.service
%ifarch s390x
install -D -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/modules-load.d/kvm.conf
%endif

# We rely on a separate project / package to provide edk2 firmware
unlink %{buildroot}%_datadir/%name/edk2-licenses.txt
unlink %{buildroot}%_datadir/%name/firmware/50-edk2-i386-secure.json
unlink %{buildroot}%_datadir/%name/firmware/50-edk2-x86_64-secure.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-aarch64.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-arm.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-i386.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-x86_64.json
unlink %{buildroot}%_datadir/%name/edk2-aarch64-code.fd
unlink %{buildroot}%_datadir/%name/edk2-arm-code.fd
unlink %{buildroot}%_datadir/%name/edk2-arm-vars.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-code.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-secure-code.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-vars.fd
unlink %{buildroot}%_datadir/%name/edk2-x86_64-code.fd
unlink %{buildroot}%_datadir/%name/edk2-x86_64-secure-code.fd

# this was never meant for customer consumption - delete even though installed
unlink %{buildroot}%_bindir/elf2dmp

# in support of update-alternatives
mv %{buildroot}%_datadir/%name/skiboot.lid %{buildroot}%_datadir/%name/skiboot.lid.qemu
# create a dummy target for /etc/alternatives/skiboot.lid
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/skiboot.lid %{buildroot}%{_datadir}/%name/skiboot.lid

install -D -m 0644 %{SOURCE201} %{buildroot}%_datadir/%name/forsplits/pkg-split.txt
for X in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16
do
  ln -s pkg-split.txt %{buildroot}%_datadir/%name/forsplits/$X
done
%suse_update_desktop_file qemu
%fdupes -s %{buildroot}

# ========================================================================

%if %{kvm_available}
%post
# Do not execute operations affecting host devices while running in a chroot
if [ $(stat -L -c "%i" /proc/1/root/) = $(stat -L -c "%i" /) ]; then
  setfacl --remove-all /dev/kvm &> /dev/null || :
%ifarch s390x
  if [ -c /dev/kvm ]; then
    %_bindir/chmod 0666 /dev/kvm
    %_bindir/chgrp kvm /dev/kvm
  fi
%endif
  %udev_rules_update
  %_bindir/udevadm trigger -y kvm || :
%ifarch s390x
  sysctl vm.allocate_pgste=1 || :
%endif
fi
%endif

%post tools
%set_permissions %_libexecdir/qemu-bridge-helper

%verifyscript tools
%verify_permissions %_libexecdir/qemu-bridge-helper

%pre guest-agent
%service_add_pre qemu-ga@.service

%post guest-agent
%service_add_post qemu-ga@.service
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl start qemu-ga@virtio\\x2dports-org.qemu.guest_agent.0.service || :
fi

%preun guest-agent
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl stop qemu-ga@virtio\\x2dports-org.qemu.guest_agent.0.service || :
fi

%postun guest-agent
%service_del_postun_without_restart qemu-ga@.service
if [ "$1" = "1" ] ; then
  if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
    /usr/bin/systemctl restart qemu-ga@virtio\\x2dports-org.qemu.guest_agent.0.service || :
  fi
fi

%pre ksm
%service_add_pre ksm.service

%post ksm
%service_add_post ksm.service

%preun ksm
%service_del_preun ksm.service

%postun ksm
%service_del_postun ksm.service

%post skiboot
update-alternatives --install \
   %{_datadir}/%name/skiboot.lid skiboot.lid %{_datadir}/%name/skiboot.lid.qemu 15

%postun skiboot
if [ ! -f %{_datadir}/%name/skiboot.lid.qemu ] ; then
   update-alternatives --remove skiboot.lid %{_datadir}/%name/skiboot.lid.qemu
fi

# above section is for qemu
%endif

# ========================================================================

%files
%defattr(-, root, root)
%doc README.rst VERSION
%license COPYING COPYING.LIB LICENSE

%if "%{name}" == "qemu"
%dir %_datadir/icons/hicolor
%dir %_datadir/icons/hicolor/*/
%dir %_datadir/icons/hicolor/*/apps
%_datadir/applications/qemu.desktop
%_datadir/icons/hicolor/16x16/apps/qemu.png
%_datadir/icons/hicolor/24x24/apps/qemu.png
%_datadir/icons/hicolor/32x32/apps/qemu.bmp
%_datadir/icons/hicolor/32x32/apps/qemu.png
%_datadir/icons/hicolor/48x48/apps/qemu.png
%_datadir/icons/hicolor/64x64/apps/qemu.png
%_datadir/icons/hicolor/128x128/apps/qemu.png
%_datadir/icons/hicolor/256x256/apps/qemu.png
%_datadir/icons/hicolor/512x512/apps/qemu.png
%_datadir/icons/hicolor/scalable/apps/qemu.svg
%dir %_datadir/%name
%dir %_datadir/%name/firmware
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/14
%_datadir/%name/forsplits/15
%_datadir/%name/forsplits/16
%_datadir/%name/forsplits/pkg-split.txt
%_datadir/%name/keymaps
%_datadir/%name/qemu-ifup
%_datadir/%name/qemu-nsis.bmp
%_datadir/%name/trace-events-all
%dir %_datadir/%name/vhost-user
%_datadir/%name/vhost-user/50-qemu-virtiofsd.json
%dir %_docdir/%name/_static
%dir %_docdir/%name/devel
%dir %_docdir/%name/interop
%dir %_docdir/%name/specs
%dir %_docdir/%name/system
%dir %_docdir/%name/system/arm
%dir %_docdir/%name/system/i386
%dir %_docdir/%name/system/ppc
%dir %_docdir/%name/system/riscv
%dir %_docdir/%name/system/s390x
%dir %_docdir/%name/tools
%dir %_docdir/%name/user
%_docdir/%name/.buildinfo
%_docdir/%name/_static/alabaster.css
%_docdir/%name/_static/basic.css
%_docdir/%name/_static/custom.css
%_docdir/%name/_static/doctools.js
%_docdir/%name/_static/documentation_options.js
%_docdir/%name/_static/file.png
%_docdir/%name/_static/jquery-*
%_docdir/%name/_static/jquery.js
%_docdir/%name/_static/language_data.js
%_docdir/%name/_static/minus.png
%_docdir/%name/_static/plus.png
%_docdir/%name/_static/pygments.css
%_docdir/%name/_static/searchtools.js
%_docdir/%name/_static/underscore-*
%_docdir/%name/_static/underscore.js
%_docdir/%name/devel/atomics.html
%_docdir/%name/devel/bitops.html
%_docdir/%name/devel/block-coroutine-wrapper.html
%_docdir/%name/devel/build-system.html
%_docdir/%name/devel/clocks.html
%_docdir/%name/devel/code-of-conduct.html
%_docdir/%name/devel/conflict-resolution.html
%_docdir/%name/devel/control-flow-integrity.html
%_docdir/%name/devel/decodetree.html
%_docdir/%name/devel/fuzzing.html
%_docdir/%name/devel/index.html
%_docdir/%name/devel/kconfig.html
%_docdir/%name/devel/loads-stores.html
%_docdir/%name/devel/memory.html
%_docdir/%name/devel/multi-process.html
%_docdir/%name/devel/migration.html
%_docdir/%name/devel/multi-thread-tcg.html
%_docdir/%name/devel/qom.html
%_docdir/%name/devel/qgraph.html
%_docdir/%name/devel/qtest.html
%_docdir/%name/devel/reset.html
%_docdir/%name/devel/s390-dasd-ipl.html
%_docdir/%name/devel/secure-coding-practices.html
%_docdir/%name/devel/stable-process.html
%_docdir/%name/devel/style.html
%_docdir/%name/devel/tcg-icount.html
%_docdir/%name/devel/tcg-plugins.html
%_docdir/%name/devel/tcg.html
%_docdir/%name/devel/testing.html
%_docdir/%name/devel/tracing.html
%_docdir/%name/genindex.html
%_docdir/%name/index.html
%_docdir/%name/interop/bitmaps.html
%_docdir/%name/interop/dbus.html
%_docdir/%name/interop/dbus-vmstate.html
%_docdir/%name/interop/index.html
%_docdir/%name/interop/live-block-operations.html
%_docdir/%name/interop/pr-helper.html
%_docdir/%name/interop/qemu-ga-ref.html
%_docdir/%name/interop/qemu-qmp-ref.html
%_docdir/%name/interop/qemu-storage-daemon-qmp-ref.html
%_docdir/%name/interop/vhost-user.html
%_docdir/%name/interop/vhost-user-gpu.html
%_docdir/%name/interop/vhost-vdpa.html
%_docdir/%name/objects.inv
%_docdir/%name/search.html
%_docdir/%name/searchindex.js
%_docdir/%name/specs/acpi_hest_ghes.html
%_docdir/%name/specs/acpi_hw_reduced_hotplug.html
%_docdir/%name/specs/index.html
%_docdir/%name/specs/ppc-spapr-numa.html
%_docdir/%name/specs/ppc-spapr-xive.html
%_docdir/%name/specs/ppc-xive.html
%_docdir/%name/specs/tpm.html
%if %{legacy_qemu_kvm}
%_docdir/%name/supported.html
%endif
%_docdir/%name/system/arm/aspeed.html
%_docdir/%name/system/arm/collie.html
%_docdir/%name/system/arm/cpu-features.html
%_docdir/%name/system/arm/digic.html
%_docdir/%name/system/arm/gumstix.html
%_docdir/%name/system/arm/integratorcp.html
%_docdir/%name/system/arm/mps2.html
%_docdir/%name/system/arm/musca.html
%_docdir/%name/system/arm/musicpal.html
%_docdir/%name/system/arm/nseries.html
%_docdir/%name/system/arm/nuvoton.html
%_docdir/%name/system/arm/orangepi.html
%_docdir/%name/system/arm/palm.html
%_docdir/%name/system/arm/raspi.html
%_docdir/%name/system/arm/realview.html
%_docdir/%name/system/arm/sabrelite.html
%_docdir/%name/system/arm/sbsa.html
%_docdir/%name/system/arm/stellaris.html
%_docdir/%name/system/arm/sx1.html
%_docdir/%name/system/arm/versatile.html
%_docdir/%name/system/arm/vexpress.html
%_docdir/%name/system/arm/virt.html
%_docdir/%name/system/arm/xlnx-versal-virt.html
%_docdir/%name/system/arm/xscale.html
%_docdir/%name/system/build-platforms.html
%_docdir/%name/system/cpu-hotplug.html
%_docdir/%name/system/deprecated.html
%_docdir/%name/system/gdb.html
%_docdir/%name/system/generic-loader.html
%_docdir/%name/system/guest-loader.html
%_docdir/%name/system/i386/microvm.html
%_docdir/%name/system/i386/pc.html
%_docdir/%name/system/images.html
%_docdir/%name/system/index.html
%_docdir/%name/system/invocation.html
%_docdir/%name/system/ivshmem.html
%_docdir/%name/system/keys.html
%_docdir/%name/system/license.html
%_docdir/%name/system/linuxboot.html
%_docdir/%name/system/managed-startup.html
%_docdir/%name/system/monitor.html
%_docdir/%name/system/multi-process.html
%_docdir/%name/system/mux-chardev.html
%_docdir/%name/system/net.html
%_docdir/%name/system/nvme.html
%_docdir/%name/system/ppc/embedded.html
%_docdir/%name/system/ppc/powermac.html
%_docdir/%name/system/ppc/powernv.html
%_docdir/%name/system/ppc/prep.html
%_docdir/%name/system/ppc/pseries.html
%_docdir/%name/system/pr-manager.html
%_docdir/%name/system/qemu-block-drivers.html
%_docdir/%name/system/qemu-cpu-models.html
%_docdir/%name/system/qemu-manpage.html
%_docdir/%name/system/quickstart.html
%_docdir/%name/system/removed-features.html
%_docdir/%name/system/riscv/microchip-icicle-kit.html
%_docdir/%name/system/riscv/sifive_u.html
%_docdir/%name/system/s390x/3270.html
%_docdir/%name/system/s390x/bootdevices.html
%_docdir/%name/system/s390x/css.html
%_docdir/%name/system/s390x/protvirt.html
%_docdir/%name/system/s390x/vfio-ap.html
%_docdir/%name/system/s390x/vfio-ccw.html
%_docdir/%name/system/security.html
%_docdir/%name/system/target-arm.html
%_docdir/%name/system/target-avr.html
%_docdir/%name/system/target-i386.html
%_docdir/%name/system/target-m68k.html
%_docdir/%name/system/target-mips.html
%_docdir/%name/system/target-ppc.html
%_docdir/%name/system/target-riscv.html
%_docdir/%name/system/target-rx.html
%_docdir/%name/system/target-s390x.html
%_docdir/%name/system/target-sparc64.html
%_docdir/%name/system/target-sparc.html
%_docdir/%name/system/target-xtensa.html
%_docdir/%name/system/targets.html
%_docdir/%name/system/tls.html
%_docdir/%name/system/usb.html
%_docdir/%name/system/virtio-net-failover.html
%_docdir/%name/system/virtio-pmem.html
%_docdir/%name/system/vnc-security.html
%_docdir/%name/tools/index.html
%_docdir/%name/tools/qemu-img.html
%_docdir/%name/tools/qemu-nbd.html
%_docdir/%name/tools/qemu-pr-helper.html
%_docdir/%name/tools/qemu-trace-stap.html
%_docdir/%name/tools/qemu-storage-daemon.html
%_docdir/%name/tools/virtfs-proxy-helper.html
%_docdir/%name/tools/virtiofsd.html
%_docdir/%name/user/index.html
%_docdir/%name/user/main.html
%dir %_libexecdir/supportconfig
%dir %_libexecdir/supportconfig/plugins
%_libexecdir/supportconfig/plugins/%name
%_mandir/man1/%name.1.gz
%_mandir/man1/qemu-storage-daemon.1.gz
%_mandir/man1/virtiofsd.1.gz
%_mandir/man7/qemu-block-drivers.7.gz
%_mandir/man7/qemu-cpu-models.7.gz
%_mandir/man7/qemu-qmp-ref.7.gz
%_mandir/man7/qemu-ga-ref.7.gz
%_mandir/man7/qemu-storage-daemon-qmp-ref.7.gz
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/firmware
%if %{kvm_available}
%ifarch s390x
%{_prefix}/lib/modules-load.d/kvm.conf
%endif
/usr/lib/udev/rules.d/80-kvm.rules
%endif

%files x86
%defattr(-, root, root)
%_bindir/qemu-system-i386
%_bindir/qemu-system-x86_64
%_datadir/%name/kvmvapic.bin
%_datadir/%name/linuxboot.bin
%_datadir/%name/linuxboot_dma.bin
%_datadir/%name/multiboot.bin
%_datadir/%name/pvh.bin
%dir %_docdir/qemu-x86
%_docdir/qemu-x86/supported.txt

%files ppc
%defattr(-, root, root)
%_bindir/qemu-system-ppc
%_bindir/qemu-system-ppc64
%_datadir/%name/bamboo.dtb
%_datadir/%name/canyonlands.dtb
%_datadir/%name/openbios-ppc
%_datadir/%name/qemu_vga.ndrv
%_datadir/%name/slof.bin
%_datadir/%name/u-boot.e500
%_datadir/%name/u-boot-sam460-20100605.bin
%dir %_docdir/qemu-ppc
%_docdir/qemu-ppc/supported.txt

%files s390x
%defattr(-, root, root)
%_bindir/qemu-system-s390x
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%dir %_docdir/qemu-s390x
%_docdir/qemu-s390x/supported.txt

%files arm
%defattr(-, root, root)
%_bindir/qemu-system-arm
%_bindir/qemu-system-aarch64
%_datadir/%name/npcm7xx_bootrom.bin
%dir %_docdir/qemu-arm
%_docdir/qemu-arm/supported.txt

%files extra
%defattr(-, root, root)
%_bindir/qemu-system-alpha
%_bindir/qemu-system-avr
%_bindir/qemu-system-cris
%_bindir/qemu-system-hppa
%_bindir/qemu-system-m68k
%_bindir/qemu-system-microblaze
%_bindir/qemu-system-microblazeel
%_bindir/qemu-system-mips
%_bindir/qemu-system-mipsel
%_bindir/qemu-system-mips64
%_bindir/qemu-system-mips64el
%_bindir/qemu-system-moxie
%_bindir/qemu-system-nios2
%_bindir/qemu-system-or1k
%_bindir/qemu-system-riscv32
%_bindir/qemu-system-riscv64
%_bindir/qemu-system-rx
%_bindir/qemu-system-sh4
%_bindir/qemu-system-sh4eb
%_bindir/qemu-system-sparc
%_bindir/qemu-system-sparc64
%_bindir/qemu-system-tricore
%_bindir/qemu-system-xtensa
%_bindir/qemu-system-xtensaeb
%_datadir/%name/hppa-firmware.img
%_datadir/%name/openbios-sparc32
%_datadir/%name/openbios-sparc64
%_datadir/%name/opensbi-riscv32-generic-fw_dynamic.bin
%_datadir/%name/opensbi-riscv32-generic-fw_dynamic.elf
%_datadir/%name/opensbi-riscv64-generic-fw_dynamic.bin
%_datadir/%name/opensbi-riscv64-generic-fw_dynamic.elf
%_datadir/%name/palcode-clipper
%_datadir/%name/petalogix-ml605.dtb
%_datadir/%name/petalogix-s3adsp1800.dtb
%_datadir/%name/QEMU,cgthree.bin
%_datadir/%name/QEMU,tcx.bin

%if %{legacy_qemu_kvm}
%files kvm
%defattr(-,root,root)
%_bindir/qemu-kvm
%dir %_docdir/qemu-kvm
%_docdir/qemu-kvm/kvm-supported.html
%_docdir/qemu-kvm/kvm-supported.txt
%_mandir/man1/qemu-kvm.1.gz
%endif

%files audio-alsa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-alsa.so

%files audio-pa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-pa.so

%files audio-spice
%defattr(-, root, root)
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/05
%dir %_libdir/%name
%_libdir/%name/audio-spice.so

%files block-curl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-curl.so

%files block-dmg
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-dmg-bz2.so
%_libdir/%name/block-dmg-lzfse.so

%files block-gluster
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-gluster.so

%files block-iscsi
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-iscsi.so

%files block-nfs
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-nfs.so

%if 0%{?with_rbd}
%files block-rbd
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-rbd.so
%endif

%files block-ssh
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-ssh.so

%files chardev-baum
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/00
%dir %_libdir/%name
%_libdir/%name/chardev-baum.so

%files chardev-spice
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/08
%dir %_libdir/%name
%_libdir/%name/chardev-spice.so

%files hw-display-qxl
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/01
%dir %_libdir/%name
%_libdir/%name/hw-display-qxl.so

%files hw-display-virtio-gpu
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/04
%_libdir/%name/hw-display-virtio-gpu.so

%files hw-display-virtio-gpu-pci
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/11
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-gpu-pci.so

%files hw-display-virtio-vga
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/12
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-vga.so

%files hw-s390x-virtio-gpu-ccw
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/13
%dir %_libdir/%name
%_libdir/%name/hw-s390x-virtio-gpu-ccw.so

%files hw-usb-redirect
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/02
%dir %_libdir/%name
%_libdir/%name/hw-usb-redirect.so

%files hw-usb-smartcard
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/03
%dir %_libdir/%name
%_libdir/%name/hw-usb-smartcard.so

%files ui-curses
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-curses.so

%files ui-gtk
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-gtk.so

%files ui-opengl
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/10
%dir %_libdir/%name
%_libdir/%name/ui-egl-headless.so
%_libdir/%name/ui-opengl.so

%files ui-spice-core
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/09
%dir %_libdir/%name
%_libdir/%name/ui-spice-core.so

%files ui-spice-app
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-spice-app.so

%files lang -f %blddir/%name.lang
%defattr(-, root, root)

%ifarch %{build_rom_arch}
%files seabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin
%_datadir/%name/firmware/50-seabios-256k.json
%_datadir/%name/firmware/60-seabios-128k.json

%files microvm
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios-microvm.bin
%_datadir/%name/qboot.rom

%files vgabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/vgabios.bin
%_datadir/%name/vgabios-ati.bin
%_datadir/%name/vgabios-bochs-display.bin
%_datadir/%name/vgabios-cirrus.bin
%_datadir/%name/vgabios-qxl.bin
%_datadir/%name/vgabios-ramfb.bin
%_datadir/%name/vgabios-stdvga.bin
%_datadir/%name/vgabios-virtio.bin
%_datadir/%name/vgabios-vmware.bin

%files sgabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/sgabios.bin

%files ipxe
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/efi-e1000.rom
%_datadir/%name/efi-e1000e.rom
%_datadir/%name/efi-eepro100.rom
%_datadir/%name/efi-ne2k_pci.rom
%_datadir/%name/efi-pcnet.rom
%_datadir/%name/efi-rtl8139.rom
%_datadir/%name/efi-virtio.rom
%_datadir/%name/efi-vmxnet3.rom
%_datadir/%name/pxe-e1000.rom
%_datadir/%name/pxe-eepro100.rom
%_datadir/%name/pxe-ne2k_pci.rom
%_datadir/%name/pxe-pcnet.rom
%_datadir/%name/pxe-rtl8139.rom
%_datadir/%name/pxe-virtio.rom
%endif

%files skiboot
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/06
%_datadir/%name/skiboot.lid
%_datadir/%name/skiboot.lid.qemu
%ghost %_sysconfdir/alternatives/skiboot.lid

%files vhost-user-gpu
%defattr(-, root, root)
%dir %_datadir/%name/vhost-user
%_datadir/%name/vhost-user/50-qemu-gpu.json
%_libexecdir/vhost-user-gpu

%files tools
%defattr(-, root, root)
%_bindir/analyze-migration.py
%_bindir/qemu-edid
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-keymap
%_bindir/qemu-nbd
%_bindir/qemu-pr-helper
%_bindir/qemu-storage-daemon
%_bindir/vmstate-static-checker.py
%verify(not mode) %attr(4750,root,kvm) %_libexecdir/qemu-bridge-helper
%_libexecdir/virtfs-proxy-helper
%_libexecdir/virtiofsd
%_mandir/man1/qemu-img.1.gz
%_mandir/man1/virtfs-proxy-helper.1.gz
%_mandir/man8/qemu-nbd.8.gz
%_mandir/man8/qemu-pr-helper.8.gz
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/bridge.conf

%files ivshmem-tools
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_datadir/%name/forsplits
%_datadir/%name/forsplits/07
%_bindir/ivshmem-client
%_bindir/ivshmem-server

%files guest-agent
%defattr(-, root, root)
%attr(0755,root,kvm) %_bindir/qemu-ga
%dir %_docdir/%name/interop
%_docdir/%name/interop/qemu-ga.html
%_mandir/man8/qemu-ga.8.gz
%{_unitdir}/qemu-ga@.service
/usr/lib/udev/rules.d/80-qemu-ga.rules

%files ksm
%defattr(-, root, root)
%{_unitdir}/ksm.service

# above section is for qemu
%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

%_bindir/qemu-aarch64
%_bindir/qemu-aarch64_be
%_bindir/qemu-alpha
%_bindir/qemu-arm
%_bindir/qemu-armeb
%_bindir/qemu-cris
%_bindir/qemu-hexagon
%_bindir/qemu-hppa
%_bindir/qemu-i386
%_bindir/qemu-m68k
%_bindir/qemu-microblaze
%_bindir/qemu-microblazeel
%_bindir/qemu-mips
%_bindir/qemu-mips64
%_bindir/qemu-mips64el
%_bindir/qemu-mipsel
%_bindir/qemu-mipsn32
%_bindir/qemu-mipsn32el
%_bindir/qemu-nios2
%_bindir/qemu-or1k
%_bindir/qemu-ppc
%_bindir/qemu-ppc64
%_bindir/qemu-ppc64le
%_bindir/qemu-riscv32
%_bindir/qemu-riscv64
%_bindir/qemu-s390x
%_bindir/qemu-sh4
%_bindir/qemu-sh4eb
%_bindir/qemu-sparc
%_bindir/qemu-sparc32plus
%_bindir/qemu-sparc64
%_bindir/qemu-x86_64
%_bindir/qemu-xtensa
%_bindir/qemu-xtensaeb
%_bindir/qemu-binfmt
%_bindir/qemu-*-binfmt
%_sbindir/qemu-binfmt-conf.sh

%endif
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-testsuite"

%_datadir/qemu/check-report.tap

%endif

%changelog
