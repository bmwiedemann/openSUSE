#
# spec file for package qemu
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


%include %{_sourcedir}/common.inc

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

# enforce pxe rom sizes for migration compatability from SLE 11 SP3 forward
# the following need to be > 64K
%define supported_nics_large {e1000 rtl8139}
# the following need to be <= 64K
%define supported_nics_small {virtio}
# Though not required, make unsupported pxe roms migration compatable as well
%define unsupported_nics {eepro100 ne2k_pci pcnet}

Name:           qemu
URL:            https://www.qemu.org/
Summary:        Machine emulator and virtualizer
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
Version:        9.0.1
Release:        0
Source0:        qemu-%{version}.tar.xz
Source1:        common.inc
Source303:      README.PACKAGING
Source1000:     qemu-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
## Packages we REQUIRE during build
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
%if %{with_xen}
BuildRequires:  xen-devel >= 4.2
%endif
BuildRequires:  pkgconfig(libpmem)
%endif
%ifnarch %arm s390x
BuildRequires:  libnuma-devel
%endif
%if 0%{with canokey}
BuildRequires:  canokey-qemu-devel
%endif
%if 0%{?with_daxctl}
BuildRequires:  pkgconfig(libndctl)
%endif
%if %{kvm_available}
BuildRequires:  pkgconfig(udev)
%endif
%if 0%{?with_rbd}
BuildRequires:  librbd-devel
%endif
%if 0%{with spice}
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.3
BuildRequires:  pkgconfig(spice-server) >= 0.12.5
%endif
%if 0%{?with_uring}
BuildRequires:  pkgconfig(liburing) >= %liburing_min_version
%endif
%if 0%{with xdp}
BuildRequires:  libxdp-devel
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base >= 3.8
%else
BuildRequires:  python311-Sphinx
BuildRequires:  python311-base
%endif
BuildRequires:  Mesa-devel
BuildRequires:  bison
BuildRequires:  brlapi-devel
BuildRequires:  discount
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  keyutils-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbpf-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcapstone-devel
BuildRequires:  libfdt-devel >= 1.4.2
BuildRequires:  libgcrypt-devel >= 1.8.0
BuildRequires:  lzfse-devel
BuildRequires:  meson
BuildRequires:  multipath-tools-devel
BuildRequires:  ninja >= 1.7
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
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
BuildRequires:  pkgconfig(libpipewire-0.3)
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
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(pixman-1) >= 0.21.8
BuildRequires:  pkgconfig(slirp) >= 4.2.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vdeplug)
BuildRequires:  pkgconfig(virglrenderer) >= 0.4.1
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
%{?systemd_ordering}
## Packages we will REQUIRE
%if %{kvm_available}
Requires(post): acl
Requires(post): udev
%endif
Requires(post): coreutils
Requires:       group(kvm)
Requires:       group(qemu)
Requires:       user(qemu)
# Due to change in where some documentation files are, if qemu-guest-agent
# is installed, we need to make sure we update it to our version.
Requires:       (qemu-guest-agent = %{version} if qemu-guest-agent)
## Packages we will RECOMMEND
%ifarch s390x
Recommends:     qemu-hw-s390x-virtio-gpu-ccw
%else
Recommends:     qemu-hw-display-qxl
Recommends:     qemu-hw-display-virtio-gpu
Recommends:     qemu-hw-display-virtio-gpu-pci
Recommends:     qemu-hw-display-virtio-vga
Recommends:     qemu-hw-usb-host
Recommends:     qemu-hw-usb-redirect
Recommends:     qemu-hw-usb-smartcard
%if 0%{with spice}
Recommends:     qemu-ui-spice-app
%endif
# End of "ifarch s390x"
%endif
%if %{kvm_available}
Recommends:     kvm_stat
%endif
Recommends:     qemu-block-curl
Recommends:     qemu-block-nfs
Recommends:     qemu-ksm = %{version}
Recommends:     qemu-tools
Recommends:     qemu-ui-curses
## Packages we will SUGGEST
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
Suggests:       qemu-ui-gtk
Suggests:       qemu-doc
## Packages we PROVIDE
Provides:       kvm = %{version}
Provides:       qemu-kvm = %{version}
## Pacakges we OBSOLETE (and CONFLICT)
Obsoletes:      kvm <= %{version}
Obsoletes:      qemu-audio-oss < %{version}
Obsoletes:      qemu-audio-sdl < %{version}
Obsoletes:      qemu-kvm <= %{version}
Obsoletes:      qemu-sgabios <= 8
Obsoletes:      qemu-ui-sdl < %{version}
## What we do with the main emulator depends on the architecture we're on
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
# End of "if kvm_available"
%endif

