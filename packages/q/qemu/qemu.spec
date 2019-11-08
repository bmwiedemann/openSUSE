#
# spec file for package qemu
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


# !! IMPORTANT !! See README.PACKAGING before modifying package in any way

%define _buildshell /bin/bash

%define build_in_tree 1
%define build_x86_firmware_from_source 0
%define build_skiboot_from_source 0
%define build_slof_from_source 0
%define build_opensbi_from_source 0
%define kvm_available 0
%define legacy_qemu_kvm 0
%define force_fit_virtio_pxe_rom 1
%define provide_edk2_firmware 0

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

%if 0%{?is_opensuse}
%define with_glusterfs 1
%endif

%ifarch x86_64 aarch64 ppc64le s390x
%define with_rbd 1
%endif

# qemu, qemu-linux-user, and qemu-testsuite "flavors" enabled via OBS Multibuild
%define flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%flavor
%endif

%if "%flavor" == "linux-user"
%define summary_string CPU emulator for user space
%else
%define summary_string Machine emulator and virtualizer
%endif

%define srcname qemu
Name:           qemu%{name_suffix}
Url:            https://www.qemu.org/
Summary:        %{summary_string}
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
%define qemuver 4.1.0
%define srcver  4.1.0
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
Source200:      qemu-rpmlintrc
Source300:      bundles.tar.xz
Source301:      update_git.sh
Source302:      config.sh
Source303:      README.PACKAGING
# Upstream First -- https://wiki.qemu.org/Contribute/SubmitAPatch
# This patch queue is auto-generated - see README.PACKAGING for process

# Patches applied in base project:
Patch00000:     mirror-Keep-mirror_top_bs-drained-after-.patch
Patch00001:     s390x-tcg-Fix-VERIM-with-32-64-bit-eleme.patch
Patch00002:     target-alpha-fix-tlb_fill-trap_arg2-valu.patch
Patch00003:     target-arm-Free-TCG-temps-in-trans_VMOV_.patch
Patch00004:     target-arm-Don-t-abort-on-M-profile-exce.patch
Patch00005:     qcow2-Fix-the-calculation-of-the-maximum.patch
Patch00006:     block-file-posix-Reduce-xfsctl-use.patch
Patch00007:     pr-manager-Fix-invalid-g_free-crash-bug.patch
Patch00008:     vpc-Return-0-from-vpc_co_create-on-succe.patch
Patch00009:     block-nfs-tear-down-aio-before-nfs_close.patch
Patch00010:     block-create-Do-not-abort-if-a-block-dri.patch
Patch00011:     curl-Keep-pointer-to-the-CURLState-in-CU.patch
Patch00012:     curl-Keep-socket-until-the-end-of-curl_s.patch
Patch00013:     curl-Check-completion-in-curl_multi_do.patch
Patch00014:     curl-Pass-CURLSocket-to-curl_multi_do.patch
Patch00015:     curl-Report-only-ready-sockets.patch
Patch00016:     curl-Handle-success-in-multi_check_compl.patch
Patch00017:     blockjob-update-nodes-head-while-removin.patch
Patch00018:     memory-Provide-an-equality-function-for-.patch
Patch00019:     vhost-Fix-memory-region-section-comparis.patch
Patch00020:     hw-arm-boot.c-Set-NSACR.-CP11-CP10-for-N.patch
Patch00021:     s390-PCI-fix-IOMMU-region-init.patch
Patch00022:     hw-core-loader-Fix-possible-crash-in-rom.patch
Patch00023:     make-release-pull-in-edk2-submodules-so-.patch
Patch00024:     roms-Makefile.edk2-don-t-pull-in-submodu.patch
Patch00025:     coroutine-Add-qemu_co_mutex_assert_locke.patch
Patch00026:     qcow2-Fix-corruption-bug-in-qcow2_detect.patch
Patch00027:     block-io-refactor-padding.patch
Patch00028:     util-iov-introduce-qemu_iovec_init_exten.patch
Patch00029:     block-Make-wait-mark-serialising-request.patch
Patch00030:     block-Add-bdrv_co_get_self_request.patch
Patch00031:     block-file-posix-Let-post-EOF-fallocate-.patch
Patch00032:     qcow2-bitmap-Fix-uint64_t-left-shift-ove.patch
Patch00033:     qcow2-Fix-QCOW2_COMPRESSED_SECTOR_MASK.patch
Patch00034:     XXX-dont-dump-core-on-sigabort.patch
Patch00035:     qemu-binfmt-conf-Modify-default-path.patch
Patch00036:     qemu-cvs-gettimeofday.patch
Patch00037:     qemu-cvs-ioctl_debug.patch
Patch00038:     qemu-cvs-ioctl_nodirection.patch
Patch00039:     linux-user-add-binfmt-wrapper-for-argv-0.patch
Patch00040:     PPC-KVM-Disable-mmu-notifier-check.patch
Patch00041:     linux-user-binfmt-support-host-binaries.patch
Patch00042:     linux-user-Fake-proc-cpuinfo.patch
Patch00043:     linux-user-use-target_ulong.patch
Patch00044:     Make-char-muxer-more-robust-wrt-small-FI.patch
Patch00045:     linux-user-lseek-explicitly-cast-non-set.patch
Patch00046:     AIO-Reduce-number-of-threads-for-32bit-h.patch
Patch00047:     xen_disk-Add-suse-specific-flush-disable.patch
Patch00048:     qemu-bridge-helper-reduce-security-profi.patch
Patch00049:     qemu-binfmt-conf-use-qemu-ARCH-binfmt.patch
Patch00050:     linux-user-properly-test-for-infinite-ti.patch
Patch00051:     roms-Makefile-pass-a-packaging-timestamp.patch
Patch00052:     Raise-soft-address-space-limit-to-hard-l.patch
Patch00053:     increase-x86_64-physical-bits-to-42.patch
Patch00054:     vga-Raise-VRAM-to-16-MiB-for-pc-0.15-and.patch
Patch00055:     i8254-Fix-migration-from-SLE11-SP2.patch
Patch00056:     acpi_piix4-Fix-migration-from-SLE11-SP2.patch
Patch00057:     Switch-order-of-libraries-for-mpath-supp.patch
Patch00058:     Make-installed-scripts-explicitly-python.patch
Patch00059:     hw-smbios-handle-both-file-formats-regar.patch
Patch00060:     xen-add-block-resize-support-for-xen-dis.patch
Patch00061:     tests-qemu-iotests-Triple-timeout-of-i-o.patch
Patch00062:     tests-Fix-block-tests-to-be-compatible-w.patch
Patch00063:     xen-ignore-live-parameter-from-xen-save-.patch
Patch00064:     Conditionalize-ui-bitmap-installation-be.patch
Patch00065:     tests-change-error-message-in-test-162.patch
Patch00066:     hw-usb-hcd-xhci-Fix-GCC-9-build-warning.patch
Patch00067:     hw-usb-dev-mtp-Fix-GCC-9-build-warning.patch
Patch00068:     hw-intc-exynos4210_gic-provide-more-room.patch
Patch00069:     configure-only-populate-roms-if-softmmu.patch
Patch00070:     pc-bios-s390-ccw-net-avoid-warning-about.patch
Patch00071:     roms-change-cross-compiler-naming-to-be-.patch
Patch00072:     tests-Disable-some-block-tests-for-now.patch
Patch00073:     test-add-mapping-from-arch-of-i686-to-qe.patch
# Patches applied in roms/seabios/:
Patch01000:     seabios-use-python2-explicitly-as-needed.patch
Patch01001:     seabios-switch-to-python3-as-needed.patch
Patch01002:     enable-cross-compilation-on-ARM.patch
Patch01003:     vga-move-modelist-from-bochsvga.c-to-new.patch
Patch01004:     vga-make-memcpy_high-public.patch
Patch01005:     vga-add-atiext-driver.patch
Patch01006:     vga-add-ati-bios-tables.patch
Patch01007:     vbe-add-edid-support.patch
Patch01008:     ati-add-edid-support.patch
Patch01009:     ati-vga-make-less-verbose.patch
Patch01010:     ati-vga-fix-ati_read.patch
Patch01011:     ati-vga-make-i2c-register-and-bits-confi.patch
Patch01012:     ati-vga-try-vga-ddc-first.patch
Patch01013:     ati-vga-add-rage128-edid-support.patch
# Patches applied in roms/ipxe/:
Patch02000:     stub-out-the-SAN-req-s-in-int13.patch
Patch02001:     ipxe-Makefile-fix-issues-of-build-reprod.patch
Patch02002:     Fix-s-directive-argument-is-null-error.patch
Patch02003:     Workaround-compilation-error-with-gcc-9..patch
Patch02004:     Do-not-apply-WORKAROUND_CFLAGS-for-host-.patch
# Patches applied in roms/sgabios/:
Patch03000:     sgabios-Makefile-fix-issues-of-build-rep.patch
Patch03001:     roms-sgabios-Fix-csum8-to-be-built-by-ho.patch
# Patches applied in roms/skiboot/:
Patch05000:     Disable-Waddress-of-packed-member-for-GC.patch
Patch05001:     hdata-vpd-fix-printing-char-0x00.patch
# Patches applied in ui/keycodemapdb/:
Patch08000:     Make-keycode-gen-output-reproducible-use.patch

