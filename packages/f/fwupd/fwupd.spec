#
# spec file for package fwupd
#
# Copyright (c) 2021 SUSE LLC
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


%ifarch %{ix86} x86_64 aarch64
%bcond_without efi_fw_update
%else
%bcond_with efi_fw_update
%endif

%ifarch %{ix86} x86_64
%bcond_without msr_support
%bcond_without dell_support
%else
%bcond_with msr_support
%bcond_with dell_support
%endif

%if 0%{?suse_version} > 1500
%bcond_without fish_support
%else
%bcond_with fish_support
%endif

Name:           fwupd
Version:        1.7.3
Release:        0
Summary:        Device firmware updater daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Management
URL:            https://fwupd.org/
# Do not use upstream tarball, we are using source service!
#Source:         https://github.com/%%{name}/%%{name}/archive/%%{version}.tar.gz
Source:         %{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE fwupd-bsc1130056-shim-path.patch bsc#1130056
Patch1:         fwupd-bsc1130056-change-shim-path.patch
# PATCH-FIX-OPENSUSE fwupd-jscSLE-11766-close-efidir-leap-gap.patch jsc#SLE-11766 qkzhu@suse.com -- Set SLE and openSUSE esp os dir at runtime
Patch2:         fwupd-jscSLE-11766-close-efidir-leap-gap.patch
Patch3:         harden_fwupd-offline-update.service.patch
Patch4:         harden_fwupd-refresh.service.patch

BuildRequires:  dejavu-fonts
%if %{with fish_support}
BuildRequires:  fish
%endif
BuildRequires:  gcab
# for certtool
BuildRequires:  gnutls
BuildRequires:  gobject-introspection
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  libelf-devel
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-Pillow
BuildRequires:  python3-cairo
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream-glib) >= 0.5.10
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colorhug) >= 1.2.12
BuildRequires:  pkgconfig(gio-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.48.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk-doc) >= 1.14
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(gusb) >= 0.2.9
BuildRequires:  pkgconfig(jcat) >= 0.1.3
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.1.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl) >= 7.62.0
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libgcab-1.0) >= 1.0
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tss2-esys) >= 2.0
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xmlb) >= 0.1.13
%if %{with efi_fw_update}
BuildRequires:  gnu-efi
BuildRequires:  pkgconfig(efiboot)
BuildRequires:  pkgconfig(efivar) >= 33
%endif
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(libsmbios_c) >= 2.3.0
%endif
%if 0%{?suse_version} < 1550
BuildRequires:  protobuf-c
%endif
%if %{with efi_fw_update}
Obsoletes:      dbxtool <= 8
Obsoletes:      fwupdate <= 12
Provides:       dbxtool
%ifarch x86_64 aarch64
Requires:       shim >= 11
Requires:       udisks2
%endif
%endif
Requires:       (fwupd-efi if shim)

%description
fwupd is a daemon to allows session software to update device firmware on
the local machine.

You can either use a GUI software manager like GNOME Software to view and apply
updates, the command line tool or the system D-Bus interface directly.

%package -n libfwupd2
Summary:        Allow session software to update device firmware
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libfwupd2
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%package -n libfwupdplugin5
Summary:        Allow session software to update device firmware
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libfwupdplugin5
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%package -n typelib-1_0-Fwupd-2_0
Summary:        GObject-introspection bindings for libfwupd
Group:          System/Libraries

%description -n typelib-1_0-Fwupd-2_0
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%package -n typelib-1_0-FwupdPlugin-1_0
Summary:        GObject-introspection bindings for libfwupd
Group:          System/Libraries

%description -n typelib-1_0-FwupdPlugin-1_0
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%package -n dfu-tool
Summary:        Generic tool Device Firmware Upgrade (DFU) tool
Group:          Development/Tools/Other

%description -n dfu-tool
A generic tool to upload firmware to USB Devices based on Device Firmware Upgrade (DFU).

