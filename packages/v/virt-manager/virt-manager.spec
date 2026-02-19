#
# spec file for package virt-manager
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global __python %{__python3}
%global with_guestfs               0
%global default_hvs                "qemu,xen,lxc"
%if 0%{?suse_version} < 1600 || 0%{?suse_version} >= 1699
    %define is_sles16 0
    %define have_spice 1
%else
    %define is_sles16 1
    %define have_spice 0
%endif

%global flavor @BUILD_FLAVOR@%{nil}
# No spice on SLES16 so no running check build
%if "%{flavor}" == "test" && %{have_spice}
%bcond_without test
%define psuffix -%{flavor}
%else
%bcond_with test
%define psuffix %{nil}
%endif

Name:           virt-manager%{psuffix}
Version:        5.1.0
Release:        0
Summary:        Virtual Machine Manager
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://virt-manager.org/
Source0:        https://releases.pagure.org/virt-manager/virt-manager-%{version}.tar.xz
Source1:        virt-install.rb
Source2:        virt-install.desktop
Source3:        virt-manager-supportconfig
# Upstream Patches
Patch1:         003-virtinst-cloudinit-include-empty-meta-data-file.patch
Patch2:         009-avoid-NoneType-pixbuf.patch
Patch3:         012-virtManager-wrapped-details-hw-panel-with-GtkScrolledWindow.patch
Patch4:         013-virtinst-interface-add-support-for-backend.hostname-and-backend.fqdn.patch
Patch5:         014-virtinst-add-support-for-acpi-generic-initiator.patch
Patch6:         015-virtinst-add-support-for-pcihole64.patch
Patch7:         017-maint-use-constants-instead-of-strings-for-boot-devices.patch
Patch8:         018-virtinst-rework-get_boot_order.patch
Patch9:         019-virtinst-guest-introduce-can_use_device_boot_order.patch
Patch10:        020-virtinst-remove-legacy-attribute-from-set_boot_order-get_boot_order.patch
Patch11:        021-installer-add-support-to-use-device-boot-order.patch
Patch12:        024-virtinst-Fix-XDG_DATA_HOME-handling.patch
Patch13:        051-addhardware-Add-usb-as-a-recommended-sound-device.patch
Patch14:        055-virtinst-Add-serial-controller-option-to-cli.patch
Patch15:        056-virtinst-Add-NVMe-Controller.patch
Patch16:        057-virtinst-implement-NVMe-disk-target-generation.patch
Patch17:        058-virtManager-Add-NVMe-disk-type.patch
Patch18:        059-ui-Show-NVMe-Controller-details.patch
Patch19:        060-virtinst-fix-locale-when-running-in-flatpak.patch
Patch20:        061-virtinst-add-support-for-iommufd.patch
# SUSE Only
Patch150:       virtman-desktop.patch
Patch151:       virtman-kvm.patch
Patch152:       virtman-show-suse-install-repos.patch
Patch153:       virtman-dont-allow-grub.xen-to-be-deleted.patch
Patch154:       virtinst-pvgrub2-bootloader.patch
Patch155:       virtinst-change-location-for-grub_xen.patch
Patch156:       virtinst-set-qemu-emulator.patch
# Features or Enhancements
Patch203:       virtman-load-stored-uris.patch
Patch204:       virtman-add-tooltip-to-firmware.patch
Patch205:       virtman-modify-gui-defaults.patch
Patch206:       virtman-add-launch-security-support.patch
Patch220:       virtinst-default-xen-to-qcow2-format.patch
Patch221:       virtinst-detect-oes-distros.patch
Patch222:       virtinst-vol-default-nocow.patch
Patch223:       virtinst-set-cache-mode-unsafe-for-install.patch
Patch224:       virtinst-s390x-disable-graphics.patch
Patch225:       virtinst-add-caasp-support.patch
Patch226:       virtinst-add-sle15-detection-support.patch
Patch227:       virtinst-media-detection.patch
Patch228:       virtinst-query-recommended-firmware.patch
# Bug Fixes
Patch251:       virtman-increase-setKeepAlive-count.patch
Patch252:       virtman-allow-destroy-from-shutdown-menu-of-crashed-vm.patch
Patch253:       virtman-allow-creating-i686-vm.patch
Patch254:       virtman-dont-specify-vte-version.patch
Patch255:       virtman-fix-restore-vm-menu-selection.patch
Patch256:       virtman-disallow-adding-floppy-disk.patch
Patch257:       virtman-register-delete-event-for-details-dialog.patch
Patch258:       virtman-revert-use-of-AyatanaAppIndicator3.patch
Patch259:       virtman-fix-inspection-apps-window.patch
Patch260:       virtman-fix-shared-disk-request-alignment-error.patch
Patch270:       virtinst-xen-drive-type.patch
Patch271:       virtinst-xenbus-disk-index-fix.patch
Patch272:       virtinst-refresh_before_fetch_pool.patch
Patch273:       virtinst-use-xenpae-kernel-for-32bit.patch
Patch274:       virtinst-use-qemu-for-cdrom-device.patch
Patch275:       virtinst-keep-install-iso-attached.patch
Patch277:       virtinst-set-default-nic.patch
Patch278:       virtinst-sap-detection.patch
Patch279:       virtinst-smbios-unsupported-for-xenpv.patch
Patch280:       virtinst-keep-iso-for-xenpv.patch
Patch281:       virtinst-add-slem-detection-support.patch
Patch282:       virtinst-add-sle-hpc-support.patch
Patch283:       virtinst-add-oracle-linux-support.patch
Patch284:       virtinst-add-slem60-detection-support.patch
Patch285:       virtinst-windows-server-detection.patch
Patch286:       virtinst-drop-removeprefix-usage.patch
Patch287:       virtinst-add-sle16-detection-support.patch
Patch288:       virtinst-remove-tpm-device-for-tdx-and-snp.patch

