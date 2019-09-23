#
# spec file for package ntfs-3g_ntfsprogs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 88

Name:           ntfs-3g_ntfsprogs
Summary:        NTFS Support in Userspace
License:        GPL-2.0-or-later
Group:          System/Filesystems
Version:        2017.3.23
Release:        0
Source:         http://tuxera.com/opensource/%{name}-%{version}.tgz
Source2:        21-storage-ntfs-3g.fdi
Url:            http://www.tuxera.com/community/ntfs-3g-download/
BuildRequires:  autoconf
# SLES 11 is still supported
%if 0%{?sles_version} && 0%{?suse_version} == 1110
BuildRequires:  cpp48
BuildRequires:  fuse-devel >= 2.6.0
BuildRequires:  gcc48
%else
BuildRequires:  pkgconfig(fuse) >= 2.6.0
%endif
BuildRequires:  gnutls-devel
BuildRequires:  hwinfo-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NTFS-3G allows for read/write access to NTFS partitions which can be
shared with Windows XP, Windows Server 2003, Windows 2000, Windows
Vista and Windows Seven.

%package -n ntfs-3g
Summary:        NTFS Support in Userspace
License:        GPL-2.0-or-later
Group:          System/Filesystems
Provides:       ntfsprogs-fuse = 1.13.1
Obsoletes:      ntfsprogs-fuse < 1.13.1
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(preun): update-alternatives
Requires(postun): update-alternatives
Supplements:    filesystem(ntfs-3g)
%endif

%description -n ntfs-3g
NTFS-3G allows for read/write access to NTFS partitions which can be
shared with Windows XP, Windows Server 2003, Windows 2000, Windows
Vista and Windows Seven.

%package -n libntfs-3g%sover
Summary:        NTFS Support in Userspace -- Library
License:        LGPL-2.1-or-later
Group:          System/Filesystems

%description -n libntfs-3g%sover
NTFS-3G allows for read/write access to NTFS partitions which can be
shared with Windows XP, Windows Server 2003, Windows 2000, Windows
Vista and Windows Seven.

%package -n libntfs-3g-devel
Summary:        NTFS Support in Userspace -- Development Files
License:        LGPL-2.1-or-later
Group:          System/Filesystems
Requires:       glibc-devel
Requires:       libntfs-3g%sover = %{version}
Provides:       ntfs-3g-devel = %{version}
Obsoletes:      ntfs-3g-devel < %{version}

%description -n libntfs-3g-devel
NTFS-3G allows for read/write access to NTFS partitions which can be
shared with Windows XP, Windows Server 2003, Windows 2000, Windows
Vista and Windows Seven.

%package -n ntfsprogs
Summary:        NTFS Utilities
License:        GPL-2.0-or-later
Group:          System/Filesystems

%description -n ntfsprogs
The ntfsprogs includes utilities for doing all required tasks to NTFS
partitions. In general, just run a utility without any command line
options to display the version number and usage syntax.

%package -n ntfsprogs-extra
Summary:        NTFS Utilities which can damage your filesystem such that Windows can't read it
License:        GPL-2.0-or-later
Group:          System/Filesystems

%description -n ntfsprogs-extra
These are programs which are considered non-functional or only test-oriented.  They are kept in the source
tarball so that volunteers can capitalize on them for improvement.  

In particular ntfsck is just a place holder.  Distributions are expected not to recommend inserting a positive value in the last field of /etc/fstab for ntfs partitions.

They have been orphaned for ten years and are unlikely to be upgraded (except ntfsfallocate, if there is some demand). 

%prep
%setup -q
# Rebuild configure to pick up the updated AC_HEADER_MAJOR
autoconf

%build
%if 0%{?sles_version} && 0%{?suse_version} == 1110
export CC=gcc-4.8
export CXX=cpp-4.8
%endif
#
# regarding -Wno-sign-compare - checked with the Szaka: There is one variable
# which is signed and would possibly ok to be unsigned. Any solution to this
# needs to be carefully reviewed and tested, so we do not change the code now:
#
export CFLAGS="$RPM_OPT_FLAGS -Wformat -Wformat-security -W -Wno-sign-compare -fPIE"
export LDFLAGS="-pie"
%configure --exec-prefix=/ --disable-static --with-pic --disable-ldconfig \
	--with-fuse=external --enable-posix-acls \
	--enable-extras \
	--enable-crypto \
	--enable-quarantined
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
%{__rm} -v %{buildroot}%{_libdir}/libntfs-3g.la
# Hal stuff for mounting on hotplug.
%{__mkdir_p} %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor/
%{__install} -m 644 %{SOURCE2} %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor/21-storage-ntfs-3g.fdi
%if 0%{?sles_version} && 0%{?suse_version} == 1110
# Touch ghost files
touch %{buildroot}/sbin/mount.ntfs %{buildroot}%{_mandir}/man8/mount.ntfs.8
%else
# Alternatives for mount.ntfs (binary and manpage)
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/mount.ntfs %{buildroot}/sbin/mount.ntfs
ln -s -f %{_sysconfdir}/alternatives/mount.ntfs.8%{ext_man} %{buildroot}%{_mandir}/man8/mount.ntfs.8%{?ext_man}
%endif

%check
TESTFS=$(mktemp) || exit 1
ntfsprogs/mkntfs -q -F $TESTFS 3000
src/ntfs-3g.probe --readonly  $TESTFS
src/ntfs-3g.probe --readwrite $TESTFS
rm -v $TESTFS

