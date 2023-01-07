#
# spec file for package e2fsprogs
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


%define flavor @BUILD_FLAVOR@%nil

%if "%{flavor}" == ""
Name:           e2fsprogs
Summary:        Utilities for the Second Extended File System
License:        GPL-2.0-only
%if 0%{?suse_version} >= 1010
# Hint for ZYPP
Supplements:    filesystem(ext2) filesystem(ext3) filesystem(ext4)
%endif
%else
Name:           fuse2fs
Summary:        FUSE file system client for ext2/ext3/ext4 file systems
License:        MIT
BuildRequires:  fuse-devel
%endif
Version:        1.46.5
Release:        0
Group:          System/Filesystems
URL:            http://e2fsprogs.sourceforge.net
Source:         http://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.xz
Source2:        README.SUSE
Source3:        baselibs.conf
Source4:        http://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.sign
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
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
BuildRequires:  xz
%if "%{flavor}" == ""
%if 0%{?suse_version} >= 1210
%bcond_without systemd
%else
%bcond_with systemd
%endif
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
# Define info macros if missing (for Fedora builds)
%if ! 0%{?suse_version}
%define install_info_prereq info
%define install_info sbin/install-info
%define install_info_delete sbin/install-info --delete
Requires(post): %install_info_prereq
Requires(preun):%install_info_prereq
%endif
# bug437293
%ifarch ppc64
Obsoletes:      e2fsprogs-64bit
%endif
#
# For regenerate_initrd_post macro
Requires(post): /usr/bin/mkdir /usr/bin/touch
Requires:       libcom_err2 >= %{version}
Requires:       libext2fs2 >= %{version}
Suggests:       e2fsprogs-scrub
# Do not suppress make commands
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Group:          Development/Libraries/C and C++
%ifarch ppc64
Obsoletes:      e2fsprogs-devel-64bit
%endif
#
Requires:       libblkid-devel
Requires:       libext2fs-devel = %version
Requires:       libuuid-devel

%description devel
Dummy development package for backwards compatibility.

%package -n e2fsprogs-scrub
Summary:        Ext2fs scrubbing scripts and service files
License:        GPL-2.0-only
Group:          System/Filesystems
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif
Requires:       e2fsprogs
Requires:       lvm2
Requires:       postfix
Requires:       util-linux

%description -n e2fsprogs-scrub
Scripts and systemd service files for background scrubbing of LVM volumes
with ext2, ext3, and ext4 filesystems.

%package -n libext2fs2
Summary:        Ext2fs library
License:        LGPL-2.0-only
Group:          System/Filesystems

%description -n libext2fs2
The basic Ext2fs shared library.

%package -n libext2fs-devel
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libcom_err-devel
Requires:       libext2fs2 = %version

%description -n libext2fs-devel
Development files for libext2fs.

%package -n libext2fs-devel-static
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libext2fs-devel = %{version}
Provides:       libext2fs-devel:%{_libdir}/libe2p.a
Provides:       libext2fs-devel:%{_libdir}/libext2fs.a

%description -n libext2fs-devel-static
Development files for libext2fs. Static libraries.

%package -n libcom_err2
Summary:        E2fsprogs error reporting library
# bug437293
License:        MIT
Group:          System/Filesystems
%ifarch ppc64
Obsoletes:      libcom_err-64bit
Obsoletes:      libcom_err2-64bit
%endif
#
Provides:       libcom_err = %{version}
Obsoletes:      libcom_err <= 1.40

%description -n libcom_err2
com_err is an error message display library.

%package -n libcom_err-devel
Summary:        Development files for libcom_err
# bug437293
License:        MIT
Group:          Development/Libraries/C and C++
%ifarch ppc64
Obsoletes:      libcom_err-devel-64bit
%endif
#
Requires:       glibc-devel
Requires:       libcom_err2 = %version

%description -n libcom_err-devel
Development files for the com_err error message display library.

%package -n libcom_err-devel-static
Summary:        Development files for libcom_err, static libraries
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       libcom_err-devel = %{version}
Provides:       libcom_err-devel:%{_libdir}/libcom_err.a
Provides:       libcom_err-devel:%{_libdir}/libss.a
# bug437293
%ifarch ppc64
Obsoletes:      libcom_err-devel-64bit
%endif
#

%description -n libcom_err-devel-static
Development files for the com_err error message display library. Static libraries.

