#
# spec file for package libguestfs
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Michal Hrusecky <mhrusecky@novell.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# needsbinariesforbuild


Version:        1.42.0
Release:        0
%{ocaml_preserve_bytecode}

%bcond_without ocaml_bindings
%bcond_without lua_bindings
%bcond_without python_bindings
%bcond_without perl_bindings
%bcond_without hivex

%bcond_without fuse

%bcond_without ruby_bindings

%bcond_with p2v

%bcond_without bash_completion
# The following defines are overridden in the individual subpackages
%define _configure_fuse --disable-fuse
%define _configure_lua --disable-lua
%define _configure_ocaml --disable-ocaml
%define _configure_perl --disable-perl
%define _configure_python --disable-python
%define _configure_ruby --disable-ruby

%define udevrulesdir /usr/lib/udev/rules.d
#
# use 'env LIBGUESTFS_HV=/path/to/kvm libguestfs-test-tool' to verify
%define kvm_binary /bin/false
%ifarch aarch64
%define kvm_binary /usr/bin/qemu-system-aarch64
%endif
%ifarch ppc64le
%define kvm_binary /usr/bin/qemu-system-ppc64
%endif
%ifarch ppc64
%define kvm_binary /usr/bin/qemu-system-ppc64
%endif
%ifarch s390x
%define kvm_binary /usr/bin/qemu-system-s390x
%endif
%ifarch x86_64
%define kvm_binary /usr/bin/qemu-system-x86_64
%endif
#
%define guestfs_docdir %{_defaultdocdir}/%{name}
#
Name:           libguestfs
%if "%{?_ignore_exclusive_arch}" == ""
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64
%endif
BuildRequires:  aaa_base
BuildRequires:  attr-devel
BuildRequires:  augeas-devel >= 1.0.0
BuildRequires:  autoconf
BuildRequires:  automake
%if %{with bash_completion}
BuildRequires:  bash-completion >= 2.0
%if 0%{?suse_version} >= 1330
BuildRequires:  bash-completion-devel >= 2.0
%endif
%endif
BuildRequires:  bison
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  libvirt-devel >= 1.2.20
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libtirpc)
%if %{with perl_bindings}
BuildRequires:  perl(Module::Build)
%endif
BuildRequires:  db48-utils
BuildRequires:  dhcp-client
BuildRequires:  libjansson-devel
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  qemu-tools
BuildRequires:  readline-devel
BuildRequires:  supermin >= 5.1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(yajl) >= 2.0.4
# Required to build tools, its independent from bindings
BuildRequires:  glib2-devel
BuildRequires:  ocaml >= 4.01
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-gettext-devel
BuildRequires:  ocaml-gettext-stub-devel
BuildRequires:  ocaml-hivex-devel
BuildRequires:  ocaml-libvirt-devel

#
BuildRequires:  ocaml-rpm-macros >= 4.03
%if %{with ocaml_bindings}
%define _configure_ocaml --enable-ocaml
%endif
#
%if %{with fuse}
BuildRequires:  fuse-devel
%define _configure_fuse --enable-fuse
%endif
#
%if %{with hivex}
BuildRequires:  glibc-locale
BuildRequires:  hivex
BuildRequires:  hivex-devel
%endif
#
%if %{with p2v}
BuildRequires:  gtk2-devel
%endif
#
Url:            http://libguestfs.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Compatibility package for guestfs-tools
# Upstream patches
License:        GPL-2.0-only
Group:          System/Filesystems
Patch1:         31e6b187-po-Remove-virt-v2v-related-dependency-from-POTFILES-ml..patch
Patch2:         7265f08c-lib-remove-extra-LIBS-from-pkg-config-file.patch

# Pending upstram review
Patch50:        0001-Introduce-a-wrapper-around-xmlParseURI.patch
Patch51:        0002-common-extract-UTF-8-conversion-function.patch
Patch52:        0003-inspector-rpm-summary-and-description-may-not-be-utf.patch
# Our patches
Patch100:       appliance.patch
Patch101:       netconfig.patch

