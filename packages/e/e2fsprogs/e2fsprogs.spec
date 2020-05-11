#
# spec file for package e2fsprogs
#
# Copyright (c) 2020 SUSE LLC
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


%define build_mini 0

Name:           e2fsprogs
%if 0%{?suse_version} >= 1010
# Hint for ZYPP
Supplements:    filesystem(ext2) filesystem(ext3) filesystem(ext4)
%endif
%if 0%{?suse_version} >= 1210
%bcond_without systemd
%else
%bcond_with systemd
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
BuildRequires:  xz
%if ! %{build_mini}
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
# Define info macros if missing (for Fedora builds)
%if 0%{!?%install_info_prereq:1}
%define install_info_prereq info
%define install_info sbin/install-info
%define install_info_delete sbin/install-info --delete
%endif
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%endif
# bug437293
%ifarch ppc64
Obsoletes:      e2fsprogs-64bit
%endif

%if %{build_mini}
Conflicts:      e2fsprogs
Conflicts:      e2fsprogs-devel
Conflicts:      libext2fs2
Conflicts:      libext2fs-devel
Conflicts:      libcom_err2
Conflicts:      libcom_err-devel
%else
Conflicts:      e2fsprogs-mini
Conflicts:      e2fsprogs-mini-devel
Conflicts:      libext2fs2-mini
Conflicts:      libext2fs-mini-devel
Conflicts:      libcom_err2-mini
Conflicts:      libcom_err-mini-devel
%endif
#
Version:        1.45.6
Release:        0
Summary:        Utilities for the Second Extended File System
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            http://e2fsprogs.sourceforge.net
Requires(post): coreutils
Requires:       libcom_err2 >= %{version}
Requires:       libext2fs2 >= %{version}
Suggests:       e2fsprogs-scrub
Source:         http://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.xz
Source2:        README.SUSE
Source3:        baselibs.conf
Source4:        http://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.sign
Source5:        https://thunk.org/tytso/tytso-key.asc#/%{name}.keyring
#
# e2fsprogs patches
#
# libcom_err patches
Patch3:         libcom_err-compile_et_permissions.patch
Patch4:         e2fsprogs-1.42-implicit_fortify_decl.patch
Patch5:         e2fsprogs-1.42-ext2fsh_implicit.patch
# PATCH-FIX-UPSTREAM e2fsprogs-1.45.2-gettext.patch -- Support gettext 0.20
Patch6:         e2fsprogs-1.45.2-gettext.patch
# Do not suppress make commands
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities needed to create and maintain ext2 and ext3 file systems
under Linux. Included in this package are: chattr, lsattr, mke2fs,
mklost+found, tune2fs, e2fsck, resize2fs, and badblocks.

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

%if %{build_mini}
%package -n e2fsprogs-scrub-mini
%else
%package -n e2fsprogs-scrub
%endif
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

%if %{build_mini}
%package -n libext2fs2-mini
%else
%package -n libext2fs2
%endif
Summary:        Ext2fs library
License:        LGPL-2.0-only
Group:          System/Filesystems

%if %{build_mini}
%description -n libext2fs2-mini
%else
%description -n libext2fs2
%endif
The basic Ext2fs shared library.

%if %{build_mini}
%package -n libext2fs-mini-devel
%else
%package -n libext2fs-devel
%endif
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libcom_err-devel
Requires:       libext2fs2 = %version

%if %{build_mini}
%description -n libext2fs-mini-devel
%else
%description -n libext2fs-devel
%endif
Development files for libext2fs.

%if ! %{build_mini}
%package -n libext2fs-devel-static
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libext2fs-devel = %{version}
Provides:       libext2fs-devel:%{_libdir}/libe2p.a
Provides:       libext2fs-devel:%{_libdir}/libext2fs.a

%description -n libext2fs-devel-static
Development files for libext2fs. Static libraries.
%endif

%if %{build_mini}
%package -n libcom_err2-mini
%else
%package -n libcom_err2
%endif
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

%if %{build_mini}
%description -n libcom_err2-mini
%else
%description -n libcom_err2
%endif
com_err is an error message display library.

%if %{build_mini}
%package -n libcom_err-mini-devel
%else
%package -n libcom_err-devel
%endif
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

%if %{build_mini}
%description -n libcom_err-mini-devel
%else
%description -n libcom_err-devel
%endif
Development files for the com_err error message display library.

%if ! %{build_mini}
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
%endif

