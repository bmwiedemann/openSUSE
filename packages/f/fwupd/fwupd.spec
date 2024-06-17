#
# spec file for package fwupd
#
# Copyright (c) 2024 SUSE LLC
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


%ifarch %{ix86} x86_64 aarch64 riscv64 s390x ppc64le
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

%define shlib_sover  2
%define docs 0

Name:           fwupd
Version:        1.9.21
Release:        0
Summary:        Device firmware updater daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Management
URL:            https://fwupd.org/
Source:         %{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE fwupd-bsc1130056-shim-path.patch bsc#1130056
Patch1:         fwupd-bsc1130056-change-shim-path.patch
# PATCH-FIX-OPENSUSE fwupd-jscSLE-11766-close-efidir-leap-gap.patch jsc#SLE-11766 qkzhu@suse.com -- Set SLE and openSUSE esp os dir at runtime
Patch2:         fwupd-jscSLE-11766-close-efidir-leap-gap.patch
# PATCH-FEATURE-OPENSUSE harden_fwupd-offline-update.service.patch -- Harden services
Patch3:         harden_fwupd-offline-update.service.patch
# PATCH-FEATURE-OPENSUSE harden_fwupd-refresh.service.patch -- Harden services
Patch4:         harden_fwupd-refresh.service.patch

BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
%if %{with fish_support}
BuildRequires:  fish
%endif
BuildRequires:  gcab
# for certtool
BuildRequires:  gnutls
BuildRequires:  gobject-introspection
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  libelf-devel
BuildRequires:  meson >= 0.62.0
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-Pillow
BuildRequires:  python3-cairo
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
BuildRequires:  vala
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(appstream-glib) >= 0.5.10
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colorhug) >= 1.2.12
%ifnarch s390x ppc64le
BuildRequires:  pkgconfig(flashrom)
%endif
%if 0%{?docs}
BuildRequires:  pandoc
%endif
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.48.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(gusb) >= 0.2.9
BuildRequires:  pkgconfig(jcat) >= 0.1.3
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.1.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libcurl) >= 7.62.0
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libgcab-1.0) >= 1.0
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mbim-glib)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(qmi-glib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tss2-esys) >= 2.0
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  pkgconfig(xmlb) >= 0.1.13
%if %{with efi_fw_update}
BuildRequires:  pkgconfig(efiboot)
BuildRequires:  pkgconfig(efivar) >= 33
%endif
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(libsmbios_c) >= 2.3.0
%endif
Obsoletes:      dbxtool <= 8
Provides:       dbxtool
%if %{with efi_fw_update}
Obsoletes:      fwupdate <= 12
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

%package -n libfwupd%{shlib_sover}
Summary:        Allow session software to update device firmware
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libfwupd%{shlib_sover}
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
Requires:       %{name} = %{version}
Requires:       libfwupd%{shlib_sover} = %{version}
Requires:       typelib-1_0-Fwupd-2_0 = %{version}

%description devel
fwupd is a daemon to allows session software to update device firmware on
the local machine.

%package doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description doc
Developer documentation for %{name}.

%package bash-completion
Summary:        Bash completion for fwupd
Group:          System/Management
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
This package contain the bash completion command for the device firmware updater daemon.

%if %{with fish_support}
%package fish-completion
Summary:        Fish completion for fwupd
Group:          System/Management
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
This package contain the fish completion command for the device firmware updater daemon.
%endif

%lang_package

%prep
%autosetup -p1

for file in $(grep -l %{_bindir}/env . -r); do
  sed -i "s|%{_bindir}/env python3|%{_bindir}/python3|" $file
done

%build
# for F_OFD_SETLK detection
export CFLAGS="%{optflags} -D_GNU_SOURCE"
# Dell support requires direct SMBIOS access,
# Synaptics requires Dell support, i.e. x86 only
%meson \
  -Dlaunchd=disabled \
  -Dplugin_amdgpu=disabled \
  -Dpassim=disabled \
%if %{with efi_fw_update}
  -Dplugin_uefi_capsule=enabled \
  -Dplugin_uefi_pk=enabled \
  -Defi_binary=false \
  -Dcompat_cli=true \
%else
  -Dplugin_uefi_capsule=false \
  -Dplugin_uefi_pk=false \
%endif
%if %{with msr_support}
  -Dplugin_msr=enabled \
%else
  -Dplugin_msr=disabled \
%endif
%if %{with dell_support}
  -Dplugin_synaptics_mst=enabled \
%else
  -Dplugin_synaptics_mst=disabled \