Source0:        http://download.libguestfs.org/1.42-stable/libguestfs-%{version}.tar.gz
Source3:        libguestfs.rpmlintrc
Source100:      mount-rootfs-and-chroot.sh
Source101:      README
Source789653:   Pod-Simple-3.23.tar.xz
#
Source10001:    libguestfs.test.simple.run-libugestfs-test-tool.sh
Source10002:    libguestfs.test.simple.create-opensuse-guest.sh
Source10003:    libguestfs.test.simple.create-opensuse-guest-crypt-on-lvm.sh
Source10004:    libguestfs.test.simple.create-sles12-guest.sh
Source10005:    libguestfs.test.simple.create-sles12-guest-crypt-on-lvm.sh

#
Requires:       guestfs-tools
Requires:       lvm2
Requires:       virt-v2v = %{version}

%description
libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images. You can use this for viewing and editing files inside guests,
scripting changes to VMs, monitoring disk used/free statistics, P2V, V2V,
performing partial backups, cloning VMs, and much else besides.

%package -n guestfs-tools
Summary:        Tools for accessing and modifying virtual machine disk images
License:        GPL-2.0-only
Group:          System/Filesystems
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Requires:       libguestfs0 = %{version}
Requires:       python3-evtx
%if %{with bash_completion}
Recommends:     bash-completion >= 2.0
%endif
%if %{with perl_bindings}
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(Locale::TextDomain)
Requires:       perl(Pod::Usage)
Requires:       perl(String::ShellQuote)
Requires:       perl(Sys::Guestfs)
%{perl_requires}
%if %{with hivex}
Requires:       perl(Win::Hivex)
Requires:       perl(Win::Hivex::Regedit)
%endif
%endif

%if %{with fuse}
Requires:       fuse
%endif

# For virt-builder
Requires:       curl
Requires:       gpg2
Requires:       xz
Conflicts:      libguestfs0 < %{version}

%description -n guestfs-tools
libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images. You can use this for viewing and editing files inside guests,
scripting changes to VMs, monitoring disk used/free statistics, P2V, V2V,
performing partial backups, cloning VMs, and much else besides.

libguestfs can access nearly any type of filesystem including: all known types
of Linux filesystem (ext2/3/4, XFS, btrfs etc), any Windows filesystem (VFAT
and NTFS), any Mac OS X and BSD filesystems, LVM2 volume management, MBR and
GPT disk partitions, raw disks, qcow2, VirtualBox VDI, VMWare VMDK, CD and DVD
ISOs, SD cards, and dozens more. libguestfs doesn't need root permissions.

All this functionality is available through a convenient shell called
guestfish, or use virt-rescue to get a rescue shell for fixing unbootable
virtual machines.

%package -n guestfsd
Summary:        Daemon for the libguestfs appliance
License:        GPL-2.0-only
Group:          System/Filesystems
Conflicts:      libaugeas0 < 1.0.0

%description -n guestfsd
guestfsd runs within the libguestfs appliance. It receives commands from the host
and performs the requested action by calling the helper binaries.
This package is only required for building the appliance.

#
%if %{with ocaml_bindings}
%package -n ocaml-libguestfs
Summary:        OCaml bindings for libguestfs
#
License:        GPL-2.0-only
Group:          Development/Languages/OCaml

%description -n ocaml-libguestfs
Allows OCaml scripts to directly use libguestfs.

%package -n ocaml-libguestfs-devel
Summary:        Development files for libguesfs OCaml bindings
License:        GPL-2.0-only
Group:          Development/Languages/OCaml

%description -n ocaml-libguestfs-devel
Allows OCaml scripts to directly use libguestfs.
%endif
#
%if %{with perl_bindings}
%package -n perl-Sys-Guestfs
Summary:        Perl bindings for libguestfs
License:        GPL-2.0-only
Group:          Development/Languages/Perl
BuildRequires:  perl
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Sys::Virt)
%if %{with hivex}
BuildRequires:  perl(Win::Hivex)
BuildRequires:  perl(Win::Hivex::Regedit)
%endif
%define _configure_perl --enable-perl
#
Provides:       libguestfs-perl = %{version}
Obsoletes:      libguestfs-perl < %{version}
Requires:       perl(File::Temp)
Requires:       perl(Locale::TextDomain)
%perl_requires

%description -n perl-Sys-Guestfs
Allows Perl scripts to directly use libguestfs.
%endif
#
%if %{with lua_bindings}
%package -n lua-libguestfs
Summary:        Lua bindings for libguestfs
License:        GPL-2.0-only
Group:          Development/Languages/Lua
BuildRequires:  lua-devel
%define _configure_lua --enable-lua
#

%description -n lua-libguestfs
Allows lua scripts to directly use libguestfs.
%endif
#

