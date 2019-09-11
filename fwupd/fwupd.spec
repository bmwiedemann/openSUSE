#
# spec file for package fwupd
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
# needssslcertforbuild


%ifarch %{ix86} x86_64 aarch64
%bcond_without efi_fw_update
%else
%bcond_with efi_fw_update
%endif
%if 0%{?is_opensuse}
%global efidir opensuse
%else
%global efidir sles
%endif
Name:           fwupd
Version:        1.2.10
Release:        0
Summary:        Device firmware updater daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Management
URL:            https://fwupd.org/
Source:         https://github.com/hughsie/%{name}/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE fwupd-bsc1130056-shim-path.patch bsc#1130056
Patch1:         fwupd-bsc1130056-change-shim-path.patch
BuildRequires:  dejavu-fonts
BuildRequires:  docbook-utils-minimal
BuildRequires:  gcab
# for certtool
BuildRequires:  gnutls
BuildRequires:  gobject-introspection
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
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
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.9
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk-doc) >= 1.14
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb) >= 0.2.9
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.1.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libgcab-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.51.92
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(xmlb)
%if %{with efi_fw_update}
BuildRequires:  gnu-efi
BuildRequires:  pesign-obs-integration
BuildRequires:  pkgconfig(efiboot)
BuildRequires:  pkgconfig(efivar) >= 33
%endif
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(libsmbios_c) >= 2.3.0
%endif
%if %{with efi_fw_update}
Obsoletes:      fwupdate
%ifarch x86_64
Requires:       shim >= 11
%endif
%endif

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

%package -n typelib-1_0-Fwupd-2_0
Summary:        GObject-introspection bindings for libfwupd
Group:          System/Libraries

%description -n typelib-1_0-Fwupd-2_0
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

%description devel
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%lang_package

%prep
%setup -q
%patch1 -p1
for file in $(grep -l %{_bindir}/env . -r); do
  sed -i "s|%{_bindir}/env python3|%{_bindir}/python3|" $file
done

%build
# Dell support requires direct SMBIOS access,
# Synaptics requires Dell support, i.e. x86 only
%meson \
%if %{without efi_fw_update}
  -Dplugin_nvme=false \
  -Dplugin_redfish=false \
  -Dplugin_uefi=false \
%else
  -Defi_os_dir="%{efidir}" \
%endif
%ifnarch %{ix86} x86_64
  -Dplugin_dell=false \
  -Dplugin_synaptics=false \
%endif
  -Dtests=false
%meson_build

%install
export BRP_PESIGN_FILES='%{_libexecdir}/fwupd/efi/fwupd*.efi'
%meson_install
# README.md is packaged as doc
rm %{buildroot}%{_localstatedir}/lib/fwupd/builder/README.md
# Add SUSE specific rcfoo service symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfwupd-offline-update
%find_lang %{name}

# Do not ship default polkit .rules - openSUSE overrides them anyway - boo#1125428
rm %{buildroot}%{_datadir}/polkit-1/rules.d/org.freedesktop.fwupd.rules

# do not package tests
rm -fr %{buildroot}%{_datadir}/installed-tests

%if %{with efi_fw_update}
# link fwupd*.efi.signed to fwupd*.efi (bsc#1129466)
FWUPD_EFI=`basename %{buildroot}/%{_libexecdir}/fwupd/efi/fwupd*.efi`
ln -s %{_libexecdir}/fwupd/efi/$FWUPD_EFI %{buildroot}/%{_libexecdir}/fwupd/efi/$FWUPD_EFI.signed
%endif

%post   -n libfwupd2 -p /sbin/ldconfig
%postun -n libfwupd2 -p /sbin/ldconfig
%preun
%service_del_preun %{name}.service fwupd-offline-update.service

%pre
%service_add_pre %{name}.service fwupd-offline-update.service

%post
%udev_rules_update
%service_add_post %{name}.service fwupd-offline-update.service
%if %{with efi_fw_update}
if [ -d "/boot/efi/EFI/%{efidir}" ]; then
	# Create the directory for firwmare update capsules
	mkdir -p /boot/efi/EFI/%{efidir}/fw
	# Install the UEFI firmware update program
	cp %{_libexecdir}/fwupd/efi/fwupd*.efi /boot/efi/EFI/%{efidir}
fi
%endif

%postun
%service_del_postun %{name}.service fwupd-offline-update.service
%if %{with efi_fw_update}
if [ "$1" = 0 ] && [ -d "/boot/efi/EFI/%{efidir}" ] ; then
	# Remove all capsule files
	rm -rf /boot/efi/EFI/%{efidir}/fw
	# Remove the UEFI firmware update program
	rm -f /boot/efi/EFI/%{efidir}/fwupd*.efi
fi
%endif

%files
%license COPYING
%doc README.md
%{_libexecdir}/systemd/system/fwupd.service
%{_libexecdir}/systemd/system/fwupd-offline-update.service
%%dir %{_libexecdir}/systemd/system/system-update.target.wants/
%{_libexecdir}/systemd/system/system-update.target.wants/fwupd-offline-update.service
%{_libexecdir}/fwupd
%{_bindir}/fwupdmgr
%{_sbindir}/rc%{name}
%{_sbindir}/rcfwupd-offline-update
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.fwupd.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.fwupd.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.fwupd.service
%{_datadir}/%{name}/
%{_mandir}/man1/fwupdmgr.1%{?ext_man}
%{_datadir}/polkit-1/actions/org.freedesktop.fwupd.policy
%config %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/fwupd
%dir %{_sysconfdir}/pki/fwupd-metadata
%{_sysconfdir}/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
%{_sysconfdir}/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
%{_sysconfdir}/pki/fwupd-metadata/LVFS-CA.pem
%{_sysconfdir}/pki/fwupd/GPG-KEY-Hughski-Limited
%{_sysconfdir}/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
%{_sysconfdir}/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
%{_sysconfdir}/pki/fwupd/LVFS-CA.pem
%{_udevrulesdir}/90-fwupd-devices.rules
%{_libdir}/fwupd-plugins-3/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.freedesktop.fwupd.metainfo.xml
%dir %{_localstatedir}/lib/%{name}/
%{_datadir}/bash-completion/completions/fwupdmgr
%{_datadir}/bash-completion/completions/fwupdtool
%{_datadir}/bash-completion/completions/fwupdagent
%{_datadir}/icons/hicolor/*
%{_prefix}/lib/systemd/system-shutdown/fwupd.shutdown

%files -n dfu-tool
%{_bindir}/dfu-tool
%{_mandir}/man1/dfu-tool.1%{?ext_man}

%files -n libfwupd2
%{_libdir}/libfwupd.so.*

%files -n typelib-1_0-Fwupd-2_0
%{_libdir}/girepository-1.0/Fwupd-2.0.typelib

%files lang -f %{name}.lang
%if %{with efi_fw_update}
%{_datadir}/locale/*/LC_IMAGES/
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/libfwupd/
%{_datadir}/gir-1.0/Fwupd-2.0.gir
%{_datadir}/vala/vapi/fwupd.deps
%{_datadir}/vala/vapi/fwupd.vapi
%{_includedir}/fwupd-1/
%{_libdir}/pkgconfig/fwupd.pc
%{_libdir}/libfwupd.so

%changelog
