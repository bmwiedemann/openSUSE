#
# spec file for package xfsprogs
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


%define _dracutmodulesdir %{_prefix}/lib/dracut/modules.d
# make sure we use systemd services on products where it is available
%if 0%{?suse_version} >= 1210
%bcond_without systemd
%else
%bcond_with systemd
%endif
%define libname libhandle1
Name:           xfsprogs
Version:        6.0.0
Release:        0
Summary:        Utilities for managing the XFS file system
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://xfs.wiki.kernel.org/
Source0:        https://www.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-%{version}.tar.sign
Source2:        %{name}.keyring
Source3:        module-setup.sh.in
Source4:        dracut-fsck-help.txt
Patch0:         xfsprogs-docdir.diff
Patch1:         0001-repair-shift-inode-back-into-place-if-corrupted-by-b.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libblkid-devel
BuildRequires:  libedit-devel
BuildRequires:  libinih-devel
BuildRequires:  liburcu-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
Requires(post): coreutils
Suggests:       xfsprogs-scrub
# hint for ZYPP
Supplements:    filesystem(xfs)
%if 0%{?suse_version} >= 1310
BuildRequires:  suse-module-tools
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%endif

%description
A set of commands to use the XFS file system, including mkfs.xfs.

XFS is a high performance journaling file system which originated on
the SGI IRIX platform.	It is completely multithreaded. It can support
large files and large file systems, extended attributes, and variable
block sizes. It is extent based and makes extensive use of Btrees
(directories, extents, and free space) to aid both performance and
scalability.

Refer to the documentation at https://xfs.wiki.kernel.org/ for complete
details.  This implementation is on-disk compatible with the IRIX
version of XFS.

%package      -n %{libname}
Summary:        XFS Filesystem-specific Shared library
Group:          Development/Libraries/C and C++

%description -n %{libname}
%{libname} contains the shared libraries needed by xfsprogs
to run xfsprogs programs.

%{libname} is always needed by xfsprogs. If you want to use this
library for your own new xfs tools install xfsprogs-devel.

%package      devel
Summary:        XFS Filesystem-specific Static Libraries and Headers
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libuuid-devel
Requires:       xfsprogs = %{version}

%description devel
xfsprogs-devel contains the libraries and header files needed to
develop XFS file system-specific programs.

You should install xfsprogs-devel if you want to develop XFS file
system-specific programs.  If you install xfsprogs-devel, you will also
want to install xfsprogs.

%package -n	xfsprogs-scrub
Summary:        XFS scrubbing scripts and service files
Group:          System/Filesystems
Requires:       xfsprogs

%description -n	xfsprogs-scrub
Scripts and systemd service files for background scrubbing of metadata
on xfs filesystems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal -I m4
autoconf

export OPTIMIZER="-fPIC"
export DEBUG=-DNDEBUG
export LIBUUID=%{_libdir}/libuuid.a

%configure \
    --exec-prefix="" \
    --enable-editline=yes \
%if %{with systemd}
    --with-systemd-unit-dir=%{_unitdir} \
%endif
%if 0%{?suse_version} < 1500
    --disable-lto \
%endif
    %{nil}
%make_build

PATH_TO_HELP="%{_dracutmodulesdir}/95suse-xfs/dracut-fsck-help.txt"
sed -e "s|@@PATH_TO_HELP@@|$PATH_TO_HELP|" %{SOURCE3} > module-setup.sh

%install
export DIST_ROOT=%{buildroot}
%make_install
make install-dev
# remove the static libs and libtool archive
rm -rf %{buildroot}/%{_lib}/*.{la,a}
rm -rf %{buildroot}/%{_libdir}/*.{la,a}
%find_lang %{name}
install -m 0755 -d %{buildroot}/%{_dracutmodulesdir}/95suse-xfs/
install -m 0755 module-setup.sh %{buildroot}/%{_dracutmodulesdir}/95suse-xfs/
install -m 0644 %{SOURCE4} %{buildroot}/%{_dracutmodulesdir}/95suse-xfs/

%if %{with systemd}
%pre -n xfsprogs-scrub
%service_add_pre xfs_scrub_all.service xfs_scrub_all.timer

%post -n xfsprogs-scrub
%service_add_post xfs_scrub_all.service xfs_scrub_all.timer

%preun -n xfsprogs-scrub
%service_del_preun xfs_scrub_all.service xfs_scrub_all.timer

%postun -n xfsprogs-scrub
%service_del_postun xfs_scrub_all.service xfs_scrub_all.timer
%endif

%post -n %{libname}
%{?regenerate_initrd_post}
/sbin/ldconfig

%postun -n %{libname}
%{?regenerate_initrd_post}
/sbin/ldconfig

%posttrans -n %{libname}
%{?regenerate_initrd_posttrans}

%files -f %{name}.lang
%defattr(-,root,root,755)
%{_sbindir}/*
%exclude %{_sbindir}/xfs_scrub_all
%{_mandir}/man[258]/*
%doc %{_defaultdocdir}/%{name}
%if 0%{?suse_version} >= 1315
# SLE12 doesn't do %license
%if 0%{?suse_version} > 1315 || 0%{?is_opensuse}
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.1
%endif
%endif
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%dir %{_dracutmodulesdir}/95suse-xfs/
%{_dracutmodulesdir}/95suse-xfs/dracut-fsck-help.txt
%{_dracutmodulesdir}/95suse-xfs/module-setup.sh
%dir %{_prefix}/share/xfsprogs/
%dir %{_prefix}/share/xfsprogs/mkfs
%{_prefix}/share/xfsprogs/mkfs/*

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/libhandle.so.*

%files -n xfsprogs-devel
%defattr(-,root,root,755)
%{_includedir}/xfs
%{_libdir}/libhandle.so
%{_mandir}/man3/*

%files -n xfsprogs-scrub
%defattr(-,root,root,755)
%dir %{_libdir}/xfsprogs/
%{_libdir}/xfsprogs/xfs_scrub_all.cron
%{_sbindir}/xfs_scrub_all
%if %{with systemd}
%{_libdir}/xfsprogs/xfs_scrub_fail
%{_unitdir}/xfs_scrub@.service
%{_unitdir}/xfs_scrub_all.service
%{_unitdir}/xfs_scrub_all.timer
%{_unitdir}/xfs_scrub_fail@.service
%endif

%changelog
