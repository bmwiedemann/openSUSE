#
# spec file for package virt-viewer
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           virt-viewer
Summary:        Virtual Machine Viewer
License:        GPL-2.0-or-later
Group:          System/Monitoring
Version:        9.0
Release:        0
Url:            http://www.virt-manager.org
Source:         https://virt-manager.org/download/sources/virt-viewer/%name-%version.tar.gz
Patch50:        netcat.patch
Patch51:        virtview-desktop.patch
Patch52:        virtview-dont-show-Domain-0.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  automake
BuildRequires:  gtk-vnc-devel >= 0.3.8
BuildRequires:  intltool
BuildRequires:  libglade2-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  libxml2-devel
BuildRequires:  spice-gtk-devel
BuildRequires:  vte-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(libvirt) >= 0.10.0
BuildRequires:  pkgconfig(libvirt-glib-1.0) >= 0.1.8
# Our Runtime requirements
Requires:       netcat

%description
Virtual Machine Viewer provides a graphical console client for
connecting to virtual machines. It uses the GTK-VNC widget to provide
the display, and libvirt for looking up VNC server details.

%prep
%setup -q
%patch50 -p1
%patch51 -p1
%patch52 -p1

%build
%configure --with-spice-gtk --disable-update-mimedb
make %{?_smp_mflags}

%install
%makeinstall
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog
%dir %{_datadir}/appdata
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/24x24/devices/virt-viewer-usb.png
%{_datadir}/icons/hicolor/24x24/devices/virt-viewer-usb.svg
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_datadir}/appdata/remote-viewer.appdata.xml

%changelog