%description
%{generic_qemu_description}

This package acts as an umbrella package to the other QEMU sub-packages.

%files
%if %{kvm_available}
%ifarch s390x
%{_prefix}/lib/modules-load.d/kvm.conf
%endif
/usr/lib/udev/rules.d/80-kvm.rules
# End of "if kvm_available"
%endif
%if %{legacy_qemu_kvm}
%doc %_docdir/qemu-kvm
%_mandir/man1/qemu-kvm.1.gz
%endif
%_bindir/qemu-kvm
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
%_mandir/man1/%name.1.gz
%_mandir/man7/qemu-block-drivers.7.gz
%_mandir/man7/qemu-cpu-models.7.gz
%_mandir/man7/qemu-qmp-ref.7.gz
%_mandir/man7/qemu-ga-ref.7.gz
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
Conflicts:      %name < %{version}-%{release} \
Conflicts:      %name > %{version}-%{release} \
Conflicts:      qemu-tools < %{version}-%{release} \
Conflicts:      qemu-tools > %{version}-%{release}

%prep
%autosetup -n qemu-%{version} -p1

# We have the meson subprojects there, but as submodules (because OBS
# SCM bridge can handle the latter, but not the former) so we need to
# apply the layering of the packagefiles manually
meson subprojects packagefiles --apply berkeley-testfloat-3
meson subprojects packagefiles --apply berkeley-softfloat-3

# for the record, this set of firmware files is installed, but we don't
# build (yet): bamboo.dtb canyonlands.dtb hppa-firmware.img hppa-firmware.img 64
# openbios-ppc openbios-sparc32 openbios-sparc64 palcode-clipper petalogix-ml605.dtb
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
pxe-virtio.rom vgabios-ati.bin vgabios-bochs-display.bin \
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

%build

%define rpmfilesdir %{_builddir}/qemu-%{version}/rpm

%if %{legacy_qemu_kvm}
# FIXME: Why are we copying the s390 specific one?
cp %{rpmfilesdir}/supported.s390.txt docs/supported.rst
sed -i '/^\ \ \ about\/index.*/i \ \ \ supported.rst' docs/index.rst
%endif

# When generating an upstream release tarball, the following commands
# are run (see scripts/make-release):
#  (cd roms/seabios && git describe --tags --long --dirty > .version)
#  (cd roms/skiboot && ./make_version.sh > .version)
# This has not happened for the archive we're using, since it's cloned
# from a git branch. We, therefore, assumed that the following commands
# have been run, and the result committed to the repository (with seabios
# and skiboot at the proper commit/tag/...):
#  git -C roms/seabios describe --tags --long --dirty > rpm/seabios_version
#  (cd roms/skiboot && ./make_version.sh > ../../rpm/skiboot_version)
cp %{rpmfilesdir}/seabios_version roms/seabios/.version
cp %{rpmfilesdir}/skiboot_version roms/skiboot/.version
find . -iname ".git" -exec rm -rf {} +

mkdir -p %blddir
cd %blddir
export USER=abuild
export HOSTNAME=OBS # is used in roms/SLOF/Makefile.gen (boo#1084909)

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
EXTRA_CFLAGS="$(echo %{optflags} | sed -E 's/-[A-Z]?_FORTIFY_SOURCE[=]?[0-9]*//g') -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -Wno-error"

%srcdir/configure \
%if 0%{?suse_version} >= 1600
	--python=%_bindir/python3 \
%else
	--python=%_bindir/python3.11 \
%endif
	--docdir=%_docdir \
	--datadir=%_datadir \
	--extra-cflags="${EXTRA_CFLAGS}" \
	--firmwarepath=%_datadir/%name \
	--libdir=%_libdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--with-pkgversion="%(echo '%{distro}' | sed 's/ (.*)//')" \
	--disable-af-xdp \
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
	--disable-download \
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
	--disable-hv-balloon \
	--disable-hvf \
	--disable-iconv \
	--disable-jack \
	--disable-kvm \
	--disable-l2tpv3 \
	--disable-libdaxctl \
	--disable-libiscsi \
	--disable-libkeyutils \
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
	--disable-pipewire \
	--disable-pixman \
	--disable-plugins \
	--disable-png \
	--disable-pvrdma \
	--disable-qcow1 \
	--disable-qed \
	--disable-qom-cast-debug \
	--disable-rbd \
	--disable-rdma \
	--disable-relocatable \
	--disable-replication \
	--disable-rng-none \
	--disable-rutabaga-gfx \
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
%if 0%{?suse_version} >= 1600
	--audio-drv-list=pipewire,pa,alsa,jack,oss \