# Please do not add patches manually here.

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# ========================================================================
%if "%{name}" == "qemu-linux-user"
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  makeinfo
BuildRequires:  pcre-devel-static
BuildRequires:  python3-base
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

# ------------------------------------------------------------------------
%else # ! qemu-linux-user
%if %{build_x86_firmware_from_source}
BuildRequires:  acpica
%endif
BuildRequires:  alsa-devel
%if %{build_x86_firmware_from_source}
BuildRequires:  binutils-devel
%endif
BuildRequires:  bison
BuildRequires:  bluez-devel
BuildRequires:  brlapi-devel
%ifnarch %{ix86} aarch64
BuildRequires:  cross-aarch64-binutils
BuildRequires:  cross-aarch64-gcc%gcc_version
%endif
%ifnarch %{ix86} armv7hl
BuildRequires:  cross-arm-binutils
BuildRequires:  cross-arm-gcc%gcc_version
%endif
%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
# We must cross-compile on non-x86*
BuildRequires:  cross-i386-binutils
BuildRequires:  cross-i386-gcc%gcc_version
BuildRequires:  cross-x86_64-binutils
BuildRequires:  cross-x86_64-gcc%gcc_version
%endif
%endif
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
%if build_x86_firmware_from_source
BuildRequires:  dos2unix
%endif
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
%if 0%{?with_glusterfs}
BuildRequires:  glusterfs-devel
%endif
BuildRequires:  gtk3-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbz2-devel
%if 0%{?is_opensuse}
BuildRequires:  libcacard-devel
%endif
BuildRequires:  libcap-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libfdt-devel
BuildRequires:  libgbm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libiscsi-devel
BuildRequires:  libjpeg-devel
%if 0%{?is_opensuse}
BuildRequires:  libnfs-devel
%endif
%ifnarch %arm s390x
BuildRequires:  libnuma-devel
%endif
BuildRequires:  libpcap-devel
BuildRequires:  libpixman-1-0-devel
%ifarch x86_64
BuildRequires:  libpmem-devel
%endif
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
%if 0%{?with_rbd}
BuildRequires:  librbd-devel
%endif
%if 0%{?is_opensuse}
BuildRequires:  libSDL2-devel
BuildRequires:  libSDL2_image-devel
%endif
BuildRequires:  libseccomp-devel
BuildRequires:  libspice-server-devel
BuildRequires:  libssh-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libvdeplug-devel
%if 0%{?is_opensuse}
BuildRequires:  lzfse-devel
%endif
BuildRequires:  Mesa-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lzo-devel
BuildRequires:  makeinfo
BuildRequires:  multipath-tools-devel
%if build_x86_firmware_from_source
BuildRequires:  nasm
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  python-base
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base
BuildRequires:  rdma-core-devel
BuildRequires:  snappy-devel
BuildRequires:  spice-protocol-devel
BuildRequires:  systemd
%{?systemd_requires}
%if %{kvm_available}
BuildRequires:  pkgconfig(udev)
%endif
BuildRequires:  usbredir-devel
BuildRequires:  virglrenderer-devel >= 0.4.1
BuildRequires:  vte-devel
%ifarch x86_64
BuildRequires:  xen-devel
%endif
BuildRequires:  xfsprogs-devel
%if %{build_x86_firmware_from_source}
BuildRequires:  xz-devel
%endif
BuildRequires:  zlib-devel
%if "%{name}" == "qemu-testsuite"
BuildRequires:  bc
BuildRequires:  python-base
BuildRequires:  qemu-arm = %{qemuver}
BuildRequires:  qemu-audio-alsa = %{qemuver}
BuildRequires:  qemu-audio-pa = %{qemuver}
%if 0%{?is_opensuse}
BuildRequires:  qemu-audio-sdl = %{qemuver}
%endif
BuildRequires:  qemu-block-curl = %{qemuver}
BuildRequires:  qemu-block-dmg = %{qemuver}
%if 0%{?with_glusterfs}
BuildRequires:  qemu-block-gluster = %{qemuver}
%endif
BuildRequires:  qemu-block-iscsi = %{qemuver}
%if 0%{?is_opensuse}
BuildRequires:  qemu-block-nfs = %{qemuver}
%endif
%if 0%{?with_rbd}
BuildRequires:  qemu-block-rbd = %{qemuver}
%endif
BuildRequires:  qemu-block-ssh = %{qemuver}
%if %{provide_edk2_firmware}
BuildRequires:  qemu-edk2 = %{qemuver}
%endif
BuildRequires:  qemu-extra = %{qemuver}
BuildRequires:  qemu-guest-agent = %{qemuver}
BuildRequires:  qemu-ipxe = 1.0.0+
%if 0%{?is_opensuse}
BuildRequires:  qemu-ksm = %{qemuver}
%endif
BuildRequires:  qemu-lang = %{qemuver}
BuildRequires:  qemu-ppc   = %{qemuver}
BuildRequires:  qemu-s390  = %{qemuver}
BuildRequires:  qemu-seabios = 1.12.1
BuildRequires:  qemu-sgabios = 8
BuildRequires:  qemu-tools = %{qemuver}
BuildRequires:  qemu-ui-curses = %{qemuver}
BuildRequires:  qemu-ui-gtk = %{qemuver}
%if 0%{?is_opensuse}
BuildRequires:  qemu-ui-sdl = %{qemuver}
%endif
BuildRequires:  qemu-vgabios = 1.12.1
BuildRequires:  qemu-x86    = %{qemuver}
%endif
Requires(pre):  shadow
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
Recommends:     qemu-tools
Recommends:     qemu-ui-curses
Recommends:     qemu-ui-gtk
%if 0%{?is_opensuse}
Recommends:     qemu-ui-sdl
%endif
Recommends:     qemu-x86
%ifarch ppc ppc64 ppc64le
Recommends:     qemu-ppc
%else
Suggests:       qemu-ppc
%endif
%ifarch s390x
Recommends:     qemu-s390
%else
Suggests:       qemu-s390
%endif
%ifarch %arm aarch64
Recommends:     qemu-arm
%else
Suggests:       qemu-arm
%endif
Suggests:       qemu-block-dmg
%if 0%{?with_glusterfs}
Suggests:       qemu-block-gluster
%endif
Suggests:       qemu-block-iscsi
%if 0%{?is_opensuse}
Suggests:       qemu-block-nfs
%endif
%if 0%{?with_rbd}
Suggests:       qemu-block-rbd
%endif
Suggests:       qemu-block-ssh
Suggests:       qemu-extra
Suggests:       qemu-lang
%if 0%{?is_opensuse}
Recommends:     qemu-ksm = %{qemuver}
%endif
Suggests:       qemu-vhost-user-gpu
Provides:       qemu-audio-oss = %{qemuver}
Obsoletes:      qemu-audio-oss < %{qemuver}

