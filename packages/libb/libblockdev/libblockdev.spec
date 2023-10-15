#
# spec file for package libblockdev
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


### PLUGINS ###
%bcond_without  btrfs_plugin
%bcond_without  crypto_plugin
%bcond_without  dm_plugin
%bcond_with     escrow_plugin
%bcond_without  fs_plugin
%bcond_without  loop_plugin
%bcond_without  lvm_plugin
%bcond_without  lvmdbus_plugin
%bcond_without  mdraid_plugin
%bcond_without  mpath_plugin
%bcond_with     nvdimm_plugin
%bcond_without  nvme_plugin
%bcond_without  part_plugin
%bcond_without  swap_plugin
###
%bcond_without  gi_bindings
%bcond_without  gtk_doc
%bcond_without  python_bindings
%bcond_without  utils
%bcond_without  tools

%define         soversion  3

Name:           libblockdev
Version:        3.0.4
Release:        0
Summary:        A library for low-level manipulation with block devices
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/storaged-project/libblockdev
Source0:        %{url}/releases/download/%{version}-1/libblockdev-%{version}.tar.gz
Source1:        %{url}/raw/%{version}-1/NEWS.rst

###############################################################################
#                          M A I N  P A C K A G E
###############################################################################

%if %{with gtk_doc}
BuildRequires:  gtk-doc
%endif
BuildRequires:  pkgconfig
BuildRequires:  (gcc >= 11 or gcc11)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(fdisk)
BuildRequires:  pkgconfig(libnvme) >= 1.3
# There is a s390x plugin that, until vtoc.h is provided by s390-tools*, can't
# be added:
#   https://github.com/ibm-s390-linux/s390-tools/blob/master/include/lib/vtoc.h
#BuildRequires:  s390-tools-devel
BuildRequires:  pkgconfig(blkid) >= 2.23.0
BuildRequires:  pkgconfig(bytesize) >= 0.1
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(devmapper) >= 1.02.93
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.2
BuildRequires:  pkgconfig(gobject-2.0) >= 2.42.2
BuildRequires:  pkgconfig(libcryptsetup) >= 2.3.0
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libkmod) >= 19
BuildRequires:  pkgconfig(libparted) >= 3.1
BuildRequires:  pkgconfig(libudev) >= 216
BuildRequires:  pkgconfig(mount) >= 2.23.0
BuildRequires:  pkgconfig(yaml-0.1)
Requires:       libblockdev%{soversion} >= %{version}
%if %{with tools}
### lvm-cache-stats binary needs LVM's plugin to work (boo#1183948) ###
Requires:       libblockdev-lvm >= %{version}
%endif

%description
The LibBlockDev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices, like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of LibBlockDev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%files
%doc NEWS.rst
%{_bindir}/lvm-cache-stats
%{_bindir}/vfat-resize
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/%{soversion}
%dir %{_sysconfdir}/libblockdev/%{soversion}/conf.d
%config %{_sysconfdir}/libblockdev/%{soversion}/conf.d/10-lvm-dbus.cfg
%config %{_sysconfdir}/libblockdev/%{soversion}/conf.d/00-default.cfg

###############################################################################
#                            D E V E L  F I L E S
###############################################################################

%package        devel
Summary:        Development files for the LibBlockDev library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libblockdev%{soversion} >= %{version}

%description    devel
This package provides header files, pkg-config modules and API documentation
needed for development with the LibBlockDev library.

%files devel
%doc %{_datadir}/gtk-doc/html/libblockdev
%{_libdir}/libblockdev.so
%{_libdir}/pkgconfig/blockdev.pc
%{_datadir}/gir-1.0/BlockDev-%{soversion}.0.gir
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/plugins.h
%{_includedir}/blockdev/logging.h
%ifarch s390x
%{_includedir}/blockdev/s390.h
%endif

###############################################################################
#                         S H A R E D  L I B R A R Y
###############################################################################

%package -n     libblockdev%{soversion}
Summary:        A library for low-level manipulation with block devices
Group:          System/Libraries

%description -n libblockdev%{soversion}
The LibBlockDev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of LibBlockDev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%ldconfig_scriptlets -n libblockdev%{soversion}

