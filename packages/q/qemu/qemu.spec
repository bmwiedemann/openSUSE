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
%define name_suffix %{nil}

%if "%{flavor}" == "linux-user"
%define name_suffix -linux-user
%define summary_string CPU emulator for user space
%else
%define summary_string Machine emulator and virtualizer
%endif

%define _buildshell /bin/bash

%define srcdir %{_builddir}/%buildsubdir
%define blddir %srcdir/build

%define build_x86_firmware 0
%define build_ppc_firmware 0
%define build_opensbi_firmware 0
%define kvm_available 0
%define legacy_qemu_kvm 0
%define force_fit_virtio_pxe_rom 1

%if "%{?distribution}" == ""
%define distro private-build
%else
%define distro %{distribution}
%endif

# So, we have openSUSE:Factory, and we have "ports". In openSUSE:Factory, we
# have i586 and x86_64. In the :ARM port, we have aarch64, armv6l and armv7l.
# In the :PowerPC port, we have ppc64, ppc and ppc64le. In the :zSystems port
# we have s390x. And in the :RISCV we have riscv.
#
# Ideally, we'd want to build the firmwares at least once per port, and then
# share the resulting packages among the arch-es within each port (check the
# `ExportFilter` directives in the project config).
#
# Of course, we always build the "native fimrwares" (e.g., x86 firmwares on
# x86_64, PPC firmwares on ppc64le, etc). But we also cross compile as much
# firmwares as we can (e.g., both x86 and PPC firmwares on aarch64) so they'll
# be available in as many ports as possible (as noarch packages).

%ifarch x86_64 aarch64
%define build_ppc_firmware 1
# Currently, opensbi does not cross build cleanly on 15.3 and 15.4
%if ! 0%{?sle_version}
%define build_opensbi_firmware 1
%endif
%define build_x86_firmware 1
%endif
%ifarch ppc64 ppc64le
%define build_ppc_firmware 1
%if ! 0%{?sle_version}
%define build_opensbi_firmware 1
%endif
# FIXME: Try to enable cross building of x86 firmwares here on PPC
%endif
%ifarch riscv64
%define build_opensbi_firmware 1
%endif

%ifarch %ix86 x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64 riscv64
%define kvm_available 1
%define with_uring 1
%define liburing_min_version 1.0
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

%bcond_with chkqtests

# enforce pxe rom sizes for migration compatability from SLE 11 SP3 forward
# the following need to be > 64K
%define supported_nics_large {e1000 rtl8139}
# the following need to be <= 64K
%define supported_nics_small {virtio}
# Though not required, make unsupported pxe roms migration compatable as well
%define unsupported_nics {eepro100 ne2k_pci pcnet}

# non-x86 archs still seem to have some issues with Link Time Optimization
%ifnarch %ix86 x86_64
%define _lto_cflags %{nil}
%endif
%define _lto_cflags %{nil}

%define generic_qemu_description \
QEMU provides full machine emulation and cross architecture usage. It closely\
integrates with KVM and Xen virtualization, allowing for excellent performance.\
Many options are available for defining the emulated environment, including\
traditional devices, direct host device access, and interfaces specific to\
virtualization.

%bcond_with system_membarrier
%bcond_with malloc_trim

%define qemuver 7.1.0
%define srcver  7.1.0
%define sbver   1.16.0_0_gd239552
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
Source7:        qemu-guest-agent.service
Source8:        80-qemu-ga.rules
Source9:        qemu-supportconfig
Source10:       supported.arm.txt
Source11:       supported.ppc.txt
Source12:       supported.x86.txt
Source13:       supported.s390.txt
Source14:       50-seabios-256k.json
Source15:       60-seabios-128k.json
Source200:      qemu-rpmlintrc
Source201:      DSDT.pcie
Source300:      bundles.tar.xz
Source301:      update_git.sh
Source302:      config.sh
Source303:      README.PACKAGING
# Upstream First -- https://wiki.qemu.org/Contribute/SubmitAPatch
# This patch queue is auto-generated - see README.PACKAGING for process

# Patches applied in base project:
Patch00000:     roms-Makefile-pass-a-packaging-timestamp.patch
Patch00001:     roms-change-cross-compiler-naming-to-be-.patch
Patch00002:     roms-Makefile-add-cross-file-to-qboot-me.patch
Patch00003:     hw-smbios-handle-both-file-formats-regar.patch
Patch00004:     Revert-roms-efirom-tests-uefi-test-tools.patch
Patch00005:     qemu-binfmt-conf-Modify-default-path.patch
Patch00006:     linux-user-Fake-proc-cpuinfo.patch
Patch00007:     linux-user-use-target_ulong.patch
Patch00008:     linux-user-lseek-explicitly-cast-non-set.patch
Patch00009:     PPC-KVM-Disable-mmu-notifier-check.patch
Patch00010:     Make-char-muxer-more-robust-wrt-small-FI.patch
Patch00011:     qemu-bridge-helper-reduce-security-profi.patch
Patch00012:     Raise-soft-address-space-limit-to-hard-l.patch
Patch00013:     increase-x86_64-physical-bits-to-42.patch
Patch00014:     xen_disk-Add-suse-specific-flush-disable.patch
Patch00015:     xen-add-block-resize-support-for-xen-dis.patch
Patch00016:     xen-ignore-live-parameter-from-xen-save-.patch
Patch00017:     scsi-generic-replace-logical-block-count.patch
Patch00018:     hw-scsi-megasas-check-for-NULL-frame-in-.patch
Patch00019:     scsi-generic-check-for-additional-SG_IO-.patch
Patch00020:     Revert-tests-qtest-enable-more-vhost-use.patch
Patch00021:     tests-change-error-message-in-test-162.patch
Patch00022:     tests-qemu-iotests-Triple-timeout-of-i-o.patch
Patch00023:     Disable-some-tests-that-have-problems-in.patch
Patch00024:     Make-installed-scripts-explicitly-python.patch
Patch00025:     meson-install-ivshmem-client-and-ivshmem.patch
Patch00026:     meson-remove-pkgversion-from-CONFIG_STAM.patch
Patch00027:     linux-user-use-max-as-default-CPU-model-.patch
Patch00028:     net-tulip-Restrict-DMA-engine-to-memorie.patch
Patch00029:     linux-user-add-more-compat-ioctl-definit.patch
Patch00030:     linux-user-remove-conditionals-for-many-.patch
Patch00031:     meson-enforce-a-minimum-Linux-kernel-hea.patch
Patch00032:     linux-user-drop-conditionals-for-obsolet.patch
Patch00033:     block-io_uring-revert-Use-io_uring_regis.patch
Patch00034:     pc-q35-Bump-max_cpus-to-1024.patch
# Patches applied in roms/seabios/:
Patch01000:     seabios-switch-to-python3-as-needed.patch
Patch01001:     enable-cross-compilation-on-ARM.patch
Patch01002:     build-be-explicit-about-mx86-used-note-n.patch
# Patches applied in roms/ipxe/:
Patch02000:     ath5k-Add-missing-AR5K_EEPROM_READ-in-at.patch
#Patch02001:     stub-out-the-SAN-req-s-in-int13.patch
Patch02002:     ipxe-Makefile-fix-issues-of-build-reprod.patch
Patch02003:     help-compiler-out-by-initializing-array.patch
Patch02004:     Silence-GCC-12-spurious-warnings.patch
# Patches applied in roms/sgabios/:
Patch03000:     sgabios-Makefile-fix-issues-of-build-rep.patch
Patch03001:     roms-sgabios-Fix-csum8-to-be-built-by-ho.patch
# Patches applied in roms/edk2/:
Patch04000:     Ignore-spurious-GCC-12-warning.patch
# Patches applied in roms/skiboot/:
Patch05000:     Makefile-define-endianess-for-cross-buil.patch
# Patches applied in roms/qboot/:
Patch11000:     qboot-add-cross.ini-file-to-handle-aarch.patch
# Patches applied in roms/opensbi/:
Patch13000:     Makefile-fix-build-with-binutils-2.38.patch