# ------------------------------------------------------------------------
%define generic_qemu_description QEMU provides full machine emulation and cross architecture usage. It closely\
integrates with KVM and Xen virtualization, allowing for excellent performance.\
Many options are available for defining the emulated environment, including\
traditional devices, direct host device access, and interfaces specific to\
virtualization.

%description
%{generic_qemu_description}

This package acts as an umbrella package to the other QEMU sub-packages.

%if "%{name}" != "qemu-testsuite"

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

%package s390
Summary:        Machine emulator and virtualizer for S/390 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}

%description s390
%{generic_qemu_description}

This package provides s390x emulation.

%package arm
Summary:        Machine emulator and virtualizer for ARM architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios
Recommends:     ovmf
Recommends:     qemu-uefi-aarch64

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
Requires:       qemu-s390 = %{qemuver}
%endif
Provides:       kvm = %{qemuver}
Obsoletes:      kvm < %{qemuver}

%description kvm
%{generic_qemu_description}

This package simply provides a shell script wrapper for the QEMU program which
does the actual machine emulation and virtualization for this architecture. The
wrapper simply adds command-line parameters to ensure that the KVM accelerator
is invoked. It provides no additional benefit, and is considered deprecated.
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

%package block-curl
Summary:        cURL block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_libdir/%name/block-curl.so
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

%if 0%{?with_glusterfs}
%package block-gluster
Summary:        GlusterFS block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-gluster
This package contains a module for accessing network-based image files over a
GlusterFS network connection from qemu-img tool and QEMU system emulation.
%endif