%endif
%ifnarch %{ix86} x86_64
  -Dplugin_synaptics_rmi=disabled \
%endif
  -Dplugin_nvme=enabled \
  -Dplugin_redfish=enabled \
  -Ddocs=enabled \
  -Dsupported_build=enabled \
  -Dtests=false \
%ifarch s390x ppc64le
  -Dplugin_flashrom=disabled \
%endif
%if 0%{?docs}
  -Dman=true \
%else
  -Dman=false \
%endif
  %{nil}
%meson_build

%install
%meson_install
# Add SUSE specific rcfoo service symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfwupd-offline-update
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfwupd-refresh
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}/doc

# Do not ship default polkit .rules - openSUSE overrides them anyway - boo#1125428
rm %{buildroot}%{_datadir}/polkit-1/rules.d/org.freedesktop.fwupd.rules

# do not package tests
rm -fr %{buildroot}%{_datadir}/installed-tests

%if %{without fish_support}
rm -fr %{buildroot}%{_datadir}/fish
%endif

%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/*
%endif

%check
%meson_test

%ldconfig_scriptlets -n libfwupd%{shlib_sover}

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
%{_bindir}/fwupdmgr
%{_bindir}/fwupdtool
%if %{with efi_fw_update}
%{_bindir}/fwupdagent
%{_bindir}/fwupdate
%endif
%{_bindir}/dbxtool
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
%{_datadir}/%{name}/add_capsule_header.py
%{_datadir}/%{name}/firmware_packager.py
%{_datadir}/%{name}/install_dell_bios_exe.py
%{_datadir}/%{name}/simple_client.py
%if %{with efi_fw_update}
%{_datadir}/%{name}/uefi-capsule-ux.tar.xz
%endif
%{_datadir}/%{name}/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
%{_datadir}/%{name}/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
%{_datadir}/%{name}/remotes.d/vendor/firmware/README.md
%if 0%{?docs}
%{_mandir}/man1/fwupdagent.1%{?ext_man}
%{_mandir}/man1/fwupdmgr.1%{?ext_man}
%{_mandir}/man1/fwupdtool.1%{?ext_man}
%if %{with efi_fw_update}
%{_mandir}/man1/dbxtool.1%{?ext_man}
%{_mandir}/man1/fwupdate.1%{?ext_man}
%endif
%endif
%{_datadir}/polkit-1/actions/org.freedesktop.fwupd.policy
%if %{with msr_support}
%dir %{_modulesloaddir}
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
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.freedesktop.fwupd.metainfo.xml
%{_datadir}/icons/hicolor/*
%{_prefix}/lib/systemd/system-shutdown/fwupd.shutdown
%dir %{_libdir}/fwupd-*
%ifnarch s390x ppc64le
%{_libdir}/fwupd-*/libfu_plugin_flashrom.so
%endif
%{_libdir}/fwupd-*/libfu_plugin_modem_manager.so
%{_libdir}/fwupd-*/libfwupdengine.so
%{_libdir}/fwupd-*/libfwupdplugin.so
%{_libdir}/fwupd-*/libfwupdutil.so
%{_datadir}/%{name}/quirks.d/builtin.quirk.gz
%_sysusersdir/fwupd.conf

%if %{with efi_fw_update}
%files -n dfu-tool
%{_bindir}/dfu-tool
%if 0%{?docs}
%{_mandir}/man1/dfu-tool.1%{?ext_man}
%endif
%endif

%files -n libfwupd%{shlib_sover}
%{_libdir}/libfwupd.so.*

%files -n typelib-1_0-Fwupd-2_0
%{_libdir}/girepository-1.0/Fwupd-2.0.typelib

%files devel
%{_datadir}/gir-1.0/Fwupd-2.0.gir
%{_datadir}/vala/vapi/fwupd.deps
%{_datadir}/vala/vapi/fwupd.vapi
%{_includedir}/fwupd-1/
%{_libdir}/pkgconfig/fwupd.pc
%{_libdir}/libfwupd.so

%files doc
%doc %{_datadir}/doc/fwupd/
%doc %{_datadir}/doc/libfwupd/
%doc %{_datadir}/doc/libfwupdplugin/

%files bash-completion
%{_datadir}/bash-completion/completions/fwupdmgr
%{_datadir}/bash-completion/completions/fwupdtool

%if %{with fish_support}
%files fish-completion
%{_datadir}/fish/vendor_completions.d/fwupdmgr.fish
%endif

%files lang -f %{name}.lang

%changelog
