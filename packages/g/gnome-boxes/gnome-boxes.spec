#
# spec file for package gnome-boxes
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define govf_libver 0_1
%define gfrdp_libver 0_1
%define govf_sover 0.1
%define gfrdp_sover 0.1
Name:           gnome-boxes
Version:        40.1
Release:        0
Summary:        A GNOME 3 application to access remote or virtual systems
License:        LGPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Design/Apps/Boxes
Source0:        https://download.gnome.org/sources/gnome-boxes/40/%{name}-%{version}.tar.xz

# PATCH-FEATURE-OPENSUSE fcrozat@suse.com -- Ensure Tumbleweed is listed as recommended distribution
Patch0:         gnome-boxes-opensuse.patch
BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.36.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20
BuildRequires:  pkgconfig(gtk-vnc-2.0) >= 0.4.4
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gudev-1.0) >= 165
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libosinfo-1.0) >= 1.7
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.38
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.9
BuildRequires:  pkgconfig(libvirt-gconfig-1.0) >= 4.0.0
BuildRequires:  pkgconfig(libvirt-gobject-1.0) >= 3.0.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(spice-client-gtk-3.0) >= 0.32
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
# Needed for unattended installations
Requires:       fuseiso
# Need libvirtd and an hypervisor
Requires:       libvirt-daemon-qemu
# Needed for unattended installations
Requires:       mtools
# gnome-boxes requires org.freedesktop.Tracker.FTS schema to be available (bnc#785356).
Requires:       tracker

%description
Boxes is an application to create, setup, access, and use: remote
machines, remote and local virtual machines, and, when technology permits,
applications on local virtual machines.

%package -n libgovf-%{govf_libver}
Summary:        Shared library for libovf-glib, a virtual machine image library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libgovf-%{govf_libver}
Libgovf is a library for reading and writing virtual machine images
in the Open Virtualization Format.

This package provides the shared library for libovf-glib.

%package -n libgtk-frdp-%{gfrdp_libver}
Summary:        Shared library for gtk-frdp, an RDP Viewer Widget for Gtk+
License:        GPL-3.0-or-later
Group:          System/Libraries
Obsoletes:      gtk-frdp < 3.29.4

%description -n libgtk-frdp-%{gfrdp_libver}
gtk-frdp is an RDP viewer widget for the GNOME Desktop Environment.

This package provides the shared library for libgtk-frdp.

%package -n typelib-1_0-Govf-%{govf_libver}
Summary:        Introspection Bindings for libovf-glib, a virtual machine image library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n typelib-1_0-Govf-%{govf_libver}
Libgovf is a library for reading and writing virtual machine images
in the Open Virtualization Format.

This package provides the GObject Introspection bindings for libovf-glib.

%package -n typelib-1_0-GtkFrdp-%{gfrdp_libver}
Summary:        Introspection Bindings for gtk-frdp, an RDP Viewer Widget for Gtk+
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n typelib-1_0-GtkFrdp-%{gfrdp_libver}
gtk-frdp is an RDP viewer widget for the GNOME Desktop Environment.

This package provides the GObject Introspection bindings for libgtk-frdp.

%package -n libovf-glib-devel
Summary:        Development Files for gtk-frdp, a virtual machine image library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       libgovf-%{govf_libver} = %{version}
Requires:       typelib-1_0-Govf-%{govf_libver} = %{version}

%description -n libovf-glib-devel
Libgovf is a library for reading and writing virtual machine images
in the Open Virtualization Format.

This package provides all the necessary files for development with
libovf-glib.

%package -n gtk-frdp-devel
Summary:        Development Files for gtk-frdp, an RDP Viewer Widget for Gtk+
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       libgtk-frdp-%{gfrdp_libver} = %{version}
Requires:       typelib-1_0-GtkFrdp-%{gfrdp_libver} = %{version}

%description -n gtk-frdp-devel
gtk-frdp is an RDP viewer widget for the GNOME Desktop Environment.

This package provides all the necessary files for development with libgtk-frdp.

%package -n gnome-shell-search-provider-boxes
Summary:        Shell search provider for GNOME Boxes
License:        LGPL-2.0-or-later
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-boxes
Boxes is an application to create, setup, access, and use: remote
machines, remote and local virtual machines, and, when technology permits,
applications on local virtual machines.

