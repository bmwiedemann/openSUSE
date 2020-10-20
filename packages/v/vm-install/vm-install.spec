#
# spec file for package vm-install
#
# Copyright (c) 2020 SUSE LLC
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


Name:           vm-install
%if %suse_version <= 1230
%define with_vminstall_as_default_installer 1
%endif
URL:            http://developer.novell.com/wiki/index.php/Vm-install
BuildRequires:  python3-devel
%if %{?with_vminstall_as_default_installer}0
BuildRequires:  update-desktop-files
%endif
# For directory ownership:
BuildRequires:  yast2
Version:        0.10.08
Release:        0
Summary:        Tool to Define a Virtual Machine and Install Its Operating System
License:        GPL-2.0-only
Group:          System/Emulators/PC
Source0:        %{name}-0.10.08.tar.bz2
Source1:        vm-install.conf
Patch1:         vm-install-extra-args.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       kdump
Requires:       python3-dbus-python
Requires:       python3-libvirt-python
Requires:       python3-libxml2-python
Requires:       python3-netifaces
Requires:       python3-pycurl
%if %suse_version > 1230
Requires:       qemu-tools
%else
Requires:       virt-utils
%endif
# FATE324167: vm-install: remove deps on udhcp on SLE15
%if 0%{?is_opensuse} && 0%{?suse_version} < 1500
Requires:       udhcp
%endif
Requires:       usbutils
Requires:       tftp(client)
%define pysite %(python3 -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())")
Recommends:     python3-gobject

%description
vm-install can define a Xen virtual machine, and cause an operating
system to begin installing within that virtual machine.

vm-install can be used in a variety of ways:

* It can be used interactively or non-interactively.

* It can automatically pick reasonable VM defaults for a given type
   of operating system.

* It can perform completely non-interactive installs, driven via XML
   files and/or command line parameters.

* The  supporting  Python  modules  can  be 'import'-ed into other
Python programs, to create VMs programmatically.



Authors:
--------
    Charles Coffing <ccoffing@novell.com>

%prep
%setup -q
%patch1 -p1

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f  $RPM_BUILD_ROOT/%pysite/*.egg-info
%find_lang xen-vm-install
%if %{?with_vminstall_as_default_installer}0
%suse_update_desktop_file %{name} X-SuSE-YaST-Virtualization
%else
rm -f  $RPM_BUILD_ROOT/%{_datadir}/applications/YaST2/vm-install.desktop
%endif
mkdir -p $RPM_BUILD_ROOT/etc/default
install -m644 %SOURCE1 $RPM_BUILD_ROOT/etc/default/vm-install

%clean
test ! -z "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%files -f xen-vm-install.lang
%defattr(-,root,root,-)
%doc COPYING
%{_mandir}/man8/*.8.gz
%{_prefix}/bin/vm-disks
%{_prefix}/bin/vm-install
%{_prefix}/bin/vm-install-jobs
%{_datadir}/vm-install
%pysite/vminstall
%pysite/vmdisks
%{_datadir}/YaST2/clients/vm-install.rb
%if %{?with_vminstall_as_default_installer}0
%{_datadir}/applications/YaST2/vm-install.desktop
%endif
%config(noreplace) %{_sysconfdir}/default/vm-install

%changelog