# Patches that will be applied directly across the spec file
Source1000:     stub-out-the-SAN-req-s-in-int13.patch

# Please do not add patches manually here.

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if "%{name}" == "qemu-linux-user"
# Build dependencies exclusive to qemu-linux-user
BuildRequires:  glib2-devel-static >= 2.56
BuildRequires:  glibc-devel-static
# passing filelist check for /usr/lib/binfmt.d
BuildRequires:  systemd
BuildRequires:  zlib-devel-static
BuildRequires:  (pcre-devel-static if glib2-devel-static < 2.73 else pcre2-devel-static)
# we must not install the qemu-linux-user package when under QEMU build
%if 0%{?qemu_user_space_build:1}
#!BuildIgnore:  post-build-checks
%endif
# End of build dependencies for qemu-linux-user
%else
# Build dependencies exclusive to qemu
%if %{build_x86_firmware}
%ifnarch %ix86 x86_64
# We must cross-compile on non-x86*
BuildRequires:  cross-x86_64-binutils
BuildRequires:  cross-x86_64-gcc%gcc_version
%endif
BuildRequires:  acpica
BuildRequires:  binutils-devel
BuildRequires:  dos2unix
BuildRequires:  glibc-devel-32bit
BuildRequires:  pkgconfig(liblzma)
%endif
%if %{build_opensbi_firmware}
%ifnarch riscv64
BuildRequires:  cross-riscv64-binutils
BuildRequires:  cross-riscv64-gcc%gcc_version
%endif
%endif
%if %{build_ppc_firmware}
%ifnarch ppc64 ppc64le
BuildRequires:  cross-ppc64-binutils
BuildRequires:  cross-ppc64-gcc%gcc_version
%endif
%endif
%ifarch x86_64
BuildRequires:  gcc-32bit
BuildRequires:  xen-devel >= 4.2
BuildRequires:  pkgconfig(libpmem)
%endif
%ifnarch %arm s390x
BuildRequires:  libnuma-devel
%endif
%if 0%{?with_daxctl}
BuildRequires:  pkgconfig(libndctl)
%endif
%if 0%{?with_rbd}
BuildRequires:  librbd-devel
%endif
%if 0%{?with_uring}
BuildRequires:  pkgconfig(liburing) >= %liburing_min_version
%endif
%if %{kvm_available}
BuildRequires:  pkgconfig(udev)
%endif
BuildRequires:  Mesa-devel
BuildRequires:  bison
BuildRequires:  brlapi-devel
BuildRequires:  flex
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbpf-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcapstone-devel
BuildRequires:  libfdt-devel >= 1.4.2
BuildRequires:  libgcrypt-devel >= 1.8.0
BuildRequires:  lzfse-devel
BuildRequires:  multipath-tools-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rdma-core-devel
BuildRequires:  snappy-devel
BuildRequires:  update-desktop-files
BuildRequires:  usbredir-devel >= 0.6
BuildRequires:  xfsprogs-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(glusterfs-api) >= 3
BuildRequires:  pkgconfig(gnutls) >= 3.5.18
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcacard) >= 2.5.1
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libcurl) >= 7.29
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libiscsi) >= 1.9.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnfs) >= 1.9.3
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libseccomp) >= 2.3.0
BuildRequires:  pkgconfig(libssh) >= 0.8.7
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.13
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pixman-1) >= 0.21.8
BuildRequires:  pkgconfig(slirp) >= 4.2.0
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.3
BuildRequires:  pkgconfig(spice-server) >= 0.12.5
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vdeplug)
BuildRequires:  pkgconfig(virglrenderer) >= 0.4.1
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
%{?systemd_ordering}
# End of build dependencies for qemu
%endif
# Common build dependencies between qemu and qemu-linux-user
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja >= 1.7
BuildRequires:  perl-Text-Markdown
BuildRequires:  python3-base >= 3.6
BuildRequires:  python3-setuptools
%if "%{name}" == "qemu"
# Requires, Recommends, etc exclusive to qemu
%if %{kvm_available}
%ifarch %ix86 x86_64
Requires:       qemu-x86
%else
Suggests:       qemu-x86
%endif
%ifarch ppc ppc64 ppc64le
Requires:       qemu-ppc
%else
Suggests:       qemu-ppc
%endif
%ifarch s390x
Requires:       qemu-s390x
Requires(post): procps
%else
Suggests:       qemu-s390x
%endif
%ifarch %arm aarch64
Requires:       qemu-arm
%else
Suggests:       qemu-arm
%endif
%ifarch riscv64
Requires:       qemu-extra
%else
Suggests:       qemu-extra
%endif
Requires(post): acl
Requires(post): udev
Recommends:     kvm_stat
# End of "if kvm_available"
%endif
Requires:       group(kvm)
Requires:       group(qemu)
Requires:       user(qemu)
Requires(post): coreutils
%ifarch s390x
Recommends:     qemu-hw-s390x-virtio-gpu-ccw
%else
# Due to change in where some documentation files are, if qemu-guest-agent
# is installed, we need to make sure we update it to our version.
Requires:       (qemu-guest-agent = %{qemuver} if qemu-guest-agent)
Recommends:     qemu-hw-display-qxl
Recommends:     qemu-hw-display-virtio-gpu
Recommends:     qemu-hw-display-virtio-gpu-pci
Recommends:     qemu-hw-display-virtio-vga
Recommends:     qemu-hw-usb-host
Recommends:     qemu-hw-usb-redirect
Recommends:     qemu-hw-usb-smartcard
Recommends:     qemu-ui-gtk
Recommends:     qemu-ui-spice-app
# End of "ifarch s390x"
%endif
Recommends:     qemu-block-curl
Recommends:     qemu-block-nfs
Recommends:     qemu-ksm = %{qemuver}
Recommends:     qemu-tools
Recommends:     qemu-ui-curses
%if 0%{?with_rbd}
Suggests:       qemu-block-rbd
%endif
Suggests:       qemu-accel-qtest
Suggests:       qemu-block-dmg
Suggests:       qemu-block-gluster
Suggests:       qemu-block-iscsi
Suggests:       qemu-block-ssh
Suggests:       qemu-chardev-baum
Suggests:       qemu-extra
Suggests:       qemu-lang
Suggests:       qemu-microvm
Suggests:       qemu-skiboot
Suggests:       qemu-vhost-user-gpu
Obsoletes:      qemu-audio-oss < %{qemuver}
Obsoletes:      qemu-audio-sdl < %{qemuver}
Obsoletes:      qemu-ui-sdl < %{qemuver}
# End of Requires, Recommends, etc for qemu.
# There isn't any for qemu-linux-user.
%endif

