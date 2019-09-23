#
# spec file for package libblockdev
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         bcachetools_version 1.0.8
%define         somajor             2
%define         libname             %{name}%{somajor}
%bcond_with     python2

Name:           libblockdev
Version:        2.22
Release:        0
Summary:        A library for low-level manipulation with block devices
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/storaged-project/libblockdev
Source0:        https://github.com/storaged-project/libblockdev/releases/download/%{version}-1/libblockdev-%{version}.tar.gz
# PATCH-FIX-OPENSUSE libblockdev-fix-libkmod-include.patch luc14n0@linuxmail.org -- openSUSE's libkmod.h file location is not under the expected /usr/include directory but /usr/include/kmod.
Patch0:         libblockdev-fix-libkmod-include.patch
BuildRequires:  dmraid-devel
BuildRequires:  gobject-introspection-devel >= 1.3.0
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
%{?with_python2:BuildRequires: python-devel}
BuildRequires:  python3-devel
# There is a s390x plugin that, until vtoc.h is provided, can't be added.
#BuildRequires:  s390-tools-devel
BuildRequires:  pkgconfig(blkid) >= 2.23.0
BuildRequires:  pkgconfig(bytesize) >= 0.1
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(devmapper) >= 1.02.93
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.2
BuildRequires:  pkgconfig(gobject-2.0) >= 2.42.2
BuildRequires:  pkgconfig(libcryptsetup) >= 1.6.7
BuildRequires:  pkgconfig(libkmod) >= 19
BuildRequires:  pkgconfig(libparted) >= 3.1
BuildRequires:  pkgconfig(libudev) >= 216
BuildRequires:  pkgconfig(mount) >= 2.23.0
BuildRequires:  pkgconfig(yaml-0.1)
Requires:       %{libname} >= %{version}

%description
The LibBlockDev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices, like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of LibBlockDev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package -n     %{libname}
Summary:        A library for low-level manipulation with block devices
Group:          System/Libraries

%description -n %{libname}
The LibBlockDev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of LibBlockDev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package -n     typelib-1_0-BlockDev-2_0
Summary:        Introspection bindings for the LibBlockDev library
Group:          System/Libraries

%description -n typelib-1_0-BlockDev-2_0
This package provides the GObject Introspection bindings for LibBlockDev, which
provides low-level manipulation of block devices.

%package        devel
Summary:        Development files for the LibBlockDev library
Group:          Development/Libraries/C and C++
Requires:       %{libname} >= %{version}
Requires:       glib2-devel

%description    devel
This package provides header files, pkg-config modules and API documentation needed for
development with the LibBlockDev library.

%package -n     python2-%{name}
Summary:        Python2 gobject-introspection bindings for the LibBlockDev library
Group:          Development/Libraries/Python
Requires:       %{libname} >= %{version}
Requires:       python2-gobject

%description -n python2-%{name}
This package contains enhancements to the gobject-introspection bindings for
LibBlockDev in Python2.

%package -n     python3-%{name}
Summary:        Python3 gobject-introspection bindings for the LibBlockDev library
Group:          Development/Libraries/Python
Requires:       %{libname} >= %{version}
Requires:       python3-gobject

%description -n python3-%{name}
This package contains enhancements to the gobject-introspection bindings for
LibBlockDev in Python3.

%package -n     libbd_btrfs%{somajor}
Summary:        The BTRFS plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-btrfs = %{version}

%description -n libbd_btrfs%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides BTRFS-related functionality.

%package -n     libbd_btrfs-devel
Summary:        Development files for the libbd_btrfs plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_btrfs%{somajor} >= %{version}
Requires:       libbd_utils-devel
Provides:       libblockdev-btrfs-devel = %{version}

%description -n libbd_btrfs-devel
This package contains header files and pkg-config files needed for development
with the libbd_btrfs plugin/library.

%package -n     libbd_crypto%{somajor}
Summary:        The crypto plugin for the LibBlockDev library
Group:          System/Libraries
Provides:       libblockdev-crypto = %{version}

%description -n libbd_crypto%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to LUKS-style encrypted devices.

%package -n     libbd_crypto-devel
Summary:        Development files for the libbd_crypto plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_crypto%{somajor} >= %{version}
Provides:       libblockdev-crypto-devel = %{version}

%description -n libbd_crypto-devel
This package contains header files and pkg-config files needed for development
with the libbd_crypto plugin/library..

%package -n     libbd_dm%{somajor}
Summary:        The Device Mapper plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       device-mapper
Requires:       dmraid
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-dm = %{version}

%description -n libbd_dm%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to Device Mapper.

