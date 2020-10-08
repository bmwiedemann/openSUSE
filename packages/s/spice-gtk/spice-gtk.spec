#
# spec file for package spice-gtk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           spice-gtk
Version:        0.38
Release:        0
Summary:        Gtk client and libraries for SPICE remote desktop servers
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://spice-space.org
Source0:        https://spice-space.org/download/gtk/%{name}-%{version}.tar.xz
Source1:        https://spice-space.org/download/gtk/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        README.SUSE
# PATCH-FIX-OPENSUSE spice-gtk-polkit-privs.patch bnc#804184 dimstar@opensuse.org -- Set the polkit defaults to auth_admin
Patch0:         spice-gtk-polkit-privs.patch
Patch1:         Remove-celt-support.patch
Patch2:         0001-quic-Check-we-have-some-data-to-start-decoding-quic-.patch
Patch3:         0002-quic-Check-image-size-in-quic_decode_begin.patch
Patch4:         0003-quic-Check-RLE-lengths.patch
Patch5:         0004-quic-Avoid-possible-buffer-overflow-in-find_bucket.patch

BuildRequires:  cyrus-sasl-devel
BuildRequires:  gstreamer-plugins-bad
BuildRequires:  gstreamer-plugins-good
BuildRequires:  intltool
BuildRequires:  json-glib-devel
BuildRequires:  libacl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-pyparsing
BuildRequires:  python3-six
BuildRequires:  vala
BuildRequires:  perl(Text::CSV)
BuildRequires:  pkgconfig(cairo) >= 1.2.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.46
BuildRequires:  pkgconfig(glib-2.0) >= 2.46
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libphodav-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.49.91
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.21
BuildRequires:  pkgconfig(libusbredirhost) >= 0.7.1
BuildRequires:  pkgconfig(libusbredirparser-0.5) >= 0.4
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(opus) >= 0.9.14
BuildRequires:  pkgconfig(pixman-1) >= 0.17.7
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.96
# spice-protocol is bundled, but we still need the system-wide .pc file for the pkgconfig() requires magic
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(spice-protocol) >= 0.14.1
Requires(pre):  permissions
BuildRequires:  pkgconfig(libcacard) >= 2.5.1
BuildRequires:  pkgconfig(liblz4) >= 1.7.3

%description
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%package -n libspice-client-glib-2_0-8
Summary:        Gtk client and libraries for SPICE remote desktop servers
Group:          System/Libraries
Requires:       libspice-client-glib-helper

%description -n libspice-client-glib-2_0-8
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%package -n libspice-client-glib-helper
Summary:        Gtk client and libraries for SPICE remote desktop servers
Group:          System/Libraries
PreReq:         permissions
Requires:       group(kvm)

%description -n libspice-client-glib-helper
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows).
Contains helpers needed by the spice glib client library.

%package -n libspice-client-gtk-3_0-5
Summary:        Gtk client and libraries for SPICE remote desktop servers
Group:          System/Libraries

%description -n libspice-client-gtk-3_0-5
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%package -n typelib-1_0-SpiceClientGtk-3_0
Summary:        Gtk client and libraries for SPICE remote desktop servers - gi-bindings
Group:          System/Libraries

%description -n typelib-1_0-SpiceClientGtk-3_0
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%package -n typelib-1_0-SpiceClientGlib-2_0
Summary:        Gtk client and libraries for SPICE remote desktop servers - gi-bindings
Group:          System/Libraries

%description -n typelib-1_0-SpiceClientGlib-2_0
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%package devel
Summary:        Devel
Group:          Development/Languages/C and C++
Requires:       libspice-client-glib-2_0-8 = %{version}
Requires:       libspice-client-gtk-3_0-5 = %{version}
Requires:       typelib-1_0-SpiceClientGlib-2_0 = %{version}
Requires:       typelib-1_0-SpiceClientGtk-3_0 = %{version}

%description devel
A Gtk client and libraries for SPICE remote desktop servers, (Linux and Windows)

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cd subprojects/spice-common
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
cd ../../
cp %{SOURCE3} .

%build
%meson -Dvapi=enabled -Dlz4=enabled -Dsmartcard=enabled -Dusb-ids-path=/usr/share/hwdata/usb.ids
%meson_build

%install
%meson_install
%find_lang %{name}

%post -n libspice-client-glib-helper
%set_permissions %{_bindir}/spice-client-glib-usb-acl-helper

%verifyscript -n libspice-client-glib-helper
%verify_permissions -e %{_bindir}/spice-client-glib-usb-acl-helper

%post -n libspice-client-glib-2_0-8 -p /sbin/ldconfig
%postun -n libspice-client-glib-2_0-8 -p /sbin/ldconfig

%post -n libspice-client-gtk-3_0-5 -p /sbin/ldconfig
%postun -n libspice-client-gtk-3_0-5 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%doc README.SUSE
%{_bindir}/spicy
%{_bindir}/spicy-screenshot
%{_bindir}/spicy-stats

%files -n libspice-client-glib-2_0-8
%{_libdir}/libspice-client-glib-2.0.so.*

%files -n libspice-client-glib-helper
%verify(not mode) %attr(4750,root,kvm) %{_bindir}/spice-client-glib-usb-acl-helper
%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy

%files -n libspice-client-gtk-3_0-5
%{_libdir}/libspice-client-gtk-3.0.so.*

%files -n typelib-1_0-SpiceClientGlib-2_0
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib

%files -n typelib-1_0-SpiceClientGtk-3_0
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib

%files devel
%{_mandir}/man1/spice-client.1%{?ext_man}
%{_includedir}/spice-client-glib-2.0/
%{_includedir}/spice-client-gtk-3.0/
%{_libdir}/libspice-client-glib-2.0.so
%{_libdir}/libspice-client-gtk-3.0.so
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir
%doc %{_datadir}/gtk-doc/html/spice-gtk/
%{_datadir}/vala/vapi/*
%{_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{_libdir}/pkgconfig/spice-client-gtk-3.0.pc

%files lang -f %{name}.lang

%changelog