%package headless
Summary:        Minimum set of packages for having a functional QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu
Requires:       qemu-tools
%if %{legacy_qemu_kvm}
Requires:       qemu-kvm
%endif
Requires:       qemu-hw-usb-redirect
# qemu-ui-spice-core will bring in qemu-audio-spice qemu-ui-opengl too
Requires:       qemu-ui-spice-core
Requires:       qemu-chardev-spice

%description headless
%{generic_qemu_description}

This meta-package brings in, as dependencies, the minimum set of packages
currently necessary for having a functional (headless) QEMU/KVM stack.

%if "%{name}" == "qemu-linux-user"
# Description and files for the qemu-linux-user package

%description
QEMU provides CPU emulation along with other related capabilities. This package
provides programs to run user space binaries and libraries meant for another
architecture. The syscall interface is intercepted and execution below the
syscall layer occurs on the native hardware and operating system.

%files
%defattr(-, root, root)
%doc README.rst VERSION
%license COPYING COPYING.LIB LICENSE
%_bindir/qemu-aarch64
%_bindir/qemu-aarch64_be
%_bindir/qemu-alpha
%_bindir/qemu-arm
%_bindir/qemu-armeb
%_bindir/qemu-cris
%_bindir/qemu-hexagon
%_bindir/qemu-hppa
%_bindir/qemu-i386
%_bindir/qemu-loongarch64
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
%_sbindir/qemu-binfmt-conf.sh
%_prefix/lib/binfmt.d/qemu-*.conf

# End of description and files for qemu-linux-user
%else
# Description and files for qemu and all its subpackages

%description
%{generic_qemu_description}

This package acts as an umbrella package to the other QEMU sub-packages.

%files
%defattr(-, root, root)
%dir %_datadir/icons/hicolor
%dir %_datadir/icons/hicolor/*/
%dir %_datadir/icons/hicolor/*/apps
%dir %_datadir/%name
%dir %_datadir/%name/firmware
%dir %_datadir/%name/vhost-user
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/firmware
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
%doc %_docdir/%name
%if %{kvm_available}
%ifarch s390x
%{_prefix}/lib/modules-load.d/kvm.conf
%endif
/usr/lib/udev/rules.d/80-kvm.rules
%endif
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
%_datadir/%name/keymaps
%_datadir/%name/qemu-ifup
%_datadir/%name/qemu-nsis.bmp
%_datadir/%name/trace-events-all
%_datadir/%name/vhost-user/50-qemu-virtiofsd.json
%_mandir/man1/%name.1.gz
%_mandir/man1/qemu-storage-daemon.1.gz
%_mandir/man1/virtiofsd.1.gz
%_mandir/man7/qemu-block-drivers.7.gz
%_mandir/man7/qemu-cpu-models.7.gz
%_mandir/man7/qemu-qmp-ref.7.gz
%_mandir/man7/qemu-ga-ref.7.gz
%_mandir/man7/qemu-storage-daemon-qmp-ref.7.gz
/usr/lib/supportconfig/plugins/%name
%license COPYING COPYING.LIB LICENSE

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
# End of "if {kvm_available}"
%endif

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

%package x86
Summary:        Machine emulator and virtualizer for x86 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Requires:       qemu-accel-tcg-x86
Requires:       qemu-ipxe
Requires:       qemu-seabios
Requires:       qemu-sgabios
Requires:       qemu-vgabios
%ifarch x86_64
Requires:       qemu-ovmf-x86_64
%else
Recommends:     qemu-ovmf-ia32
Recommends:     qemu-ovmf-x86_64
%endif
Recommends:     ovmf
Recommends:     qemu-microvm

%description x86
%{generic_qemu_description}

This package provides i386 and x86_64 emulation.

%files x86
%defattr(-, root, root)
%_bindir/qemu-system-i386
%_bindir/qemu-system-x86_64
%_datadir/%name/kvmvapic.bin
%_datadir/%name/linuxboot.bin
%_datadir/%name/linuxboot_dma.bin
%_datadir/%name/multiboot.bin
%_datadir/%name/multiboot_dma.bin
%_datadir/%name/pvh.bin
%doc %_docdir/qemu-x86

%package ppc
Summary:        Machine emulator and virtualizer for Power architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Requires:       qemu-SLOF
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios

%description ppc
%{generic_qemu_description}

This package provides ppc and ppc64 emulation.

%files ppc
%defattr(-, root, root)
%_bindir/qemu-system-ppc
%_bindir/qemu-system-ppc64
%_datadir/%name/bamboo.dtb
%_datadir/%name/canyonlands.dtb
%_datadir/%name/openbios-ppc
%_datadir/%name/qemu_vga.ndrv
%_datadir/%name/u-boot.e500
%_datadir/%name/u-boot-sam460-20100605.bin
%_datadir/%name/vof*.bin
%doc %_docdir/qemu-ppc

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

%files s390x
%defattr(-, root, root)
%_bindir/qemu-system-s390x
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%doc %_docdir/qemu-s390x

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

%files arm
%defattr(-, root, root)
%_bindir/qemu-system-arm
%_bindir/qemu-system-aarch64
%_datadir/%name/npcm7xx_bootrom.bin
%doc %_docdir/qemu-arm

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
mips, sparc, and xtensa. (The term "extra" is juxtapositioned against more
popular QEMU packages which are dedicated to a single architecture.)

%files extra
%defattr(-, root, root)
%_bindir/qemu-system-alpha
%_bindir/qemu-system-avr
%_bindir/qemu-system-cris
%_bindir/qemu-system-hppa
%_bindir/qemu-system-loongarch64
%_bindir/qemu-system-m68k
%_bindir/qemu-system-microblaze
%_bindir/qemu-system-microblazeel
%_bindir/qemu-system-mips
%_bindir/qemu-system-mipsel
%_bindir/qemu-system-mips64
%_bindir/qemu-system-mips64el
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
%_datadir/%name/opensbi-riscv64-generic-fw_dynamic.bin
%_datadir/%name/palcode-clipper
%_datadir/%name/petalogix-ml605.dtb
%_datadir/%name/petalogix-s3adsp1800.dtb
%_datadir/%name/QEMU,cgthree.bin
%_datadir/%name/QEMU,tcx.bin

%package lang
Summary:        Translations for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0

%description lang
This package contains a few language translations, particularly for the
graphical user interface components that come with QEMU. The bulk of strings
in QEMU are not localized.

%files lang -f %blddir/%name.lang
%defattr(-, root, root)

%package audio-alsa
Summary:        ALSA based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-alsa
This package contains a module for ALSA based audio support for QEMU.

%files audio-alsa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-alsa.so

%package audio-dbus
Summary:        D-Bus based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-dbus
This package provides a module for D-Bus based audio support for QEMU.

%files audio-dbus
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-dbus.so

%package audio-pa
Summary:        Pulse Audio based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-pa
This package contains a module for Pulse Audio based audio support for QEMU.

%files audio-pa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-pa.so

%package audio-jack
Summary:        JACK based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-jack
This package contains a module for JACK based audio support for QEMU.

%files audio-jack
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-jack.so