%package block-iscsi
Summary:        iSCSI block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-iscsi
This package contains a module for accessing network-based image files over an
iSCSI network connection from qemu-img tool and QEMU system emulation.

%if 0%{?is_opensuse}
%package block-nfs
Summary:        direct Network File System support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-nfs
This package contains a module for directly accessing nfs based image files.
%endif

%if 0%{?with_rbd}
%package block-rbd
Summary:        Rados Block Device (Ceph) support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-rbd
This package contains a module for accessing ceph (rbd,rados) image files.
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
%{qemu_module_conflicts}

%description ui-gtk
This package contains a module for doing GTK based UI for QEMU.

%if 0%{?is_opensuse}
%package ui-sdl
Summary:        SDL based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-sdl
This package contains a module for doing SDL based UI for QEMU.
%endif

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

%if 0%{?is_opensuse}
%package audio-sdl
Summary:        SDL based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-sdl
This package contains a module for SDL based audio support for QEMU.
%endif

%package vhost-user-gpu
Summary:        Vhost user mode virtio-gpu 2D/3D rendering backend for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description vhost-user-gpu
This package contains a vhost user mode virtio-gpu 2D/3D rendering backend for QEMU

%package tools
Summary:        Tools for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_libexecdir/qemu-bridge-helper
Requires(pre):  permissions
Requires(pre):  shadow
Recommends:     multipath-tools
Recommends:     qemu-block-curl
%if 0%{?with_rbd}
Recommends:     qemu-block-rbd
%endif

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper, ivshmem, disk utilities and scripts for various purposes.

%package guest-agent
Summary:        Guest agent for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_bindir/qemu-ga
Requires(pre):  shadow
Requires(post): udev
Supplements:    modalias(acpi*:QEMU0002%3A*)
Supplements:    modalias(pci:v0000FFFDd00000101sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00005853d00000001sv*sd*bc*sc*i*)
%{?systemd_requires}

%description guest-agent
This package contains the QEMU guest agent. It is installed in the linux guest
to provide information and control at the guest OS level.

%ifarch %{build_rom_arch}
%package seabios
Summary:        x86 Legacy BIOS for QEMU
Group:          System/Emulators/PC
Version:        1.12.1
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description seabios
SeaBIOS is an open source implementation of a 16bit x86 BIOS. SeaBIOS
is the default and legacy BIOS for QEMU.

%package vgabios
Summary:        VGA BIOSes for QEMU
Group:          System/Emulators/PC
Version:        1.12.1
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description vgabios
VGABIOS provides the video ROM BIOSes for the following variants of VGA
emulated devices: Std VGA, QXL, Cirrus CLGD 5446 and VMware emulated
video card.

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
were attached.

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

%if %{provide_edk2_firmware}
%package edk2
Summary:        EDK II based firmware
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
BuildArch:      noarch

%description edk2
Provides EDK II based firmware.
%endif

%if 0%{?is_opensuse}
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
%endif

%endif # ! qemu-testsuite
%endif # ! qemu-linux-user

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
%patch00040 -p1
%patch00041 -p1
%patch00042 -p1
%patch00043 -p1
%patch00044 -p1
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
%patch00060 -p1
%patch00061 -p1
%patch00062 -p1
%patch00063 -p1
%patch00064 -p1
%patch00065 -p1
%patch00066 -p1
%patch00067 -p1
%patch00068 -p1
%patch00069 -p1
%patch00070 -p1
%patch00071 -p1
%patch00072 -p1
%patch00073 -p1
%patch01000 -p1
%patch01001 -p1
%patch01002 -p1
%patch01003 -p1
%patch01004 -p1
%patch01005 -p1
%patch01006 -p1
%patch01007 -p1
%patch01008 -p1
%patch01009 -p1
%patch01010 -p1
%patch01011 -p1
%patch01012 -p1
%patch01013 -p1
%if 0%{?patch-possibly-applied-elsewhere}
%patch02000 -p1
%endif
%patch02001 -p1
%patch02002 -p1
%patch02003 -p1
%ifarch aarch64
%patch02004 -p1
%endif
%patch03000 -p1
%patch03001 -p1
%patch05000 -p1
%patch05001 -p1
%patch08000 -p1

%if "%{name}" != "qemu-linux-user"
# for the record, this set of firmware files is installed, but we don't
# build (yet): bamboo.dtb canyonlands.dtb hppa-firmware.img openbios-ppc openbios-sparc32
# openbios-sparc64 palcode-clipper petalogix-ml605.dtb petalogix-s3adsp1800.dtb ppc_rom.bin
# QEMU,cgthree.bin QEMU,tcx.bin qemu_vga.ndrv u-boot.e500 u-boot-sam460-20100605.bin
# opensbi-riscv32-virt-fw_jump.bin

# This first list group isn't specific to what this instance builds
%define ppc_default_firmware {%nil}
%define ppc_extra_firmware {skiboot.lid slof.bin}
%define ppc64_only_default_firmware {spapr-rtas.bin}
%define ppc64_only_extra_firmware {%nil}
%define riscv64_default_firmware {opensbi-riscv64-sifive_u-fw_jump.bin opensbi-riscv64-virt-fw_jump.bin}
%define riscv64_extra_firmware {%nil}
%define s390x_default_firmware {s390-ccw.img s390-netboot.img}
%define s390x_extra_firmware {%nil}
%define x86_default_firmware {linuxboot.bin linuxboot_dma.bin multiboot.bin \
kvmvapic.bin pvh.bin}
%define x86_extra_firmware {bios.bin bios-256k.bin pxe-e1000.rom \
pxe-eepro100.rom pxe-ne2k_pci.rom pxe-pcnet.rom pxe-rtl8139.rom pxe-virtio.rom \
sgabios.bin vgabios-ati.bin vgabios-bochs-display.bin vgabios.bin \
vgabios-cirrus.bin vgabios-qxl.bin vgabios-ramfb.bin vgabios-stdvga.bin \
vgabios-virtio.bin vgabios-vmware.bin}
%define x86_64_only_default_firmware {%nil}
%define x86_64_only_extra_firmware {edk2-aarch64-code.fd.bz2 \
edk2-arm-code.fd.bz2 edk2-arm-vars.fd.bz2 edk2-i386-code.fd.bz2 \
edk2-i386-secure-code.fd.bz2 edk2-i386-vars.fd.bz2 edk2-x86_64-code.fd.bz2 \
edk2-x86_64-secure-code.fd.bz2 efi-e1000.rom efi-e1000e.rom efi-eepro100.rom \
efi-ne2k_pci.rom efi-pcnet.rom efi-rtl8139.rom efi-virtio.rom efi-vmxnet3.rom}

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

