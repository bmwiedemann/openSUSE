#
# spec file for package qemu-linux-user
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

%ifarch %ix86 x86_64 s390x
%define legacy_qemu_kvm 1
%endif

Name:           qemu-linux-user
URL:            https://www.qemu.org/
Summary:        CPU emulator for user space
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
Version:        9.0.1
Release:        0
Source0:        qemu-%{version}.tar.xz
Source1:        common.inc
Source200:      qemu-rpmlintrc
Source303:      README.PACKAGING
Source1000:     qemu-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  glib2-devel-static >= 2.56
BuildRequires:  glibc-devel-static
BuildRequires:  (pcre-devel-static if glib2-devel-static < 2.73 else pcre2-devel-static)
# passing filelist check for /usr/lib/binfmt.d
BuildRequires:  systemd
BuildRequires:  zlib-devel-static
# we must not install the qemu-linux-user package when under QEMU build
%if 0%{?qemu_user_space_build:1}
#!BuildIgnore:  post-build-checks
%endif
BuildRequires:  discount
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja >= 1.7
%if 0%{?suse_version} >= 1600
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base >= 3.8
%else
BuildRequires:  python311-Sphinx
BuildRequires:  python311-base
%endif

%description
QEMU provides CPU emulation along with other related capabilities. This package
provides programs to run user space binaries and libraries meant for another
architecture. The syscall interface is intercepted and execution below the
syscall layer occurs on the native hardware and operating system.

%files
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

%prep
%autosetup -n qemu-%{version} -p1

# We have the meson subprojects there, but as submodules (because OBS
# SCM bridge can handle the latter, but not the former) so we need to
# apply the layering of the packagefiles manually
meson subprojects packagefiles --apply berkeley-testfloat-3
meson subprojects packagefiles --apply berkeley-softfloat-3

%build

%define rpmfilesdir %{_builddir}/qemu-%{version}/rpm

%if %{legacy_qemu_kvm}
# FIXME: Why are we copying the s390 specific one?
cp %{rpmfilesdir}/supported.s390.txt docs/supported.rst
sed -i '/^\ \ \ about\/index.*/i \ \ \ supported.rst' docs/index.rst
%endif

find . -iname ".git" -exec rm -rf {} +

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
%if %{with system_membarrier}
	--enable-membarrier \
%endif
%if %{with malloc_trim}
	--enable-malloc-trim \
%endif
%if "%{_lto_cflags}" != "%{nil}"
	--enable-lto \
%endif
	--disable-install-blobs \
	--enable-attr \
	--enable-coroutine-pool \
	--enable-linux-user \
	--enable-selinux \
	--enable-tcg \
	--static

echo "=== Content of config-host.mak: ==="
cat config-host.mak
echo "=== ==="

%make_build

%install
cd %blddir

%make_build install DESTDIR=%{buildroot}

rm -rf %{buildroot}%_datadir/qemu/keymaps
unlink %{buildroot}%_datadir/qemu/trace-events-all
install -d -m 755 %{buildroot}%_sbindir
install -m 755 scripts/qemu-binfmt-conf.sh %{buildroot}%_sbindir
install -d -m 755 %{buildroot}%{_prefix}/lib/binfmt.d/
scripts/qemu-binfmt-conf.sh --systemd ALL --persistent yes --preserve-argv0 yes --exportdir %{buildroot}%{_prefix}/lib/binfmt.d/

%fdupes -s %{buildroot}

%check
cd %blddir

%ifarch aarch64 %ix86 ppc ppc64 ppc64le riscv64 s390x x86_64
./qemu-%{qemu_arch} %_bindir/ls > /dev/null
%endif

%make_build check-softfloat

%changelog