%prep
%setup -q -n e2fsprogs-%{version}
# libcom_err patches
%patch3 -p1
%patch4
%patch5
%patch6 -p1
cp %{SOURCE2} .
# Don't use intl/ subdirectory as it's deprecated since gettext 0.20
rm -r intl

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf --force --install
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
%if %{build_mini}
rm -rf doc
%endif
make %{?_smp_mflags} V=1
#Guarantee that tranlations match the source messages
make -C po update-po

%install
make install install-libs DESTDIR=$RPM_BUILD_ROOT ELF_INSTALL_DIR=/%{_libdir}

%{find_lang} e2fsprogs

rm $RPM_BUILD_ROOT%{_libdir}/e2initrd_helper

#UsrMerge
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
#EndUsrMerge

%if %{with systemd}
%if %{build_mini}
%pre -n e2fsprogs-scrub-mini
%else
%pre -n e2fsprogs-scrub
%endif
%service_add_pre e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%post
/sbin/ldconfig
%if ! %{build_mini}
%install_info --info-dir=%{_infodir} %{_infodir}/libext2fs.info.gz || :
%{?regenerate_initrd_post}
%endif

%if %{with systemd}
%if %{build_mini}
%post -n e2fsprogs-scrub-mini
%else
%post -n e2fsprogs-scrub
%endif
%service_add_post e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%if %{with systemd}
%if %{build_mini}
%preun -n e2fsprogs-scrub-mini
%else
%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libext2fs.info.gz || :
%preun -n e2fsprogs-scrub
%endif
%service_del_preun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%postun
/sbin/ldconfig
%if ! %{build_mini}
%{?regenerate_initrd_post}
%endif

%if %{with systemd}
%if %{build_mini}
%postun -n e2fsprogs-scrub-mini
%else
%postun -n e2fsprogs-scrub
%endif
%service_del_postun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%if ! %{build_mini}
%posttrans
%{?regenerate_initrd_posttrans}
%endif

%if %{build_mini}
%post -n libext2fs2-mini -p /sbin/ldconfig
%else
%post -n libext2fs2 -p /sbin/ldconfig
%endif

%if %{build_mini}
%postun -n libext2fs2-mini -p /sbin/ldconfig
%else
%postun -n libext2fs2 -p /sbin/ldconfig
%endif

%if %{build_mini}
%post -n libcom_err2-mini -p /sbin/ldconfig
%else
%post -n libcom_err2 -p /sbin/ldconfig
%endif

%if %{build_mini}
%postun -n libcom_err2-mini -p /sbin/ldconfig
%else
%postun -n libcom_err2 -p /sbin/ldconfig
%endif

%files -f e2fsprogs.lang
%defattr(-, root, root)
%doc RELEASE-NOTES README
%if 0%{?sle_version} > 120200
%license NOTICE
%endif
%config /etc/mke2fs.conf
#UsrMerge 
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
#EndUsrMerge
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
%if ! %{build_mini}
%{_infodir}/libext2fs.info.gz
%endif
%{_mandir}/man1/chattr.1.gz
%{_mandir}/man1/lsattr.1.gz
%{_mandir}/man5/ext?.5.gz
%{_mandir}/man5/e2fsck.conf.5.gz
%{_mandir}/man5/mke2fs.conf.5.gz
%{_mandir}/man8/*.8.gz

%files devel
%defattr(-,root,root)
%doc README.SUSE

%if %{build_mini}
%files -n e2fsprogs-scrub-mini
%else
%files -n e2fsprogs-scrub
%endif
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

%if %{build_mini}
%files -n libext2fs2-mini
%else
%files -n libext2fs2
%endif
%defattr(-, root, root)
#UsrMerge
/%{_lib}/libext2fs.so.*
/%{_lib}/libe2p.so.*
#EndUsrMerge
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%if %{build_mini}
%files -n libext2fs-mini-devel
%else
%files -n libext2fs-devel
%endif
%defattr(-, root, root)
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
/usr/include/ext2fs
/usr/include/e2p
%_libdir/pkgconfig/e2p.pc
%_libdir/pkgconfig/ext2fs.pc

%if %{build_mini}
%files -n libcom_err2-mini
%else
%files -n libcom_err2
%endif
%defattr(-, root, root)
#UsrMerge
/%{_lib}/libcom_err.so.*
/%{_lib}/libss.so.*
#EndUsrMerge
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%if %{build_mini}
%files -n libcom_err-mini-devel
%else
%files -n libcom_err-devel
%endif
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

%if ! %{build_mini}
%files -n libcom_err-devel-static
%defattr(-, root, root)
%{_libdir}/libcom_err.a
%{_libdir}/libss.a

%files -n libext2fs-devel-static
%defattr(-, root, root)
%{_libdir}/libext2fs.a
%{_libdir}/libe2p.a
%endif

%changelog