%prep
%setup -q -n e2fsprogs-%{version}
# libcom_err patches
%patch3 -p1
%patch4
%patch5
cp %{SOURCE2} .
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

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
  CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} V=1
#Guarantee that tranlations match the source messages
make -C po update-po

%install
%if "%{flavor}" == ""
make install install-libs DESTDIR=$RPM_BUILD_ROOT ELF_INSTALL_DIR=/%{_libdir}

%{find_lang} e2fsprogs

rm $RPM_BUILD_ROOT%{_libdir}/e2initrd_helper

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
%{?regenerate_initrd_post}

%if %{with systemd}
%post -n e2fsprogs-scrub
%service_add_post e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%if %{with systemd}
%if 0%{?suse_version} <= 1530
%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libext2fs.info.gz
%endif

%preun -n e2fsprogs-scrub
%service_del_preun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%postun
/sbin/ldconfig
%{?regenerate_initrd_post}

%if %{with systemd}
%postun -n e2fsprogs-scrub
%service_del_postun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%posttrans
%{?regenerate_initrd_posttrans}

%post -n libext2fs2 -p /sbin/ldconfig

%postun -n libext2fs2 -p /sbin/ldconfig

%post -n libcom_err2 -p /sbin/ldconfig

%postun -n libcom_err2 -p /sbin/ldconfig

%files -f e2fsprogs.lang
%defattr(-, root, root)
%doc doc/RelNotes/v%{version}.txt README
%if 0%{?sle_version} > 120200
%license NOTICE
%endif
%config /etc/mke2fs.conf
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
%{_infodir}/libext2fs.info.gz
%{_mandir}/man1/chattr.1.gz
%{_mandir}/man1/lsattr.1.gz
%{_mandir}/man5/ext?.5.gz
%{_mandir}/man5/e2fsck.conf.5.gz
%{_mandir}/man5/mke2fs.conf.5.gz
%{_mandir}/man8/*.8.gz

%files devel
%defattr(-,root,root)
%doc README.SUSE

%files -n e2fsprogs-scrub
%defattr(-,root,root)
%config /etc/e2scrub.conf
%{_sbindir}/e2scrub
%{_sbindir}/e2scrub_all
%if %{with systemd}
%{_libdir}/e2fsprogs/
%{_libdir}/e2fsprogs/e2scrub_fail
%{_unitdir}/e2scrub@.service
%{_unitdir}/e2scrub_all.service
%{_unitdir}/e2scrub_all.timer
%{_unitdir}/e2scrub_fail@.service
%{_unitdir}/e2scrub_reap.service
%endif

%files -n libext2fs2
%defattr(-, root, root)
%if 0%{?suse_version} < 1550
/%{_lib}/libext2fs.so.*
/%{_lib}/libe2p.so.*
%endif
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%files -n libext2fs-devel
%defattr(-, root, root)
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
/usr/include/ext2fs
/usr/include/e2p
%_libdir/pkgconfig/e2p.pc
%_libdir/pkgconfig/ext2fs.pc

%files -n libcom_err2
%defattr(-, root, root)
%if 0%{?suse_version} < 1550
/%{_lib}/libcom_err.so.*
/%{_lib}/libss.so.*
%endif
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%files -n libcom_err-devel
%defattr(-, root, root)
%_bindir/compile_et
%_bindir/mk_cmds
%{_libdir}/libcom_err.so
%{_libdir}/libss.so
%_libdir/pkgconfig/com_err.pc
%_libdir/pkgconfig/ss.pc
%_includedir/com_err.h
%_includedir/et
%_includedir/ss
%_datadir/et
%_datadir/ss
%{_mandir}/man1/compile_et.1.gz
%{_mandir}/man1/mk_cmds.1.gz
%{_mandir}/man3/com_err.3.gz

%files -n libcom_err-devel-static
%defattr(-, root, root)
%{_libdir}/libcom_err.a
%{_libdir}/libss.a

%files -n libext2fs-devel-static
%defattr(-, root, root)
%{_libdir}/libext2fs.a
%{_libdir}/libe2p.a

%else
%make_install
(cd %{buildroot}; find -L -type f | grep -v fuse2fs | xargs rm)

%files
%_bindir/fuse2fs
%{_mandir}/man1/fuse2fs.1.gz
%endif

%changelog