%if %{with python_bindings}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%package -n python2-libguestfs
Summary:        Python 2 bindings for libguestfs
License:        GPL-2.0-only
Group:          Development/Languages/Python
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
%define _configure_python --enable-python
#
Obsoletes:      libguestfs-python < %{version}
Obsoletes:      python-libguestfs < %{version}
Provides:       python-libguestfs = %{version}

%description -n python2-libguestfs
Allows Python 2 scripts to directly use libguestfs.

%package -n python3-libguestfs
Summary:        Python 3 bindings for libguestfs
License:        GPL-2.0-only
Group:          Development/Languages/Python
BuildRequires:  python3
BuildRequires:  python3-devel
%define _configure_python --enable-python
#
Obsoletes:      libguestfs-python < %{version}
Obsoletes:      python-libguestfs < %{version}
Provides:       python-libguestfs = %{version}

%description -n python3-libguestfs
Allows Python 3 scripts to directly use libguestfs.
%endif
#
%if %{with ruby_bindings}
%package -n rubygem-libguestfs
Summary:        Ruby bindings for libguestfs
License:        GPL-2.0-only
Group:          Development/Languages/Ruby
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
%define _configure_ruby --enable-ruby
#

%description -n rubygem-libguestfs
Allows Ruby scripts to directly use libguestfs.
%endif

%package test
Summary:        Testcases for libguestfs
License:        GPL-2.0-only
Group:          Development/Tools/Other
Requires:       %{name}

%description test
This package contains testcases to verify libguestfs functionality.

%package -n guestfs-data
BuildRequires:  augeas-lenses
BuildRequires:  bc
BuildRequires:  btrfsprogs
BuildRequires:  bzip2
BuildRequires:  coreutils
BuildRequires:  cpio
BuildRequires:  cryptsetup
BuildRequires:  diffutils
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  gawk
%if 0%{?suse_version} >= 1500
BuildRequires:  mkisofs
%else
BuildRequires:  cdrkit-cdrtools-compat
BuildRequires:  genisoimage
%endif
BuildRequires:  glibc
BuildRequires:  gptfdisk
BuildRequires:  grep
BuildRequires:  gzip
BuildRequires:  initviocons
BuildRequires:  iproute2
BuildRequires:  jfsutils
BuildRequires:  lvm2
BuildRequires:  mdadm
BuildRequires:  module-init-tools
BuildRequires:  ncurses-utils
BuildRequires:  nfs-client
BuildRequires:  ntfs-3g
BuildRequires:  ntfsprogs
BuildRequires:  pam-config
BuildRequires:  parted
BuildRequires:  pciutils
BuildRequires:  pciutils-ids
BuildRequires:  psmisc
BuildRequires:  reiserfs
BuildRequires:  rsync
BuildRequires:  sg3_utils
BuildRequires:  strace
%ifarch %ix86 x86_64
BuildRequires:  syslinux
%endif
BuildRequires:  ldmtool
BuildRequires:  systemd-sysvinit
BuildRequires:  tar
BuildRequires:  terminfo-base
BuildRequires:  tunctl
BuildRequires:  udev
BuildRequires:  util-linux
BuildRequires:  util-linux-lang
BuildRequires:  xfsprogs
BuildRequires:  xz
BuildRequires:  pkgconfig(systemd)

# Needed by guestfsd which is burried in the appliance
#
# The problem with this design is that rpm can't find the
# library dependencies from the guestfsd hidden in the
# daemon.tar.gz tarball.Supermin will compute an appliance
# at runtime based on the packages it will find on the host.
# Thus if there is no libaugeas, libhivex, etc on the host,
# the appliance will fail to start the guestfsd.
Requires:       augeas
Requires:       augeas-lenses
Requires:       libaugeas0
Requires:       libcap2
Requires:       libhivex0
Requires:       libpcre1

# For core disk features
Requires:       qemu-tools

# Optional packages that could be picked up by supermin
Recommends:     btrfsprogs
Recommends:     dosfstools
Recommends:     e2fsprogs
Recommends:     cryptsetup
Recommends:     gptfdisk
Recommends:     jfsutils
Recommends:     reiserfs
Recommends:     xfsprogs
Recommends:     mdadm
Recommends:     parted
Recommends:     zerofree
%if 0%{?suse_version} >= 1500
Recommends:     mkisofs
%else
Recommends:     genisoimage
%endif
Recommends:     ldmtool
%if ! 0%{?is_opensuse}
Recommends:     guestfs-winsupport
%endif

