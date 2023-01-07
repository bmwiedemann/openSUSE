#
# spec file for package btrfsprogs
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


%define udev_with_btrfs_builtin 190
%define udev_version %(pkg-config --modversion udev)
%define package_udev_rules %{udev_version} >= %{udev_with_btrfs_builtin}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

# enable building of btrfsprogs-static
%if 0%{?suse_version} <= 1310 || 0%{?suse_version} == 1315
%define build_static	0
%else
%define build_static	1
%endif

# the tarball contains prebuilt documentation
%define build_docs	1

%define _dracutmodulesdir %(pkg-config --variable dracutmodulesdir dracut)

Name:           btrfsprogs
Version:        6.1.2
Release:        0
Summary:        Utilities for the Btrfs filesystem
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://btrfs.wiki.kernel.org/
#Git-Web:	http://git.kernel.org/cgit/linux/kernel/git/kdave/btrfs-progs.git
#Git-Clone:	git://git.kernel.org/pub/scm/linux/kernel/git/kdave/btrfs-progs
Source:         https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v%{version}.tar.gz
Source100:      https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v%{version}.tar.sign
Source101:      btrfsprogs.keyring
# support for mkinitrd in < 13.1
Source1:        boot-btrfs.sh
Source2:        module-setup.sh.in
Source3:        dracut-fsck-help.txt
Source4:        setup-btrfs.sh
# Alias that matches the upstream project name
Provides:       btrfs-progs = %{version}-%{release}
Provides:       btrfs-progs(%_arch) = %{version}-%{release}

Patch1:         mkfs-default-features.patch

%if %build_docs
BuildRequires:  python3-Sphinx
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dracut
BuildRequires:  libattr-devel
BuildRequires:  libblkid-devel
BuildRequires:  libext2fs-devel
%if 0%{?suse_version} == 1500
BuildRequires:  libreiserfscore-devel >= 3.6.27
Requires:       libreiserfscore0 >= 3.6.27
%endif
BuildRequires:  libuuid-devel
%if 0%{?suse_version} > 1500
BuildRequires:  libzstd-devel
%endif
BuildRequires:  lzo-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1310
BuildRequires:  suse-module-tools
%endif
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig(udev)
%if %build_docs
BuildRequires:  xmlto
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1310
Requires(post): coreutils
Requires(postun):coreutils
%endif
Supplements:    filesystem(btrfs)
Recommends:     btrfsmaintenance
%if %{package_udev_rules}
Requires:       btrfsprogs-udev-rules
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities needed to create and maintain btrfs file systems under Linux.

%if %build_static
%package -n btrfsprogs-static
Summary:        Static build of utilities for the Btrfs filesystem
Group:          System/Filesystems
Provides:       btrfs-progs-static = %{version}-%{release}
Provides:       btrfs-progs-static(%_arch) = %{version}-%{release}
BuildRequires:  glibc-devel-static
BuildRequires:  libblkid-devel-static
BuildRequires:  libcom_err-devel-static
BuildRequires:  libext2fs-devel-static
BuildRequires:  libuuid-devel-static
%if 0%{?suse_version} > 1500
BuildRequires:  libzstd-devel-static
%endif
BuildRequires:  lzo-devel-static
BuildRequires:  zlib-devel-static

%description -n btrfsprogs-static
Static build of utilities needed to create and maintain btrfs file systems
under Linux. Suitable for limited or rescue environments.

Warning: the zlib and lzo libraries are statically linked in and may lack
important updates
%endif

%package -n libbtrfs0
Summary:        Library for interacting with Btrfs
Group:          System/Libraries

%description -n libbtrfs0
This package contains the libbtrfs.so shared library needed for some
applications to interface with btrfs.

%package -n libbtrfs-devel
Summary:        Include Files and Libraries for developing with Btrfs
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libbtrfs0 = %{version}

%description -n libbtrfs-devel
This package contains the libraries and headers files for developers to
build applications to interface with Btrfs.

# rpm < 4.6.0 (SLE11 uses 4.4) doesn't support noarch subpackages.
# Fortunately, it doesn't use systemd either so we can just skip it.
%if %{package_udev_rules}
%package udev-rules
Summary:        Udev rules for configuring btrfs file systems
Group:          System/Kernel
Conflicts:      udev < %{udev_with_btrfs_builtin}
BuildArch:      noarch

%description udev-rules
This package contains the udev rule file for configuring device mapper
devices that are components of btrfs file systems.  It is meant to be
used with versions of udev that contain the "built-in" btrfs command
(v190 and newer).  Older versions of udev will call the version of
"btrfs ready" contained in the btrfsprogs package, which does the right
thing.
%endif

%package -n libbtrfsutil1
Summary:        Utility library for interacting with Btrfs
Group:          System/Libraries