%package audio-spice
Summary:        Spice based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description audio-spice
This package contains a module for Spice based audio support for QEMU.

%files audio-spice
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-spice.so

%package audio-oss
Summary:        OSS based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-oss
This package contains a module for OSS based audio support for QEMU.

%files audio-oss
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-oss.so

%package block-curl
Summary:        cURL block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-curl
This package contains a module for accessing network-based image files over
a network connection from qemu-img tool and QEMU system emulation.

%files block-curl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-curl.so

%package block-dmg
Summary:        DMG block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-dmg
This package contains a module for accessing Mac OS X image files from
qemu-img tool and QEMU system emulation.

%files block-dmg
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-dmg-bz2.so
%_libdir/%name/block-dmg-lzfse.so

%package block-gluster
Summary:        GlusterFS block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-gluster
This package contains a module for accessing network-based image files over a
GlusterFS network connection from qemu-img tool and QEMU system emulation.

%files block-gluster
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-gluster.so

%package block-iscsi
Summary:        iSCSI block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-iscsi
This package contains a module for accessing network-based image files over an
iSCSI network connection from qemu-img tool and QEMU system emulation.

%files block-iscsi
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-iscsi.so

%package block-nfs
Summary:        direct Network File System support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-nfs
This package contains a module for directly accessing nfs based image files
for QEMU.

%files block-nfs
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-nfs.so

%package block-ssh
Summary:        SSH (SFTP) block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-ssh
This package contains a module for accessing network-based image files over an
SSH network connection from qemu-img tool and QEMU system emulation.

%files block-ssh
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-ssh.so

%package chardev-baum
Summary:        Baum braille chardev support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description chardev-baum
This package contains a module for baum braille chardev support for QEMU.

%files chardev-baum
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/chardev-baum.so

%package chardev-spice
Summary:        Spice vmc and port chardev support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description chardev-spice
This package contains a module for Spice chardev support for QEMU.

%files chardev-spice
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/chardev-spice.so

%package hw-display-qxl
Summary:        QXL display support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-spice-core
%{qemu_module_conflicts}

%description hw-display-qxl
This package contains a module for QXL display support for QEMU.

%files hw-display-qxl
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-qxl.so

%package hw-display-virtio-gpu
Summary:        Virtio GPU display support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description hw-display-virtio-gpu
This package contains a module for Virtio GPU display support for QEMU.

%files hw-display-virtio-gpu
%defattr(-, root, root)
%dir %_datadir/%name
%_libdir/%name/hw-display-virtio-gpu.so
%_libdir/%name/hw-display-virtio-gpu-gl.so

%package hw-display-virtio-gpu-pci
Summary:        Virtio-gpu pci device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-hw-display-virtio-gpu
%{qemu_module_conflicts}

%description hw-display-virtio-gpu-pci
This package contains a module providing the virtio gpu pci device for QEMU.

%files hw-display-virtio-gpu-pci
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-gpu-pci.so
%_libdir/%name/hw-display-virtio-gpu-pci-gl.so

%package hw-display-virtio-vga
Summary:        Virtio vga device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description hw-display-virtio-vga
This package contains a module providing the virtio vga device for QEMU.

%files hw-display-virtio-vga
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-vga.so
%_libdir/%name/hw-display-virtio-vga-gl.so

%package hw-s390x-virtio-gpu-ccw
Summary:        S390x virtio-gpu ccw device for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-hw-display-virtio-gpu
%{qemu_module_conflicts}

%description hw-s390x-virtio-gpu-ccw
This package contains a module providing the s390x virtio gpu ccw device for
QEMU.

%files hw-s390x-virtio-gpu-ccw
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-s390x-virtio-gpu-ccw.so

%package hw-usb-redirect
Summary:        USB redirection support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description hw-usb-redirect
This package contains a module for USB redirection support for QEMU.

%files hw-usb-redirect
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-redirect.so

%package hw-usb-smartcard
Summary:        USB smartcard support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description hw-usb-smartcard
This package contains a modules for USB smartcard support for QEMU.

%files hw-usb-smartcard
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-smartcard.so

%package hw-usb-host
Summary:        USB passthrough driver support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description hw-usb-host
This package contains a modules for USB passthrough driver for QEMU.

%files hw-usb-host
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-host.so

%package ui-dbus
Summary:        D-Bus based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-dbus
This package contains a module for doing D-Bus based UI for QEMU.

%files ui-dbus
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-dbus.so

%package ui-curses
Summary:        Curses based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-curses
This package contains a module for doing curses based UI for QEMU.

%files ui-curses
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-curses.so

%package ui-gtk
Summary:        GTK based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-opengl
%{qemu_module_conflicts}

%description ui-gtk
This package contains a module for doing GTK based UI for QEMU.

%files ui-gtk
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-gtk.so

%package ui-opengl
Summary:        OpenGL based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-opengl
This package contains a module for doing OpenGL based UI for QEMU.

%files ui-opengl
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/ui-egl-headless.so
%_libdir/%name/ui-opengl.so

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

%files ui-spice-app
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-spice-app.so

%package ui-spice-core
Summary:        Core Spice support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       qemu-ui-opengl
# This next Requires is only since virt-manager expects audio support
Requires:       qemu-audio-spice
%{qemu_module_conflicts}

%description ui-spice-core
This package contains a module with core Spice support for QEMU.

%files ui-spice-core
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/ui-spice-core.so

%package vhost-user-gpu
Summary:        Vhost user mode virtio-gpu 2D/3D rendering backend for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description vhost-user-gpu
This package contains a vhost user mode virtio-gpu 2D/3D rendering backend for
QEMU.

%files vhost-user-gpu
%defattr(-, root, root)
%dir %_datadir/%name/vhost-user
%_datadir/%name/vhost-user/50-qemu-gpu.json
%_libexecdir/vhost-user-gpu

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
%_bindir/vmxcap
%verify(not mode) %attr(4750,root,kvm) %_libexecdir/qemu-bridge-helper
%_libexecdir/virtfs-proxy-helper
%_libexecdir/virtiofsd
%_mandir/man1/qemu-img.1.gz
%_mandir/man1/virtfs-proxy-helper.1.gz
%_mandir/man8/qemu-nbd.8.gz
%_mandir/man8/qemu-pr-helper.8.gz
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/bridge.conf

%post tools
%set_permissions %_libexecdir/qemu-bridge-helper

%verifyscript tools
%verify_permissions %_libexecdir/qemu-bridge-helper

%package ivshmem-tools
Summary:        Inter-VM Shared Memory Tools for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0

%description ivshmem-tools
This package contains a sample shared memory client and server which utilize
QEMU's Inter-VM shared memory device as specified by the ivshmem client-server
protocol specification documented in docs/specs/ivshmem-spec.txt in QEMU source
code.

%files ivshmem-tools
%defattr(-, root, root)
%dir %_datadir/%name
%_bindir/ivshmem-client
%_bindir/ivshmem-server

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

%files guest-agent
%defattr(-, root, root)
%attr(0755,root,kvm) %_bindir/qemu-ga
%_mandir/man8/qemu-ga.8.gz
%{_unitdir}/qemu-guest-agent.service
/usr/lib/udev/rules.d/80-qemu-ga.rules