%files -n libblockdev%{soversion}
%license LICENSE
%{_libdir}/libblockdev.so.%{soversion}
%{_libdir}/libblockdev.so.%{soversion}.?.?
%ifarch s390x
%{_libdir}/libbd_s390.so.%{soversion}
%{_libdir}/libbd_s390.so.%{soversion}.?.?
%endif

###############################################################################
#         G O B J E C T  I N T R O S P E C T I O N  B I N D I N G S
###############################################################################

%if %{with gi_bindings}
%package -n     typelib-1_0-BlockDev-%{soversion}_0
Summary:        GI bindings for the LibBlockDev library
Group:          System/Libraries
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.3.0

%description -n typelib-1_0-BlockDev-%{soversion}_0
This package provides the GObject Introspection bindings for LibBlockDev, which
provides low-level manipulation of block devices.

%files -n typelib-1_0-BlockDev-%{soversion}_0
%{_libdir}/girepository-1.0/BlockDev-%{soversion}.0.typelib

###############################################################################
#                     P Y T H O N  3  B I N D I N G S
###############################################################################

%if %{with python_bindings}
%package -n     python3-%{name}
Summary:        Python 3 GI bindings for the LibBlockDev library
Group:          Development/Libraries/Python
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       python3-bytesize
Requires:       python3-gobject

%description -n python3-%{name}
This package contains enhancements to the GObject Introspection bindings for
LibBlockDev, in Python 3.

%files -n python3-%{name}
%{python3_sitearch}/gi/overrides/BlockDev.py
%endif
%endif

###############################################################################
#                           B T R F S  P L U G I N
###############################################################################

%if %{with btrfs_plugin}
%package -n     libbd_btrfs%{soversion}
Summary:        The Btrfs plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-btrfs = %{version}

%description -n libbd_btrfs%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides Btrfs-related functionality.

%files -n libbd_btrfs%{soversion} -f btrfs-plugin.filelist

%package -n     libbd_btrfs-devel
Summary:        Development files for the libbd_btrfs plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_btrfs%{soversion} >= %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-btrfs-devel = %{version}

%description -n libbd_btrfs-devel
This package contains header files and pkg-config files needed for development
with the libbd_btrfs plugin/library.

%ldconfig_scriptlets -n libbd_btrfs%{soversion}

%files -n libbd_btrfs-devel -f btrfs-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                          C R Y P T O  P L U G I N
###############################################################################

%if %{with crypto_plugin}
%package -n     libbd_crypto%{soversion}
Summary:        The Crypto plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-crypto = %{version}

%description -n libbd_crypto%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to LUKS-style encrypted devices.

%ldconfig_scriptlets -n libbd_crypto%{soversion}

%files -n libbd_crypto%{soversion} -f crypto-plugin.filelist

%package -n     libbd_crypto-devel
Summary:        Development files for the libbd_crypto plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_crypto%{soversion} >= %{version}
Provides:       libblockdev-crypto-devel = %{version}

%description -n libbd_crypto-devel
This package contains header files and pkg-config files needed for development
with the libbd_crypto plugin/library..

%files -n libbd_crypto-devel -f crypto-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                   D E V I C E  M A P P E R  P L U G I N
###############################################################################

%if %{with dm_plugin}
%package -n     libbd_dm%{soversion}
Summary:        The Device Mapper plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       device-mapper
Requires:       dmraid
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-dm = %{version}

%description -n libbd_dm%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to Device Mapper.

%ldconfig_scriptlets -n libbd_dm%{soversion}

%files -n libbd_dm%{soversion} -f dm-plugin.filelist

%package -n     libbd_dm-devel
Summary:        Development files for the libbd_dm plugin/library
Group:          Development/Libraries/C and C++
Requires:       device-mapper-devel
Requires:       dmraid-devel
Requires:       glib2-devel
Requires:       libbd_dm%{soversion} >= %{version}
Requires:       libbd_utils-devel
Requires:       systemd-devel
Provides:       libblockdev-dm-devel = %{version}

%description -n libbd_dm-devel
This package contains header files and pkg-config files needed for development
with the libbd_dm plugin/library..

%files -n libbd_dm-devel -f dm-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                     F I L E  S Y S T E M  P L U G I N
###############################################################################

