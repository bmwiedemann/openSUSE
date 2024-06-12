#
# spec file
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
Source0:        https://releases.pagure.org/virt-manager/virt-manager-%{version}.tar.gz
Source1:        virt-install.rb
Source2:        virt-install.desktop
Source3:        virt-manager-supportconfig
# Upstream Patches
Patch1:         001-cli-disk-Add-driver.metadata_cache-options.patch
Patch2:         002-tests-cli-Fix-test-output-after-previous-commit.patch
Patch3:         003-fsdetails-Fix-an-error-with-source.socket-of-virtiofs.patch
Patch4:         004-cli-Drop-unnecessary-disk-prop-aliases.patch
Patch5:         005-tests-testdriver-Add-filesystem-socket-example.patch
Patch6:         006-virtinstall-split-no_install-conditional-apart-to-track-code-coverage.patch
Patch7:         007-virtinstall-fix-regression-with-boot-and-no-install-method.patch
Patch8:         008-tests-Add-a-compat-check-for-linux2020-in-amd-sev-test-case.patch
Patch9:         009-cli-cpu-Add-maxphysaddr.mode-bits-options.patch
Patch10:        010-virt-install-help-required-options-are-wrong.patch
Patch11:        011-cloner-Sync-uuid-and-sysinfo-system-uuid.patch
Patch12:        012-virt-install-unattended-and-cloud-init-conflict.patch
Patch13:        013-virt-install-Reuse-cli.fail_conflicting.patch
Patch14:        014-cli-support-boot-loader.stateless-.patch
Patch15:        015-diskbackend-Drop-support-for-sheepdog.patch
Patch16:        016-Fix-pylint-pycodestyle-warnings-with-latest-versions.patch
Patch17:        017-tests-cpio-set-owner-to-00.patch
Patch18:        018-addhardware-Fix-backtrace-when-controller.index-is-None.patch
Patch19:        019-Clean-up-FileChooser-usage-a-bit.patch
Patch20:        020-guest-Query-availability-of-usb-redirdevs-in-domcaps.patch
Patch21:        021-guest-Query-availability-of-spicevmc-channels-in-domcaps.patch
Patch22:        022-tests-Add-domcaps-coverage-for-usb-redir-spicevmc-channel-checks.patch
Patch23:        023-tests-Update-to-latest-kvm-domcaps.patch
Patch24:        024-progress-Fix-showing-correct-final-total.patch
Patch25:        025-virtinstall-Fix-the-allocating-disk-size-printed-by-the-progress-bar.patch
Patch26:        026-virtinstall-Hide-total_size-in-the-progress-bar-if-it-doesnt-need.patch
Patch27:        027-asyncjob-Fix-backtrace-when-no-cursor-theme-installed.patch
Patch29:        029-asyncjob-Remove-unused-import.patch
Patch30:        030-Packit-initial-enablement.patch
Patch31:        031-virt-install-Recommend-boot-uefi.patch
Patch32:        032-virt-install-Document-Secure-Boot-setups.patch
Patch33:        033-cloner-clone-serial-files.patch
Patch34:        034-tests-cli-test-serial-file-clone.patch
Patch35:        035-man-virt-install-Add-a-note-about-different-behavior-of-boot-on-s390x.patch
Patch36:        036-tests-uitests-Fix-window-reposition-on-f38.patch
Patch37:        037-tests-livetests-work-around-qemu-media-change-regression.patch
Patch38:        038-tests-uitests-Fix-manager-window-repositioning-test.patch
Patch39:        039-tests-Default-uitests-to-verbosity-2.patch
Patch40:        040-uitests-Make-hotplug-test-pass-on-both-f37-and-f38.patch
Patch41:        041-uitests-More-attempts-at-making-manager-reposition-test-reliable.patch
Patch42:        042-tests-uitests-make-menu-operations-more-robust.patch
Patch43:        043-rpm-convert-license-to-SPDX-format.patch
Patch44:        044-uitests-Drop-hotplug-work-around-f38-libvirt-is-fixed-now.patch
Patch45:        045-virtinst-delay-lookup_capsinfo-until-we-really-need-it.patch
Patch46:        046-virtinst-suppress-lookup_capsinfo-exception-in-machine-type-alias-check.patch
Patch47:        047-tests-data-refresh-Fedora-tree-URLs-in-virt-install-osinfo-expected-XMLs.patch
Patch48:        048-tests-Add-unit-test-coverage-for-539.patch
Patch49:        049-fix-indentation-of-multiline-log.exception-invocations.patch
Patch50:        050-virt-clone-Copy-disk-permissions-as-well.patch
Patch51:        051-data-appstream-add-launchable-tag.patch
Patch52:        052-Fix-some-pylint.patch
Patch55:        055-connectauth-Drop-sanity-checking-for-libvirtd.patch
Patch56:        056-delete-Fix-ambiguity-that-confused-pylint.patch
Patch57:        057-Fix-filesystem-socket.source.patch
Patch58:        058-uri-Mock-domcaps-returning-NO_SUPPORT.patch
Patch59:        059-tests-cli-Adjust-hotplug-test-for-latest-libvirt.patch
Patch60:        060-Fix-some-pylint.patch
Patch61:        061-tests-ui-make-newvm-test-start-less-flakey.patch
Patch62:        062-tests-ui-make-creatnet-test-start-less-flakey.patch
Patch63:        063-Support-creating-sparse-volumes-on-ZFS-pools.patch
Patch64:        064-domain-rename-handle-firmware-ending-with-.qcow2.patch
Patch65:        065-testdriver-Add-portgroups-example-to-test-many-devices.patch
Patch66:        066-netlist-Fix-UI-error-when-virtual-network-doesnt-exist.patch
Patch67:        067-ui-details-fix-Applications-width.patch
Patch68:        068-ui-details-Increased-scrolledview6s-height-request.patch
Patch69:        069-uitests-Fix-walkUI-flakyness.patch
Patch70:        070-uitests-Handle-slow-app-launch-on-fedora-39.patch
Patch71:        071-createvm-Replace-deprecated-pkgutil.find_loader.patch
Patch72:        072-Fix-pylint-3.1.0-issues.patch
Patch73:        073-console-Move-embeddable_graphics-to-console.py.patch
Patch74:        074-domain-Add-idx-parameter-to-open_graphics_fd.patch
Patch75:        075-console-Select-the-first-embeddable-graphics-device-as-graphical-console.patch
Patch76:        076-console-Cleanup-and-improve-console-menu-handling.patch
Patch77:        077-cli-add-show-systray-option.patch
Patch78:        078-man-document-show-systray-option.patch
Patch79:        079-baseclass-Avoid-glib-Source-ID-XX-not-found-at-app-shutdown.patch
Patch80:        080-uitests-More-handling-for-slow-startup-on-f39.patch
Patch81:        081-systray-Cleanups-and-improvements-for-show-systray.patch
Patch82:        082-virtinst-add-external-snapshot-capability.patch
Patch83:        083-virtinst-snapshot-add-memory-file-attribute.patch
Patch84:        084-virtManager-domain-allow-disk-only-snapshots.patch
Patch85:        085-virtManager-add-support-to-create-external-snapshots.patch
Patch86:        086-virtManager-ignore-agen-livecycle-event-for-shutoff-VMs.patch
Patch87:        087-Allow-serial-console-resize-to-beyond-80-columns.patch
Patch88:        088-tests-Fix-host-copy-XML-with-libvirt-10.1.0.patch
Patch89:        089-hostdev-Fix-error-when-mdev-type_id-is-missing.patch
Patch90:        090-db1b2fbc-Use-GtkFileChooserNative.patch
Patch91:        091-uitests-Fix-with-GtkFileChooserNative.patch
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
Patch227:       virtinst-add-pvh-support.patch
Patch228:       virtinst-media-detection.patch
Patch229:       virtinst-enable-video-virtio-for-arm.patch
# Bug Fixes
Patch251:       virtman-increase-setKeepAlive-count.patch
Patch252:       virtman-allow-destroy-from-shutdown-menu-of-crashed-vm.patch
Patch253:       virtman-allow-creating-i686-vm.patch
Patch254:       virtman-dont-specify-vte-version.patch
Patch255:       virtman-dont-specify-gtksource-version.patch
Patch256:       virtman-fix-restore-vm-menu-selection.patch
Patch257:       virtman-disallow-adding-floppy-disk.patch
Patch258:       virtman-register-delete-event-for-details-dialog.patch
Patch259:       virtman-revert-use-of-AyatanaAppIndicator3.patch
Patch270:       virtinst-xen-drive-type.patch
Patch271:       virtinst-xenbus-disk-index-fix.patch
Patch272:       virtinst-refresh_before_fetch_pool.patch
Patch273:       virtinst-use-xenpae-kernel-for-32bit.patch
Patch274:       virtinst-use-qemu-for-cdrom-device.patch
Patch275:       virtinst-keep-install-iso-attached.patch
Patch276:       virtinst-dont-use-special-copy-cpu-features.patch
Patch277:       virtinst-set-default-nic.patch
Patch278:       virtinst-sap-detection.patch
Patch279:       virtinst-smbios-unsupported-for-xenpv.patch
Patch280:       virtinst-keep-iso-for-xenpv.patch
Patch281:       virtinst-add-slem-detection-support.patch
Patch282:       virtinst-add-sle-hpc-support.patch
Patch283:       virtinst-add-oracle-linux-support.patch
Patch284:       virtinst-add-slm-detection-support.patch
Patch285:       virtinst-windows-server-detection.patch
Patch286:       virtman-fix-shared-disk-request-alignment-error.patch
Patch287:       virtman-language-fixes.patch
Patch288:       virtman-fix-inspection-apps-window.patch

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
# depends on osc/obs host cpu?
donttest="$donttest or testCLI0003virt_install_singleton_config_2"
donttest="$donttest or testCLI0113virt_install_reinstall_cdrom"
donttest="$donttest or testCLI0165virt_install"
donttest="$donttest or testCLI0172virt_install_s390x_cdrom"
# Fedora specific
donttest="$donttest or testCLI0178virt_install_arm_defaultmach_f20"
donttest="$donttest or testCLI0179virt_install_arm_kvm_import"
donttest="$donttest or testCLI0193virt_install_xen_default"
donttest="$donttest or testCLI0194virt_install_xen_pv"
donttest="$donttest or testCLI0195virt_install_xen_hvm"
donttest="$donttest or testCLI0196virt_install_xen_hvm"
donttest="$donttest or testCLI0203virt_install_bhyve_default_f27"
donttest="$donttest or testCLI0280virt_xml_build_disk_domain"
donttest="$donttest or testCLI0287virt_xml_edit_cpu_host_copy"
donttest="$donttest or testCLI0288virt_xml_build_pool_logical_disk"
donttest="$donttest or testCLI0375virt_xml_add_disk_create_storage_start"
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