%pre guest-agent
%service_add_pre qemu-guest-agent.service

%post guest-agent
%service_add_post qemu-guest-agent.service
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl start qemu-guest-agent.service || :
fi

%preun guest-agent
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl stop qemu-guest-agent.service || :
fi

%postun guest-agent
%service_del_postun_without_restart qemu-guest-agent.service
if [ "$1" = "1" ] ; then
  if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
    /usr/bin/systemctl restart qemu-guest-agent.service || :
  fi
fi

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

%files ksm
%defattr(-, root, root)
%{_unitdir}/ksm.service

%pre ksm
%service_add_pre ksm.service

%post ksm
%service_add_post ksm.service

%preun ksm
%service_del_preun ksm.service

%postun ksm
%service_del_postun ksm.service

%package accel-tcg-x86
Summary:        TCG accelerator for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description accel-tcg-x86
TCG is the QEMU binary translator, responsible for converting from target to
host instruction set.

This package provides the TCG accelerator for QEMU.

%files accel-tcg-x86
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/accel-tcg-i386.so
%_libdir/%name/accel-tcg-x86_64.so

%package accel-qtest
Summary:        QTest accelerator for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description accel-qtest
QTest is a device emulation testing framework. It is useful to test device
models.

This package provides QTest accelerator for testing QEMU.

%files accel-qtest
%defattr(-, root, root)
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/accel-qtest-aarch64.so
%_libdir/%name/accel-qtest-alpha.so
%_libdir/%name/accel-qtest-arm.so
%_libdir/%name/accel-qtest-avr.so
%_libdir/%name/accel-qtest-cris.so
%_libdir/%name/accel-qtest-hppa.so
%_libdir/%name/accel-qtest-i386.so
%_libdir/%name/accel-qtest-loongarch64.so
%_libdir/%name/accel-qtest-m68k.so
%_libdir/%name/accel-qtest-microblaze.so
%_libdir/%name/accel-qtest-microblazeel.so
%_libdir/%name/accel-qtest-mips.so
%_libdir/%name/accel-qtest-mips64.so
%_libdir/%name/accel-qtest-mips64el.so
%_libdir/%name/accel-qtest-mipsel.so
%_libdir/%name/accel-qtest-nios2.so
%_libdir/%name/accel-qtest-or1k.so
%_libdir/%name/accel-qtest-ppc.so
%_libdir/%name/accel-qtest-ppc64.so
%_libdir/%name/accel-qtest-riscv32.so
%_libdir/%name/accel-qtest-riscv64.so
%_libdir/%name/accel-qtest-rx.so
%_libdir/%name/accel-qtest-s390x.so
%_libdir/%name/accel-qtest-sh4.so
%_libdir/%name/accel-qtest-sh4eb.so
%_libdir/%name/accel-qtest-sparc.so
%_libdir/%name/accel-qtest-sparc64.so
%_libdir/%name/accel-qtest-tricore.so
%_libdir/%name/accel-qtest-x86_64.so
%_libdir/%name/accel-qtest-xtensa.so
%_libdir/%name/accel-qtest-xtensaeb.so

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

%files block-rbd
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-rbd.so
# End of "if with_rbd"
%endif

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

%files kvm
%defattr(-,root,root)
%_bindir/qemu-kvm
%doc %_docdir/qemu-kvm
%_mandir/man1/qemu-kvm.1.gz
# End of "if legacy_qemu_kvm"
%endif

%if %{build_ppc_firmware}
%package SLOF
Summary:        Slimline Open Firmware - SLOF
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
BuildArch:      noarch

%description SLOF
Slimline Open Firmware (SLOF) is an implementation of the IEEE 1275 standard.
It can be used as partition firmware for pSeries machines running on QEMU or KVM.

%files SLOF
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/slof.bin

%package skiboot
Summary:        OPAL firmware (aka skiboot), used in booting OpenPOWER systems
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description skiboot
Provides OPAL (OpenPower Abstraction Layer) firmware, aka skiboot, as
traditionally packaged with QEMU.

%files skiboot
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/skiboot.lid
%_datadir/%name/skiboot.lid.qemu
%ghost %_sysconfdir/alternatives/skiboot.lid

%post skiboot
update-alternatives --install \
   %{_datadir}/%name/skiboot.lid skiboot.lid %{_datadir}/%name/skiboot.lid.qemu 15

%preun skiboot
if [ ! -f %{_datadir}/%name/skiboot.lid.qemu ] ; then
   update-alternatives --remove skiboot.lid %{_datadir}/%name/skiboot.lid.qemu
fi
# End of "if build_ppc_firmware"
%endif

%if %{build_x86_firmware}
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

%files microvm
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios-microvm.bin
%_datadir/%name/qboot.rom

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

%files seabios -f roms/seabios/docs/docs.txt
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin
%_datadir/%name/firmware/50-seabios-256k.json
%_datadir/%name/firmware/60-seabios-128k.json
%license  roms/seabios/COPYING

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

%files sgabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/sgabios.bin

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
# End of "if build_x86_firmware"
%endif

# End of description and files for qemu and all its subpackages
%endif

%prep
#if 0%{?sle_version} <= 150400
# Apparently, autosetup does not work, not even in 15.4. So,
# keep 'setup' plus the generated list of patches here for a
# while. Hopefully we'll be able to get rid of this soon enough.
#setup -q -n %{srcname}-%{expand:%%(SV=%{srcver};echo ${SV%%%%+git*})}
#PATCH_EXEC
#else
#autosetup -p1 -n %{srcname}-%{expand:%%(SV=%{srcver};echo ${SV%%%%+git*})}
%autosetup -p1 -n %{srcname}-%{srcver}
#endif

%if "%{name}" == "qemu"
# Specific preparation steps for building qemu

# for the record, this set of firmware files is installed, but we don't
# build (yet): bamboo.dtb canyonlands.dtb hppa-firmware.img openbios-ppc
# openbios-sparc32 openbios-sparc64 palcode-clipper petalogix-ml605.dtb
# petalogix-s3adsp1800.dtb QEMU,cgthree.bin QEMU,tcx.bin qemu_vga.ndrv
# u-boot.e500 u-boot-sam460-20100605.bin opensbi-riscv32-generic-fw_dynamic.bin
# opensbi-riscv32-generic-fw_dynamic.elfnpcm7xx_bootrom.bin vof.bin
# vof-nvram.bin

# Note that:
# - default firmwares are built "by default", i.e., they're built automatically
#   during the process of building QEMU (on each specific arch)
# - extra firmwares are built "manually" (see below)  from their own sources
#   (which, typically, are submodules checked out in the {srcdi}r/roms directory)
%define ppc_default_firmware %{nil}
#{vof.bin vof-nvram.bin}
%define ppc_extra_firmware {skiboot.lid slof.bin}
%define riscv64_default_firmware %{nil}
%define riscv64_extra_firmware {opensbi-riscv64-generic-fw_dynamic.bin}
%define s390x_default_firmware {s390-ccw.img s390-netboot.img}
%define s390x_extra_firmware %{nil}
%define x86_default_firmware {linuxboot.bin linuxboot_dma.bin multiboot.bin \
multiboot_dma.bin kvmvapic.bin pvh.bin}
%define x86_extra_firmware {bios.bin bios-256k.bin bios-microvm.bin qboot.rom \
pxe-e1000.rom pxe-eepro100.rom pxe-ne2k_pci.rom pxe-pcnet.rom pxe-rtl8139.rom \
pxe-virtio.rom sgabios.bin vgabios-ati.bin vgabios-bochs-display.bin \
vgabios.bin vgabios-cirrus.bin vgabios-qxl.bin vgabios-ramfb.bin \
vgabios-stdvga.bin vgabios-virtio.bin vgabios-vmware.bin \
efi-e1000.rom efi-e1000e.rom efi-eepro100.rom efi-ne2k_pci.rom efi-pcnet.rom \
efi-rtl8139.rom efi-virtio.rom efi-vmxnet3.rom}