%description -n libbtrfsutil1
This package contains the libbtrfsutil.so shared library. This library is
LGPL unlike libbtrfs.so and can be used by applications to interact with Btrfs
filesystems.

%package -n libbtrfsutil-devel
Summary:        Include Files and Libraries for developing with libbtrfsutil
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libbtrfsutil1 = %{version}

%description -n libbtrfsutil-devel
This package contains the libraries and headers files for developers to
build applications to interface with Btrfs using libbtrfsutil.

%package -n python-btrfsutil
Summary:        Python bindings for developing with libbtrfsutil
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
Requires:       libbtrfsutil1 = %{version}
Requires:       python3
BuildRequires:  %{python_module setuptools}
BuildRequires:  pkgconfig(python3)

%description -n python-btrfsutil
This package contains the python bindings to build applications to interface
with Btrfs using libbtrfsutil.

%prep
%setup -q -n btrfs-progs-v%{version}
%patch1 -p1

%build
./autogen.sh

%configure			\
			--enable-python	\
%if !%{build_docs}
			--disable-documentation	\
%endif
%if 0%{?suse_version} <= 1500
			--disable-zoned	\
			--disable-zstd
%endif

make V=1 %{?_smp_mflags} all \
%if %{build_static}
			static
%endif

%install
make install		\
%if %{build_static}
	install-static 	\
%endif
	DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir} libdir=%{_libdir} \
	install_python

%if !%{build_docs}
cd Documentation
install -m 0755 -d %{buildroot}/%{_mandir}/man5
install -m 0755 -d %{buildroot}/%{_mandir}/man8
install -m 0644 *.5 %{buildroot}/%{_mandir}/man5
install -m 0644 *.8 %{buildroot}/%{_mandir}/man8
cd ..
%endif

%if %{build_static}
make install-static DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir} libdir=%{_libdir}
%endif

