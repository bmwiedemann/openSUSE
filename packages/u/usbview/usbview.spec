#
# spec file for package usbview
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


Name:           usbview
Version:        3.0
Release:        0
Summary:        USB Topology and Device Viewer
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/gregkh/usbview
Source:         https://github.com/gregkh/usbview/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  ImageMagick
BuildRequires:  automake
BuildRequires:  gtk3-devel
BuildRequires:  update-desktop-files

%description
USBView is a GTK program that displays the topography of the devices
that are plugged into the USB on a Linux machine. It also displays
information on each of the devices. This can be useful to determine if
a device is working properly.

%prep
%setup -q

%build
sh autogen.sh
%configure --disable-polkit

%install
%make_install
%suse_update_desktop_file -i %{name} System Monitor

%files
%license LICENSES/GPL-2.0-only.txt
%doc ChangeLog README
%{_bindir}/usbview
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/usbview.*
%{_mandir}/man?/*.*

%changelog
