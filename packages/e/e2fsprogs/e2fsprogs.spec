#
# spec file for package e2fsprogs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define flavor @BUILD_FLAVOR@%{nil}
Version:        1.47.4
Release:        0
%if "%{flavor}" == ""
Name:           e2fsprogs
Summary:        Utilities for the Second Extended File System
License:        GPL-2.0-only
%if 0%{?suse_version} >= 1010
# Hint for ZYPP
Supplements:    filesystem(ext2)
Supplements:    filesystem(ext3)
Supplements:    filesystem(ext4)
%endif
%else
Name:           fuse2fs
Summary:        FUSE file system client for ext2/ext3/ext4 file systems
License:        MIT
BuildRequires:  pkgconfig(fuse3)
%endif
URL:            http://e2fsprogs.sourceforge.net
Source:         https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.xz
Source2:        README.SUSE
Source3:        baselibs.conf
Source4:        https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.sign
Source5:        https://thunk.org/tytso/tytso-key.asc#/e2fsprogs.keyring
#
# e2fsprogs patches
#
# libcom_err patches
Patch3:         libcom_err-compile_et_permissions.patch
Patch4:         e2fsprogs-1.42-implicit_fortify_decl.patch
Patch5:         e2fsprogs-1.42-ext2fsh_implicit.patch
Patch6:         harden_e2scrub@.service.patch
Patch7:         harden_e2scrub_all.service.patch
Patch8:         harden_e2scrub_fail@.service.patch
Patch9:         harden_e2scrub_reap.service.patch
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(uuid)
%if "%{flavor}" == ""
# Define info macros if missing (for Fedora builds)
%if ! 0%{?suse_version}
%define install_info_prereq info
%define install_info sbin/install-info
%define install_info_delete sbin/install-info --delete
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
%endif
%if 0%{?suse_version} >= 1210
%bcond_without systemd
%else
%bcond_with systemd
%endif
Requires:       libcom_err2 >= %{version}
Requires:       libext2fs2 >= %{version}
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Suggests:       e2fsprogs-scrub
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
#
# For regenerate_initrd_post macro
%if 0%{?suse_version} < 1550
BuildRequires:  suse-module-tools
%else
BuildRequires:  rpm-config-SUSE
%endif
# Do not suppress make commands

%description
Utilities needed to create and maintain ext2 and ext3 file systems
under Linux. Included in this package are: chattr, lsattr, mke2fs,
mklost+found, tune2fs, e2fsck, resize2fs, and badblocks.
%else

%description
fuse2fs is a FUSE file system client that supports reading and
writing from devices or image files containing ext2, ext3, and
ext4 file systems.
%endif

%package devel
Summary:        Dummy development package
# bug437293
License:        LGPL-2.0-only
#
Requires:       pkgconfig(blkid)
Requires:       pkgconfig(e2p) = %{version}
Requires:       pkgconfig(ext2fs) = %{version}
Requires:       pkgconfig(uuid)
%ifarch ppc64
Obsoletes:      e2fsprogs-devel-64bit
%endif

%description devel
Dummy development package for backwards compatibility.

%package -n e2fsprogs-scrub
Summary:        Ext2fs scrubbing scripts and service files
License:        GPL-2.0-only
Requires:       e2fsprogs
Requires:       lvm2
Requires:       postfix
Requires:       util-linux
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif

%description -n e2fsprogs-scrub
Scripts and systemd service files for background scrubbing of LVM volumes
with ext2, ext3, and ext4 filesystems.

%package -n libext2fs2
Summary:        Ext2fs library
License:        LGPL-2.0-only

%description -n libext2fs2
The basic Ext2fs shared library.

%package -n libext2fs-devel
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Requires:       libext2fs2 = %{version}
Requires:       pkgconfig(com_err)
Requires:       pkgconfig(ss)

%description -n libext2fs-devel
Development files for libext2fs.

%package -n libext2fs-devel-static
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Requires:       pkgconfig(e2p) = %{version}
Requires:       pkgconfig(ext2fs) = %{version}
Provides:       libext2fs-devel:%{_libdir}/libe2p.a
Provides:       libext2fs-devel:%{_libdir}/libext2fs.a

%description -n libext2fs-devel-static
Development files for libext2fs. Static libraries.

%package -n libcom_err2
Summary:        E2fsprogs error reporting library
# bug437293
License:        MIT
#
Provides:       libcom_err = %{version}
Obsoletes:      libcom_err <= 1.40
%ifarch ppc64
Obsoletes:      libcom_err-64bit
Obsoletes:      libcom_err2-64bit
%endif

