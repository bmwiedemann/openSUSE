#
# spec file for package qemu-linux-user
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


%define build_in_tree 1

%define srcname qemu
Name:           qemu-linux-user
Url:            https://www.qemu.org/
Summary:        CPU emulator for user space
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
%define qemuver 4.0.0
%define srcver  4.0.0
Version:        %qemuver
Release:        0
Source:         https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz
Source99:       https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz.sig
Source100:      %{srcname}.keyring
Source400:      update_git.sh
# Upstream First -- https://wiki.qemu.org/Contribute/SubmitAPatch
# This patch queue is auto-generated from https://github.com/openSUSE/qemu
Patch0001:      0001-XXX-dont-dump-core-on-sigabort.patch
Patch0002:      0002-qemu-binfmt-conf-Modify-default-pat.patch
Patch0003:      0003-qemu-cvs-gettimeofday.patch
Patch0004:      0004-qemu-cvs-ioctl_debug.patch
Patch0005:      0005-qemu-cvs-ioctl_nodirection.patch
Patch0006:      0006-linux-user-add-binfmt-wrapper-for-a.patch
Patch0007:      0007-PPC-KVM-Disable-mmu-notifier-check.patch
Patch0008:      0008-linux-user-binfmt-support-host-bina.patch
Patch0009:      0009-linux-user-Fake-proc-cpuinfo.patch
Patch0010:      0010-linux-user-use-target_ulong.patch
Patch0011:      0011-Make-char-muxer-more-robust-wrt-sma.patch
Patch0012:      0012-linux-user-lseek-explicitly-cast-no.patch
Patch0013:      0013-AIO-Reduce-number-of-threads-for-32.patch
Patch0014:      0014-xen_disk-Add-suse-specific-flush-di.patch
Patch0015:      0015-qemu-bridge-helper-reduce-security-.patch
Patch0016:      0016-qemu-binfmt-conf-use-qemu-ARCH-binf.patch
Patch0017:      0017-linux-user-properly-test-for-infini.patch
Patch0018:      0018-roms-Makefile-pass-a-packaging-time.patch
Patch0019:      0019-Raise-soft-address-space-limit-to-h.patch
Patch0020:      0020-increase-x86_64-physical-bits-to-42.patch
Patch0021:      0021-vga-Raise-VRAM-to-16-MiB-for-pc-0.1.patch
Patch0022:      0022-i8254-Fix-migration-from-SLE11-SP2.patch
Patch0023:      0023-acpi_piix4-Fix-migration-from-SLE11.patch
Patch0024:      0024-Switch-order-of-libraries-for-mpath.patch
Patch0025:      0025-Make-installed-scripts-explicitly-p.patch
Patch0026:      0026-hw-smbios-handle-both-file-formats-.patch
Patch0027:      0027-tests-test-thread-pool-is-racy-add-.patch
Patch0028:      0028-xen-add-block-resize-support-for-xe.patch
Patch0029:      0029-tests-qemu-iotests-Triple-timeout-o.patch
Patch0030:      0030-tests-block-io-test-130-needs-some-.patch
Patch0031:      0031-xen-ignore-live-parameter-from-xen-.patch
Patch0032:      0032-tests-Fix-Makefile-handling-of-chec.patch
Patch0033:      0033-Conditionalize-ui-bitmap-installati.patch
Patch0034:      0034-Revert-target-i386-kvm-add-VMX-migr.patch
Patch0035:      0035-tests-change-error-message-in-test-.patch
Patch0036:      0036-sockets-avoid-string-truncation-war.patch
Patch0037:      0037-hw-usb-hcd-xhci-Fix-GCC-9-build-war.patch
Patch0038:      0038-hw-usb-dev-mtp-Fix-GCC-9-build-warn.patch
Patch0039:      0039-linux-user-avoid-string-truncation-.patch
Patch0040:      0040-linux-user-elfload-Fix-GCC-9-build-.patch
Patch0041:      0041-qxl-avoid-unaligned-pointer-reads-w.patch
Patch0042:      0042-libvhost-user-fix-Waddress-of-packe.patch
Patch0043:      0043-target-i386-define-md-clear-bit.patch
Patch0044:      0044-hw-intc-exynos4210_gic-provide-more.patch
Patch0045:      0045-kbd-state-fix-autorepeat-handling.patch
Patch0046:      0046-target-ppc-ensure-we-get-null-termi.patch
Patch0047:      0047-configure-only-populate-roms-if-sof.patch
Patch0048:      0048-pc-bios-s390-ccw-net-avoid-warning-.patch
Patch0049:      0049-qxl-check-release-info-object.patch
Patch0050:      0050-qemu-bridge-helper-restrict-interfa.patch
Patch0051:      0051-linux-user-fix-to-handle-variably-s.patch
# Please do not add QEMU patches manually here.
# Run update_git.sh to regenerate this queue.
ExcludeArch:    s390
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  makeinfo
BuildRequires:  pcre-devel-static
%if 0%{?suse_version} > 1320
BuildRequires:  python3-base
%else
BuildRequires:  python-base
%endif
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