%package -n     libbd_dm-devel
Summary:        Development files for the libbd_dm plugin/library
Group:          Development/Libraries/C and C++
Requires:       device-mapper-devel
Requires:       dmraid-devel
Requires:       glib2-devel
Requires:       libbd_dm%{somajor} >= %{version}
Requires:       libbd_utils-devel
Requires:       systemd-devel
Provides:       libblockdev-dm-devel = %{version}

%description -n libbd_dm-devel
This package contains header files and pkg-config files needed for development
with the libbd_dm plugin/library..

%package -n     libbd_fs%{somajor}
Summary:        The FS plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       device-mapper
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-fs = %{version}

%description -n libbd_fs%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to operations with file systems.

%package -n     libbd_fs-devel
Summary:        Development files for the libbd_fs plugin/library
Group:          Development/Libraries/C and C++
Requires:       dosfstools
Requires:       glib2-devel
Requires:       libbd_fs%{somajor} >= %{version}
Requires:       libbd_utils-devel
Requires:       xfsprogs
Provides:       libblockdev-fs-devel = %{version}

%description -n libbd_fs-devel
This package contains header files and pkg-config files needed for development
with the libbd_fs plugin/library..

%package -n     libbd_kbd%{somajor}
Summary:        The KBD plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       bcache-tools >= %{bcachetools_version}
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-kbd = %{version}

%description -n libbd_kbd%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to kernel block devices, namely zRAM and
Bcache.

%package -n     libbd_kbd-devel
Summary:        Development files for the libbd_kbd plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_kbd%{somajor} >= %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-kbd-devel = %{version}

%description -n libbd_kbd-devel
This package contains header files and pkg-config files needed for development
with the libbd_kbd plugin/library..

%package -n     libbd_loop%{somajor}
Summary:        The loop plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-loop = %{version}

%description -n libbd_loop%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to loop devices.

%package -n     libbd_loop-devel
Summary:        Development files for the libblockdev-loop plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_loop%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-loop-devel = %{version}

%description -n libbd_loop-devel
This package contains header files and pkg-config files needed for development
with the libbd_loop plugin/library.

%package -n     libbd_lvm%{somajor}
Summary:        The LVM plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       lvm2
# For thin_metadata_size.
Requires:       thin-provisioning-tools
Provides:       libblockdev-lvm = %{version}

%description -n libbd_lvm%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides LVM-related functionality.

%package -n     libbd_lvm-devel
Summary:        Development files for the libblockdev-lvm plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_lvm%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-lvm-devel = %{version}

%description -n libbd_lvm-devel
This package contains header files and pkg-config files needed for development
with the libbd_lvm plugin/library.

%package -n     libbd_lvm-dbus%{somajor}
Summary:        The LVM plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       lvm2
# For thin_metadata_size.
Requires:       thin-provisioning-tools
Provides:       libblockdev-lvm-dbus = %{version}

%description -n libbd_lvm-dbus%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides LVM-related functionality utilizing the LVM DBus API.

%package -n     libbd_lvm-dbus-devel
Summary:        Development files for the libblockdev-lvm-dbus plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_lvm-dbus%{somajor} = %{version}
Requires:       libbd_lvm-devel >= %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-lvm-dbus-devel = %{version}

%description -n libbd_lvm-dbus-devel
This package contains header files and pkg-config files needed for development
with the libbd_lvm-dbus plugin/library.

%package -n     libbd_mdraid%{somajor}
Summary:        The MD RAID plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       mdadm
Provides:       libblockdev-mdraid = %{version}

%description -n libbd_mdraid%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to MD RAID.

%package -n     libbd_mdraid-devel
Summary:        Development files for the libblockdev-mdraid plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_mdraid%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-mdraid-devel = %{version}

%description -n libbd_mdraid-devel
This package contains header files and pkg-config files needed for development
with the libbd_mdraid plugin/library.

%package -n     libbd_mpath%{somajor}
Summary:        The multipath plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       multipath-tools
Provides:       libblockdev-mpath = %{version}

%description -n libbd_mpath%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to multipath devices.

%package -n     libbd_mpath-devel
Summary:        Development files for the libblockdev-mpath plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_mpath%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-mpath-devel = %{version}

%description -n libbd_mpath-devel
This package contains header files and pkg-config files needed for development
with the libbd_mpath plugin/library.

%package -n     libbd_part%{somajor}
Summary:        The partitioning plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       gptfdisk
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       multipath-tools
Requires:       util-linux
Provides:       libblockdev-part = %{version}

%description -n libbd_part%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to partitioning.

%package -n     libbd_part-devel
Summary:        Development files for the libblockdev-part plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_part%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-part-devel = %{version}

%description -n libbd_part-devel
This package contains header files and pkg-config files needed for development
with the libbd_part plugin/library.