# Complete list of all the firmwares that we build, if we consider
# all the builds, on all the arches.
%define firmware { \
%{ppc_default_firmware} %{ppc_extra_firmware} \
%{riscv64_default_firmware} %{riscv64_extra_firmware} \
%{s390x_default_firmware} %{s390x_extra_firmware} \
%{x86_default_firmware} %{x86_extra_firmware} }

# Note that:
# - {arch}_default_built_firmware are the firmwares that we will be built by
#   default in this particular build, on the arch where we currently are on
# - {arch}_extra_built_fimrware, likewise, but for extra firmwares, built manually
%ifarch ppc64 ppc64le
%define ppc_default_built_firmware %{ppc_default_firmware}
%endif
%ifarch riscv64
%define riscv64_default_built_firmware %{riscv64_default_firmware}
%endif
%ifarch s390x
%define s390x_default_built_firmware %{s390x_default_firmware}
%endif
%ifarch %ix86 x86_64
%define x86_default_built_firmware %{x86_default_firmware}
%endif

%if %{build_opensbi_firmware}
%define riscv64_extra_built_firmware %{riscv64_extra_firmware}
%endif
%if %{build_ppc_firmware}
%define ppc_extra_built_firmware %{ppc_extra_firmware}
%endif
%if %{build_x86_firmware}
%define x86_extra_built_firmware %{x86_extra_firmware}
%endif

# List of only firmwares that will actually be built, in this instance
%define built_firmware { \
%{?ppc_default_built_firmware} %{?ppc_extra_built_firmware} \
%{?riscv64_default_built_firmware} %{?riscv64_extra_built_firmware} \
%{?s390x_default_built_firmware} %{?s390x_extra_built_firmware} \
%{?x86_default_built_firmware} %{?x86_extra_built_firmware} }

# End of source preparation for qemu
%endif

%build