%if "%{name}" != "qemu-testsuite"

# delete the firmware files that we intend to build
for i in %built_firmware
do
  unlink pc-bios/$i
done

# ------------------------------------------------------------------------
%else # qemu-testsuite

# delete the firmware files that we intend to link from built packages
for i in %firmware
do
  if [[ $i =~ .*[.]bz2 ]]; then
    echo "Skipping %i"
  else
    unlink pc-bios/$i
  fi
done

%endif # qemu-testsuite
%endif # ! qemu-linux-user

# ========================================================================
%build
%define _lto_cflags %{nil}

%if %build_in_tree
%define mybuilddir %{_builddir}/%buildsubdir
%else
%define mybuilddir %{_builddir}/mybuilddir
mkdir -p %mybuilddir
cd %mybuilddir
%endif

%{_builddir}/%buildsubdir/configure \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--docdir=%_docdir/%name \
	--firmwarepath=%_datadir/%name \
        --python=%_bindir/python3 \
	--extra-cflags="%{optflags}" \
	--disable-stack-protector \
	--disable-strip \
%if "%{name}" != "qemu-linux-user"
	--with-pkgversion="%(echo '%{distro}' | sed 's/ (.*)//')" \
	--with-default-devices \
	--enable-system --disable-linux-user \
	--enable-tools --enable-guest-agent \
	--enable-modules \
	--enable-pie \
	--enable-docs \
%if 0%{?is_opensuse}
	--audio-drv-list="pa alsa sdl" \
%else
	--audio-drv-list="pa alsa" \
%endif
	--enable-attr \
	--disable-auth-pam \
	--enable-bluez \
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
	--enable-gcrypt \
%if 0%{?with_glusterfs}
	--enable-glusterfs \
%else
	--disable-glusterfs \
%endif
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
	--enable-libiscsi \
%if 0%{?is_opensuse}
	--enable-libnfs \
%else
	--disable-libnfs \
%endif
%ifarch x86_64
	--enable-libpmem \
%else
	--disable-libpmem \
%endif
	--enable-libssh \
	--enable-libusb \
	--disable-libxml2 \
	--enable-linux-aio \
%if 0%{?is_opensuse}
	--enable-lzfse \
%else
	--disable-lzfse \
%endif
	--enable-lzo \
	--disable-malloc-trim \
	--enable-membarrier \
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
	--disable-sanitizers \
%if 0%{?is_opensuse}
	--enable-sdl \
	--enable-sdl-image \
%else
	--disable-sdl \
	--disable-sdl-image \
%endif
	--enable-seccomp \
	--enable-sheepdog \
%if 0%{?is_opensuse}
	--enable-smartcard \
%else
	--disable-smartcard \
%endif
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
# ------------------------------------------------------------------------
%else # qemu-linux-user
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
	--disable-iconv \
	--disable-kvm \
	--disable-malloc-trim \
	--enable-membarrier \
	--disable-parallels \
	--disable-qcow1 \
	--disable-qed \
	--disable-replication \
	--disable-sheepdog \
	--disable-slirp \
	--disable-tpm \
	--disable-vdi \
	--disable-vhost-crypto \
	--disable-vhost-kernel \
	--disable-vhost-net \
	--disable-vhost-scsi \
	--disable-vhost-user \
	--disable-vhost-vsock \
	--disable-vnc \
	--disable-vvfat \
%endif # qemu-linux-user

%if "%{name}" == "qemu"

make %{?_smp_mflags} V=1

# Firmware

%ifarch s390x
for i in %s390x_default_built_firmware
do
  cp pc-bios/s390-ccw/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif

%ifarch ppc64
for i in %ppc64_only_default_built_firmware
do
  cp pc-bios/spapr-rtas/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif

%ifarch %ix86 x86_64
for i in %x86_default_built_firmware
do
  cp pc-bios/optionrom/$i %{_builddir}/%buildsubdir/pc-bios/
done
%ifarch x86_64
for i in %x86_64_only_default_built_firmware
do
  cp pc-bios/optionrom/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif
%endif

%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
export CC=x86_64-suse-linux-gcc
export LD=x86_64-suse-linux-ld
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms bios \
%if 0%{?is_opensuse} == 0
  SEABIOS_EXTRAVERSION="-rebuilt.suse.com" \
%else
  SEABIOS_EXTRAVERSION="-rebuilt.opensuse.org" \
%endif
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

%ifnarch %ix86
%if %{provide_edk2_firmware}
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms efi \
  EDK2_BASETOOLS_OPTFLAGS='-fPIE'
%endif
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms seavgabios \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms seavgabios-ati \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms pxerom

%ifnarch %ix86
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms efirom \
  EDK2_BASETOOLS_OPTFLAGS='-fPIE'
%endif

make                 -C %{_builddir}/%buildsubdir/roms sgabios \
  HOSTCC=cc