%else
	--audio-drv-list=pa,pipewire,alsa,jack,oss \
%endif
%ifarch x86_64
	--enable-avx2 \
	--enable-libpmem \
%if %{with_xen}
	--enable-xen \
	--enable-xen-pci-passthrough \
%endif
%endif
%if 0%{with xdp}
	--enable-af-xdp \
%endif
%if 0%{with canokey}
	--enable-canokey \
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
%if "%{_lto_cflags}" != "%{nil}"
	--enable-lto \
%endif
%if %{with malloc_trim}
	--enable-malloc-trim \
%endif
%if %{with system_membarrier}
	--enable-membarrier \
%endif
%ifnarch %arm s390x
	--enable-numa \
%endif
%if 0%{?with_rbd}
	--enable-rbd \
%endif
%if %{has_rutabaga_gfx}
	--enable-rutabaga-gfx \
%endif
	--enable-alsa \
	--enable-attr \
	--enable-auth-pam \
	--enable-bochs \
	--enable-bpf \
	--enable-brlapi \
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
	--enable-hv-balloon \
	--enable-iconv \
	--enable-jack \
	--enable-l2tpv3 \
	--enable-libiscsi \
	--enable-libkeyutils \
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
	--enable-pipewire \
	--enable-pixman \
	--enable-png \
	--enable-pvrdma \
	--enable-qcow1 \
	--enable-qed \
	--enable-rdma \
	--enable-relocatable \
	--enable-replication \
	--enable-seccomp \
	--enable-selinux \
	--enable-slirp \
	--enable-slirp-smbd \
	--enable-smartcard \
	--enable-snappy \
%if 0%{with spice}
	--enable-spice \
	--enable-spice-protocol \
%endif
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

echo "=== Content of config-host.mak: ==="
cat config-host.mak
echo "=== ==="

# For building QEMU and all the "default" firmwares, for each arch,
# for the package qemu, we first need to delete the firmware files that
# we intend to build...
#
# TODO: check if this can be common to qemu and qemu-linux-user
for i in %built_firmware
do
  unlink %srcdir/pc-bios/$i
done

%make_build

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

pushd %srcdir/roms/seabios/docs
for f in *.md
do
  b="${f%.md}"
  # Ensure the correct media type
  markdown "${f}" >"${b}.html"
  # Links to b.md will be rendered as to b
  ln -Ts "${b}.html" "${b}"
done
popd

# FIXME: check if we can upstream: roms-Makefile-add-cross-file-to-qboot-me.patch
# and qboot-add-cross.ini-file-to-handle-aarch.patch
%make_build -C %srcdir/roms qboot

%make_build -C %srcdir/roms seavgabios \

%make_build -C %srcdir/roms seavgabios-ati \

%make_build -C %srcdir/roms pxerom

%make_build -C %srcdir/roms edk2-basetools EXTRA_OPTFLAGS='-fPIE'
%make_build -C %srcdir/roms efirom

%if %{force_fit_virtio_pxe_rom}
pushd %srcdir
patch -p1 < %{rpmfilesdir}/openSUSE-pcbios-stub-out-the-SAN-req-s-i.patch
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
    %srcdir/roms/ipxe/src/util/padimg.pl %srcdir/pc-bios/pxe-$i.rom -s 65536 -b 255
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

%install
cd %blddir

%make_build install DESTDIR=%{buildroot}

%find_lang %name
install -d -m 0755 %{buildroot}%_datadir/%name/firmware
install -d -m 0755 %{buildroot}/usr/lib/supportconfig/plugins
install -d -m 0755 %{buildroot}%_sysconfdir/%name/firmware
install -D -m 0644 %{rpmfilesdir}/bridge.conf %{buildroot}%_sysconfdir/%name/bridge.conf
install -D -m 0755 %{rpmfilesdir}/qemu-ifup %{buildroot}%_datadir/%name/qemu-ifup
install -D -p -m 0644 %{rpmfilesdir}/80-qemu-ga.rules %{buildroot}/usr/lib/udev/rules.d/80-qemu-ga.rules
install -D -m 0755 scripts/analyze-migration.py  %{buildroot}%_bindir/analyze-migration.py
install -D -m 0755 scripts/vmstate-static-checker.py  %{buildroot}%_bindir/vmstate-static-checker.py
install -D -m 0755 scripts/kvm/vmxcap  %{buildroot}%_bindir/vmxcap
install -D -m 0755 %{rpmfilesdir}/qemu-supportconfig %{buildroot}/usr/lib/supportconfig/plugins/%name
install -D -m 0644 %{rpmfilesdir}/supported.arm.txt %{buildroot}%_docdir/qemu-arm/supported.txt
install -D -m 0644 %{rpmfilesdir}/supported.ppc.txt %{buildroot}%_docdir/qemu-ppc/supported.txt
install -D -m 0644 %{rpmfilesdir}/supported.x86.txt %{buildroot}%_docdir/qemu-x86/supported.txt
install -D -m 0644 %{rpmfilesdir}/supported.s390.txt %{buildroot}%_docdir/qemu-s390x/supported.txt