%{nil build documentation for SeaBIOS }
(d=roms/seabios/docs/
cd "${d}"
%{nil remember list of jobs in $@ }
set --
for f in *.md
  do b="${f%.md}"

    %{nil the following 2 commands are independent }

    %{nil ensure the correct media type }
    Markdown.pl "${f}" >"${b}.html" & set -- "${@}" "${!}"

    %{nil links to b.md will be rendered as to b;
    soft link because %%doc makes a copy }
    ln -Ts "${b}.html" "${b}" & set -- "${@}" "${!}"

    echo >>docs.txt %%doc "${d}${b}.html" "${d}${b}"

  done

  %{nil wait here because we are running in a subshell }
  while ((${#}))
  do wait "${1}"
    shift
  done
  ) & ((seabios_docs_pid = $!))

%if %{legacy_qemu_kvm}
# FIXME: Why are we copying the s390 specific one (SOURCE13)?
cp %{SOURCE13} docs/supported.rst
sed -i '/^\ \ \ about\/index.*/i \ \ \ supported.rst' docs/index.rst
%endif

mkdir -p %blddir
cd %blddir

# We define a few general and common options and then we disable
# pretty much everything. Afterwards, there is a section for each
# of the flavors where we explicitly enable all the feature we want
# for them.

# TODO: Check whether we want to enable the followings:
# * avx512f
# * debug-info
# * fuse
# * malloc-trim
# * multiprocess
# * qom-cast-debug
# * trace-backends=dtrace
#
# Fedora has avx2 enabled for ix86, while we can't (I tried). Guess it's
# because, for them, ix86 == i686 (while for us it's i586).

# Let's try to stick to _FORTIFY_SOURCE=2 for now
EXTRA_CFLAGS="$(echo %{optflags} | sed -E 's/-[A-Z]?_FORTIFY_SOURCE[=]?[0-9]*//g') -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2"

%srcdir/configure \
	--docdir=%_docdir \
	--datadir=%_datadir \
	--extra-cflags="${EXTRA_CFLAGS}" \
	--firmwarepath=%_datadir/%name \
	--libdir=%_libdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--prefix=%_prefix \
        --python=%_bindir/python3 \
	--sysconfdir=%_sysconfdir \
	--with-git-submodules=ignore \
	--with-pkgversion="%(echo '%{distro}' | sed 's/ (.*)//')" \
	--disable-alsa \
	--disable-attr \
	--disable-auth-pam \
	--disable-avx2 \
	--disable-avx512f \
	--disable-block-drv-whitelist-in-tools \
	--disable-bochs \
	--disable-bpf \
	--disable-brlapi \
	--disable-bsd-user \
	--disable-bzip2 \
	--disable-cap-ng \
	--disable-capstone \
	--disable-cfi \
	--disable-cfi-debug \
	--disable-cloop \
	--disable-cocoa \
	--disable-coreaudio \
	--disable-coroutine-pool \
	--disable-crypto-afalg \
	--disable-curl \
	--disable-curses \
	--disable-dbus-display \
	--disable-debug-info \
	--disable-debug-mutex \
	--disable-debug-tcg \
	--disable-dmg \
	--disable-docs \
	--disable-dsound \
	--disable-fdt \
	--disable-fuse \
	--disable-fuse-lseek \
	--disable-gcrypt \
	--disable-gettext \
	--disable-gio \
	--disable-glusterfs \
	--disable-gnutls \
	--disable-gtk \
	--disable-guest-agent \
	--disable-guest-agent-msi \
	--disable-hax \
	--disable-hvf \
	--disable-iconv \
	--disable-jack \
	--disable-kvm \
	--disable-l2tpv3 \
	--disable-libdaxctl \
	--disable-libiscsi \
	--disable-libnfs \
	--disable-libpmem \
	--disable-libssh \
	--disable-libudev \
	--disable-libusb \
	--disable-linux-aio \
	--disable-linux-io-uring \
	--disable-linux-user \
	--disable-live-block-migration \
	--disable-lto \
	--disable-lzfse \
	--disable-lzo \
	--disable-malloc-trim \
	--disable-membarrier \
	--disable-module-upgrades \
	--disable-modules \
	--disable-mpath \
	--disable-multiprocess \
	--disable-netmap \
	--disable-nettle \
	--disable-numa \
	--disable-nvmm \
	--disable-opengl \
	--disable-oss \
	--disable-pa \
	--disable-parallels \
	--disable-pie \
	--disable-plugins \
	--disable-png \
	--disable-pvrdma \
	--disable-qcow1 \
	--disable-qed \
	--disable-qom-cast-debug \
	--disable-rbd \
	--disable-rdma \
	--disable-replication \
	--disable-rng-none \
	--disable-safe-stack \
	--disable-sanitizers \
	--disable-sdl \
	--disable-sdl-image \
	--disable-seccomp \
	--disable-selinux \
	--disable-slirp \
	--disable-slirp-smbd \
	--disable-smartcard \
	--disable-snappy \
	--disable-sparse \
	--disable-spice \
	--disable-spice-protocol \
	--disable-strip \
	--disable-system \
	--disable-tcg \
	--disable-tcg-interpreter \
	--disable-tools \
	--disable-tpm \
	--disable-u2f \
	--disable-usb-redir \
	--disable-user \
	--disable-vde \
	--disable-vdi \
	--disable-vhost-crypto \
	--disable-vhost-kernel \
	--disable-vhost-net \
	--disable-vhost-user \
	--disable-vhost-user-blk-server \
	--disable-vhost-vdpa \
	--disable-virglrenderer \
	--disable-virtfs \
	--disable-virtiofsd \
	--disable-vnc \
	--disable-vnc-jpeg \
	--disable-vnc-sasl \
	--disable-vte \
	--disable-vvfat \
	--disable-werror \
	--disable-whpx \
	--disable-xen \
	--disable-xen-pci-passthrough \
	--disable-xkbcommon \
	--disable-zstd \
	--without-default-devices \
%if %{with system_membarrier}
	--enable-membarrier \
%endif
%if %{with malloc_trim}
	--enable-malloc-trim \
%endif
%if "%{_lto_cflags}" != "%{nil}"
	--enable-lto \
%endif
%if "%{name}" == "qemu-linux-user"
	--disable-install-blobs \
	--enable-attr \
	--enable-coroutine-pool \
	--enable-linux-user \
	--enable-selinux \
	--enable-tcg \
	--static \
%else
	--audio-drv-list=pa,alsa,jack,oss \
	--enable-auth-pam \
%ifarch x86_64
	--enable-avx2 \
	--enable-libpmem \
	--enable-xen \
	--enable-xen-pci-passthrough \
%endif
%ifnarch %arm s390x
	--enable-numa \
%endif
%if %{kvm_available}
	--enable-kvm \
%endif
%if 0%{?with_daxctl}
	--enable-libdaxctl \
%endif
%if 0%{?with_uring}
        --enable-linux-io-uring \
%endif
%if 0%{?with_rbd}
	--enable-rbd \
%endif
	--enable-alsa \
	--enable-attr \
	--enable-bochs \
	--enable-brlapi \
	--enable-bpf \
	--enable-bzip2 \
	--enable-cap-ng \
	--enable-capstone \
	--enable-cloop \
	--enable-coroutine-pool \
	--enable-curl \
	--enable-curses \
	--enable-dbus-display \
	--enable-dmg \
	--enable-docs \
	--enable-fdt=system \
	--enable-gcrypt \
	--enable-gettext \
	--enable-gio \
	--enable-glusterfs \
	--enable-gnutls \
	--enable-gtk \
	--enable-guest-agent \
	--enable-iconv \
	--enable-jack \
	--enable-l2tpv3 \
	--enable-libiscsi \
	--enable-libnfs \
	--enable-libssh \
	--enable-libudev \
	--enable-libusb \
	--enable-linux-aio \
	--enable-live-block-migration \
	--enable-lzfse \
	--enable-lzo \
	--enable-modules \
	--enable-mpath \
	--enable-opengl \
	--enable-oss \
	--enable-pa \
	--enable-parallels \
	--enable-pie \
	--enable-png \
	--enable-pvrdma \
	--enable-qcow1 \
	--enable-qed \
	--enable-rdma \
	--enable-replication \
	--enable-seccomp \
	--enable-selinux \
	--enable-slirp-smbd \
	--enable-slirp=system \
	--enable-smartcard \
	--enable-snappy \
	--enable-spice \
	--enable-spice-protocol \
	--enable-system \
	--enable-tcg \
	--enable-tools \
	--enable-tpm \
	--enable-usb-redir \
	--enable-vde \
	--enable-vdi \
	--enable-vhost-crypto \
	--enable-vhost-kernel \
	--enable-vhost-net \
	--enable-vhost-user \
	--enable-vhost-user-blk-server \
	--enable-vhost-vdpa \
	--enable-virglrenderer \
	--enable-virtfs \
	--enable-virtiofsd \
	--enable-vnc \
	--enable-vnc-jpeg \
	--enable-vnc-sasl \
	--enable-vte \
	--enable-vvfat \
	--enable-werror \
	--enable-xkbcommon \
	--enable-zstd \
	--with-coroutine=ucontext \
	--with-default-devices
# End of configure option ("name == qemu-linux-user" above)
%endif

echo "=== Content of config-host.mak: ==="
cat config-host.mak
echo "=== ==="

%if "%{name}" == "qemu"
# For building QEMU and all the "default" firmwares, for each arch,
# for the package qemu, we first need to delete the firmware files that
# we intend to build...
#
# TODO: check if this can be common to qemu and qemu-linux-user
for i in %built_firmware
do
  unlink %srcdir/pc-bios/$i
done
# End of unlinking pre-built firmwares for qemu
%endif

# Common build steps for qemu and qemu-linux-user
%make_build

%if "%{name}" == "qemu"
# ... Then, we need to reinstate the firmwares that have been built already
for i in %{?s390x_default_built_firmware}
do
  cp pc-bios/s390-ccw/$i %srcdir/pc-bios/
done

for i in %{?x86_default_built_firmware}
do
  cp pc-bios/optionrom/$i %srcdir/pc-bios/
done

# Build the "extra" firmwares. Note that the QEMU Makefile in {srcdir}/roms
# does some cross-compiler auto detection. So we often don't need to define
# or pass CROSS= and CROSS_COMPILE ourselves.

%if %{build_ppc_firmware}
# FIXME: check if we can upstream: Makefile-define-endianess-for-cross-buil.patch
%make_build -C %srcdir/roms skiboot

%make_build -C %srcdir/roms slof
%endif

%if %{build_opensbi_firmware}
%make_build -C %srcdir/roms opensbi64-generic
# End of "if build_ppc_firmware"
%endif

%if %{build_x86_firmware}
%make_build %{?_smp_mflags} -C %srcdir/roms bios \
  SEABIOS_EXTRAVERSION="-rebuilt.opensuse.org" \

# FIXME: check if we can upstream: roms-Makefile-add-cross-file-to-qboot-me.patch
# and qboot-add-cross.ini-file-to-handle-aarch.patch
%make_build -C %srcdir/roms qboot

%make_build -C %srcdir/roms seavgabios \

%make_build -C %srcdir/roms seavgabios-ati \

%make_build -C %srcdir/roms pxerom

%make_build -C %srcdir/roms efirom \
  EDK2_BASETOOLS_OPTFLAGS='-fPIE'

# We're currently not building firmware on ix86, but let's make sure this works
# fine if one enables it, e.g., locally (for debugging or something).
# FIXME: check if we can get rid or upstream: roms-sgabios-Fix-csum8-to-be-built-by-ho.patch
make -C %srcdir/roms sgabios HOSTCC=cc \
%ifnarch %ix86 x86_64
    CC=x86_64-suse-linux-gcc LD=x86_64-suse-linux-ld \
%endif

%if %{force_fit_virtio_pxe_rom}
pushd %srcdir
patch -p1 < %_sourcedir/stub-out-the-SAN-req-s-in-int13.patch
popd
%make_build -C %srcdir/roms pxerom_variants=virtio pxerom_targets=1af41000 pxerom
%endif

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
# End of "if build_x86_firmware"
%endif

# End of the build for qemu
%endif
wait $seabios_docs_pid

%install
cd %blddir

%make_build install DESTDIR=%{buildroot}

%if "%{name}" == "qemu-linux-user"
# Additional installation steps specific to qemu-linux-user

rm -rf %{buildroot}%_datadir/qemu/keymaps
unlink %{buildroot}%_datadir/qemu/trace-events-all
install -d -m 755 %{buildroot}%_sbindir
install -m 755 scripts/qemu-binfmt-conf.sh %{buildroot}%_sbindir
install -d -m 755 %{buildroot}%{_prefix}/lib/binfmt.d/
scripts/qemu-binfmt-conf.sh --systemd ALL --persistent yes --exportdir %{buildroot}%{_prefix}/lib/binfmt.d/

# End of additional installation steps for qemu-linux-user
%else
# Additional installation steps specific to qemu

%find_lang %name
install -d -m 0755 %{buildroot}%_datadir/%name/firmware
install -d -m 0755 %{buildroot}/usr/lib/supportconfig/plugins
install -d -m 0755 %{buildroot}%_sysconfdir/%name/firmware
install -D -m 0644 %{SOURCE4} %{buildroot}%_sysconfdir/%name/bridge.conf
install -D -m 0755 %{SOURCE3} %{buildroot}%_datadir/%name/qemu-ifup
install -D -p -m 0644 %{SOURCE8} %{buildroot}/usr/lib/udev/rules.d/80-qemu-ga.rules
install -D -m 0755 scripts/analyze-migration.py  %{buildroot}%_bindir/analyze-migration.py
install -D -m 0755 scripts/vmstate-static-checker.py  %{buildroot}%_bindir/vmstate-static-checker.py
install -D -m 0755 scripts/kvm/vmxcap  %{buildroot}%_bindir/vmxcap
install -D -m 0755 %{SOURCE9} %{buildroot}/usr/lib/supportconfig/plugins/%name
install -D -m 0644 %{SOURCE10} %{buildroot}%_docdir/qemu-arm/supported.txt
install -D -m 0644 %{SOURCE11} %{buildroot}%_docdir/qemu-ppc/supported.txt
install -D -m 0644 %{SOURCE12} %{buildroot}%_docdir/qemu-x86/supported.txt
install -D -m 0644 %{SOURCE13} %{buildroot}%_docdir/qemu-s390x/supported.txt

%if %{legacy_qemu_kvm}
install -D -m 0644 %{SOURCE5} %{buildroot}%_mandir/man1/qemu-kvm.1.gz
install -d %{buildroot}%_docdir/qemu-kvm
# FIXME: Why do we onlly generate the HTML for the legacy package documentation?
%ifarch s390x
ln -s qemu-system-s390x %{buildroot}%_bindir/qemu-kvm
ln -s ../qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
%else
ln -s qemu-system-x86_64 %{buildroot}%_bindir/qemu-kvm
ln -s ../qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
# End of "ifarch s390x"
%endif
# End of "if legacy_qemu_kvm"
%endif

%if %{kvm_available}
install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d/80-kvm.rules
%endif
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/qemu-guest-agent.service
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/ksm.service
%ifarch s390x
install -D -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/modules-load.d/kvm.conf
# End of "if kvm_available"
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

# For PPC and x86 firmwares, there are a few extra install steps necessary.
# In general, if we know that we have not built a firmware, remove it from the
# install base, as the one that we have there is the upstream binary, that got
# copied there during `make install`.

%if %{build_ppc_firmware}
# In support of update-alternatives
#
# The reason why we do this, is because we have (only for PPC) an skiboot
# package, shipping an alternative version of skiboot.lid. That is, in fact,
# what's "on the other end" of us supporting update-alternatives for this
# particular firmware.
mv %{buildroot}%_datadir/%name/skiboot.lid %{buildroot}%_datadir/%name/skiboot.lid.qemu
# create a dummy target for /etc/alternatives/skiboot.lid
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/skiboot.lid %{buildroot}%{_datadir}/%name/skiboot.lid
%else
for f in %{ppc_extra_firmware} ; do
  unlink %{buildroot}%_datadir/%name/$f
done
# End of "if build_ppc_fimrware"
%endif

# For riscv64 firmwares (currently, only opensbi), we leave them there in
# any case, because they're part of the qemu-extra package, and riscv is
# a bit special in many ways already.

%if %{build_x86_firmware}
install -D -m 0644 %{SOURCE14} %{buildroot}%_datadir/%name/firmware/50-seabios-256k.json
install -D -m 0644 %{SOURCE15} %{buildroot}%_datadir/%name/firmware/60-seabios-128k.json
%else
for f in %{x86_extra_firmware} ; do
  unlink %{buildroot}%_datadir/%name/$f
done
# End of "if build_x86_firmware"
%endif

%suse_update_desktop_file qemu

# End of additional installation steps for qemu
%endif

# Common install steps for qemu and qemu-linux-user
%fdupes -s %{buildroot}

%check
cd %blddir

%if "%{name}" == "qemu"
# Let's try to run 'make check' for the qemu package

# Patch 'increase x86_64 physical bits to 42' requires that the DSDT used for
# acpi [q]tests is modified too. But it's binary, and that means we cannot
# do that in the patch itself. Instead, we keep a copy of the binary in the
# package sources, and put it in place now, before the tests themselves.
# If that patch is removed, the following line needs to go as well.
cp %{SOURCE201} %{srcdir}/tests/data/acpi/microvm/

%if 0%{?qemu_user_space_build}
# Seccomp is not supported by linux-user emulation
echo 'int main (void) { return 0; }' > %{srcdir}/tests/unit/test-seccomp.c
%endif

# Compile the QOM test binary first, so that ...
%make_build tests/qtest/qom-test
# ... make comes in fresh and has lots of address space (needed for 32bit, bsc#957379)
# FIXME: is this still a problem?

# Let's build everything first
%make_build check-build
# Let's now run the 'make check' component individually, so we have
# more control on the options (like -j, etc)
%make_build check-unit
%make_build check-qapi-schema
%make_build check-softfloat
# This would be `make_build check-block`. But iotests are not reliable
# if ran in parallel in OBS, so let's be slow for now.
make -O V=1 VERBOSE=1 -j1 check-block
%if %{with chkqtests} && !0%{?qemu_user_space_build}
# Run qtests sequentially, as it's too unreliable, when run in OBS, if parallelized
make -O V=1 VERBOSE=1 -j1 check-qtest
%endif
# Last step will be to run a full check-report, but we will
# enable this at a later point
#make -O V=1 VERBOSE=1 -j1 check-report.junit.xml

# End of checks for qemu
%else
# Let's run the relevant check for the qemu-linux-user package

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

%ifarch %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le s390x
%ifnarch %arm
%{qemu_arch}-linux-user/qemu-%{qemu_arch} %_bindir/ls > /dev/null
%endif
%endif

%make_build check-softfloat
# End of the checks for qemu-linux-user
%endif

%changelog