BuildArch:      noarch

%define verrel %{version}-%{release}
Requires:       dconf
Requires:       gtk3
Requires:       python3-gobject
Requires:       virt-manager-common = %{verrel}
Requires:       vte

Recommends:     gtksourceview4
Recommends:     libvirt-daemon-config-network
Recommends:     (libvirt-daemon-kvm or libvirt-daemon-qemu)

Suggests:       python3-libguestfs

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{is_sles16}
%define __requires_exclude typelib\\(AppIndicator3|SpiceClientGtk|SpiceClientGLib|GtkSource\\) = 3.0
%else
# GtkSource = 4 is available everywhere we run this version of virt-manager
%define __requires_exclude typelib\\(GtkSource\\) = 3.0
%endif
%if %{with test}
BuildRequires:  python3-argcomplete
BuildRequires:  python3-pytest
BuildRequires:  virt-install = %{version}
BuildRequires:  virt-manager = %{version}
BuildRequires:  pkgconfig(vte-2.91)
%endif

%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and QEmu. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package common
Summary:        Common files used by the different Virtual Machine Manager interfaces
Group:          System/Monitoring

# This version not strictly required: virt-manager should work with older,
# however varying amounts of functionality will not be enabled.
Requires:       libosinfo >= 0.2.10
Requires:       python3-argcomplete
Requires:       python3-gobject
Requires:       python3-libvirt-python >= 0.7.0
Requires:       python3-libxml2-python
Requires:       python3-requests
Requires:       xorriso

%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary:        Utilities for installing virtual machines
Group:          System/Monitoring

Requires:       libvirt-client
Requires:       virt-manager-common = %{verrel}

Provides:       python3-virtinst
Provides:       virt-clone
Provides:       virt-xml
Supplements:    virt-manager

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%prep
%autosetup -p1 -n virt-manager-%{version}

%if !%{with test}
%build
%if %{default_hvs}
%global _default_hvs --default-hvs %{default_hvs}
%endif
%if %{have_spice}
%global _default_graphics -Ddefault-graphics=spice
%else
%global _default_graphics -Ddefault-graphics=vnc
%endif
%meson \
    -Ddefault-hvs=%{default_hvs} \
    %{?_default_graphics} \
    -Dupdate-icon-cache=false \
    -Dcompile-schemas=false \
    -Dtests=disabled
%meson_build

%install
%meson_install

# YaST is not used on SLES16
%if ! %{?is_sles16}
mkdir -p %{buildroot}/%{_datadir}/YaST2/clients/
install -m644 %SOURCE1 %{buildroot}/%{_datadir}/YaST2/clients/virt-install.rb
mkdir -p %{buildroot}/%{_datadir}/applications/YaST2/
install -m644 %SOURCE2 %{buildroot}/%{_datadir}/applications/YaST2/virt-install.desktop
%endif
# Oddly, supportconfig doesn't execute plugins with '-' in the name, so use 'virt_manager'
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins
install -m 755 %SOURCE3 %{buildroot}/usr/lib/supportconfig/plugins/virt_manager
chmod -x %{buildroot}%{_datadir}/virt-manager/virtManager/virtmanager.py

%python3_fix_shebang

%find_lang %{name}
%endif