%description -n libcom_err2
com_err is an error message display library.

%package -n libcom_err-devel
Summary:        Development files for libcom_err
# bug437293
License:        MIT
#
Requires:       glibc-devel
Requires:       libcom_err2 = %{version}
%ifarch ppc64
Obsoletes:      libcom_err-devel-64bit
%endif

%description -n libcom_err-devel
Development files for the com_err error message display library.

%package -n libcom_err-devel-static
Summary:        Development files for libcom_err, static libraries
License:        MIT
Requires:       pkgconfig(com_err) = %{version}
Requires:       pkgconfig(ss) = %{version}
Provides:       libcom_err-devel:%{_libdir}/libcom_err.a
Provides:       libcom_err-devel:%{_libdir}/libss.a
#

%description -n libcom_err-devel-static
Development files for the com_err error message display library. Static libraries.

%prep
%setup -q -n e2fsprogs-%{version}
# libcom_err patches
%patch -P 3 -p1
%patch -P 4
%patch -P 5
cp %{SOURCE2} .
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure \
  --with-root-prefix=''   \
  --enable-elf-shlibs \
  --disable-libblkid \
  --disable-libuuid \
  --disable-uuidd \
  --disable-fsck \
  --without-crond-dir \
  --with-systemd-unit-dir=%{?_unitdir} \
  CFLAGS="%{optflags}"
%make_build
#Guarantee that tranlations match the source messages
%make_build -C po update-po

%install
%if "%{flavor}" == ""
make install install-libs DESTDIR=%{buildroot} ELF_INSTALL_DIR=/%{_libdir}

%find_lang e2fsprogs

rm %{buildroot}%{_libdir}/e2initrd_helper

%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -s %{_sbindir}/badblocks %{buildroot}/sbin/badblocks
ln -s %{_sbindir}/debugfs   %{buildroot}/sbin/debugfs
ln -s %{_sbindir}/dumpe2fs  %{buildroot}/sbin/dumpe2fs
ln -s %{_sbindir}/e2undo    %{buildroot}/sbin/e2undo
ln -s %{_sbindir}/e2fsck    %{buildroot}/sbin/e2fsck
ln -s %{_sbindir}/e2label   %{buildroot}/sbin/e2label
ln -s %{_sbindir}/e2mmpstatus %{buildroot}/sbin/e2mmpstatus
ln -s %{_sbindir}/fsck.ext2 %{buildroot}/sbin/fsck.ext2
ln -s %{_sbindir}/fsck.ext3 %{buildroot}/sbin/fsck.ext3
ln -s %{_sbindir}/fsck.ext4 %{buildroot}/sbin/fsck.ext4
ln -s %{_sbindir}/mke2fs    %{buildroot}/sbin/mke2fs
ln -s %{_sbindir}/mkfs.ext2 %{buildroot}/sbin/mkfs.ext2
ln -s %{_sbindir}/mkfs.ext3 %{buildroot}/sbin/mkfs.ext3
ln -s %{_sbindir}/mkfs.ext4 %{buildroot}/sbin/mkfs.ext4
ln -s %{_sbindir}/resize2fs %{buildroot}/sbin/resize2fs
ln -s %{_sbindir}/tune2fs   %{buildroot}/sbin/tune2fs
ln -s %{_sbindir}/e2image   %{buildroot}/sbin/e2image
ln -s %{_sbindir}/logsave   %{buildroot}/sbin/logsave
mkdir %{buildroot}/%{_lib}
pushd %{buildroot}/%{_libdir}
LIBNAMES=$(ls *.so.*)
popd
for libName in $LIBNAMES;
  do ln -s %{_libdir}/$libName %{buildroot}/%{_lib};
done
%endif

%if %{with systemd}
%pre -n e2fsprogs-scrub
%service_add_pre e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%post
/sbin/ldconfig
%if 0%{?suse_version} <= 1530
%install_info --info-dir=%{_infodir} %{_infodir}/libext2fs.info.gz
%endif
%{regenerate_initrd_post}

%if %{with systemd}
%post -n e2fsprogs-scrub
%service_add_post e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%if 0%{?suse_version} <= 1530
%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libext2fs.info.gz
%endif

%if %{with systemd}
%preun -n e2fsprogs-scrub
%service_del_preun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%postun
/sbin/ldconfig
%{regenerate_initrd_post}

%if %{with systemd}
%postun -n e2fsprogs-scrub
%service_del_postun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%posttrans
%{regenerate_initrd_posttrans}