%if %{with fs_plugin}
%package -n     libbd_fs%{soversion}
Summary:        The FS plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       device-mapper
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-fs = %{version}

%description -n libbd_fs%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to operations with file systems.

%ldconfig_scriptlets -n libbd_fs%{soversion}

%files -n libbd_fs%{soversion} -f fs-plugin.filelist

%package -n     libbd_fs-devel
Summary:        Development files for the libbd_fs plugin/library
Group:          Development/Libraries/C and C++
Requires:       dosfstools
Requires:       glib2-devel
Requires:       libbd_fs%{soversion} >= %{version}
Requires:       libbd_utils-devel
Requires:       xfsprogs
Provides:       libblockdev-fs-devel = %{version}

%description -n libbd_fs-devel
This package contains header files and pkg-config files needed for development
with the libbd_fs plugin/library..

%files -n libbd_fs-devel -f fs-plugin-devel.filelist
%dir %{_includedir}/blockdev
%dir %{_includedir}/blockdev/fs
%endif

###############################################################################
#                           L O O P  P L U G I N
###############################################################################

%if %{with loop_plugin}
%package -n     libbd_loop%{soversion}
Summary:        The loop plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-loop = %{version}

%description -n libbd_loop%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to loop devices.

%ldconfig_scriptlets -n libbd_loop%{soversion}

%files -n libbd_loop%{soversion} -f loop-plugin.filelist

%package -n     libbd_loop-devel
Summary:        Development files for the libblockdev-loop plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_loop%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-loop-devel = %{version}

%description -n libbd_loop-devel
This package contains header files and pkg-config files needed for development
with the libbd_loop plugin/library.

%files -n libbd_loop-devel -f loop-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                            L V M  P L U G I N
###############################################################################

%if %{with lvm_plugin}
%package -n     libbd_lvm%{soversion}
Summary:        The LVM plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       lvm2
# For thin_metadata_size.
Requires:       thin-provisioning-tools
Provides:       libblockdev-lvm = %{version}

%description -n libbd_lvm%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides LVM-related functionality.

%ldconfig_scriptlets -n libbd_lvm%{soversion}

%files -n libbd_lvm%{soversion} -f lvm-plugin.filelist

%package -n     libbd_lvm-devel
Summary:        Development files for the libblockdev-lvm plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_lvm%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-lvm-devel = %{version}

%description -n libbd_lvm-devel
This package contains header files and pkg-config files needed for development
with the libbd_lvm plugin/library.

%files -n libbd_lvm-devel -f lvm-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                         L V M  D B U S  P L U G I N
###############################################################################

%if %{with lvmdbus_plugin}
%package -n     libbd_lvm-dbus%{soversion}
Summary:        The LVM plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       lvm2
# For thin_metadata_size.
Requires:       thin-provisioning-tools
Provides:       libblockdev-lvm-dbus = %{version}

%description -n libbd_lvm-dbus%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides LVM-related functionality utilizing the LVM D-Bus API.

%ldconfig_scriptlets -n libbd_lvm-dbus%{soversion}

%files -n libbd_lvm-dbus%{soversion} -f lvm-dbus-plugin.filelist

%package -n     libbd_lvm-dbus-devel
Summary:        Development files for the libblockdev-lvm-dbus plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_lvm-dbus%{soversion} = %{version}
Requires:       libbd_lvm-devel >= %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-lvm-dbus-devel = %{version}

%description -n libbd_lvm-dbus-devel
This package contains header files and pkg-config files needed for development
with the libbd_lvm-dbus plugin/library.

%files -n libbd_lvm-dbus-devel -f lvm-dbus-plugin-devel.filelist
%endif

###############################################################################
#                          M D  R A I D  P L U G I N
###############################################################################

%if %{with mdraid_plugin}
%package -n     libbd_mdraid%{soversion}
Summary:        The MD RAID plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       mdadm
Provides:       libblockdev-mdraid = %{version}

%description -n libbd_mdraid%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to MD RAID.

%ldconfig_scriptlets -n libbd_mdraid%{soversion}

%files -n libbd_mdraid%{soversion} -f mdraid-plugin.filelist