%prep
%setup -q -n %{srcname}-%{expand:%%(SV=%{srcver};echo ${SV%%%%+git*})}
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1

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
%if 0%{?suse_version} > 1320
	--python=%_bindir/python3 \
%else
	--python=%_bindir/python2 \
%endif
	--extra-cflags="%{optflags}" \
	--disable-stack-protector \
	--disable-strip \
	--without-default-devices \
	--disable-system --enable-linux-user \
	--disable-tools --disable-guest-agent \
	--static \
	--disable-modules \
	--disable-pie \
	--disable-docs \
	--audio-drv-list="" \
	--enable-attr \
	--disable-auth-pam \
	--disable-blobs \
	--disable-bluez \
	--disable-bochs \
	--disable-brlapi \
	--disable-bzip2 \
	--disable-cap-ng \
	--disable-capstone \
	--disable-cloop \
	--enable-coroutine-pool \
	--disable-curl \
	--disable-curses \
	--disable-dmg \
	--disable-fdt \
	--disable-gcrypt \
	--disable-glusterfs \
	--disable-gnutls \
	--disable-gtk \
	--disable-hax \
	--disable-hvf \
	--disable-iconv \
	--disable-jemalloc \
	--disable-kvm \
	--disable-libiscsi \
	--disable-libnfs \
	--disable-libpmem \
	--disable-libssh2 \
	--disable-libusb \
	--disable-libxml2 \
	--disable-linux-aio \
	--disable-lzfse \
	--disable-lzo \
	--disable-malloc-trim \
	--enable-membarrier \
	--disable-mpath \
	--disable-netmap \
	--disable-nettle \
	--disable-numa \
	--disable-opengl \
	--disable-parallels \
	--disable-pvrdma \
	--disable-qcow1 \
	--disable-qed \
	--disable-rbd \
	--disable-rdma \
	--disable-replication \
	--disable-sanitizers \
	--disable-sdl \
	--disable-sdl-image \
	--disable-seccomp \
	--disable-sheepdog \
	--disable-slirp \
	--disable-smartcard \
	--disable-snappy \
	--disable-spice \
	--disable-tcmalloc \
	--disable-tpm \
	--disable-usb-redir \
	--disable-vde \
	--disable-vdi \
	--disable-vhost-crypto \
	--disable-vhost-kernel \
	--disable-vhost-net \
	--disable-vhost-scsi \
	--disable-vhost-user \
	--disable-vhost-vsock \
	--disable-virglrenderer \
	--disable-virtfs \
	--disable-vnc \
	--disable-vnc-jpeg \
	--disable-vnc-png \
	--disable-vnc-sasl \
	--disable-vte \
	--disable-vvfat \
	--enable-werror \
	--disable-whpx \
	--disable-xen \
	--disable-xen-pci-passthrough \
	--disable-xfsctl \

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

%ifarch %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le s390x
%check
cd %mybuilddir
%{qemu_arch}-linux-user/qemu-%{qemu_arch} %_bindir/ls > /dev/null
make %{?_smp_mflags} check-softfloat
%endif

%install
cd %mybuilddir
make %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}%_datadir/qemu/keymaps
unlink %{buildroot}%_datadir/qemu/trace-events-all
install -d -m 755 %{buildroot}%_sbindir
install -m 755 scripts/qemu-binfmt-conf.sh %{buildroot}%_sbindir
%fdupes -s %{buildroot}

%files
%defattr(-, root, root)
%doc Changelog README VERSION
%license COPYING COPYING.LIB LICENSE
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
%_bindir/qemu-ppc64abi32
%_bindir/qemu-ppc64
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

%changelog
