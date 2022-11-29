#
# spec file
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


%global __python %{__python3}
%global with_guestfs               0
%global default_hvs                "qemu,xen,lxc"

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -%{flavor}
%else
%bcond_with test
%define psuffix %{nil}
%endif

Name:           virt-manager%{psuffix}
Version:        4.1.0
Release:        0
Summary:        Virtual Machine Manager
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://virt-manager.org/
Source0:        https://virt-manager.org/download/sources/virt-manager/virt-manager-%{version}.tar.gz
Source1:        virt-install.rb
Source2:        virt-install.desktop
Source3:        virt-manager-supportconfig
# Upstream Patches
Patch1:         revert-363fca41-virt-install-Require-osinfo-for-non-x86-HVM-case-too.patch
Patch2:         11a887ec-cli-disk-Add-driver.metadata_cache-options.patch
Patch3:         7295ebfb-tests-cli-Fix-test-output-after-previous-commit.patch
Patch4:         58f5e36d-fsdetails-Fix-an-error-with-source.socket-of-virtiofs.patch
Patch5:         1cb0be40-virtinstall-split-no_install-conditional-apart-to-track-code-coverage.patch
Patch6:         e94786c0-virtinstall-fix-regression-with-boot-and-no-install-method.patch
Patch7:         c22a876e-tests-Add-a-compat-check-for-linux2020-in-amd-sev-test-case.patch
Patch8:         fbdf0516-cli-cpu-Add-maxphysaddr.mode-bits-options.patch
Patch9:         b0d05167-cloner-Sync-uuid-and-sysinfo-system-uuid.patch
Patch10:        999ccb85-virt-install-unattended-and-cloud-init-conflict.patch
# SUSE Only
Patch70:        virtman-desktop.patch
Patch71:        virtman-kvm.patch
Patch72:        virtman-show-suse-install-repos.patch
Patch73:        virtman-dont-allow-grub.xen-to-be-deleted.patch
Patch74:        virtinst-pvgrub2-bootloader.patch
Patch75:        virtinst-change-location-for-grub_xen.patch
Patch76:        virtinst-set-qemu-emulator.patch
# Features or Enhancements
Patch103:       virtman-load-stored-uris.patch
Patch104:       virtman-add-tooltip-to-firmware.patch
Patch105:       virtman-modify-gui-defaults.patch
Patch106:       virtman-add-sev-memory-support.patch
Patch120:       virtinst-default-xen-to-qcow2-format.patch
Patch121:       virtinst-detect-oes-distros.patch
Patch122:       virtinst-vol-default-nocow.patch
Patch123:       virtinst-set-cache-mode-unsafe-for-install.patch
Patch124:       virtinst-s390x-disable-graphics.patch
Patch125:       virtinst-add-caasp-support.patch
Patch126:       virtinst-add-sle15-detection-support.patch
Patch127:       virtinst-add-pvh-support.patch
Patch128:       virtinst-media-detection.patch
# Bug Fixes
Patch151:       virtman-increase-setKeepAlive-count.patch
Patch152:       virtman-allow-destroy-from-shutdown-menu-of-crashed-vm.patch
Patch153:       virtman-check-for-valid-display.patch
Patch154:       virtman-allow-creating-i686-vm.patch
Patch155:       virtman-dont-specify-vte-version.patch
Patch156:       virtman-dont-specify-gtksource-version.patch
Patch157:       virtman-fix-restore-vm-menu-selection.patch
Patch158:       virtman-disallow-adding-floppy-disk.patch
Patch159:       virtman-register-delete-event-for-details-dialog.patch
Patch160:       virtman-revert-use-of-AyatanaAppIndicator3.patch
Patch161:       virtman-fix-uninitialized-controller-index.patch
Patch170:       virtinst-xen-drive-type.patch
Patch171:       virtinst-xenbus-disk-index-fix.patch
Patch172:       virtinst-refresh_before_fetch_pool.patch
Patch173:       virtinst-use-xenpae-kernel-for-32bit.patch
Patch174:       virtinst-use-qemu-for-cdrom-device.patch
Patch175:       virtinst-keep-install-iso-attached.patch
Patch176:       virtinst-dont-use-special-copy-cpu-features.patch
Patch177:       virtinst-set-default-nic.patch
Patch178:       virtinst-sap-detection.patch
Patch179:       virtinst-smbios-unsupported-for-xenpv.patch
Patch180:       virtinst-keep-iso-for-xenpv.patch
Patch181:       virtinst-add-slem-detection-support.patch
Patch182:       virtinst-add-sle-hpc-support.patch
Patch183:       virtinst-add-oracle-linux-support.patch
Patch184:       virtinst-windows-server-detection.patch

BuildArch:      noarch

%define verrel %{version}-%{release}
Requires:       dbus-1-x11
Requires:       dconf
Requires:       gstreamer-plugins-good
Requires:       gtk3
Requires:       python3-gobject
# For console widget
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Recommends:     python3-SpiceClientGtk
Requires:       virt-install
Requires:       virt-manager-common = %{verrel}
Requires:       typelib(GtkSource)

