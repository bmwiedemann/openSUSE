#
# spec file for package qemu-linux-user
#
# Copyright (c) 2025 SUSE LLC
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
Version:        10.0.2
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
BuildRequires:  pcre2-devel-static
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
%ifnarch %ix86 armv7hl
%_bindir/qemu-aarch64
%_bindir/qemu-aarch64_be
%_bindir/qemu-alpha
%_bindir/qemu-hppa
%_bindir/qemu-loongarch64
%_bindir/qemu-mips64
%_bindir/qemu-mips64el
%_bindir/qemu-mipsn32
%_bindir/qemu-mipsn32el
%_bindir/qemu-ppc64
%_bindir/qemu-ppc64le
%_bindir/qemu-riscv64
%_bindir/qemu-s390x
%_bindir/qemu-sparc32plus
%_bindir/qemu-sparc64
%_bindir/qemu-x86_64
%endif
%_bindir/qemu-arm
%_bindir/qemu-armeb
%_bindir/qemu-hexagon
%_bindir/qemu-m68k
%_bindir/qemu-microblaze
%_bindir/qemu-microblazeel
%_bindir/qemu-mips
%_bindir/qemu-mipsel
%_bindir/qemu-or1k
%_bindir/qemu-ppc
%_bindir/qemu-riscv32
%_bindir/qemu-sh4
%_bindir/qemu-sh4eb
%_bindir/qemu-sparc
%_bindir/qemu-i386
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
	%{disable_everything} \
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

echo "######## Soft Float tests ########"
%make_build check-softfloat

%changelog
