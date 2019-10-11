#
# spec file for package spice-gtk
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# FIXME: /usr/bin/spice-client-glib-usb-acl-helper should be installed u+s, see bnc#744251.
# FIXME: Once phodav is packaged and available in openSUSE, enable pkgconfig(libphodav-2.0)
Name:           spice-gtk
Version:        0.37
Release:        0
Summary:        Gtk client and libraries for SPICE remote desktop servers
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://spice-space.org
Source0:        http://spice-space.org/download/gtk/%{name}-%{version}.tar.bz2
Source1:        http://spice-space.org/download/gtk/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source3:        README.SUSE
# PATCH-FIX-OPENSUSE spice-gtk-polkit-privs.patch bnc#804184 dimstar@opensuse.org -- Set the polkit defaults to auth_admin
Patch0:         spice-gtk-polkit-privs.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gstreamer-plugins-bad
BuildRequires:  gstreamer-plugins-good
BuildRequires:  intltool
BuildRequires:  json-glib-devel
BuildRequires:  libacl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
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
BuildRequires:  pkgconfig(gudev-1.0)
#BuildRequires:  pkgconfig(libphodav-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.49.91
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.16
BuildRequires:  pkgconfig(libusbredirhost) >= 0.7.1
BuildRequires:  pkgconfig(libusbredirparser-0.5) >= 0.4
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(pixman-1) >= 0.17.7
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.96
# spice-protocol is bundled, but we still need the system-wide .pc file for the pkgconfig() requires magic
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.15
Requires(pre):  permissions
Recommends:     %{name}-lang
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libcacard) >= 2.5.1
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
%endif

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
cp %{SOURCE3} .

%build
autoreconf -fi

export PYTHON=/usr/bin/python3
%configure \
    --disable-static \
    --enable-vala \
%if 0%{?is_opensuse} == 0
    --disable-lz4 \
    --disable-smartcard \
%endif
    --disable-silent-rules \
    --with-usb-ids-path=/usr/share/hwdata/usb.ids \
    %{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
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
%if 0%{?suse_version} >= 1500
%verify(not mode) %attr(4750,root,kvm) %{_bindir}/spice-client-glib-usb-acl-helper
%else
%attr(755,root,root) %{_bindir}/spice-client-glib-usb-acl-helper
%endif
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