Summary:        Virtual machine needed for libguestfs
License:        GPL-2.0-only
Group:          System/Filesystems
Provides:       libguestfs-data = %{version}
Obsoletes:      libguestfs-data < %{version}

%description -n guestfs-data
libguestfs needs for it's run a virtual machine image.
This package provides such an image, an initrd and a kernel.

%if ! 0%{?is_opensuse}
%package -n guestfs-winsupport
Summary:        Windows guest support in libguestfs
License:        GPL-2.0-or-later
Group:          System/Filesystems
Requires:       libguestfs >= 1.32
BuildRequires:  ntfs-3g
BuildRequires:  ntfsprogs
BuildRequires:  rsync

%description -n guestfs-winsupport
Provides the needed pieces for libguestfs to handle Windows guests.

%endif

%package devel
Summary:        Development files for libguestfs
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libguestfs0 = %{version}

%description devel
Development files for libguestfs.

libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images. You can use this for viewing and editing files inside guests,
scripting changes to VMs, monitoring disk used/free statistics, P2V, V2V,
performing partial backups, cloning VMs, and much else besides.

%package -n libguestfs0
Summary:        Runtime library of libguestfs
License:        LGPL-2.1-only
Group:          System/Libraries
Requires:       %{kvm_binary}
Requires:       db48-utils
Requires:       guestfs-data >= %{version}
Requires:       qemu >= 2.0
Requires:       qemu-tools
Requires:       supermin >= 5.1.6

%description -n libguestfs0
Library for libguestfs.

libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images. You can use this for viewing and editing files inside guests,
scripting changes to VMs, monitoring disk used/free statistics, P2V, V2V,
performing partial backups, cloning VMs, and much else besides.

libguestfs can access nearly any type of filesystem including: all known types
of Linux filesystem (ext2/3/4, XFS, btrfs etc), any Windows filesystem (VFAT
and NTFS), any Mac OS X and BSD filesystems, LVM2 volume management, MBR and
GPT disk partitions, raw disks, qcow2, VirtualBox VDI, VMWare VMDK, CD and DVD
ISOs, SD cards, and dozens more. libguestfs doesn't need root permissions.

All this functionality is available through a convenient shell called
guestfish, or use virt-rescue to get a rescue shell for fixing unbootable
virtual machines.


%package -n virt-v2v
Summary:        Convert a virtual machine to run on KVM
License:        GPL-2.0-only
Group:          System/Management
Requires:       libguestfs0 = %{version}
Requires:       qemu-block-ssh
# Conflicts with the old perl version
Conflicts:      virt-v2v <= 0.9.1

%description -n virt-v2v
virt-v2v is a tool for converting and importing virtual machines to
libvirt-managed KVM. It can import a variety of guest operating systems
from libvirt-managed hosts.

%if %{with p2v}
%package -n virt-p2v
Summary:        Convert a physical machine to run on KVM
License:        GPL-2.0-only
Group:          System/Management
Requires:       gawk
Requires:       virt-v2v = %{version}

%description -n virt-p2v
virt-p2v is a tool for converting physical machines into libvirt-managed KVM machines.
It can import a variety of guest operating systems from libvirt-managed hosts.
%endif

%prep
: _ignore_exclusive_arch '%{?_ignore_exclusive_arch}'
%setup -q -a 789653
%patch1 -p1
%patch2 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch100 -p1
%patch101 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
bison --version
# [Bug 789653] sles11 perl obsoletes perl-Pod-Simple unconditionally
export PERLLIB=`echo $PWD/Pod-Simple-*/lib`
# disable qemu test.
# If the package is built within kvm the configure test will fail because it starts kvm within kvm
# With QEMU in environment qemu and kvm packages are not needed at build time.
# With SUPERMIN and SUPERMIN_HELPER in environment, supermin package is not needed at build time.
export vmchannel_test=no
export QEMU="%{kvm_binary}"
export SUPERMIN=supermin
export SUPERMIN_HELPER=supermin-helper
# for configure macro below
export CFLAGS="%{optflags} -Wno-unused"
export CXXFLAGS="%{optflags} -Wno-unused"
autoreconf -fi

#
%configure \
	--help || :