# Workaround old bug in 11.1/11.2 packages that always removed the symlinks in
# %postun.
%if 0%{?sles_version} && 0%{?suse_version} == 1110
%posttrans -n ntfs-3g
if [ ! -f /sbin/mount.ntfs -a -f /sbin/mount.ntfs-3g ]; then
  update-alternatives --install /sbin/mount.ntfs mount.ntfs /sbin/mount.ntfs-3g 10 --slave /usr/share/man/man8/mount.ntfs.8.gz mount.ntfs.8.gz /usr/share/man/man8/mount.ntfs-3g.8.gz
fi
%endif

%post -n ntfs-3g
# If the mount.ntfs group is in automatic mode, then this will also switch all
# symlinks automatically
update-alternatives --install /sbin/mount.ntfs mount.ntfs /sbin/mount.ntfs-3g 10 --slave %{_mandir}/man8/mount.ntfs.8%{?ext_man} mount.ntfs.8%{?ext_man} %{_mandir}/man8/mount.ntfs-3g.8%{?ext_man}

%preun -n ntfs-3g
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f /sbin/mount.ntfs-3g ]; then
  update-alternatives --remove mount.ntfs /sbin/mount.ntfs-3g
fi

%post -n libntfs-3g%sover -p /sbin/ldconfig

%postun -n libntfs-3g%sover -p /sbin/ldconfig

%files -n ntfs-3g
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog CREDITS NEWS README
%license COPYING
%dir %{_datadir}/hal
%dir %{_datadir}/hal/fdi
%dir %{_datadir}/hal/fdi/policy
%dir %{_datadir}/hal/fdi/policy/10osvendor
%{_datadir}/hal/fdi/policy/10osvendor/21-storage-ntfs-3g.fdi
%{_bindir}/ntfs-3g
%{_bindir}/ntfs-3g.probe
%{_bindir}/ntfssecaudit
%{_bindir}/ntfsusermap
%{_bindir}/lowntfs-3g
%ghost /sbin/mount.ntfs
%if 0%{?suse_version} > 1110
%ghost %{_sysconfdir}/alternatives/mount.ntfs
%ghost %{_sysconfdir}/alternatives/mount.ntfs.8%{?ext_man}
%endif
/sbin/mount.ntfs-3g
/sbin/mount.lowntfs-3g
%{_mandir}/man8/mount.lowntfs-3g.8%{?ext_man}
%ghost %{_mandir}/man8/mount.ntfs.8%{?ext_man}
%{_mandir}/man8/mount.ntfs-3g.8%{?ext_man}
%{_mandir}/man8/ntfs-3g.8%{?ext_man}
%{_mandir}/man8/ntfs-3g.probe.8%{?ext_man}
%{_mandir}/man8/ntfssecaudit.8%{?ext_man}
%{_mandir}/man8/ntfsusermap.8%{?ext_man}
# We already have this, so no need to package it again.
%exclude /usr/share/doc/ntfs-3g/README

%files -n libntfs-3g%sover
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/libntfs-3g.so.*

%files -n libntfs-3g-devel
%defattr(-,root,root,-)
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so
%{_libdir}/pkgconfig/libntfs-3g.pc

%files -n ntfsprogs
%defattr(-, root, root)
%doc AUTHORS ChangeLog CREDITS NEWS README
%license COPYING
/sbin/mkfs.ntfs
%{_sbindir}/mkntfs
%{_sbindir}/ntfsclone
%{_sbindir}/ntfscp
%{_sbindir}/ntfslabel
%{_sbindir}/ntfsresize
%{_sbindir}/ntfsundelete
%{_bindir}/ntfscat
%{_bindir}/ntfscluster
%{_bindir}/ntfscmp
%{_bindir}/ntfsfix
%{_bindir}/ntfsinfo
%{_bindir}/ntfsls
%{_bindir}/ntfswipe
%{_bindir}/ntfstruncate
%{_bindir}/ntfsdecrypt
%{_bindir}/ntfsrecover
%{_mandir}/man8/mkfs.ntfs.8%{?ext_man}
%{_mandir}/man8/mkntfs.8%{?ext_man}
%{_mandir}/man8/ntfscat.8%{?ext_man}
%{_mandir}/man8/ntfsclone.8%{?ext_man}
%{_mandir}/man8/ntfscluster.8%{?ext_man}
%{_mandir}/man8/ntfscmp.8%{?ext_man}
%{_mandir}/man8/ntfscp.8%{?ext_man}
%{_mandir}/man8/ntfsdecrypt.8%{?ext_man}
%{_mandir}/man8/ntfsfix.8%{?ext_man}
%{_mandir}/man8/ntfsinfo.8%{?ext_man}
%{_mandir}/man8/ntfslabel.8%{?ext_man}
%{_mandir}/man8/ntfsls.8%{?ext_man}
%{_mandir}/man8/ntfsprogs.8%{?ext_man}
%{_mandir}/man8/ntfsresize.8%{?ext_man}
%{_mandir}/man8/ntfstruncate.8%{?ext_man}
%{_mandir}/man8/ntfsundelete.8%{?ext_man}
%{_mandir}/man8/ntfswipe.8%{?ext_man}
%{_mandir}/man8/ntfsrecover.8%{?ext_man}

%files -n ntfsprogs-extra
%defattr(-, root, root)
%doc AUTHORS ChangeLog CREDITS NEWS README
%license COPYING
%{_bindir}/ntfsck
%{_bindir}/ntfsdump_logfile
%{_bindir}/ntfsfallocate
%{_bindir}/ntfsmftalloc
%{_bindir}/ntfsmove
%{_mandir}/man8/ntfsfallocate.8%{?ext_man}

%changelog
