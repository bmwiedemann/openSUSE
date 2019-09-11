#
# spec file for package usbview
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           usbview
Version:        2.0
Release:        0
Summary:        USB Topology and Device Viewer
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://www.kroah.com/linux-usb/
Source:         http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz
Source1:        %name.desktop
BuildRequires:  gtk3-devel
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
USBView is a GTK program that displays the topography of the devices
that are plugged into the USB on a Linux machine. It also displays
information on each of the devices. This can be useful to determine if
a device is working properly.



Authors:
--------
    Greg Kroah-Hartman <greg@kroah.com>

%prep
%setup -q

%build
%configure

%install
%makeinstall
%suse_update_desktop_file -i %name System Monitor

%files
%defattr(-,root,root)
%doc ChangeLog COPYING* README TODO
%{_bindir}/usbview
%{_datadir}/applications/*.desktop
%doc %{_mandir}/man?/*.*

%changelog