%if %{legacy_qemu_kvm}
install -D -m 0644 %{rpmfilesdir}/qemu-kvm.1.gz %{buildroot}%_mandir/man1/qemu-kvm.1.gz
install -d %{buildroot}%_docdir/qemu-kvm
# FIXME: Why do we onlly generate the HTML for the legacy package documentation?
%ifarch s390x
ln -s ../qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-s390x/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
%else
ln -s ../qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
rst2html --exit-status=2 %{buildroot}%_docdir/qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.html
# End of "ifarch s390x"
%endif
# End of "if legacy_qemu_kvm"
%endif

%ifarch aarch64 %arm %ix86 ppc ppc64 ppc64le riscv64 s390x x86_64
%ifarch ppc64le
%define qemu_arch ppc64
%endif
ln -s qemu-system-%{qemu_arch} %{buildroot}%_bindir/qemu-kvm
%endif

%if %{kvm_available}
install -D -m 0644 %{rpmfilesdir}/80-kvm.rules %{buildroot}/usr/lib/udev/rules.d/80-kvm.rules
%endif
install -D -p -m 0644 %{rpmfilesdir}/qemu-guest-agent.service %{buildroot}%{_unitdir}/qemu-guest-agent.service
install -D -p -m 0644 %{rpmfilesdir}/ksm.service %{buildroot}%{_unitdir}/ksm.service
%ifarch s390x
install -D -m 0644 %{rpmfilesdir}/kvm.conf %{buildroot}%{_prefix}/lib/modules-load.d/kvm.conf
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
install -D -m 0644 %{rpmfilesdir}/50-seabios-256k.json %{buildroot}%_datadir/%name/firmware/50-seabios-256k.json
install -D -m 0644 %{rpmfilesdir}/60-seabios-128k.json %{buildroot}%_datadir/%name/firmware/60-seabios-128k.json
install -d -m 0755 %{buildroot}%_docdir/qemu-seabios
%else
for f in %{x86_extra_firmware} ; do
  unlink %{buildroot}%_datadir/%name/$f
done
# End of "if build_x86_firmware"
%endif

%suse_update_desktop_file qemu

# Common install steps for qemu and qemu-linux-user
%fdupes -s %{buildroot}

%check
cd %blddir

# Patch 'increase x86_64 physical bits to 42' requires that the DSDT used for
# acpi [q]tests is modified too. But it's binary, and that means we cannot
# do that in the patch itself. Instead, we keep a copy of the binary in the
# package sources, and put it in place now, before the tests themselves.
# If that patch is removed, the following line needs to go as well.
cp %{rpmfilesdir}/DSDT.pcie %{srcdir}/tests/data/acpi/microvm/

# Patch 'tests/acpi: update tables for new core count test' requires some new
# binaries to be introcuded too. Let's copy them in place as well
cp %{rpmfilesdir}/APIC.core-count2 %{rpmfilesdir}/DSDT.core-count2 %{rpmfilesdir}/FACP.core-count2 %{srcdir}/tests/data/acpi/q35/

%if 0%{?qemu_user_space_build}
# Seccomp is not supported by linux-user emulation
echo 'int main (void) { return 0; }' > %{srcdir}/tests/unit/test-seccomp.c
# keyctl is not yet supported by linux-user emulation
echo 'int main (void) { return 0; }' > %{srcdir}/tests/unit/test-crypto-secret.c
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

%if 0%{with spice}
%package spice
Summary:        Modules and packages for SPICE
Group:          System/Emulators/PC
Requires:       qemu-audio-spice
Requires:       qemu-chardev-spice
Requires:       qemu-headless
Requires:       qemu-hw-display-qxl
Requires:       qemu-hw-usb-redirect
Requires:       qemu-ui-spice-core