%if %{force_fit_virtio_pxe_rom}
patch -p1 < %_sourcedir/stub-out-the-SAN-req-s-in-int13.patch
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms pxerom_variants=virtio pxerom_targets=1af41000 pxerom
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
    if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -gt "131072" ; then
    echo "pxe rom is too large"
    exit 1
  fi
  if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -le "65536" ; then
    ./%{_builddir}/%buildsubdir/roms/ipxe/src/util/padimg.pl %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom -s 65536 -b 255
    echo -ne "SEGMENT OVERAGE\0" >> %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom
  fi
done
for i in %supported_nics_small
  do
    if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -gt "65536" ; then
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
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms skiboot CROSS=
%endif

%if %{build_slof_from_source}
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms slof
%endif

%if %{build_opensbi_from_source}
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms opensbi64-virt CROSS_COMPILE=
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms opensbi64-sifive_u CROSS_COMPILE=
%endif

%endif # qemu
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
ln -s %_bindir/qemu-pr-helper scsi/qemu-pr-helper
ln -s %_bindir/virtfs-proxy-helper fsdev/virtfs-proxy-helper

for i in %firmware
do
  if [[ $i =~ .*[.]bz2 ]]; then
    echo "Skipping $i"
  else
    ln -s %_datadir/qemu/$i pc-bios/$i
  fi
done