install -m 0755 -d %{buildroot}/%{_sbindir}
install -m 0755 -d %{buildroot}/%{_bindir}
# move some utilities out of /usr/sbin
mv %{buildroot}/%{_sbindir}/btrfs-map-logical %{buildroot}/%{_bindir}
# initrd rescue utilities
install -m 0755 btrfs-select-super %{buildroot}/%{_sbindir}
install -m 0755 btrfs-image %{buildroot}/%{_sbindir}
install -m 0755 btrfstune %{buildroot}/%{_sbindir}
install -m 0755 btrfs-find-root %{buildroot}/%{_sbindir}
%if 0%{?suse_version} < 1550
install -m 0755 -d %{buildroot}/sbin
ln -s %{_sbindir}/btrfs %{buildroot}/sbin
ln -s %{_sbindir}/btrfs-convert %{buildroot}/sbin
ln -s %{_sbindir}/btrfs-select-super %{buildroot}/sbin
ln -s %{_sbindir}/btrfs-image %{buildroot}/sbin
ln -s %{_sbindir}/btrfstune %{buildroot}/sbin
ln -s %{_sbindir}/btrfsck %{buildroot}/sbin
ln -s %{_sbindir}/btrfs-find-root %{buildroot}/sbin
ln -s %{_sbindir}/mkfs.btrfs %{buildroot}/sbin
ln -s %{_sbindir}/fsck.btrfs %{buildroot}/sbin
%endif
%if 0%{?suse_version} < 1310
install -d -m0755 %{buildroot}/lib/mkinitrd/scripts/
install -m 0755 %{SOURCE1} %{buildroot}/lib/mkinitrd/scripts/
install -m 0755 %{SOURCE4} %{buildroot}/lib/mkinitrd/scripts/
%endif
# don't install .a for now
rm -f %{buildroot}/%{_libdir}/*.a
# bash completion
install -m 0755 -d %{buildroot}/%{_datadir}/bash-completion/completions
install -m 0644 btrfs-completion %{buildroot}/%{_datadir}/bash-completion/completions/btrfs
sed -e 's,@@INSTALLDIR@@,%{_datadir}/%{name}/,;' %{SOURCE2} > module-setup.sh
install -m 0755 -D module-setup.sh %{buildroot}/%{_dracutmodulesdir}/95suse-btrfs/module-setup.sh
rm -f module-setup.sh
install -m 0644 -D %{SOURCE3} %{buildroot}/%{_datadir}/%{name}/dracut-fsck-help.txt

%if 0%{!?for_debugging:1}
DEBUG_FILES="/sbin/btrfs-find-root
  %{_sbindir}/btrfs-find-root
  %{_mandir}/man8/btrfs-find-root.8
  /sbin/btrfs-select-super
  %{_sbindir}/btrfs-select-super"
for file in $DEBUG_FILES; do
  rm -f %{buildroot}$file
done
%endif

%post -n libbtrfs0 -p /sbin/ldconfig

%postun -n libbtrfs0 -p /sbin/ldconfig

%post -n libbtrfsutil1 -p /sbin/ldconfig

%postun -n libbtrfsutil1 -p /sbin/ldconfig

%if 0%{?suse_version} >= 1310
%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}
%endif

%files
%defattr(-, root, root)
%license COPYING
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dracut-fsck-help.txt
%dir %{_dracutmodulesdir}/95suse-btrfs/
%{_dracutmodulesdir}/95suse-btrfs/module-setup.sh
%if 0%{?suse_version} < 1550
/sbin/fsck.btrfs
# mkinitrd utils
/sbin/btrfs
/sbin/btrfs-convert
/sbin/btrfs-image
/sbin/btrfstune
/sbin/btrfsck
/sbin/mkfs.btrfs
%endif
%{_sbindir}/btrfs
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-image
%{_sbindir}/btrfstune
%{_sbindir}/btrfsck
%{_sbindir}/fsck.btrfs
%{_sbindir}/mkfs.btrfs
%if 0%{?suse_version} < 1310
%dir /lib/mkinitrd
%dir /lib/mkinitrd/scripts
/lib/mkinitrd/scripts/boot-btrfs.sh
/lib/mkinitrd/scripts/setup-btrfs.sh
%endif
%{_bindir}/btrfs-map-logical
%{_mandir}/man8/btrfs-image.8%{?ext_man}
%{_mandir}/man8/btrfsck.8%{?ext_man}
%{_mandir}/man8/fsck.btrfs.8%{?ext_man}
%{_mandir}/man8/mkfs.btrfs.8%{?ext_man}
%{_mandir}/man8/btrfs.8%{?ext_man}
%{_mandir}/man5/btrfs.5%{?ext_man}
%{_mandir}/man8/btrfs-convert.8%{?ext_man}
%{_mandir}/man8/btrfs-map-logical.8%{?ext_man}
%{_mandir}/man8/btrfstune.8%{?ext_man}
%{_mandir}/man8/btrfs-balance.8%{?ext_man}
%{_mandir}/man8/btrfs-check.8%{?ext_man}
%{_mandir}/man8/btrfs-device.8%{?ext_man}
%{_mandir}/man8/btrfs-filesystem.8%{?ext_man}
%{_mandir}/man8/btrfs-inspect-internal.8%{?ext_man}
%{_mandir}/man8/btrfs-property.8%{?ext_man}
%{_mandir}/man8/btrfs-qgroup.8%{?ext_man}
%{_mandir}/man8/btrfs-quota.8%{?ext_man}
%{_mandir}/man8/btrfs-receive.8%{?ext_man}
%{_mandir}/man8/btrfs-replace.8%{?ext_man}
%{_mandir}/man8/btrfs-rescue.8%{?ext_man}
%{_mandir}/man8/btrfs-restore.8%{?ext_man}
%{_mandir}/man8/btrfs-scrub.8%{?ext_man}
%{_mandir}/man8/btrfs-send.8%{?ext_man}
%{_mandir}/man8/btrfs-subvolume.8%{?ext_man}
%{_mandir}/man8/btrfs-select-super.8%{?ext_man}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/btrfs

%if 0%{?for_debugging:1}
/sbin/btrfs-find-root
%{_sbindir}/btrfs-find-root
%{_mandir}/man8/btrfs-find-root.8%{?ext_man}
/sbin/btrfs-select-super
%{_sbindir}/btrfs-select-super
%endif

%if %{build_static}
%files -n btrfsprogs-static
%defattr(-, root, root)
%{_sbindir}/btrfs.static
%{_sbindir}/btrfs-convert.static
%{_sbindir}/btrfs-image.static
%{_sbindir}/btrfstune.static
%{_sbindir}/btrfsck.static
%{_sbindir}/mkfs.btrfs.static
%{_sbindir}/btrfs-corrupt-block.static
%{_sbindir}/btrfs-find-root.static
%{_sbindir}/btrfs-map-logical.static
%{_sbindir}/btrfs-select-super.static
%endif

%files -n libbtrfs0
%defattr(-, root, root)
%{_libdir}/libbtrfs.so.*

%files -n libbtrfs-devel
%defattr(-, root, root)
%dir %{_includedir}/btrfs
%{_includedir}/btrfs/*
%{_libdir}/libbtrfs.so

%files -n libbtrfsutil1
%defattr(-, root, root)
%{_libdir}/libbtrfsutil.so.*

%files -n libbtrfsutil-devel
%defattr(-, root, root)
%{_includedir}/btrfsutil.h
%{_libdir}/libbtrfsutil.so
%{_libdir}/pkgconfig/libbtrfsutil.pc

%if %{package_udev_rules}
%files udev-rules
%defattr(-, root, root)
%dir %{_udevrulesdir}
%{_udevrulesdir}/64-btrfs-dm.rules
%{_udevrulesdir}/64-btrfs-zoned.rules
%endif

%files -n python-btrfsutil
%{python3_sitearch}/*

%changelog
