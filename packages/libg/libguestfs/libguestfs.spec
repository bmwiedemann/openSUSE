#
# spec file for package libguestfs
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libguestfs
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64 riscv64
Version:        1.48.6
Release:        0
Summary:        Access and modify virtual machine disk images
License:        GPL-2.0-or-later
URL:            http://libguestfs.org

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.sig
Source3:        libguestfs.rpmlintrc
Source5:        guestfish.sh
Source100:      mount-rootfs-and-chroot.sh
Source101:      README

# Patches

BuildRequires:  bison
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-hivex-devel
BuildRequires:  po4a
BuildRequires:  readline-devel
BuildRequires:  supermin >= 5.1.18
BuildRequires:  zstd
BuildRequires:  ocamlfind(findlib)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  pkgconfig(augeas)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(hivex)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(rpm) >= 4.6.0
BuildRequires:  pkgconfig(tinfo)

Requires:       supermin >= 5.1.18
Obsoletes:      guestfs-tools <= 1.44.2

%description
Libguestfs is a library for accessing and modifying virtual machine
disk images.  http://libguestfs.org

Libguestfs uses Linux kernel and qemu code, and can access any type of
guest filesystem that Linux and qemu can, including but not limited
to: ext2/3/4, btrfs, FAT and NTFS, LVM, many different disk partition
schemes, qcow, qcow2, vmdk.

%prep
%autosetup -p1

sed -i 's|RPMVSF_MASK_NOSIGNATURES|_RPMVSF_NOSIGNATURES|' daemon/rpm-c.c

%build
%define _lto_cflags %{nil}

# use 'env LIBGUESTFS_HV=/path/to/kvm libguestfs-test-tool' to verify
%define kvm_binary /bin/false
%ifarch aarch64
%define kvm_binary %{_bindir}/qemu-system-aarch64
%endif
%ifarch ppc64le
%define kvm_binary %{_bindir}/qemu-system-ppc64
%endif
%ifarch ppc64
%define kvm_binary %{_bindir}/qemu-system-ppc64
%endif
%ifarch riscv64
%define kvm_binary %{_bindir}/qemu-system-riscv64
%endif
%ifarch s390x
%define kvm_binary %{_bindir}/qemu-system-s390x
%endif
%ifarch x86_64
%define kvm_binary %{_bindir}/qemu-system-x86_64
%endif
#
%define guestfs_docdir %{_defaultdocdir}/%{name}

export AWK='%{_bindir}/gawk'
export CPIO='%{_bindir}/cpio'
export GPERF='%{_bindir}/gperf'
export MKISOFS='%{_bindir}/xorrisofs'
export XMLLINT='%{_bindir}/xmllint'
export PO4A_GETTEXTIZE='%{_bindir}/po4a-gettextize'
export PO4A_TRANSLATE='%{_bindir}/po4a-translate'
export SQLITE3='%{_bindir}/sqlite3'
export PBMTEXT='%{_bindir}/pbmtext'
export PNMTOPNG='%{_bindir}/pnmtopng'
export BMPTOPNM='%{_bindir}/bmptopnm'
export PAMCUT='%{_bindir}/pamcut'
export WRESTOOL='%{_bindir}/wrestool'
export XZCAT='%{_bindir}/xzcat'
export VALGRIND='%{_bindir}/valgrind'
export FUSER='%{_bindir}/fuser'
export TOOL_TRUE='%{_bindir}/true'
export XGETTEXT='%{_bindir}/xgettext'
export MSGCAT='%{_bindir}/msgcat'
export MSGFMT='%{_bindir}/msgfmt'
export MSGMERGE='%{_bindir}/msgmerge'
export RPCGEN='%{_bindir}/rpcgen'
export SUPERMIN='%{_bindir}/supermin'
export QEMU="%{kvm_binary}"
export vmchannel_test=no
export PERL='%{_bindir}/perl'
export PYTHON='%{_bindir}/python3'

sed -i~ '
/test-data/d
' configure.ac
diff -u "$_"~ "$_" && exit 0
sed -i~ '
/SUBDIRS/s@test-data@@
' Makefile.am
diff -u "$_"~ "$_" && exit 0
autoreconf -fi