%description spice
%{generic_qemu_description}

This meta-package brings in, as dependencies, the modules and packages
necessary for having SPICE working for your VMs.

%files spice

%package audio-spice
Summary:        Spice based audio support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-ui-spice-core = %{version}-%{release}
%{qemu_module_conflicts}

%description audio-spice
This package contains a module for Spice based audio support for QEMU.

%files audio-spice
%dir %_libdir/%name
%_libdir/%name/audio-spice.so

%package chardev-spice
Summary:        Spice vmc and port chardev support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-ui-spice-core = %{version}-%{release}
%{qemu_module_conflicts}

%description chardev-spice
This package contains a module for Spice chardev support for QEMU.

%files chardev-spice
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/chardev-spice.so

%package ui-spice-app
Summary:        Spice UI support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-chardev-spice = %{version}-%{release}
Requires:       qemu-ui-spice-core = %{version}-%{release}
%{qemu_module_conflicts}

%description ui-spice-app
This package contains a module for doing Spice based UI for QEMU.

%files ui-spice-app
%dir %_libdir/%name
%_libdir/%name/ui-spice-app.so

%package ui-spice-core
Summary:        Core Spice support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-ui-opengl
# This next Requires is only since virt-manager expects audio support
Requires:       qemu-audio-spice = %{version}-%{release}
%{qemu_module_conflicts}

%description ui-spice-core
This package contains a module with core Spice support for QEMU.

%files ui-spice-core
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/ui-spice-core.so

%package hw-display-qxl
Summary:        QXL display support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-ui-spice-core = %{version}-%{release}
%{qemu_module_conflicts}

%description hw-display-qxl
This package contains a module for QXL display support for QEMU.

%files hw-display-qxl
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-qxl.so

# End of "with spice"
%endif

%package headless
Summary:        Minimum set of packages for having a functional QEMU
Group:          System/Emulators/PC
Requires:       qemu
Requires:       qemu-block-curl
Requires:       qemu-block-nfs
Requires:       qemu-img
%if %{has_virtiofsd}
Requires:       virtiofsd
%endif
Recommends:     qemu-tools

%description headless
%{generic_qemu_description}

This meta-package brings in, as dependencies, the minimum set of packages
currently necessary for having a functional (headless) QEMU/KVM stack.

%files headless

%package x86
Summary:        Machine emulator and virtualizer for x86 architectures
Group:          System/Emulators/PC
Requires:       %name = %{version}
Requires:       qemu-accel-tcg-x86
Requires:       qemu-ipxe
Requires:       qemu-seabios
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
Requires:       %name = %{version}
Requires:       qemu-SLOF
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios

%description ppc
%{generic_qemu_description}

This package provides ppc and ppc64 emulation.

%files ppc
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
Requires:       %name = %{version}
Provides:       qemu-s390 = %{version}
Obsoletes:      qemu-s390 < %{version}

%description s390x
%{generic_qemu_description}

This package provides s390x emulation.

%files s390x
%_bindir/qemu-system-s390x
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%doc %_docdir/qemu-s390x

%package arm
Summary:        Machine emulator and virtualizer for ARM architectures
Group:          System/Emulators/PC
Requires:       %name = %{version}
Recommends:     ovmf
Recommends:     qemu-ipxe
Recommends:     qemu-uefi-aarch64
Recommends:     qemu-vgabios

%description arm
%{generic_qemu_description}

This package provides arm emulation.

%files arm
%_bindir/qemu-system-arm
%_bindir/qemu-system-aarch64
%_datadir/%name/npcm7xx_bootrom.bin
%doc %_docdir/qemu-arm

%package extra
Summary:        Machine emulator and virtualizer for "extra" architectures
Group:          System/Emulators/PC
Requires:       %name = %{version}
Recommends:     qemu-ipxe
Recommends:     qemu-skiboot
Recommends:     qemu-vgabios

%description extra
%{generic_qemu_description}

This package provides some lesser used emulations, including alpha, m68k,
mips, sparc, and xtensa. (The term "extra" is juxtapositioned against more
popular QEMU packages which are dedicated to a single architecture.)

%files extra
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
%_datadir/%name/hppa-firmware64.img
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

%description lang
This package contains a few language translations, particularly for the
graphical user interface components that come with QEMU. The bulk of strings
in QEMU are not localized.

%files lang -f %blddir/%name.lang

%package audio-alsa
Summary:        ALSA based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-alsa
This package contains a module for ALSA based audio support for QEMU.

