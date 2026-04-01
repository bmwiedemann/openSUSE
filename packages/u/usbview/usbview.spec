#
# spec file for package usbview
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


Name:           usbview
Version:        3.1
Release:        0
Summary:        USB Topology and Device Viewer
License:        GPL-2.0-only
URL:            https://github.com/gregkh/usbview
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-make-PNG_XPM-transparent.patch gh#gregkh/usbview#30
Patch0:         fix-make-PNG_XPM-transparent.patch
# PATCH-FIX-UPSTREAM fix-support-for-SuperSpeed+20Gb_s.patch gh#gregkh/usbview#34
Patch1:         fix-support-for-SuperSpeed+20Gb_s.patch
BuildRequires:  ImageMagick
BuildRequires:  ImageMagick-config-7-upstream-open
BuildRequires:  appstream-glib
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)

%description
USBView is a GTK program that displays the topography of the devices
that are plugged into the USB on a Linux machine. It also displays
information on each of the devices. This can be useful to determine if
a device is working properly.

%prep
%autosetup -p1
desktop-file-edit --remove-key=Categories \
	--add-category=System --add-category=Monitor %{name}.desktop

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/com.kroah.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSES/GPL-2.0-only.txt
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/usbview.{png,svg}
%{_datadir}/metainfo/com.kroah.%{name}.metainfo.xml
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