%package devel
Summary:        Allow session software to update device firmware
Group:          Development/Languages/C and C++
Requires:       libfwupd2 = %{version}
Requires:       libfwupdplugin5 = %{version}

%description devel
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%lang_package

%prep
%autosetup -p1

for file in $(grep -l %{_bindir}/env . -r); do
  sed -i "s|%{_bindir}/env python3|%{_bindir}/python3|" $file
done

%build
# Dell support requires direct SMBIOS access,
# Synaptics requires Dell support, i.e. x86 only
%meson \
%if %{with efi_fw_update}
  -Dplugin_uefi_capsule=true \
  -Dplugin_uefi_pk=true \
  -Defi_binary=false \
%else
  -Dplugin_uefi_capsule=false \
  -Dplugin_uefi_pk=false \
%endif
%if %{with msr_support}
  -Dplugin_msr=true \
%else
  -Dplugin_msr=false \
%endif
%if %{with dell_support}
  -Dplugin_dell=true \
  -Dplugin_synaptics_mst=true \
%else
  -Dplugin_dell=false \
  -Dplugin_synaptics_mst=false \
%endif
%ifnarch %{ix86} x86_64
  -Dplugin_amt=false \
  -Dplugin_synaptics_rmi=false \
%endif
  -Dplugin_nvme=false \
  -Dplugin_redfish=false \
  -Ddocs=gtkdoc \
  -Dsupported_build=true \
  -Dtests=false \
  %{nil}
%meson_build

%install
export BRP_PESIGN_FILES='%{_libexecdir}/fwupd/efi/fwupd*.efi'
%meson_install
# README.md is packaged as doc
rm %{buildroot}/usr/share/doc/fwupd/builder/README.md
# Add SUSE specific rcfoo service symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfwupd-offline-update
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfwupd-refresh
%find_lang %{name}

# Do not ship default polkit .rules - openSUSE overrides them anyway - boo#1125428
rm %{buildroot}%{_datadir}/polkit-1/rules.d/org.freedesktop.fwupd.rules

# do not package tests
rm -fr %{buildroot}%{_datadir}/installed-tests

%if %{without fish_support}
rm -fr %{buildroot}%{_datadir}/fish
%endif

%post   -n libfwupd2 -p /sbin/ldconfig
%postun -n libfwupd2 -p /sbin/ldconfig

%post   -n libfwupdplugin5 -p /sbin/ldconfig
%postun -n libfwupdplugin5 -p /sbin/ldconfig

%preun
%service_del_preun %{name}.service fwupd-offline-update.service fwupd-refresh.service

%pre
%service_add_pre %{name}.service fwupd-offline-update.service fwupd-refresh.service

%post
%udev_rules_update
%service_add_post %{name}.service fwupd-offline-update.service fwupd-refresh.service

%postun
%service_del_postun %{name}.service fwupd-offline-update.service fwupd-refresh.service

%files