%package -n     libbd_swap%{somajor}
Summary:        The swap plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Requires:       util-linux
Provides:       libblockdev-swap = %{version}

%description -n libbd_swap%{somajor}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to swap devices.

%package -n     libbd_swap-devel
Summary:        Development files for the libblockdev-swap plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_swap%{somajor} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-swap-devel = %{version}

%description -n libbd_swap-devel
This package contains header files and pkg-config files needed for development
with the libbd_swap plugin/library.

%package -n     libbd_utils%{somajor}
Summary:        Utility functions library for the LibBlockDev library
Group:          System/Libraries

%description -n libbd_utils%{somajor}
libbd_utils is a library providing utility functions used by the
LibBlockDev library and its plugins.

%package -n     libbd_utils-devel
Summary:        Development files for libbd_utils
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_utils%{somajor} >= %{version}

%description -n libbd_utils-devel
This package contains header files and pkg-config files needed for development
with the libbd_utils library.

%package -n     libbd_vdo%{somajor}
Summary:        The VDO plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{somajor} >= %{version}
Provides:       libblockdev-vdo = %{version}

%description -n libbd_vdo%{somajor}
The VDO library plugin (and, at the same time, a standalone library)
provides functionality related to the Virtual Data Optimizer,
a software for creating compressed and deduplicated pools of
block storage.

%package -n     libbd_vdo-devel
Summary:        Development files for the libblockdev-vdo plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_utils-devel >= %{version}
Requires:       libbd_vdo%{somajor} = %{version}
Provides:       libblockdev-vdo-devel = %{version}

%description -n libbd_vdo-devel
This package contains header files and pkg-config files needed for development
with the libbd_vdo plugin/library.

%prep
%autosetup -p1

%build
%configure \
        --disable-static \
        --enable-introspection \
        --with-bcache \
        --with-btrfs \
        --with-crypto \
        --with-dm \
        --with-dmraid \
        --with-fs \
        --with-gtk-doc \
        --with-kbd \
        --with-loop \
        --with-lvm \
        --with-lvm_dbus \
        --with-mdraid \
        --with-mpath \
        --with-part \
        --with-swap \
        --with-vdo \
        --without-escrow \
        --without-nvdimm \
        %{nil}
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -print -type f -delete

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post   -n libbd_btrfs%{somajor} -p /sbin/ldconfig
%postun -n libbd_btrfs%{somajor} -p /sbin/ldconfig

%post   -n libbd_crypto%{somajor} -p /sbin/ldconfig
%postun -n libbd_crypto%{somajor} -p /sbin/ldconfig

%post   -n libbd_dm%{somajor} -p /sbin/ldconfig
%postun -n libbd_dm%{somajor} -p /sbin/ldconfig

%post   -n libbd_fs%{somajor} -p /sbin/ldconfig
%postun -n libbd_fs%{somajor} -p /sbin/ldconfig

%post   -n libbd_kbd%{somajor} -p /sbin/ldconfig
%postun -n libbd_kbd%{somajor} -p /sbin/ldconfig

%post   -n libbd_loop%{somajor} -p /sbin/ldconfig
%postun -n libbd_loop%{somajor} -p /sbin/ldconfig

%post   -n libbd_lvm%{somajor} -p /sbin/ldconfig
%postun -n libbd_lvm%{somajor} -p /sbin/ldconfig

%post   -n libbd_lvm-dbus%{somajor} -p /sbin/ldconfig
%postun -n libbd_lvm-dbus%{somajor} -p /sbin/ldconfig

%post   -n libbd_mdraid%{somajor} -p /sbin/ldconfig
%postun -n libbd_mdraid%{somajor} -p /sbin/ldconfig

%post   -n libbd_mpath%{somajor} -p /sbin/ldconfig
%postun -n libbd_mpath%{somajor} -p /sbin/ldconfig

%post   -n libbd_part%{somajor} -p /sbin/ldconfig
%postun -n libbd_part%{somajor} -p /sbin/ldconfig

%post   -n libbd_swap%{somajor} -p /sbin/ldconfig
%postun -n libbd_swap%{somajor} -p /sbin/ldconfig

%post   -n libbd_utils%{somajor} -p /sbin/ldconfig
%postun -n libbd_utils%{somajor} -p /sbin/ldconfig

%post   -n libbd_vdo%{somajor} -p /sbin/ldconfig
%postun -n libbd_vdo%{somajor} -p /sbin/ldconfig

%files
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/conf.d
%config %{_sysconfdir}/libblockdev/conf.d/00-default.cfg
%{_bindir}/lvm-cache-stats

%files -n %{libname}
%license LICENSE
%{_libdir}/libblockdev.so.%{somajor}*