This package contains a search provider to enable GNOME Shell to get
search results from Boxes.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson \
  -Drdp=true
%meson_build

%check
%meson_test

%install
%meson_install
%suse_update_desktop_file -r org.gnome.Boxes %{name} GNOME GTK System Emulator
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%post   -n libgovf-%{govf_libver} -p /sbin/ldconfig
%post   -n libgtk-frdp-%{gfrdp_libver} -p /sbin/ldconfig

%postun -n libgovf-%{govf_libver} -p /sbin/ldconfig
%postun -n libgtk-frdp-%{gfrdp_libver} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS HACKING README.md README.logos
%doc %{_datadir}/help/C/gnome-boxes
%{_bindir}/gnome-boxes
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Boxes.appdata.xml
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%dir %{_datadir}/gnome-boxes
%dir %{_datadir}/gnome-boxes/sources
%dir %{_datadir}/gnome-boxes/unattended
%{_datadir}/gnome-boxes/osinfo/
%{_datadir}/gnome-boxes/sources/QEMU_Session
%{_datadir}/gnome-boxes/unattended/disk.img
%{_datadir}/icons/hicolor/*/apps/org.gnome.Boxes*

%files -n libgovf-%{govf_libver}
%dir %{_libdir}/gnome-boxes/
%{_libdir}/gnome-boxes/libgovf-%{govf_sover}.so

%files -n libgtk-frdp-%{gfrdp_libver}
%dir %{_libdir}/gnome-boxes/
%{_libdir}/gnome-boxes/libgtk-frdp-%{gfrdp_sover}.so

%files -n typelib-1_0-Govf-%{govf_libver}
%dir %{_libdir}/gnome-boxes/girepository-1.0
%{_libdir}/gnome-boxes/girepository-1.0/Govf-%{govf_sover}.typelib

%files -n typelib-1_0-GtkFrdp-%{gfrdp_libver}
%dir %{_libdir}/gnome-boxes/girepository-1.0
%{_libdir}/gnome-boxes/girepository-1.0/GtkFrdp-%{gfrdp_sover}.typelib

%files -n libovf-glib-devel
%dir %{_datadir}/gnome-boxes/
%dir %{_datadir}/gnome-boxes/gir-1.0/
%dir %{_datadir}/gnome-boxes/vapi/
%dir %{_includedir}/gnome-boxes/
%dir %{_includedir}/gnome-boxes/govf/
%dir %{_libdir}/gnome-boxes/pkgconfig/
%{_libdir}/gnome-boxes/pkgconfig/govf-%{govf_sover}.pc
%{_datadir}/gnome-boxes/vapi/govf-%{govf_sover}.deps
%{_datadir}/gnome-boxes/vapi/govf-%{govf_sover}.vapi
%{_datadir}/gnome-boxes/gir-1.0/Govf-%{govf_sover}.gir
%{_includedir}/gnome-boxes/govf/govf-disk.h
%{_includedir}/gnome-boxes/govf/govf-package.h
%{_includedir}/gnome-boxes/govf/govf.h

%files -n gtk-frdp-devel
%dir %{_datadir}/gnome-boxes/
%dir %{_datadir}/gnome-boxes/gir-1.0/
%dir %{_datadir}/gnome-boxes/vapi/
%dir %{_includedir}/gnome-boxes/
%dir %{_includedir}/gnome-boxes/gtk-frdp/
%dir %{_libdir}/gnome-boxes/pkgconfig/
%{_libdir}/gnome-boxes/pkgconfig/gtk-frdp-%{gfrdp_sover}.pc
%{_datadir}/gnome-boxes/vapi/gtk-frdp-%{gfrdp_sover}.deps
%{_datadir}/gnome-boxes/vapi/gtk-frdp-%{gfrdp_sover}.vapi
%{_datadir}/gnome-boxes/gir-1.0/GtkFrdp-%{gfrdp_sover}.gir
%{_includedir}/gnome-boxes/gtk-frdp/frdp-display.h
%{_includedir}/gnome-boxes/gtk-frdp/frdp-session.h
%{_includedir}/gnome-boxes/gtk-frdp/gtk-frdp.h
%{_includedir}/gnome-boxes/gtk-frdp/gtk-frdp-version.h

%files -n gnome-shell-search-provider-boxes
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_libexecdir}/gnome-boxes-search-provider

%files lang -f %{name}.lang

%changelog
