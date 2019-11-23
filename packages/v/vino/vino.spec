#
# spec file for package vino
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vino
Version:        3.22.0
Release:        0
Summary:        GNOME VNC Server
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/vino/3.22/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM vino-error-on-wayland.patch boo#1122549 mgorse@suse.com -- have vino-server print an error if wayland is detected, rather than segfaulting.
Patch0:         vino-error-on-wayland.patch
# PATCH-FIX-UPSTREAM vino-CVE-2019-15681.patch boo#1155419 mgorse@suse.com -- fix uninitialized memory read in LibVNCServer.
Patch1:         vino-CVE-2019-15681.patch

BuildRequires:  fdupes
BuildRequires:  intltool >= 0.50.0
BuildRequires:  libavahi-glib-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gnutls) >= 2.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.0.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd)
# Disable telepathy support and pass --without-telepathy to configure
#BuildRequires:  pkgconfig(telepathy-glib) >= 0.18.0
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang

%description
A VNC Server for GNOME

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	--libexecdir=%{_libexecdir}/vino \
	--enable-ipv6 \
	--without-telepathy \
	--with-gnutls \
	--with-gcrypt \
	--with-avahi \
	--with-zlib \
	--with-jpeg \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/applications/vino-server.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.gschema.xml
# Disable telepathy support
#%%dir %%{_datadir}/telepathy/
#%%dir %%{_datadir}/telepathy/clients/
#%%{_datadir}/telepathy/clients/Vino.client
%{_libexecdir}/vino
%{_userunitdir}/vino-server.service

%files lang -f %{name}.lang

%changelog