%post -n libext2fs2 -p /sbin/ldconfig
%postun -n libext2fs2 -p /sbin/ldconfig
%post -n libcom_err2 -p /sbin/ldconfig
%postun -n libcom_err2 -p /sbin/ldconfig

%files -f e2fsprogs.lang
%doc doc/RelNotes/v%{version}.txt README
%license NOTICE
%config %{_sysconfdir}/mke2fs.conf
%if 0%{?suse_version} < 1550
/sbin/badblocks
/sbin/debugfs
/sbin/dumpe2fs
/sbin/e2undo
/sbin/e2fsck
/sbin/e2label
/sbin/e2mmpstatus
/sbin/fsck.ext2
/sbin/fsck.ext3
/sbin/fsck.ext4
/sbin/mke2fs
/sbin/mkfs.ext2
/sbin/mkfs.ext3
/sbin/mkfs.ext4
/sbin/resize2fs
/sbin/tune2fs
/sbin/e2image
/sbin/logsave
%endif
%{_sbindir}/badblocks
%{_sbindir}/debugfs
%{_sbindir}/dumpe2fs
%{_sbindir}/e2undo
%{_sbindir}/e2fsck
%{_sbindir}/e2label
%{_sbindir}/e2mmpstatus
%{_sbindir}/fsck.ext2
%{_sbindir}/fsck.ext3
%{_sbindir}/fsck.ext4
%{_sbindir}/mke2fs
%{_sbindir}/mkfs.ext2
%{_sbindir}/mkfs.ext3
%{_sbindir}/mkfs.ext4
%{_sbindir}/resize2fs
%{_sbindir}/tune2fs
%{_sbindir}/e2image
%{_sbindir}/logsave
%{_bindir}/chattr
%{_bindir}/lsattr
%{_sbindir}/mklost+found
%{_sbindir}/filefrag
%{_sbindir}/e2freefrag
%{_sbindir}/e4defrag
%{_sbindir}/e4crypt
%{_infodir}/libext2fs.info%{?ext_info}
%{_mandir}/man1/chattr.1%{?ext_man}
%{_mandir}/man1/lsattr.1%{?ext_man}
%{_mandir}/man5/ext?.5%{?ext_man}
%{_mandir}/man5/e2fsck.conf.5%{?ext_man}
%{_mandir}/man5/mke2fs.conf.5%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}

%files devel
%doc README.SUSE

%files -n e2fsprogs-scrub
%config %{_sysconfdir}/e2scrub.conf
%{_sbindir}/e2scrub
%{_sbindir}/e2scrub_all
%if %{with systemd}
%{_libexecdir}/e2fsprogs/
%{_libexecdir}/e2fsprogs/e2scrub_fail
%{_unitdir}/e2scrub@.service
%{_unitdir}/e2scrub_all.service
%{_unitdir}/e2scrub_all.timer
%{_unitdir}/e2scrub_fail@.service
%{_unitdir}/e2scrub_reap.service
%endif

%files -n libext2fs2
%if 0%{?suse_version} < 1550
/%{_lib}/libext2fs.so.*
/%{_lib}/libe2p.so.*
%endif
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%files -n libext2fs-devel
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
%{_includedir}/ext2fs
%{_includedir}/e2p
%{_libdir}/pkgconfig/e2p.pc
%{_libdir}/pkgconfig/ext2fs.pc

%files -n libcom_err2
%if 0%{?suse_version} < 1550
/%{_lib}/libcom_err.so.*
/%{_lib}/libss.so.*
%endif
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%files -n libcom_err-devel
%{_bindir}/compile_et
%{_bindir}/mk_cmds
%{_libdir}/libcom_err.so
%{_libdir}/libss.so
%{_libdir}/pkgconfig/com_err.pc
%{_libdir}/pkgconfig/ss.pc
%{_includedir}/com_err.h
%{_includedir}/et
%{_includedir}/ss
%{_datadir}/et
%{_datadir}/ss
%{_mandir}/man1/compile_et.1%{?ext_man}
%{_mandir}/man1/mk_cmds.1%{?ext_man}
%{_mandir}/man3/com_err.3%{?ext_man}

%files -n libcom_err-devel-static
%{_libdir}/libcom_err.a
%{_libdir}/libss.a

%files -n libext2fs-devel-static
%{_libdir}/libext2fs.a
%{_libdir}/libe2p.a

%else
%make_install
(cd %{buildroot}; find -L -type f | grep -v fuse2fs | xargs rm)

%files
%{_bindir}/fuse2fs
%{_mandir}/man1/fuse2fs.1%{?ext_man}
%endif

%changelog