%if %{with_guestfs}
Requires:       python3-libguestfs
%endif

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
%if %{with test}
BuildRequires:  python3-argcomplete
BuildRequires:  python3-pytest
BuildRequires:  virt-install = %{version}
BuildRequires:  virt-manager = %{version}
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
Requires:       mkisofs
Requires:       python3-gobject
Requires:       python3-ipaddr
Requires:       python3-libvirt-python >= 0.7.0
Requires:       python3-libxml2-python
Requires:       python3-pycurl
Requires:       xorriso
Requires:       typelib(AppIndicator3)
Requires:       typelib(LibvirtGLib)
Suggests:       python3-virt-bootstrap
BuildRequires:  gobject-introspection

%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary:        Utilities for installing virtual machines
Group:          System/Monitoring

Requires:       virt-manager-common = %{verrel}

Requires:       python3-requests
Provides:       python3-virtinst
Provides:       virt-clone
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

python3 setup.py configure \
    --prefix=%{_prefix} \
    --default-graphics="spice" \
    %{?_default_hvs}

%install
python3 setup.py \
    --no-update-icon-cache \
    --no-compile-schemas install \
    --prefix=%{_prefix} \
    -O1 --root=%{buildroot}
mkdir -p %{buildroot}/%{_datadir}/YaST2/clients/
install -m644 %SOURCE1 %{buildroot}/%{_datadir}/YaST2/clients/virt-install.rb
mkdir -p %{buildroot}/%{_datadir}/applications/YaST2/
install -m644 %SOURCE2 %{buildroot}/%{_datadir}/applications/YaST2/virt-install.desktop
# Oddly, supportconfig doesn't execute plugins with '-' in the name, so use 'virt_manager'
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins
install -m 755 %SOURCE3 %{buildroot}/usr/lib/supportconfig/plugins/virt_manager
chmod -x %{buildroot}%{_datadir}/virt-manager/virtManager/virtmanager.py

%find_lang %{name}
%endif

%if %{with test}
%check
# TODO: check if these are genuine failures or due to the non-upstream patches
# different device names
donttest="test_disk_numtotarget"
donttest="$donttest or testCLI0001virt_install_many_devices"
donttest="$donttest or testCLI0113virt_install_reinstall_cdrom"
donttest="$donttest or testCLI0165virt_install"
donttest="$donttest or testCLI0172virt_install_s390x_cdrom"
donttest="$donttest or testCLI0193virt_install_xen_default"
donttest="$donttest or testCLI0194virt_install_xen_pv"
donttest="$donttest or testCLI0195virt_install_xen_hvm"
donttest="$donttest or testCLI0196virt_install_xen_hvm"
donttest="$donttest or testCLI0203virt_install_bhyve_default_f27"
donttest="$donttest or testCLI0276virt_xml_build_disk_domain"
donttest="$donttest or testCLI0277virt_xml_build_disk_domain"
donttest="$donttest or testCLI0280virt_xml_build_disk_domain"
donttest="$donttest or testCLI0284virt_xml_build_pool_logical_disk"
donttest="$donttest or testCLI0285virt_xml_build_pool_logical_disk"
donttest="$donttest or testCLI0287virt_xml_edit_cpu_host_copy"
donttest="$donttest or testCLI0288virt_xml_build_pool_logical_disk"
donttest="$donttest or testCLI0371virt_xml_add_disk_create_storage_start"
donttest="$donttest or testCLI0372virt_xml_add_disk_create_storage_start"
donttest="$donttest or testCLI0375virt_xml_add_disk_create_storage_start"
# depends on osc/obs host cpu?
donttest="$donttest or testCLI0003virt_install_singleton_config_2"
donttest="$donttest or testCLI0283virt_xml_edit_cpu_host_copy"
donttest="$donttest or testCLI0284virt_xml_edit_cpu_host_copy"
# RuntimeError: SEV launch security requires a Q35 machine -- due to patch for bsc#1196806, jsc#SLE-18834 ?
donttest="$donttest or testCLI0162virt_install"
# Expectsion <video> element
donttest="$donttest or testCLI0168virt_install_s390x_cdrom"
donttest="$donttest or testCLI0169virt_install_s390x_cdrom"
# missing <boot> element, extra <kernel> element
donttest="$donttest or testCLI0189virt_install_xen_default"
donttest="$donttest or testCLI0190virt_install_xen_default"
donttest="$donttest or testCLI0190virt_install_xen_pv"
donttest="$donttest or testCLI0191virt_install_xen_pv"
# different <emulator> additional <model> in <interface>
donttest="$donttest or testCLI0191virt_install_xen_hvm"
donttest="$donttest or testCLI0192virt_install_xen_hvm"
donttest="$donttest or testCLI0193virt_install_xen_hvm"
# different source image format
donttest="$donttest or testCLI0199virt_install_bhyve_default_f27"
donttest="$donttest or testCLI0200virt_install_bhyve_default_f27"
# Due to the above skips:
# "there are XML properties that are untested in the test suite"
donttest="$donttest or testCheckXMLBuilderProps"
# "These command line arguments or aliases are not checked in the test suite"
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
%{_datadir}/applications/YaST2/virt-install.desktop
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

%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/clients
%dir %{_datadir}/applications/YaST2
%{_datadir}/YaST2/clients/virt-install.rb
%endif

%changelog