%configure --help
%configure \
        --docdir=%{guestfs_docdir} \
	--with-distro=SUSE \
	--with-readline \
        --with-guestfs-path=%{_libdir}/guestfs \
        --with-qemu=$QEMU \
        --with-supermin-packager-config="$PWD/zypper.priv.conf --use-installed --verbose" \
        --without-java \
        --enable-daemon \
	--enable-install-daemon \
        --enable-ocaml \
        --enable-perl \
        --enable-python \
        --disable-erlang \
        --disable-haskell \
        --disable-php \
        --disable-rpath \
        --disable-static \
	%nil

# 'INSTALLDIRS' ensures that perl libs are installed in the vendor dir instead of the site dir
build_it() {
make \
	INSTALLDIRS=vendor \
	LD_RUN_PATH= \
	"$@"
}

build_it %{?_smp_mflags} || build_it

%install
%make_install \
	INSTALLDIRS=vendor \
	udevrulesdir=%{_udevrulesdir}
find %buildroot -ls

rm -f $( find %buildroot -name '*.a' | grep -v /ocaml/ )

find %buildroot -name '*.la' -delete

mkdir -p %{buildroot}/etc/profile.d
cp %{S:5} %{buildroot}/etc/profile.d

# Perl
find %{buildroot}/ -name "*.bs" -size 0c -print -delete
%perl_process_packlist
%perl_gen_filelist
# The macro above packages everything, here only the perl files are desired
grep "%perl_vendorarch/" %{name}.files | tee t
mv t %{name}.files

# Supermin
pushd $RPM_BUILD_ROOT%{_libdir}/guestfs/supermin.d

function remove
{
    grep -Ev "^$1$" < packages > packages-t
    mv packages-t packages
}

function move_to
{
    if ! grep -Esq "^$1$" packages; then
        echo "move_to $1: package name not found in packages file"
        exit 1
    fi
    remove "$1"
    echo "$1" >> "$2"
}

move_to iputils         zz-packages-rescue
move_to lsof            zz-packages-rescue
move_to pciutils        zz-packages-rescue
move_to strace          zz-packages-rescue
move_to vim             zz-packages-rescue
move_to rsync           zz-packages-rsync
move_to xfsprogs        zz-packages-xfs

popd

# Remove the .gitignore file from ocaml/html which will be copied to docdir.
rm ocaml/html/.gitignore

%find_lang %{name}

# Appliance NTFS files
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

# do some cleanup so that rpm can properly empty directories without permission denie
# The winsupport directory has already been tar'ed up, so we don't care much
find winsupport -type d -exec chmod 755 {} \;