%license COPYING
%doc README.md
%{_unitdir}/fwupd.service
%{_unitdir}/fwupd-offline-update.service
%dir %{_unitdir}/system-update.target.wants/
%{_unitdir}/system-update.target.wants/fwupd-offline-update.service
%{_unitdir}/fwupd-refresh.service
%{_unitdir}/fwupd-refresh.timer
%{_libexecdir}/fwupd
%{_bindir}/fwupdagent
%{_bindir}/fwupdmgr
%{_bindir}/fwupdtool
%if %{with efi_fw_update}
%{_bindir}/fwupdate
%{_bindir}/dbxtool
%endif
%{_sbindir}/rc%{name}
%{_sbindir}/rcfwupd-offline-update
%{_sbindir}/rcfwupd-refresh
%{_datadir}/dbus-1/system.d/org.freedesktop.fwupd.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.fwupd.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.fwupd.service
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/metainfo
%dir %{_datadir}/%{name}/quirks.d
%dir %{_datadir}/%{name}/remotes.d
%dir %{_datadir}/%{name}/remotes.d/vendor
%dir %{_datadir}/%{name}/remotes.d/vendor/firmware
%if %{with dell_support}
%dir %{_datadir}/%{name}/remotes.d/dell-esrt
%{_datadir}/%{name}/remotes.d/dell-esrt/metadata.xml
%endif
%{_datadir}/%{name}/add_capsule_header.py
%{_datadir}/%{name}/firmware_packager.py
%{_datadir}/%{name}/install_dell_bios_exe.py
%{_datadir}/%{name}/simple_client.py
%if %{with efi_fw_update}
%{_datadir}/%{name}/uefi-capsule-ux.tar.xz
%endif
%{_datadir}/%{name}/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
%{_datadir}/%{name}/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
%{_datadir}/%{name}/quirks.d/*.quirk
%{_datadir}/%{name}/remotes.d/vendor/firmware/README.md
%{_mandir}/man1/fwupdagent.1%{?ext_man}
%{_mandir}/man1/fwupdmgr.1%{?ext_man}
%{_mandir}/man1/fwupdtool.1%{?ext_man}
%if %{with efi_fw_update}
%{_mandir}/man1/dbxtool.1%{?ext_man}
%{_mandir}/man1/fwupdate.1%{?ext_man}
%endif
%{_datadir}/polkit-1/actions/org.freedesktop.fwupd.policy
%if %{with msr_support}
%{_modulesloaddir}/fwupd-msr.conf
%endif
%config %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/fwupd
%dir %{_sysconfdir}/pki/fwupd-metadata
%{_sysconfdir}/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
%{_sysconfdir}/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
%{_sysconfdir}/pki/fwupd-metadata/LVFS-CA.pem
%{_sysconfdir}/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
%{_sysconfdir}/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
%{_sysconfdir}/pki/fwupd/LVFS-CA.pem
%if %{with efi_fw_update}
%dir %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/35_fwupd
%endif
%{_udevrulesdir}/90-fwupd-devices.rules
%{_libdir}/fwupd-plugins-5/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.freedesktop.fwupd.metainfo.xml
%{_datadir}/bash-completion/completions/fwupdmgr
%{_datadir}/bash-completion/completions/fwupdtool
%{_datadir}/bash-completion/completions/fwupdagent
%if %{with fish_support}
%{_datadir}/fish/vendor_completions.d/fwupdmgr.fish
%endif
%{_datadir}/icons/hicolor/*
%{_prefix}/lib/systemd/system-shutdown/fwupd.shutdown
%{_prefix}/lib/systemd/system-preset/fwupd-refresh.preset

%files -n dfu-tool
%{_bindir}/dfu-tool
%{_mandir}/man1/dfu-tool.1%{?ext_man}

%files -n libfwupd2
%{_libdir}/libfwupd.so.*

%files -n libfwupdplugin5
%{_libdir}/libfwupdplugin.so.*

%files -n typelib-1_0-Fwupd-2_0
%{_libdir}/girepository-1.0/Fwupd-2.0.typelib

%files -n typelib-1_0-FwupdPlugin-1_0
%{_libdir}/girepository-1.0/FwupdPlugin-1.0.typelib

%files lang -f %{name}.lang

%files devel
%doc %{_datadir}/gtk-doc/html/fwupd/
%{_datadir}/gir-1.0/Fwupd-2.0.gir
%{_datadir}/gir-1.0/FwupdPlugin-1.0.gir
%{_datadir}/vala/vapi/fwupd.deps
%{_datadir}/vala/vapi/fwupd.vapi
%{_includedir}/fwupd-1/
%{_libdir}/pkgconfig/fwupd.pc
%{_libdir}/pkgconfig/fwupdplugin.pc
%{_libdir}/libfwupd.so
%{_libdir}/libfwupdplugin.so

%changelog