if python --version && ! pkg-config python
then
	export PYTHON_LIBS="-lpython`python -c 'import distutils.sysconfig; print (distutils.sysconfig.get_python_version ());'`"
	export PYTHON_CFLAGS="-I`python -c 'import distutils.sysconfig; print (distutils.sysconfig.get_python_inc ());'`"
	export PYTHON_EXT_SUFFIX=.so
fi

#sed -i '1 s@^.*@#!/bin/sh -x@' configure
%configure \
	--docdir=%{guestfs_docdir} \
	--enable-daemon \
	--enable-install-daemon \
	--with-qemu=$QEMU \
	--without-java \
	--with-supermin-packager-config="$PWD/zypper.priv.conf --use-installed --verbose" \
	--disable-haskell \
	--disable-php \
	%{_configure_fuse} \
	%{_configure_lua} \
	%{_configure_ocaml} \
	%{_configure_perl} \
	%{_configure_python} \
	%{_configure_ruby} \
	--disable-rpath \
	--disable-static \
    --with-distro=SUSE
#Workaround an autotools bug
make -j1 -C builder index-parse.c
# 'INSTALLDIRS' ensures that perl libs are installed in the vendor dir instead of the site dir
make \
	INSTALLDIRS=vendor \
	LD_RUN_PATH= \
	%{?_smp_mflags}

%install
%makeinstall \
	INSTALLDIRS=vendor \
	udevrulesdir=%{udevrulesdir}
find %{buildroot} -ls
mkdir -p %{buildroot}/%{_datadir}/guestfs
cp -avLt %{buildroot}/%{_datadir}/guestfs \
	%{S:10005} \
	%{S:10004} \
	%{S:10003} \
	%{S:10002} \
	%{S:10001}