%files -n typelib-1_0-BlockDev-2_0
%{_libdir}/girepository-1.0/BlockDev-2.0.typelib

%files devel
%doc features.rst specs.rst
%doc %{_datadir}/gtk-doc/html/libblockdev
%{_libdir}/libblockdev.so
%{_libdir}/pkgconfig/blockdev.pc
%{_datadir}/gir-1.0/BlockDev-2.0.gir
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/plugins.h

%if %{with python2}
%files -n python2-%{name}
%dir %{python2_sitearch}/gi
%dir %{python2_sitearch}/gi/overrides
%{python2_sitearch}/gi/overrides/BlockDev.py
%endif

%files -n python3-%{name}
%dir %{python3_sitearch}/gi
%dir %{python3_sitearch}/gi/overrides
%{python3_sitearch}/gi/overrides/BlockDev.py

%files -n libbd_btrfs%{somajor}
%{_libdir}/libbd_btrfs.so.%{somajor}*

%files -n libbd_btrfs-devel
%{_libdir}/libbd_btrfs.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/btrfs.h

%files -n libbd_crypto%{somajor}
%{_libdir}/libbd_crypto.so.%{somajor}*

%files -n libbd_crypto-devel
%{_libdir}/libbd_crypto.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/crypto.h

%files -n libbd_dm%{somajor}
%{_libdir}/libbd_dm.so.%{somajor}*

%files -n libbd_dm-devel
%{_libdir}/libbd_dm.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/dm.h

%files -n libbd_fs%{somajor}
%{_libdir}/libbd_fs.so.%{somajor}*

%files -n libbd_fs-devel
%{_libdir}/libbd_fs.so
%dir %{_includedir}/blockdev
%dir %{_includedir}/blockdev/fs
%{_includedir}/blockdev/fs.h
%{_includedir}/blockdev/fs/ext.h
%{_includedir}/blockdev/fs/generic.h
%{_includedir}/blockdev/fs/mount.h
%{_includedir}/blockdev/fs/ntfs.h
%{_includedir}/blockdev/fs/vfat.h
%{_includedir}/blockdev/fs/xfs.h

%files -n libbd_kbd%{somajor}
%{_libdir}/libbd_kbd.so.%{somajor}*

%files -n libbd_kbd-devel
%{_libdir}/libbd_kbd.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/kbd.h

%files -n libbd_loop%{somajor}
%{_libdir}/libbd_loop.so.%{somajor}*

%files -n libbd_loop-devel
%{_libdir}/libbd_loop.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/loop.h

%files -n libbd_lvm%{somajor}
%{_libdir}/libbd_lvm.so.%{somajor}*

%files -n libbd_lvm-devel
%{_libdir}/libbd_lvm.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/lvm.h

%files -n libbd_lvm-dbus%{somajor}
%{_libdir}/libbd_lvm-dbus.so.%{somajor}*
%config %{_sysconfdir}/libblockdev/conf.d/10-lvm-dbus.cfg

%files -n libbd_lvm-dbus-devel
%{_libdir}/libbd_lvm-dbus.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/dbus.h

%files -n libbd_mdraid%{somajor}
%{_libdir}/libbd_mdraid.so.%{somajor}*

%files -n libbd_mdraid-devel
%{_libdir}/libbd_mdraid.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/mdraid.h

%files -n libbd_mpath%{somajor}
%{_libdir}/libbd_mpath.so.%{somajor}*

%files -n libbd_mpath-devel
%{_libdir}/libbd_mpath.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/mpath.h

%files -n libbd_part%{somajor}
%{_libdir}/libbd_part.so.%{somajor}*

%files -n libbd_part-devel
%{_libdir}/libbd_part.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/part.h

%files -n libbd_swap%{somajor}
%{_libdir}/libbd_swap.so.%{somajor}*

%files -n libbd_swap-devel
%{_libdir}/libbd_swap.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/swap.h

%files -n libbd_utils%{somajor}
%{_libdir}/libbd_part_err.so.%{somajor}*
%{_libdir}/libbd_utils.so.%{somajor}*

%files -n libbd_utils-devel
%{_libdir}/libbd_utils.so
%{_libdir}/libbd_part_err.so
%{_libdir}/pkgconfig/blockdev-utils.pc
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/utils.h
%{_includedir}/blockdev/sizes.h
%{_includedir}/blockdev/exec.h
%{_includedir}/blockdev/extra_arg.h
%{_includedir}/blockdev/dev_utils.h
%{_includedir}/blockdev/module.h

%files -n libbd_vdo%{somajor}
%{_libdir}/libbd_vdo.so.%{somajor}*

%files -n libbd_vdo-devel
%{_libdir}/libbd_vdo.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/vdo.h

%changelog
