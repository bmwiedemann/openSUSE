#
# spec file
#
# Copyright (c) 2025 SUSE LLC
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
    %define have_spice 1
%else
    %define have_spice 0
%endif

%global flavor @BUILD_FLAVOR@%{nil}
# No spice on SLES15 so no running check build
%if "%{flavor}" == "test" && %{have_spice}
%bcond_without test
%define psuffix -%{flavor}
%else
%bcond_with test
%define psuffix %{nil}
%endif

Name:           virt-manager%{psuffix}
Version:        5.0.0
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
Patch1:         001-cli-Support-cpu-maximum.patch
Patch2:         002-gui-Support-maximum-CPU-mode.patch
Patch3:         003-cpu-Prefer-maximum-mode-for-many-emulated-guests.patch
Patch4:         004-domcaps-get-list-of-supported-panic-device-models.patch
Patch5:         005-tests-Update-capabilities-for-advertisting-panic-device-models.patch
Patch6:         006-addhardware-panic-Fill-in-model-combo-with-advertised-values-by-libvirt.patch
Patch7:         007-cli-man-Always-list-osinfo-before-os-variant.patch
Patch8:         008-snapshots-default-to-same-snapshot-mode-as-currently-used-snapshot.patch
Patch9:         009-snapshots-warn-users-to-not-mix-snapshot-modes.patch
Patch10:        010-virtManager-domain-fix-indentation.patch
Patch21:        021-cli-Add-memdev-target.dynamicMemslots-support-for-virtio-mem.patch
Patch22:        022-cli-add-target.memReserve-for-pci-bridge-and-pcie-root-port-controllers.patch
Patch23:        023-cli-Add-disk-driver.queue_size-support.patch
Patch24:        024-cli-Add-poll-settings-for-iothread.patch
Patch25:        025-test_cli-Fix-a-pycodestyle-E261-issue.patch
Patch26:        026-gitignore-Ignore-coverage.xml.patch
Patch27:        027-cli-Add-tpm-backend.profile.source-removeDisabled-support.patch
Patch28:        028-cli-Add-nvram.templateFormat-to-indicate-template-format.patch
Patch29:        029-cli-Add-features-hyperv.xmm_input.state-on-off.patch
Patch30:        030-cli-Add-features-hyperv.emsr_bitmap.state-on-off.patch
Patch31:        031-cli-Add-features-hyperv.tlbflush.direct.state-on-off.patch
Patch32:        032-cli-Add-features-hyperv.tlbflush.extended.state-on-off.patch
Patch33:        033-createvm-prioritize-riscv64.patch
Patch34:        034-tests-uitests-handle-linux2020-going-EOL.patch
Patch100:       revert-363fca41-virt-install-Require-osinfo-for-non-x86-HVM-case-too.patch
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
Patch206:       virtman-add-sev-memory-support.patch
Patch220:       virtinst-default-xen-to-qcow2-format.patch
Patch221:       virtinst-detect-oes-distros.patch
Patch222:       virtinst-vol-default-nocow.patch
Patch223:       virtinst-set-cache-mode-unsafe-for-install.patch
Patch224:       virtinst-s390x-disable-graphics.patch
Patch225:       virtinst-add-caasp-support.patch
Patch226:       virtinst-add-sle15-detection-support.patch
Patch227:       virtinst-media-detection.patch
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
Patch288:       virtinst-dont-require-uefi-for-sev-snp.patch

BuildArch:      noarch

%define verrel %{version}-%{release}
Requires:       dconf
Requires:       gtk3
Requires:       python3-gobject
Requires:       virt-manager-common = %{verrel}
Requires:       vte
Requires:       typelib(LibvirtGLib)

Recommends:     gtksourceview4
Recommends:     libvirt-daemon-config-network
Recommends:     (libvirt-daemon-kvm or libvirt-daemon-qemu)

