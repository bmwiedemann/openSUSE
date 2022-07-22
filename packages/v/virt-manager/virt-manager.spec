#
# spec file for package virt-manager
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

Name:           virt-manager
Version:        4.0.0
Release:        0
Summary:        Virtual Machine Manager
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://virt-manager.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        virt-install.rb
Source2:        virt-install.desktop
Source3:        virt-manager-supportconfig
# Upstream Patches
Patch1:         revert-363fca41-virt-install-Require-osinfo-for-non-x86-HVM-case-too.patch
Patch2:         d51541e1-Fix-UI-rename-with-firmware-efi.patch
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Obsoletes:      python-virtinst <= 0.600.4
Supplements:    virt-manager

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%prep
%autosetup -p1

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

%find_lang %{name}

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

%changelog