chmod 0755 %{buildroot}/%{_datadir}/guestfs/*
#remove ocaml bindings files if they are disable via rpm macro
%if !%{with ocaml_bindings}
rm -rfv %{buildroot}/%{_libdir}/ocaml
%endif
rm -rfv %{buildroot}/%{guestfs_docdir}
rm -rfv %{buildroot}/etc/libguestfs-tools.conf
find %{buildroot}/ -type f \( \
	-name "virt-list-filesystems" -o -name "virt-list-filesystems.*" -o \
	-name "virt-list-partitions" -o -name "virt-list-partitions.*" -o \
	-name "virt-tar" -o -name "virt-tar.*" \
	\) -print -delete
%if %{with perl_bindings}
# Delete empty perl bootstrap files
find %{buildroot}/ -name "*.bs" -size 0c -print -delete
%perl_process_packlist
%perl_gen_filelist
# the macro above packages everything, here only the perl files are desrired
grep "%perl_vendorarch/" %{name}.files | tee t
mv t %{name}.files
%endif

%if %{with python_bindings}
pushd python
sed -i -e "s:libraries=:library_dirs=['%{buildroot}/%{_libdir}'], libraries=:" setup.py
make stamp-extra-files
# Build needs libguestfs library to be installed

# HACKY! Change config.h for python2
echo '#define HAVE_PYSTRING_ASSTRING 1' >> config.h
%python2_build
%python2_install

# HACKY! Change config.h for python3
sed 's/\(#define HAVE_PYSTRING_ASSTRING 1\)/\/* \1 *\//' -i config.h
%python3_build
%python3_install
popd
%endif

# Don't package the test harness (yet)
rm -rf  %{buildroot}/%{_libdir}/ocaml/v2v_test_harness

#
find %{buildroot}/ -name "*.la" -print -delete
rm -fv %{buildroot}/%{_libdir}/*.a
#
touch %{name}.lang
%find_lang %{name}

# Appliance NTFS files
%if 0%{?is_opensuse}
mkdir -p %{buildroot}/tmp/etc/alternatives
pushd %{buildroot}/tmp/etc/alternatives
ln -s /sbin/mount.ntfs-3g mount.ntfs
popd
pushd %{buildroot}/tmp
tar -czf %{buildroot}/%{_libdir}/guestfs/supermin.d/zz-ntfs-symlink.tar.gz etc
popd
rm -rf %{buildroot}/tmp
%else
# Just copy the content of the ntfs packages
mkdir winsupport
for pkg in $(rpm -qa | grep ntfs); do
    rpm -ql $pkg > $pkg.list
    rsync -av --files-from $pkg.list / winsupport
done

cp %{S:101} winsupport

pushd winsupport
tar zcf %{buildroot}%{_libdir}/guestfs/supermin.d/zz-winsupport.tar.gz .
popd

cat > %{buildroot}%{_libdir}/guestfs/supermin.d/zz-packages-winsupport << EOF
libfuse2
hwinfo
EOF
%endif

mkdir -p %{buildroot}/tmp/usr/bin
cp %{S:100} %{buildroot}/tmp/usr/bin
chmod a+x %{buildroot}/tmp/usr/bin/*
pushd %{buildroot}/tmp
tar -czf %{buildroot}/%{_libdir}/guestfs/supermin.d/zz-scripts.tar.gz usr
popd
rm -rf %{buildroot}/tmp

%if %{with p2v}
# Remove the kickstart files from p2v package
rm %{buildroot}/%{_datadir}/virt-p2v/p2v.ks.in
%endif

%post -n libguestfs0 -p /sbin/ldconfig
%postun -n libguestfs0 -p /sbin/ldconfig

%files test
%defattr(-,root,root)
%{_datadir}/guestfs

%files -n guestfs-data
%defattr(-,root,root)
%dir %{_libdir}/guestfs
%dir %{_libdir}/guestfs/supermin.d
%{_libdir}/guestfs/supermin.d/base.tar.gz
%{_libdir}/guestfs/supermin.d/daemon.tar.gz
%{_libdir}/guestfs/supermin.d/init.tar.gz
%{_libdir}/guestfs/supermin.d/udev-rules.tar.gz
%{_libdir}/guestfs/supermin.d/excludefiles
%{_libdir}/guestfs/supermin.d/hostfiles
%{_libdir}/guestfs/supermin.d/packages
%{_libdir}/guestfs/supermin.d/zz-scripts.tar.gz

%if 0%{?is_opensuse}
%{_libdir}/guestfs/supermin.d/zz-ntfs-symlink.tar.gz
%else

%files -n guestfs-winsupport
%defattr(-,root,root)
%{_libdir}/guestfs/supermin.d/zz-*winsupport*
%endif

%if %{with ocaml_bindings}
%files -n ocaml-libguestfs
%defattr(-,root,root)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/guestfs
%{_libdir}/ocaml/guestfs/META
%{_libdir}/ocaml/guestfs/*.cmi
%{_libdir}/ocaml/guestfs/*.cma
%{_libdir}/ocaml/stublibs

%files -n ocaml-libguestfs-devel
%defattr(-,root,root)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/guestfs
%{_libdir}/ocaml/guestfs/*.a
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/guestfs/*.cmx
%{_libdir}/ocaml/guestfs/*.cmxa
%endif
%{_libdir}/ocaml/guestfs/*.mli
%endif
#
%if %{with lua_bindings}
%files -n lua-libguestfs
%defattr(-,root,root)
%{_libdir}/lua
%endif
#
%if %{with perl_bindings}
%post -n perl-Sys-Guestfs -p /sbin/ldconfig

%postun -n perl-Sys-Guestfs -p /sbin/ldconfig

%files -n perl-Sys-Guestfs -f %{name}.files
%defattr(-,root,root)
%endif
#
%if %{with python_bindings}
%files -n python2-libguestfs
%defattr(-,root,root)
%{python2_sitearch}/*

%files -n python3-libguestfs
%defattr(-,root,root)
%{python3_sitearch}/*
%endif
#
%if %{with ruby_bindings}
%files -n rubygem-libguestfs
%defattr(-,root,root)
%{_libdir}/ruby
%endif

%files -n libguestfs0
%defattr(-,root,root)
%license COPYING.LIB
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/guestfs.h
%{_includedir}/guestfs-gobject
%{_includedir}/guestfs-gobject.h
%{_mandir}/man3/*

%files -n guestfsd
%defattr(-,root,root)
%{udevrulesdir}
%{_sbindir}/guestfsd
%{_mandir}/man8/*

%files -n guestfs-tools -f %{name}.lang
%defattr(-,root,root)
%license COPYING
%{_sbindir}/libguestfs-make-fixed-appliance
%{_bindir}/*
/etc/virt-builder
%dir /etc/xdg/virt-builder
%dir /etc/xdg/virt-builder/repos.d
%config /etc/xdg/virt-builder/repos.d/*
%if %{with bash_completion}
%{_datadir}/bash-completion
%endif
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