%package -n     libbd_mdraid-devel
Summary:        Development files for the libblockdev-mdraid plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_mdraid%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-mdraid-devel = %{version}

%description -n libbd_mdraid-devel
This package contains header files and pkg-config files needed for development
with the libbd_mdraid plugin/library.

%files -n libbd_mdraid-devel -f mdraid-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                      M U L T I P A T H  P L U G I N
###############################################################################

%if %{with mpath_plugin}
%package -n     libbd_mpath%{soversion}
Summary:        The multipath plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       multipath-tools
Provides:       libblockdev-mpath = %{version}

%description -n libbd_mpath%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to multipath devices.

%ldconfig_scriptlets -n libbd_mpath%{soversion}

%files -n libbd_mpath%{soversion} -f mpath-plugin.filelist

%package -n     libbd_mpath-devel
Summary:        Development files for the libblockdev-mpath plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_mpath%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-mpath-devel = %{version}

%description -n libbd_mpath-devel
This package contains header files and pkg-config files needed for development
with the libbd_mpath plugin/library.

%files -n libbd_mpath-devel -f mpath-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                            N V M E  P L U G I N
###############################################################################

%if %{with nvme_plugin}
%package -n     libbd_nvme%{soversion}
Summary:        The NVMe plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-nvme = %{version}

%description -n libbd_nvme%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides NVMe-related functionality.

%ldconfig_scriptlets -n libbd_nvme%{soversion}

%files -n libbd_nvme%{soversion} -f nvme-plugin.filelist

%package -n     libbd_nvme-devel
Summary:        Development files for the libblockdev-nvme plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_nvme%{soversion} >= %{version}
Requires:       libbd_utils-devel
Provides:       libblockdev-nvme-devel = %{version}

%description -n libbd_nvme-devel
This package contains header files and pkg-config files needed for development
with the libbd_nvme plugin/library.

%files -n libbd_nvme-devel -f nvme-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                    P A R T I T I O N I N G  P L U G I N
###############################################################################

%if %{with part_plugin}
%package -n     libbd_part%{soversion}
Summary:        The partitioning plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       gptfdisk
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       util-linux
Provides:       libblockdev-part = %{version}

%description -n libbd_part%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to partitioning.

%ldconfig_scriptlets -n libbd_part%{soversion}

%files -n libbd_part%{soversion} -f part-plugin.filelist

%package -n     libbd_part-devel
Summary:        Development files for the libblockdev-part plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_part%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-part-devel = %{version}

%description -n libbd_part-devel
This package contains header files and pkg-config files needed for development
with the libbd_part plugin/library.

%files -n libbd_part-devel -f part-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                            S W A P  P L U G I N
###############################################################################

%if %{with swap_plugin}
%package -n     libbd_swap%{soversion}
Summary:        The swap plugin for the LibBlockDev library
Group:          System/Libraries
Requires:       libbd_utils%{soversion} >= %{version}
Requires:       util-linux
Provides:       libblockdev-swap = %{version}

%description -n libbd_swap%{soversion}
This LibBlockDev library plugin (and, at the same time, a standalone library)
provides functionality related to swap devices.

%ldconfig_scriptlets -n libbd_swap%{soversion}

%files -n libbd_swap%{soversion} -f swap-plugin.filelist

%package -n     libbd_swap-devel
Summary:        Development files for the libblockdev-swap plugin/library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_swap%{soversion} = %{version}
Requires:       libbd_utils-devel >= %{version}
Provides:       libblockdev-swap-devel = %{version}

%description -n libbd_swap-devel
This package contains header files and pkg-config files needed for development
with the libbd_swap plugin/library.

%files -n libbd_swap-devel -f swap-plugin-devel.filelist
%dir %{_includedir}/blockdev
%endif

###############################################################################
#                        U T I L I T Y  L I B R A R Y
###############################################################################

%if %{with utils}
%package -n     libbd_utils%{soversion}
Summary:        Utility functions library for the LibBlockDev library
Group:          System/Libraries
Provides:       libblockdev-utils = %{version}

%description -n libbd_utils%{soversion}
This library provides utility functions used by the LibBlockDev library
and its plugins.

%ldconfig_scriptlets -n libbd_utils%{soversion}

%files -n libbd_utils%{soversion} -f utils-plugin.filelist