%files audio-alsa
%dir %_libdir/%name
%_libdir/%name/audio-alsa.so

%package audio-dbus
Summary:        D-Bus based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-dbus
This package provides a module for D-Bus based audio support for QEMU.

%files audio-dbus
%dir %_libdir/%name
%_libdir/%name/audio-dbus.so

%package audio-pa
Summary:        Pulse Audio based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-pa
This package contains a module for Pulse Audio based audio support for QEMU.

%files audio-pa
%dir %_libdir/%name
%_libdir/%name/audio-pa.so

%package audio-jack
Summary:        JACK based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-jack
This package contains a module for JACK based audio support for QEMU.

%files audio-jack
%dir %_libdir/%name
%_libdir/%name/audio-jack.so

%package audio-oss
Summary:        OSS based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-oss
This package contains a module for OSS based audio support for QEMU.

%files audio-oss
%dir %_libdir/%name
%_libdir/%name/audio-oss.so

%package audio-pipewire
Summary:        Pipewire based audio support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description audio-pipewire
This package contains a module for Pipewire based audio support for QEMU.

%files audio-pipewire
%dir %_libdir/%name
%_libdir/%name/audio-pipewire.so

%package block-curl
Summary:        cURL block support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-curl
This package contains a module for accessing network-based image files over
a network connection from qemu-img tool and QEMU system emulation.

%files block-curl
%dir %_libdir/%name
%_libdir/%name/block-curl.so

%package block-dmg
Summary:        DMG block support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-dmg
This package contains a module for accessing Mac OS X image files from
qemu-img tool and QEMU system emulation.

%files block-dmg
%dir %_libdir/%name
%_libdir/%name/block-dmg-bz2.so
%_libdir/%name/block-dmg-lzfse.so

%package block-gluster
Summary:        GlusterFS block support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-gluster
This package contains a module for accessing network-based image files over a
GlusterFS network connection from qemu-img tool and QEMU system emulation.

%files block-gluster
%dir %_libdir/%name
%_libdir/%name/block-gluster.so

%package block-iscsi
Summary:        iSCSI block support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-iscsi
This package contains a module for accessing network-based image files over an
iSCSI network connection from qemu-img tool and QEMU system emulation.

%files block-iscsi
%dir %_libdir/%name
%_libdir/%name/block-iscsi.so

%package block-nfs
Summary:        direct Network File System support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-nfs
This package contains a module for directly accessing nfs based image files
for QEMU.

%files block-nfs
%dir %_libdir/%name
%_libdir/%name/block-nfs.so

%package block-ssh
Summary:        SSH (SFTP) block support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description block-ssh
This package contains a module for accessing network-based image files over an
SSH network connection from qemu-img tool and QEMU system emulation.

%files block-ssh
%dir %_libdir/%name
%_libdir/%name/block-ssh.so

%package chardev-baum
Summary:        Baum braille chardev support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description chardev-baum
This package contains a module for baum braille chardev support for QEMU.

%files chardev-baum
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/chardev-baum.so

%package hw-display-virtio-gpu
Summary:        Virtio GPU display support for QEMU
Group:          System/Emulators/PC
# Make sure that VGA is pretty much always there. Technically, this isn't
# really necessary (and/or, should be dealt with in other places) but it
# makes it easier to deal with strange situation where, e.g., GRUB is
# configured to work only with a graphical terminal (see bsc#1219164),
# and the hw-display-virtio-vga package is small enough, anyway.
Requires:       qemu-hw-display-virtio-vga = %{version}-%{release}
%{qemu_module_conflicts}

%description hw-display-virtio-gpu
This package contains a module for Virtio GPU display support for QEMU.

%files hw-display-virtio-gpu
%dir %_datadir/%name
%_libdir/%name/hw-display-virtio-gpu.so
%_libdir/%name/hw-display-virtio-gpu-gl.so

%package hw-display-virtio-gpu-pci
Summary:        Virtio-gpu pci device for QEMU
Group:          System/Emulators/PC
Requires:       qemu-hw-display-virtio-gpu = %{version}-%{release}
%{qemu_module_conflicts}

%description hw-display-virtio-gpu-pci
This package contains a module providing the virtio gpu pci device for QEMU.

%files hw-display-virtio-gpu-pci
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-gpu-pci.so
%_libdir/%name/hw-display-virtio-gpu-pci-gl.so

%package hw-display-virtio-vga
Summary:        Virtio vga device for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description hw-display-virtio-vga
This package contains a module providing the virtio vga device for QEMU.

