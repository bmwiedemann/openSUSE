#
# spec file for package xpra
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


%global __requires_exclude ^typelib\\(GtkosxApplication\\)|typelib\\(GdkGLExt\\)|typelib\\(GtkGLExt\\).*$
Name:           xpra
Version:        4.0.3
Release:        0
Summary:        Remote display server for applications and desktops
License:        GPL-2.0-or-later AND BSD-3-Clause AND LGPL-3.0-or-later AND MIT
URL:            https://www.xpra.org/
Source0:        https://xpra.org/src/%{name}-%{version}.tar.xz
Source1:        xpra-icon.png
# PATCH-FIX-OPENSUSE xpra-paths.patch -- use suse-specific paths
Patch0:         %{name}-paths.patch
BuildRequires:  ImageMagick
BuildRequires:  brotli
BuildRequires:  cups
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython >= 0.20.0
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libswscale) >= 5
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  pkgconfig(pygtk-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
Requires:       dbus-1-x11
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       pulseaudio
Requires:       pulseaudio-utils
Requires:       python3-Pillow
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject-Gdk
Requires:       python3-gst
Requires:       python3-lz4
Requires:       python3-numpy
Requires:       python3-opencv
Requires:       python3-pycups
Requires:       python3-rencode
Requires:       shared-mime-info
Requires:       xf86-video-dummy
Requires:       xorg-x11-xauth
Requires(post): %fillup_prereq
Recommends:     python3-dnspython
Recommends:     python3-opencv
Recommends:     python3-paramiko
Recommends:     python3-opengl
Recommends:     python3-opengl-accelerate
%{?systemd_ordering}

%description
Xpra is "screen for X": it allows you to run X programs, usually on a remote
host, direct their display to your local machine, and then to disconnect from
these programs and reconnect from the same or another machine, without losing
any state. It gives you remote access to individual applications.

Xpra is "rootless" or "seamless": programs you run under it show up on your
desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing
network bandwidth constraints.

%package        html5
Summary:        HTML5 server and client support for xpra
Requires:       %{name} = %{version}
# websockify is required to allow xpra to listen for an html5 client
Requires:       python3-websockify
Provides:       bundled(js-aurora)
Provides:       bundled(js-bencode)
Provides:       bundled(js-broadway)
Provides:       bundled(js-forge)
Provides:       bundled(js-jquery) = 3.1.1
Provides:       bundled(js-jquery-ui) = 1.12.1
Provides:       bundled(js-lz4)
Provides:       bundled(js-zlib)
BuildArch:      noarch

%description    html5
This package adds websockify support to allow xpra to listen for http
connections, and also the xpra html5 client.

%prep
%autosetup -p1
# fix shebangs
find -name '*.py' \
     -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} +
sed -i "1 s|^#!/usr/bin/env python\b|#!%__python3|" cups/xpraforwarder
sed -i "1 s|^/usr/bin/bash|#!$(which bash)|" scripts/xpra_udev_product_version
install -m0644 %{SOURCE1} -t xdg
# set fillup dir
sed -e 's|__FILLUPDIR__|%{_fillupdir}|' \
    -e 's|__UNITDIR__|%{_unitdir}|' \
    -i setup.py

%build
python3 setup.py build \
    --verbose \
    --with-enc_ffmpeg \
    --with-vpx \
    --with-dec_avcodec2 \
    --with-csc_swscale \
    --with-webp \
    --with-Xdummy \
    --with-Xdummy_wrapper \
    --with-opengl \
    --with-service

%install
python3 setup.py install \
    --skip-build \
    --root %{buildroot} \
    --prefix %{_prefix} \
    --with-service \
    --with-Xdummy \
    --with-Xdummy_wrapper \
    --verbose

#Install nvenc.keys file
mkdir -p %{buildroot}%{_sysconfdir}/xpra
install -pm 644 etc/xpra/nvenc.keys %{buildroot}%{_sysconfdir}/xpra

%suse_update_desktop_file -r xpra Network RemoteAccess
%suse_update_desktop_file -r xpra-gui Network RemoteAccess
%suse_update_desktop_file -r xpra-launcher Network RemoteAccess

mkdir -pv %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%fdupes -s %{buildroot}

%pre
getent group xpra >/dev/null || groupadd -r xpra
mkdir -p %{_rundir}/%{name} || exit 1
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only %{name}
%tmpfiles_create %{_tmpfilesdir}/xpra.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README NEWS
%license COPYING
%dir %{_datadir}/xpra
%dir %{_datadir}/xpra/content-categories
%dir %{_datadir}/xpra/content-type
%dir %{_datadir}/xpra/http-headers
%dir %{_prefix}/lib/xpra
%dir %{_sysconfdir}/pam.d
%dir %{_sysconfdir}/xpra
%dir %{_sysconfdir}/xpra/conf.d
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/xpra.conf
%config(noreplace) %{_sysconfdir}/pam.d/xpra
%config(noreplace) %{_sysconfdir}/xpra/*.conf
%config(noreplace) %{_sysconfdir}/xpra/nvenc.keys
%config(noreplace) %{_sysconfdir}/xpra/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/90-xpra-virtual.conf
%{_fillupdir}/sysconfig.%{name}
%{_bindir}/xpra
%{_bindir}/xpra_Xdummy
%{_bindir}/xpra_launcher
%{_bindir}/xpra_signal_listener
%{_bindir}/xpra_udev_product_version
%{_udevrulesdir}/71-xpra-virtual-pointer.rules
%{_prefix}/lib/xpra/auth_dialog
%{_prefix}/lib/xpra/gnome-open
%{_prefix}/lib/xpra/gvfs-open
%{_prefix}/lib/xpra/xdg-open
%{_sbindir}/rc%{name}
%{python3_sitearch}/xpra
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/applications/xpra-gui.desktop
%{_datadir}/applications/xpra-launcher.desktop
%{_datadir}/applications/xpra-shadow.desktop
%{_datadir}/applications/xpra.desktop
%{_datadir}/metainfo/xpra.appdata.xml
%{_datadir}/pixmaps/xpra-mdns.png
%{_datadir}/pixmaps/xpra-shadow.png
%{_datadir}/pixmaps/xpra.png
%{_datadir}/mime/packages/application-x-xpraconfig.xml
%{_datadir}/xpra/bell.wav
%{_datadir}/xpra/content-categories/10_default.conf
%{_datadir}/xpra/content-type/10_role.conf
%{_datadir}/xpra/content-type/30_title.conf
%{_datadir}/xpra/content-type/50_class.conf
%{_datadir}/xpra/content-type/70_commands.conf
%{_datadir}/xpra/http-headers/00_nocache.txt
%{_datadir}/xpra/http-headers/10_content_security_policy.txt
%{_datadir}/xpra/icons
%{_prefix}/lib/cups/backend/xpraforwarder
%{_mandir}/man1/xpra.1%{?ext_man}
%{_mandir}/man1/xpra_launcher.1%{?ext_man}
%{_sysusersdir}/xpra.conf
%{_tmpfilesdir}/xpra.conf
%{_unitdir}/xpra.service
%{_unitdir}/xpra.socket
%ghost %dir %{_rundir}/xpra

%files html5
%{_datadir}/xpra/www

%changelog