mkdir -p %{buildroot}/tmp/usr/bin
cp %{S:100} %{buildroot}/tmp/usr/bin
chmod a+x %{buildroot}/tmp/usr/bin/*
pushd %{buildroot}/tmp
tar -czf %{buildroot}/%{_libdir}/guestfs/supermin.d/zz-scripts.tar.gz usr
popd
rm -rf %{buildroot}/tmp

%package -n libguestfs0
Summary:        Runtime library of libguestfs
Requires:       %{kvm_binary}

%description -n libguestfs0
Shared object library for libguestfs tools which are used to access
and modify virtual machines.

%package -n libguestfsd
Summary:        Daemon for the libguestfs appliance
Provides:       guestfsd = %{version}
Obsoletes:      guestfsd < %{version}

%description -n libguestfsd
guestfsd runs within the libguestfs appliance. It receives commands from the host
and performs the requested action by calling the helper binaries.
This package is only required for building the appliance.

%package -n libguestfs-appliance
BuildRequires:  augeas-lenses
BuildRequires:  bc
BuildRequires:  btrfsprogs
BuildRequires:  bzip2
BuildRequires:  coreutils
BuildRequires:  cpio
BuildRequires:  cryptsetup
BuildRequires:  dhcp-client
BuildRequires:  diffutils
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  glibc
BuildRequires:  gptfdisk
BuildRequires:  grep
BuildRequires:  gzip
BuildRequires:  initviocons
BuildRequires:  iproute2
BuildRequires:  jfsutils
BuildRequires:  ldmtool
BuildRequires:  lvm2
BuildRequires:  mdadm
BuildRequires:  mkisofs
BuildRequires:  module-init-tools
BuildRequires:  ncurses-utils
BuildRequires:  nfs-client
BuildRequires:  ntfs-3g
BuildRequires:  ntfsprogs
BuildRequires:  pam-config
BuildRequires:  parted
BuildRequires:  psmisc
BuildRequires:  sg3_utils
BuildRequires:  strace
%ifarch %ix86 x86_64
BuildRequires:  syslinux
%endif
BuildRequires:  tar
BuildRequires:  terminfo-base
BuildRequires:  tunctl
BuildRequires:  udev
BuildRequires:  util-linux
BuildRequires:  util-linux-lang
BuildRequires:  xfsprogs
BuildRequires:  xz

# Needed by guestfsd which is burried in the appliance
#
# The problem with this design is that rpm can't find the
# library dependencies from the guestfsd hidden in the
# daemon.tar.gz tarball. Supermin will compute an appliance
# at runtime based on the packages it will find on the host.
# Thus if there is no libaugeas, libhivex, etc on the host,
# the appliance will fail to start the guestfsd.
Requires:       augeas
Requires:       augeas-lenses
Requires:       libaugeas0
Requires:       libcap2
Requires:       libguestfs0
Requires:       libhivex0
Requires:       libpcre1

# For core disk features
Requires:       qemu-tools

# Optional packages that could be picked up by supermin
Recommends:     btrfsprogs
Recommends:     cryptsetup
Recommends:     dosfstools
Recommends:     e2fsprogs
Recommends:     gptfdisk
Recommends:     jfsutils
Recommends:     ldmtool
Recommends:     mdadm
Recommends:     mkisofs
Recommends:     parted
Recommends:     xfsprogs
Recommends:     zerofree

Summary:        Virtual machine needed for libguestfs
Provides:       guestfs-data = %{version}
Obsoletes:      guestfs-data < %{version}

%description -n libguestfs-appliance
libguestfs-appliance provides the appliance used by libguestfs.

%package winsupport
Summary:        Windows guest support in libguestfs
Requires:       libguestfs >= 1.32
BuildRequires:  ntfs-3g
BuildRequires:  ntfsprogs
BuildRequires:  rsync
Provides:       guestfs-winsupport = %{version}
Obsoletes:      guestfs-winsupport < %{version}

%description winsupport
Provides the needed pieces for libguestfs to handle Windows guests.

%package devel
Summary:        Development files for libguestfs
Requires:       libguestfs0 = %{version}

%description devel
Development files for libguestfs.

libguestfs is a set of tools for accessing and modifying virtual machine (VM)
disk images. You can use this for viewing and editing files inside guests,
scripting changes to VMs, monitoring disk used/free statistics, P2V, V2V,
performing partial backups, cloning VMs, and much else besides.

%package bash-completion
Summary:        Bash tab-completion scripts for %{name} tools
BuildArch:      noarch
Requires:       bash-completion >= 2.0

%description bash-completion
Install this package if you want intelligent bash tab-completion
for guestfish, guestmount and various virt-* tools.

%package inspect-icons
Summary:        Additional dependencies for inspecting guest icons
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version} > 1500
Requires:       icoutils
%endif

%description inspect-icons
%{name}-inspect-icons is a metapackage that pulls in additional
dependencies required by libguestfs to pull icons out of non-Linux
guests.  Install this package if you want libguestfs to be able to
inspect non-Linux guests and display icons from them.

The only reason this is a separate package is to avoid core libguestfs
having to depend on Perl.

%package -n ocaml-%{name}
Summary:        OCaml bindings for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n ocaml-%{name}
ocaml-%{name} contains OCaml bindings for %{name}.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %{name} you will also need ocaml-%{name}-devel.

%package -n ocaml-%{name}-devel
Summary:        OCaml bindings for %{name}
Requires:       ocaml-%{name} = %{version}-%{release}

%description -n ocaml-%{name}-devel
ocaml-%{name}-devel contains development libraries
required to use the OCaml bindings for %{name}.

%package -n perl-Sys-Guestfs
Summary:        Perl bindings for %{name} (Sys::Guestfs)
Requires:       %{name} = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %{name} (Sys::Guestfs).

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
BuildRequires:  python-rpm-macros
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
python3-%{name} contains Python 3 bindings for %{name}.

%package -n rubygem-%{name}
Summary:        Ruby bindings for %{name}
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
Requires:       %{name} = %{version}-%{release}
Requires:       ruby

%description -n rubygem-%{name}
ruby-%{name} contains Ruby bindings for %{name}.

%package -n lua-%{name}
Summary:        Lua bindings for %{name}
BuildRequires:  lua-devel
Requires:       %{name} = %{version}-%{release}
Requires:       lua

%description -n lua-%{name}
lua-%{name} contains Lua bindings for %{name}.

%package gobject-1_0
Summary:        GObject bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      libguestfs0 <= 1.44.2

%description gobject-1_0
%{name}-gobject-1_0 contains GObject bindings for %{name}.

To develop software against these bindings, you need to install
%{name}-gobject-devel.

%package typelib-Guestfs-1_0
Summary:        Libguestfs GObject introspection data
Group:          System/Libraries

%description typelib-Guestfs-1_0
This package contains the GObject introspection data.

%package gobject-devel
Summary:        GObject bindings for %{name}
Requires:       %{name}-gobject-1_0 = %{version}-%{release}
Requires:       glib2-devel

%description gobject-devel
%{name}-gobject contains GObject bindings for %{name}.

This package is needed if you want to write software using the
GObject bindings.  It also contains GObject Introspection information.

%package rescue
Summary:        Virt-rescue shell
BuildRequires:  iputils
BuildRequires:  lsof
BuildRequires:  pciutils
BuildRequires:  strace
BuildRequires:  vim

%description rescue
This adds the virt-rescue shell which is a "rescue disk" for virtual
machines, and additional tools to use inside the shell such as ssh,
network utilities, editors and debugging utilities.

%package rsync
Summary:        Rsync support for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  rsync

%description rsync
This adds rsync support to %{name}.  Install it if you want to use
rsync to upload or download files into disk images.

%package xfs
Summary:        XFS support for %{name}
Requires:       %{name} = %{version}-%{release}

%description xfs
This adds XFS support to %{name}.  Install it if you want to process
disk images containing XFS.

%package man-pages-ja
Summary:        Japanese (ja) man pages for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.

%package man-pages-uk
Summary:        Ukrainian (uk) man pages for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig
%post -n libguestfs0 -p /sbin/ldconfig
%postun -n libguestfs0 -p /sbin/ldconfig
%post -n %{name}-gobject-1_0 -p /sbin/ldconfig
%postun -n %{name}-gobject-1_0 -p /sbin/ldconfig

%files -f %{name}.lang
%license README COPYING
%{_bindir}/guestfish
%{_bindir}/guestmount
%{_bindir}/guestunmount
%{_bindir}/libguestfs-test-tool
%{_bindir}/virt-copy-in
%{_bindir}/virt-copy-out
%{_bindir}/virt-tar-in
%{_bindir}/virt-tar-out
%{_mandir}/man1/guestfish.1*
%{_mandir}/man1/guestfs-faq.1*
%{_mandir}/man1/guestfs-performance.1*
%{_mandir}/man1/guestfs-recipes.1*
%{_mandir}/man1/guestfs-release-notes.1.gz
%{_mandir}/man1/guestfs-release-notes-1*.1*
%{_mandir}/man1/guestfs-security.1*
%{_mandir}/man1/guestmount.1*
%{_mandir}/man1/guestunmount.1*
%{_mandir}/man1/libguestfs-test-tool.1*
%{_mandir}/man1/virt-copy-in.1*
%{_mandir}/man1/virt-copy-out.1*
%{_mandir}/man1/virt-tar-in.1*
%{_mandir}/man1/virt-tar-out.1*
%{_mandir}/man5/libguestfs-tools.conf.5*
%config %{_sysconfdir}/profile.d/guestfish.sh
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf

%files -n libguestfs0
%license COPYING.LIB
%{_libdir}/libguestfs.so.*

%files -n libguestfs-appliance
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

%files winsupport
%{_libdir}/guestfs/supermin.d/zz-*winsupport*

%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/guestfish
%{_datadir}/bash-completion/completions/guestmount
%{_datadir}/bash-completion/completions/guestunmount
%{_datadir}/bash-completion/completions/libguestfs-test-tool
%{_datadir}/bash-completion/completions/virt-copy-in
%{_datadir}/bash-completion/completions/virt-copy-out
%{_datadir}/bash-completion/completions/virt-rescue
%{_datadir}/bash-completion/completions/virt-tar-in
%{_datadir}/bash-completion/completions/virt-tar-out

%files inspect-icons
# no files

%files -n ocaml-%{name}
%{_libdir}/ocaml/guestfs
%exclude %{_libdir}/ocaml/guestfs/*.a
%exclude %{_libdir}/ocaml/guestfs/*.cmxa
%exclude %{_libdir}/ocaml/guestfs/*.cmx
%exclude %{_libdir}/ocaml/guestfs/*.mli
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner

%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml ocaml/html
%{_libdir}/ocaml/guestfs/*.a
%{_libdir}/ocaml/guestfs/*.cmxa
%{_libdir}/ocaml/guestfs/*.cmx
%{_libdir}/ocaml/guestfs/*.mli
%{_mandir}/man3/guestfs-ocaml.3*

%files -n perl-Sys-Guestfs
%{perl_vendorarch}/*
%doc perl/examples/*.pl
%{_mandir}/man3/Sys::Guestfs.3pm*
%{_mandir}/man3/guestfs-perl.3*

%files -n python3-%{name}
%doc python/examples/*.py
%{python3_sitearch}/libguestfsmod*.so
%{python3_sitearch}/guestfs.py
%{_mandir}/man3/guestfs-python.3*

%files -n rubygem-%{name}
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%{_libdir}/ruby
%{_mandir}/man3/guestfs-ruby.3*

%files -n lua-%{name}
%doc lua/examples/*.lua
%doc lua/examples/LICENSE
%{_libdir}/lua
%{_mandir}/man3/guestfs-lua.3*

%files gobject-1_0
%{_libdir}/libguestfs-gobject-1.0.so.0*

%files typelib-Guestfs-1_0
%{_libdir}/girepository-1.0/Guestfs-1.0.typelib

%files gobject-devel
%{_libdir}/libguestfs-gobject-1.0.so
%{_includedir}/guestfs-gobject.h
%dir %{_includedir}/guestfs-gobject
%{_includedir}/guestfs-gobject/*.h
%{_datadir}/gir-1.0/Guestfs-1.0.gir
%{_libdir}/pkgconfig/libguestfs-gobject-1.0.pc
%{_mandir}/man3/guestfs-gobject.3*

%files devel
%doc examples/*.c
%{_sbindir}/libguestfs-make-fixed-appliance
%{_libdir}/*.so
%{_libdir}/pkgconfig/libguestfs.pc
%{_includedir}/guestfs.h
%{_mandir}/man1/guestfs-building.1*
%{_mandir}/man1/guestfs-hacking.1*
%{_mandir}/man1/guestfs-internals.1*
%{_mandir}/man1/guestfs-testing.1*
%{_mandir}/man1/libguestfs-make-fixed-appliance.1*
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*

%files -n libguestfsd
%{_udevrulesdir}
%{_sbindir}/guestfsd
%{_mandir}/man8/*

%files rescue
%{_libdir}/guestfs/supermin.d/zz-packages-rescue
%{_bindir}/virt-rescue
%{_mandir}/man1/virt-rescue.1*

%files rsync
%{_libdir}/guestfs/supermin.d/zz-packages-rsync

%files xfs
%{_libdir}/guestfs/supermin.d/zz-packages-xfs

%files man-pages-ja
%lang(ja) %{_mandir}/ja/man1/*.1*
%lang(ja) %{_mandir}/ja/man3/*.3*
%lang(ja) %{_mandir}/ja/man5/*.5*

%files man-pages-uk
%if 0%{?suse_version} <= 1500
%dir %{_mandir}/uk
%dir %{_mandir}/uk/man{1,3,5}
%endif
%lang(uk) %{_mandir}/uk/man1/*.1*
%lang(uk) %{_mandir}/uk/man3/*.3*
%lang(uk) %{_mandir}/uk/man5/*.5*

%changelog