%files hw-display-virtio-vga
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-display-virtio-vga.so
%_libdir/%name/hw-display-virtio-vga-gl.so

%package hw-s390x-virtio-gpu-ccw
Summary:        S390x virtio-gpu ccw device for QEMU
Group:          System/Emulators/PC
Requires:       qemu-hw-display-virtio-gpu = %{version}-%{release}
%{qemu_module_conflicts}

%description hw-s390x-virtio-gpu-ccw
This package contains a module providing the s390x virtio gpu ccw device for
QEMU.

%files hw-s390x-virtio-gpu-ccw
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-s390x-virtio-gpu-ccw.so

%package hw-usb-redirect
Summary:        USB redirection support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description hw-usb-redirect
This package contains a module for USB redirection support for QEMU.

%files hw-usb-redirect
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-redirect.so

%package hw-usb-smartcard
Summary:        USB smartcard support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description hw-usb-smartcard
This package contains a modules for USB smartcard support for QEMU.

%files hw-usb-smartcard
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-smartcard.so

%package hw-usb-host
Summary:        USB passthrough driver support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description hw-usb-host
This package contains a modules for USB passthrough driver for QEMU.

%files hw-usb-host
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/hw-usb-host.so

%package ui-dbus
Summary:        D-Bus based UI support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description ui-dbus
This package contains a module for doing D-Bus based UI for QEMU.

%files ui-dbus
%dir %_libdir/%name
%_libdir/%name/ui-dbus.so

%package ui-curses
Summary:        Curses based UI support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description ui-curses
This package contains a module for doing curses based UI for QEMU.

%files ui-curses
%dir %_libdir/%name
%_libdir/%name/ui-curses.so

%package ui-gtk
Summary:        GTK based UI support for QEMU
Group:          System/Emulators/PC
Requires:       qemu-ui-opengl
Supplements:    (qemu and libgtk-3-0)
%{qemu_module_conflicts}

%description ui-gtk
This package contains a module for doing GTK based UI for QEMU.

%files ui-gtk
%dir %_libdir/%name
%_libdir/%name/ui-gtk.so

%package ui-opengl
Summary:        OpenGL based UI support for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description ui-opengl
This package contains a module for doing OpenGL based UI for QEMU.

%files ui-opengl
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/ui-egl-headless.so
%_libdir/%name/ui-opengl.so

%package vhost-user-gpu
Summary:        Vhost user mode virtio-gpu 2D/3D rendering backend for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description vhost-user-gpu
This package contains a vhost user mode virtio-gpu 2D/3D rendering backend for
QEMU.

%files vhost-user-gpu
%dir %_datadir/%name/vhost-user
%_datadir/%name/vhost-user/50-qemu-gpu.json
%_libexecdir/vhost-user-gpu

%package img
Summary:        QEMU disk image utility
Group:          System/Emulators/PC

%description img
This package provides command line tools for manipulating disk images.

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_bindir/qemu-storage-daemon
%_mandir/man1/qemu-img.1.gz
%_mandir/man8/qemu-nbd.8.gz
%_mandir/man1/qemu-storage-daemon.1.gz
%_mandir/man7/qemu-storage-daemon-qmp-ref.7.gz

%package pr-helper
Summary:        QEMU persistent reservation helper
Group:          System/Emulators/PC

%description pr-helper
This package provides a helper utility for SCSI persistent reservations.

%files pr-helper
%_bindir/qemu-pr-helper
%_mandir/man8/qemu-pr-helper.8.gz

%package tools
Summary:        Tools for QEMU
Group:          System/Emulators/PC
Requires(pre):  permissions
Requires:       qemu-img
Requires:       qemu-pr-helper
Requires:       group(kvm)
%if %{has_virtiofsd}
Requires:       virtiofsd
%endif
Recommends:     multipath-tools
Recommends:     qemu-block-curl
%if 0%{?with_rbd}
Recommends:     qemu-block-rbd
%endif

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper, ivshmem, disk utilities and scripts for various purposes.

%files tools
%_bindir/analyze-migration.py
%_bindir/qemu-edid
%_bindir/qemu-keymap
%_bindir/vmstate-static-checker.py
%_bindir/vmxcap
%verify(not mode) %attr(4750,root,kvm) %_libexecdir/qemu-bridge-helper
%_libexecdir/virtfs-proxy-helper
%_mandir/man1/virtfs-proxy-helper.1.gz
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/bridge.conf

%post tools
%set_permissions %_libexecdir/qemu-bridge-helper

%verifyscript tools
%verify_permissions %_libexecdir/qemu-bridge-helper