%package -n     libbd_utils-devel
Summary:        Development files for libblockdev-utils
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libbd_utils%{soversion} >= %{version}
Provides:       libblockdev-utils-devel = %{version}

%description -n libbd_utils-devel
This package contains header files and pkg-config files needed for development
with the libbd_utils library.

%files -n libbd_utils-devel -f utils-plugin-devel.filelist
%{_libdir}/pkgconfig/blockdev-utils.pc
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/{dbus,dev_utils,exec,extra_arg,module,sizes}.h
%endif

###############################################################################

%prep
%autosetup -p1
# Place NEWS.rst in the source tree for %%doc'ing it later.
install -m 644 -t . %{SOURCE1}

%build
# A bit of auto magic for exporting the CC variable when we don't have a
# /usr/bin/cc symlink to a gcc >= 11
if [ ! -f %{_bindir}/cc ]; then
    %define __gcc %(ls -1 %{_bindir}/gcc-[0-9][0-9] | tail -1)
    export CC=%{__gcc}
fi
%configure \
    --disable-static \
    --with%{!?with_btrfs_plugin:out}-btrfs \
    --with%{!?with_crypto_plugin:out}-crypto \
    --with%{!?with_dm_plugin:out}-dm \
    --with%{!?with_escrow_plugin:out}-escrow \
    --with%{!?with_fs_plugin:out}-fs \
    --with%{!?with_gtk_doc:out}-gtk-doc \
    --%{?with_gi_bindings:en}%{!?with_gi_bindings:dis}able-introspection \
    --with%{!?with_tools:out}-tools \
    --with%{!?with_nvdimm_plugin:out}-nvdimm \
    --with%{!?with_nvme_plugin:out}-nvme \
    --with%{!?with_loop_plugin:out}-loop \
    --with%{!?with_lvm_plugin:out}-lvm \
    --with%{!?with_lvmdbus_plugin:out}-lvm-dbus \
    --with%{!?with_mdraid_plugin:out}-mdraid \
    --with%{!?with_mpath_plugin:out}-mpath \
    --with%{!?with_part_plugin:out}-part \
    --with%{!?with_swap_plugin:out}-swap \
    ;

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -print -type f -delete

%{?with_btrfs_plugin:   %global plugins %{?plugins} btrfs}
%{?with_crypto_plugin:  %global plugins %{?plugins} crypto}
%{?with_dm_plugin:      %global plugins %{?plugins} dm}
%{?with_escrow_plugin:  %global plugins %{?plugins} escrow}
%{?with_fs_plugin:      %global plugins %{?plugins} fs}
%{?with_nvdimm_plugin:  %global plugins %{?plugins} nvdimm}
%{?with_nvme_plugin:    %global plugins %{?plugins} nvme}
%{?with_loop_plugin:    %global plugins %{?plugins} loop}
%{?with_lvm_plugin:     %global plugins %{?plugins} lvm}
%{?with_lvmdbus_plugin: %global plugins %{?plugins} lvm-dbus}
%{?with_mdraid_plugin:  %global plugins %{?plugins} mdraid}
%{?with_mpath_plugin:   %global plugins %{?plugins} mpath}
%{?with_part_plugin:    %global plugins %{?plugins} part}
%{?with_swap_plugin:    %global plugins %{?plugins} swap}
%{?with_utils:          %global plugins %{?plugins} utils}

echo %{?plugins}

for plugin in %{?plugins}; do
  ls -1 %{buildroot}%{_libdir}/libbd_${plugin}.so.%{soversion}* \
    > ${plugin}-plugin.filelist
  ls -1 %{buildroot}%{_libdir}/libbd_${plugin}.so \
    > ${plugin}-plugin-devel.filelist

  test "${plugin}" = lvm-dbus && continue

  ls -1 %{buildroot}%{_includedir}/blockdev/${plugin}.h \
    >> ${plugin}-plugin-devel.filelist

  if [ "${plugin}" = fs ]; then
    ls -1 %{buildroot}%{_includedir}/blockdev/${plugin}/* \
      >> ${plugin}-plugin-devel.filelist
  fi
done

sed -i -r 's,%{buildroot}(.*),\1,' ./*.filelist

%changelog
