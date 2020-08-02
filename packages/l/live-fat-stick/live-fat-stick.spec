#
# spec file for package live-fat-stick
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           live-fat-stick
Version:        0.4.2
Release:        0
Summary:        Tool for creating live USB stick with a FAT partition
License:        GPL-2.0+
Group:          System/Management
URL:            https://github.com/cyberorg/live-fat-stick
Source0:        live-fat-stick
Source1:        live-usb-gui
Source2:        live-usb-gui.desktop
Source3:        live-grub-stick
Source4:        INSTRUCTIONS.fat.txt
Source5:		INSTRUCTIONS.gui.txt
Source6:		INSTRUCTIONS.grub.txt
Requires:       dd_rescue
Requires:       parted
Requires:       syslinux
Requires:       util-linux
%if 0%{?fedora_version}
Requires:       qemu-kvm
%else
Requires:       qemu-tools
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# depends on syslinux, which exists only for the following arches:
ExclusiveArch:  %ix86 x86_64 noarch
BuildArch:      noarch

%description
This tool creates multi-boot capable USB stick/hard disk images with
whole ISOs on a FAT32 partition, keeping existing data untouched.

%package -n live-grub-stick
Requires:       dd_rescue
Requires:       grub2
Requires:       lsb-release
Requires:       parted
Requires:       util-linux
%if 0%{?fedora_version}
Requires:       qemu-kvm
%else
Requires:       qemu-tools
%endif
Summary:        Tool for creating multiboot live USB stick using grub2
Group:          System/Management

%description -n live-grub-stick
This tool creates multi-boot capable USB stick/hard disk with whole ISOs on any partition
supported by grub2, keeping existing data untouched. This tool uses grub2
instead of syslinux to achieve the same goal as live-fat-stick.

%package -n live-usb-gui
Requires:       live-fat-stick = %{version}
Requires:       live-grub-stick = %{version}
%if 0%{?suse_version}
Recommends:     zenity kdialog
%else
Requires:       zenity
%endif
Summary:        zenity-based frontend for live-fat-stick
Group:          System/Management

%description -n live-usb-gui
A zenity/kdialog-based GUI that runs the live-fat-stick or live-grub-stick scripts.

%prep
cp %{_sourcedir}/INS*.txt .

%build

%install
install -d -m 755 %{buildroot}/%_bindir/
install -d -m 755 %{buildroot}/%_datadir/applications/
cp %{SOURCE0} %{buildroot}/%_bindir/
cp %{SOURCE1} %{buildroot}/%_bindir/
cp %{SOURCE3} %{buildroot}/%_bindir/
cp %{SOURCE2} %{buildroot}/%_datadir/applications/

chmod 755 %{buildroot}/usr/bin/*
%if 0%{?suse_version}
%suse_update_desktop_file live-usb-gui
%endif

%post -n live-usb-gui
%desktop_database_post

%postun -n live-usb-gui
%desktop_database_postun

%files
%defattr(-,root,root)
%doc INSTRUCTIONS.fat.txt
%_bindir/live-fat-stick

%files -n live-grub-stick
%defattr(-,root,root)
%doc INSTRUCTIONS.grub.txt
%_bindir/live-grub-stick

%files -n live-usb-gui
%defattr(-,root,root)
%doc INSTRUCTIONS.gui.txt
%_bindir/live-usb-gui
%_datadir/applications/live-usb-gui.desktop

%changelog