%package ivshmem-tools
Summary:        Inter-VM Shared Memory Tools for QEMU
Group:          System/Emulators/PC

%description ivshmem-tools
This package contains a sample shared memory client and server which utilize
QEMU's Inter-VM shared memory device as specified by the ivshmem client-server
protocol specification documented in docs/specs/ivshmem-spec.txt in QEMU source
code.

%files ivshmem-tools
%dir %_datadir/%name
%_bindir/ivshmem-client
%_bindir/ivshmem-server

%package guest-agent
Summary:        Guest agent for QEMU
Group:          System/Emulators/PC
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
Requires(pre):  coreutils
Requires(post): coreutils

%description ksm
Kernel Samepage Merging (KSM) is a memory-saving de-duplication feature, that
merges anonymous (private) pages (not pagecache ones).

This package provides a service file for starting and stopping KSM.

%files ksm
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
%{qemu_module_conflicts}

%description accel-tcg-x86
TCG is the QEMU binary translator, responsible for converting from target to
host instruction set.

This package provides the TCG accelerator for QEMU.

%files accel-tcg-x86
%dir %_datadir/%name
%dir %_libdir/%name
%_libdir/%name/accel-tcg-i386.so
%_libdir/%name/accel-tcg-x86_64.so

%package accel-qtest
Summary:        QTest accelerator for QEMU
Group:          System/Emulators/PC
%{qemu_module_conflicts}

%description accel-qtest
QTest is a device emulation testing framework. It is useful to test device
models.

This package provides QTest accelerator for testing QEMU.

%files accel-qtest
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
%{qemu_module_conflicts}

%description block-rbd
This package contains a module for accessing ceph (rbd,rados) image files
for QEMU.

%files block-rbd
%dir %_libdir/%name
%_libdir/%name/block-rbd.so
# End of "if with_rbd"
%endif

%if %{build_ppc_firmware}
%package SLOF
Summary:        Slimline Open Firmware - SLOF
Group:          System/Emulators/PC
BuildArch:      noarch

%description SLOF
Slimline Open Firmware (SLOF) is an implementation of the IEEE 1275 standard.
It can be used as partition firmware for pSeries machines running on QEMU or KVM.

%files SLOF
%dir %_datadir/%name
%_datadir/%name/slof.bin

%package skiboot
Summary:        OPAL firmware (aka skiboot), used in booting OpenPOWER systems
Group:          System/Emulators/PC
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description skiboot
Provides OPAL (OpenPower Abstraction Layer) firmware, aka skiboot, as
traditionally packaged with QEMU.

%files skiboot
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
BuildArch:      noarch

%description microvm
This package provides minimal x86 firmware for booting certain guests under
QEMU. qboot provides the minimum resources needed to boot PVH and bzImages.
bios-microvm, created from a minimal seabios configuration, provides slightly
wider support than qboot, but still focuses on quick boot up.

%files microvm
%dir %_datadir/%name
%_datadir/%name/bios-microvm.bin
%_datadir/%name/qboot.rom

%package seabios
Summary:        x86 Legacy BIOS for QEMU
Group:          System/Emulators/PC
Version:        9.0.1%{sbver}
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description seabios
SeaBIOS is an open source implementation of a 16bit x86 BIOS. SeaBIOS
is the default and legacy BIOS for QEMU.

%files seabios
%dir %_datadir/%name
%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin
%_datadir/%name/firmware/50-seabios-256k.json
%_datadir/%name/firmware/60-seabios-128k.json
%license roms/seabios/COPYING
%doc %_docdir/qemu-seabios

%package vgabios
Summary:        VGA BIOSes for QEMU
Group:          System/Emulators/PC
Version:        9.0.1%{sbver}
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description vgabios
VGABIOS provides the video ROM BIOSes for the following variants of VGA
emulated devices: Std VGA, QXL, Cirrus CLGD 5446 and VMware emulated
video card. For use with QEMU.

%files vgabios
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
%license roms/seabios/COPYING

%package ipxe
Summary:        PXE ROMs for QEMU NICs
Group:          System/Emulators/PC
Version:        9.0.1
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description ipxe
Provides Preboot Execution Environment (PXE) ROM support for various emulated
network adapters available with QEMU.

%files ipxe
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

%package doc
Summary:        Documentation for QEMU
Group:          System/Emulators/PC
BuildArch:      noarch
Suggests:       qemu

%files doc
%doc %_docdir/%name

%description doc
%{generic_qemu_description}

This package contains user and developer documentation for QEMU.

%changelog