%if %{with test}
%check
# bsc#1253017: Set this for testCLI0181virt_install_kvm_session_defaults
export XDG_DATA_HOME="/tmp/.local/share"
# XML contains hda instead of hdc
donttest="test_disk_numtotarget"
# XML contains sd{a,b,c,d} instead of sda{a,b,c,d}
donttest="$donttest or testCLI0001virt_install_many_devices"
# There are XML properties that are untested in the test suite.
donttest="$donttest or testCheckXMLBuilderProps"
# There are command line arguments or aliases are not checked in the test suite.
donttest="$donttest or testCheckCLISuboptions"
# We insert cache="unsafe" during installation
donttest="$donttest or testCLI0007virt_install_singleton_config_2"
donttest="$donttest or testCLI0105virt_install_cloud_init_default"
donttest="$donttest or testCLI0106virt_install_cloud_init_options1"
donttest="$donttest or testCLI0111virt_install_cloud_init_options6"
donttest="$donttest or testCLI0123virt_install_reinstall_cdrom"
donttest="$donttest or testCLI0153virt_install_win11"
donttest="$donttest or testCLI0154virt_install_win11_no_uefi"
donttest="$donttest or testCLI0157virt_install_location_iso_and_cloud_init"
# RuntimeError: SEV launch security requires a Q35 machine
donttest="$donttest or testCLI0179virt_install"
# Size must be specified for non existent volume '__virtinst_cli_exist1.img'
donttest="$donttest or testCLI0186virt_install_s390x_cdrom"
# We insert cache="unsafe" during installation
donttest="$donttest or testCLI0192virt_install_riscv64_cloud_init"
donttest="$donttest or testCLI0193virt_install_riscv64_cdrom"
donttest="$donttest or testCLI0194virt_install_riscv64_unattended"
donttest="$donttest or testCLI0207virt_install_aarch64_cloud_init"
# We default to 4 vcpus instead of 1
donttest="$donttest or testCLI0208virt_install_aarch64_win11"
# We insert cache="unsafe" during installation
donttest="$donttest or testCLI0212virt_install_loongarch64_cloud_init"
donttest="$donttest or testCLI0213virt_install_loongarch64_cdrom"
donttest="$donttest or testCLI0214virt_install_loongarch64_unattended"
# We use grub.xen instead of pygrub
donttest="$donttest or testCLI0228virt_install_xen_default"
donttest="$donttest or testCLI0229virt_install_xenpvh"
donttest="$donttest or testCLI0230virt_install_xen_pv"
# We use qemu-system-i386 instead of the ancient qemu-dm and also no e1000 nic
donttest="$donttest or testCLI0231virt_install_xen_hvm"
donttest="$donttest or testCLI0232virt_install_xen_hvm"
# foobhyve.qcow2 used instead of foobhyve.img
donttest="$donttest or testCLI0239virt_install_bhyve_default_f27"
# XML contains vda instead of vdaf
donttest="$donttest or testCLI0319virt_xml_build_disk_domain"
donttest="$donttest or testCLI0328virt_xml_build_pool_logical_disk"
# XML contains hda instead of hdd
donttest="$donttest or testCLI0428virt_xml_add_disk_create_storage_start"
# Disk path '/tmp/__virtinst_cli_exist1.img' does not exist.
donttest="$donttest or testCLI0450virt_clone_auto_unmanaged"
donttest="$donttest or testCLI0454virt_clone"
donttest="$donttest or testCLI0455virt_clone"
donttest="$donttest or testCLI0469virt_clone"
donttest="$donttest or testCLI0470virt_clone"
donttest="$donttest or testCLI0472virt_clone"
donttest="$donttest or testCLI0473virt_clone"
donttest="$donttest or testCLI0480virt_clone"
#
pytest -v -rfEs -k "not ($donttest)"
%endif

%post
/bin/touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>&1 || :
/usr/bin/update-desktop-database > /dev/null 2>&1 || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>&1
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>&1 || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas > /dev/null 2>&1 || :
fi
/usr/bin/update-desktop-database > /dev/null 2>&1 || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>&1 || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas > /dev/null 2>&1 || :

%if !%{with test}
%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1*

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/%{name}/virtManager

%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/%{name}/icons
%{_datadir}/icons/hicolor/*/apps/*

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%if ! %{?is_sles16}
%{_datadir}/applications/YaST2/virt-install.desktop
%endif
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%{_datadir}/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/virt_manager

%files common -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}

%{_datadir}/%{name}/virtinst

%files -n virt-install
%defattr(-,root,root,-)
%{_mandir}/man1/virt-install.1*
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-xml.1*

%{_bindir}/virt-install
%{_datadir}/bash-completion/completions/virt-install
%{_bindir}/virt-clone
%{_datadir}/bash-completion/completions/virt-clone
%{_bindir}/virt-xml
%{_datadir}/bash-completion/completions/virt-xml

%if ! %{?is_sles16}
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/clients
%dir %{_datadir}/applications/YaST2
%{_datadir}/YaST2/clients/virt-install.rb
%endif
%endif

%changelog