for conf in %{_builddir}/%buildsubdir/default-configs/*-softmmu.mak; do
  arch=`echo "$conf" | sed -e 's|%{_builddir}/%buildsubdir/default-configs/\(.*\)-softmmu.mak|\1|g'`
  ln -s %_bindir/qemu-system-$arch $arch-softmmu/qemu-system-$arch
done

# Compile the QOM test binary first, so that ...
touch -r config-host.mak pc-bios
make %{?_smp_mflags} tests/qom-test %{?_smp_mflags} V=1
# ... make comes in fresh and has lots of address space (needed for 32bit, bsc#957379)
make %{?_smp_mflags} check-report.tap V=1

%endif # qemu-testsuite
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

%endif # qemu-linux-user

# ========================================================================
%check
cd %mybuilddir
%if "%{name}" == "qemu-testsuite"

export QEMU_PROG=%_bindir/qemu-system-x86_64
export QEMU_IMG_PROG=%_bindir/qemu-img
export QEMU_IO_PROG=%_bindir/qemu-io
export QEMU_NBD_PROG=%_bindir/qemu-nbd
make %{?_smp_mflags} check-block V=1

%endif # qemu-testsuite
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

%ifarch %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le s390x
%{qemu_arch}-linux-user/qemu-%{qemu_arch} %_bindir/ls > /dev/null
make %{?_smp_mflags} check-softfloat
%endif

%endif # qemu-linux-user

# ========================================================================

%install
cd %mybuilddir

%if "%{name}" == "qemu-testsuite"

install -D -m 0644 check-report.tap %{buildroot}%_datadir/qemu/check-report.tap

%endif # qemu-testsuite
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

make %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}%_datadir/qemu/keymaps
unlink %{buildroot}%_datadir/qemu/trace-events-all
install -d -m 755 %{buildroot}%_sbindir
install -m 755 scripts/qemu-binfmt-conf.sh %{buildroot}%_sbindir
%fdupes -s %{buildroot}

%endif # qemu-linux-user
# ------------------------------------------------------------------------
%if "%{name}" == "qemu"

make %{?_smp_mflags} install DESTDIR=%{buildroot}
%ifnarch %{build_rom_arch}
for f in %{x86_extra_firmware} \
         %{x86_64_only_extra_firmware}; do
  unlink %{buildroot}%_datadir/%name/${f%.bz2}
done
%define do_more_edk2_unlinks 1
%else
%ifarch %ix86 aarch64
unlink %{buildroot}%_datadir/%name/edk2-aarch64-code.fd
unlink %{buildroot}%_datadir/%name/edk2-arm-code.fd
unlink %{buildroot}%_datadir/%name/edk2-arm-vars.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-code.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-secure-code.fd
unlink %{buildroot}%_datadir/%name/edk2-i386-vars.fd
unlink %{buildroot}%_datadir/%name/edk2-licenses.txt || true
unlink %{buildroot}%_datadir/%name/edk2-x86_64-code.fd
unlink %{buildroot}%_datadir/%name/edk2-x86_64-secure-code.fd
%endif
%endif
%if 0%{?do_more_edk2_unlinks} || %{provide_edk2_firmware} == 0
unlink %{buildroot}%_datadir/%name/edk2-licenses.txt || true
unlink %{buildroot}%_datadir/%name/firmware/50-edk2-i386-secure.json
unlink %{buildroot}%_datadir/%name/firmware/50-edk2-x86_64-secure.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-aarch64.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-arm.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-i386.json
unlink %{buildroot}%_datadir/%name/firmware/60-edk2-x86_64.json
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
%if 0%{?is_opensuse} == 0
install -D -m 0644 %{SOURCE10} %{buildroot}%_docdir/qemu-arm/supported.txt
install -D -m 0644 %{SOURCE11} %{buildroot}%_docdir/qemu-ppc/supported.txt
install -D -m 0644 %{SOURCE12} %{buildroot}%_docdir/qemu-x86/supported.txt
install -D -m 0644 %{SOURCE13} %{buildroot}%_docdir/qemu-s390/supported.txt
%endif
%if %{legacy_qemu_kvm}
cat > %{buildroot}%_bindir/qemu-kvm << 'EOF'
#!/bin/sh

%ifarch s390x
exec %_bindir/qemu-system-s390x -machine accel=kvm "$@"
%else
exec %_bindir/qemu-system-x86_64 -machine accel=kvm "$@"
%endif
EOF
chmod 755 %{buildroot}%_bindir/qemu-kvm
install -D -m 0644 %{SOURCE5} %{buildroot}%_mandir/man1/qemu-kvm.1.gz
%if 0%{?is_opensuse} == 0
install -d %{buildroot}%_docdir/qemu-kvm
%ifarch s390x
ln -s ../qemu-s390/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
%else
ln -s ../qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
%endif
%endif
%endif
%if %{kvm_available}
install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d/80-kvm.rules
%endif
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/qemu-ga@.service
%if 0%{?is_opensuse}
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/ksm.service
%endif
%ifarch s390x
install -D -m 0644 %{SOURCE2} %{buildroot}%_libexecdir/modules-load.d/kvm.conf
%endif
%fdupes -s %{buildroot}

# ========================================================================
# (qemu alone has pre* and post* sections for itself and subpackages):

%pre
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
%_bindir/getent group qemu >/dev/null || %_sbindir/groupadd -r qemu
%_bindir/getent passwd qemu >/dev/null ||
  %_sbindir/useradd -r -g qemu -G kvm -d / -s /sbin/nologin \
  -c "qemu user" qemu

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

%pre tools
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
%post tools
%set_permissions %_libexecdir/qemu-bridge-helper

%verifyscript tools
%verify_permissions %_libexecdir/qemu-bridge-helper

%pre guest-agent
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
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
%service_del_postun qemu-ga@.service

%if 0%{?is_opensuse}
%pre ksm
%service_add_pre ksm.service

%post ksm
%service_add_post ksm.service

%preun ksm
%service_del_preun ksm.service

%postun ksm
%service_del_postun ksm.service
%endif

%endif # qemu

# ========================================================================
%files
%defattr(-, root, root)
%doc Changelog README VERSION
%license COPYING COPYING.LIB LICENSE

%if "%{name}" == "qemu"
%dir %_docdir/%name/interop
%dir %_docdir/%name/interop/_static
%dir %_docdir/%name/specs
%dir %_docdir/%name/specs/_static
%_docdir/%name/interop/.buildinfo
%_docdir/%name/interop/_static/*
%_docdir/%name/interop/bitmaps.html
%_docdir/%name/interop/genindex.html
%_docdir/%name/interop/index.html
%_docdir/%name/interop/live-block-operations.html
%_docdir/%name/interop/objects.inv
%_docdir/%name/interop/pr-helper.html
%_docdir/%name/interop/search.html
%_docdir/%name/interop/searchindex.js
%_docdir/%name/interop/vhost-user.html
%_docdir/%name/specs/.buildinfo
%_docdir/%name/specs/_static/*
%_docdir/%name/specs/genindex.html
%_docdir/%name/specs/index.html
%_docdir/%name/specs/objects.inv
%_docdir/%name/specs/ppc-spapr-xive.html
%_docdir/%name/specs/ppc-xive.html
%_docdir/%name/specs/search.html
%_docdir/%name/specs/searchindex.js
%_docdir/%name/qemu-doc.txt
%_docdir/%name/qemu-doc.html
%_docdir/%name/qemu-qmp-ref.txt
%_docdir/%name/qemu-qmp-ref.html
%_docdir/%name/qemu-ga-ref.txt
%_docdir/%name/qemu-ga-ref.html
%_mandir/man1/%name.1.gz
%_mandir/man7/qemu-block-drivers.7.gz
%_mandir/man7/qemu-cpu-models.7.gz
%_mandir/man7/qemu-qmp-ref.7.gz
%_mandir/man7/qemu-ga-ref.7.gz
%dir %_datadir/%name
%dir %_datadir/%name/firmware
%_datadir/%name/keymaps
%_datadir/%name/qemu-nsis.bmp
%_datadir/%name/trace-events-all
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/firmware
%_datadir/%name/qemu-ifup
%dir %_libexecdir/supportconfig
%dir %_libexecdir/supportconfig/plugins
%_libexecdir/supportconfig/plugins/%name
%if %{kvm_available}
/usr/lib/udev/rules.d/80-kvm.rules
%ifarch s390x
%_libexecdir/modules-load.d/kvm.conf
%endif
%endif
%dir %_datadir/icons/hicolor
%dir %_datadir/icons/hicolor/*/
%dir %_datadir/icons/hicolor/*/apps
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
%_datadir/applications/qemu.desktop

%files x86
%defattr(-, root, root)
%_bindir/qemu-system-i386
%_bindir/qemu-system-x86_64
%_datadir/%name/kvmvapic.bin
%_datadir/%name/linuxboot.bin
%_datadir/%name/linuxboot_dma.bin
%_datadir/%name/multiboot.bin
%_datadir/%name/pvh.bin
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-x86
%_docdir/qemu-x86/supported.txt
%endif

%files ppc
%defattr(-, root, root)
%_bindir/qemu-system-ppc
%_bindir/qemu-system-ppc64
%_datadir/%name/bamboo.dtb
%_datadir/%name/canyonlands.dtb
%_datadir/%name/openbios-ppc
%_datadir/%name/ppc_rom.bin
%_datadir/%name/qemu_vga.ndrv
%_datadir/%name/skiboot.lid
%_datadir/%name/slof.bin
%_datadir/%name/spapr-rtas.bin
%_datadir/%name/u-boot.e500
%_datadir/%name/u-boot-sam460-20100605.bin
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-ppc
%_docdir/qemu-ppc/supported.txt
%endif

%files s390
%defattr(-, root, root)
%_bindir/qemu-system-s390x
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-s390
%_docdir/qemu-s390/supported.txt
%endif

%files arm
%defattr(-, root, root)
%_bindir/qemu-system-arm
%_bindir/qemu-system-aarch64
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-arm
%_docdir/qemu-arm/supported.txt
%endif

%files extra
%defattr(-, root, root)
%_bindir/qemu-system-alpha
%_bindir/qemu-system-cris
%_bindir/qemu-system-hppa
%_bindir/qemu-system-lm32
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
%_bindir/qemu-system-sh4
%_bindir/qemu-system-sh4eb
%_bindir/qemu-system-sparc
%_bindir/qemu-system-sparc64
%_bindir/qemu-system-tricore
%_bindir/qemu-system-unicore32
%_bindir/qemu-system-xtensa
%_bindir/qemu-system-xtensaeb
%_datadir/%name/hppa-firmware.img
%_datadir/%name/opensbi-riscv32-virt-fw_jump.bin
%_datadir/%name/opensbi-riscv64-sifive_u-fw_jump.bin
%_datadir/%name/opensbi-riscv64-virt-fw_jump.bin
%_datadir/%name/openbios-sparc32
%_datadir/%name/openbios-sparc64
%_datadir/%name/palcode-clipper
%_datadir/%name/petalogix-ml605.dtb
%_datadir/%name/petalogix-s3adsp1800.dtb
%_datadir/%name/QEMU,cgthree.bin
%_datadir/%name/QEMU,tcx.bin

%if %{legacy_qemu_kvm}
%files kvm
%defattr(-,root,root)
%_bindir/qemu-kvm
%_mandir/man1/qemu-kvm.1.gz
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-kvm
%_docdir/qemu-kvm/kvm-supported.txt
%endif
%endif

%files block-curl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-curl.so

%files block-dmg
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-dmg-bz2.so
%if 0%{?is_opensuse}
%_libdir/%name/block-dmg-lzfse.so
%endif

%if 0%{?with_glusterfs}
%files block-gluster
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-gluster.so
%endif

%files block-iscsi
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-iscsi.so

%if 0%{?is_opensuse}
%files block-nfs
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-nfs.so
%endif

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

%files ui-curses
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-curses.so

%files ui-gtk
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-gtk.so

%if 0%{?is_opensuse}
%files ui-sdl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-sdl.so
%endif

%files audio-alsa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-alsa.so

%files audio-pa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-pa.so

%if 0%{?is_opensuse}
%files audio-sdl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-sdl.so
%endif

%files lang -f %mybuilddir/%name.lang
%defattr(-, root, root)

%ifarch %{build_rom_arch}
%files seabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin

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

%if %{provide_edk2_firmware}

%files edk2
%dir %_datadir/%name
%dir %_datadir/%name/firmware
%_datadir/%name/edk2-aarch64-code.fd
%_datadir/%name/edk2-arm-code.fd
%_datadir/%name/edk2-arm-vars.fd
%_datadir/%name/edk2-i386-code.fd
%_datadir/%name/edk2-i386-secure-code.fd
%_datadir/%name/edk2-i386-vars.fd
%_datadir/%name/edk2-licenses.txt
%_datadir/%name/edk2-x86_64-code.fd
%_datadir/%name/edk2-x86_64-secure-code.fd
%_datadir/%name/firmware/50-edk2-i386-secure.json
%_datadir/%name/firmware/50-edk2-x86_64-secure.json
%_datadir/%name/firmware/60-edk2-aarch64.json
%_datadir/%name/firmware/60-edk2-arm.json
%_datadir/%name/firmware/60-edk2-i386.json
%_datadir/%name/firmware/60-edk2-x86_64.json
%endif
%endif

%files vhost-user-gpu
%defattr(-, root, root)
%_libexecdir/vhost-user-gpu
%_docdir/%name/interop/vhost-user-gpu.html
%dir %_datadir/%name/vhost-user
%_datadir/%name/vhost-user/50-qemu-gpu.json

%files tools
%defattr(-, root, root)
%_mandir/man1/qemu-img.1.gz
%_mandir/man1/virtfs-proxy-helper.1.gz
%_mandir/man8/qemu-nbd.8.gz
%_bindir/elf2dmp
%_bindir/ivshmem-client
%_bindir/ivshmem-server
%_bindir/qemu-edid
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-keymap
%_bindir/qemu-nbd
%_bindir/qemu-pr-helper
%_bindir/virtfs-proxy-helper
%verify(not mode) %attr(4750,root,kvm) %_libexecdir/qemu-bridge-helper
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/bridge.conf
%_bindir/analyze-migration.py
%_bindir/vmstate-static-checker.py

%files guest-agent
%defattr(-, root, root)
%_mandir/man8/qemu-ga.8.gz
%attr(0755,root,kvm) %_bindir/qemu-ga
%{_unitdir}/qemu-ga@.service
/usr/lib/udev/rules.d/80-qemu-ga.rules

%if 0%{?is_opensuse}
%files ksm
%defattr(-, root, root)
%{_unitdir}/ksm.service
%endif

%endif # qemu
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-linux-user"

%_bindir/qemu-aarch64
%_bindir/qemu-aarch64_be
%_bindir/qemu-alpha
%_bindir/qemu-arm
%_bindir/qemu-armeb
%_bindir/qemu-cris
%_bindir/qemu-hppa
%_bindir/qemu-i386
%_bindir/qemu-m68k
%_bindir/qemu-microblaze
%_bindir/qemu-microblazeel
%_bindir/qemu-mips
%_bindir/qemu-mipsel
%_bindir/qemu-mipsn32
%_bindir/qemu-mipsn32el
%_bindir/qemu-mips64
%_bindir/qemu-mips64el
%_bindir/qemu-nios2
%_bindir/qemu-or1k
%_bindir/qemu-ppc64
%_bindir/qemu-ppc64abi32
%_bindir/qemu-ppc64le
%_bindir/qemu-ppc
%_bindir/qemu-riscv32
%_bindir/qemu-riscv64
%_bindir/qemu-s390x
%_bindir/qemu-sh4
%_bindir/qemu-sh4eb
%_bindir/qemu-sparc32plus
%_bindir/qemu-sparc64
%_bindir/qemu-sparc
%_bindir/qemu-tilegx
%_bindir/qemu-x86_64
%_bindir/qemu-xtensa
%_bindir/qemu-xtensaeb
%_bindir/qemu-*-binfmt
%_sbindir/qemu-binfmt-conf.sh

%endif # qemu-linux-user
# ------------------------------------------------------------------------
%if "%{name}" == "qemu-testsuite"

%_datadir/qemu/check-report.tap

%endif # qemu-testsuite

%changelog