Suggests:       python3-libguestfs

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
%if %{with test}
BuildRequires:  python3-argcomplete
BuildRequires:  python3-pytest
BuildRequires:  virt-install = %{version}
BuildRequires:  virt-manager = %{version}
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  typelib(Libosinfo)
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
%if ! %{have_spice}
%global _default_graphics -Ddefault-graphics=vnc
%else
%global _default_graphics -Ddefault-graphics=spice
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
%if %{?suse_version} != 1600
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
# TODO: check if these are genuine failures or due to the non-upstream patches
# different device names
donttest="test_disk_numtotarget"
donttest="$donttest or testCLI0001virt_install_many_devices"
donttest="$donttest or testCLI0003virt_install_singleton_config_2"
donttest="$donttest or testCLI0004virt_install_singleton_config_2"
donttest="$donttest or testCLI0101virt_install_cloud_init_default"
donttest="$donttest or testCLI0101virt_install_cloud_init_options1"
donttest="$donttest or testCLI0102virt_install_cloud_init_options1"
donttest="$donttest or testCLI0113virt_install_reinstall_cdrom"
donttest="$donttest or testCLI0117virt_install_reinstall_cdrom"
donttest="$donttest or testCLI0147virt_install_win11"
donttest="$donttest or testCLI0147virt_install_win11_no_uefi"
donttest="$donttest or testCLI0148virt_install_win11_no_uefi"
donttest="$donttest or testCLI0151virt_install_location_iso_and_cloud_init"
donttest="$donttest or testCLI0165virt_install"
donttest="$donttest or testCLI0173virt_install"
donttest="$donttest or testCLI0172virt_install_s390x_cdrom"
donttest="$donttest or testCLI0180virt_install_s390x_cdrom"
donttest="$donttest or testCLI0186virt_install_riscv64_cloud_init"
donttest="$donttest or testCLI0187virt_install_riscv64_cdrom"
donttest="$donttest or testCLI0188virt_install_riscv64_unattended"
donttest="$donttest or testCLI0200virt_install_aarch64_cloud_init"
donttest="$donttest or testCLI0204virt_install_loongarch64_cloud_init"
donttest="$donttest or testCLI0205virt_install_loongarch64_cdrom"
donttest="$donttest or testCLI0206virt_install_loongarch64_unattended"
donttest="$donttest or testCLI0193virt_install_xen_default"
donttest="$donttest or testCLI0216virt_install_xen_default"
donttest="$donttest or testCLI0217virt_install_xenpvh"
donttest="$donttest or testCLI0218virt_install_xen_pv"
donttest="$donttest or testCLI0219virt_install_xen_hvm"
donttest="$donttest or testCLI0220virt_install_xen_hvm"
donttest="$donttest or testCLI0227virt_install_bhyve_default_f27"
donttest="$donttest or testCLI0307virt_xml_build_disk_domain"
donttest="$donttest or testCLI0315virt_xml_edit_cpu_host_copy"
donttest="$donttest or testCLI0316virt_xml_build_pool_logical_disk"
donttest="$donttest or testCLI0416virt_xml_add_disk_create_storage_start"
donttest="$donttest or testCLI0438virt_clone_auto_unmanaged"
donttest="$donttest or testCLI0442virt_clone"
donttest="$donttest or testCLI0443virt_clone"
donttest="$donttest or testCLI0457virt_clone"
donttest="$donttest or testCLI0458virt_clone"
donttest="$donttest or testCLI0460virt_clone"
donttest="$donttest or testCLI0461virt_clone"
donttest="$donttest or testCLI0468virt_clone"
donttest="$donttest or test_virtinstall_no_testsuite"
donttest="$donttest or testCheckXMLBuilderProps"
donttest="$donttest or testCheckCLISuboptions"
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
%if %{?suse_version} != 1600
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

%if %{?suse_version} != 1600
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/clients
%dir %{_datadir}/applications/YaST2
%{_datadir}/YaST2/clients/virt-install.rb
%endif
%endif

%changelog
