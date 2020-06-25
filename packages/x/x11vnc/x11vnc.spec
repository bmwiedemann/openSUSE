# vim: set ts=4 sw=4 et:
#
# spec file for package x11vnc
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


Name:           x11vnc
Version:        0.9.16
Release:        0
Summary:        VNC Server for Real X Displays
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/LibVNC/x11vnc
Source:         https://github.com/LibVNC/x11vnc/archive/%{version}.tar.gz
Source1:        %{name}-tkx11vnc.desktop
Source2:        x11vnc_ssh
Source3:        x11vnc.png
Source99:       %{name}-rpmlintrc
Patch1:         stack-check
Patch2:         x11vnc-thread-auth.diff
Patch3:         x11vnc-examples.diff
Patch4:         x11vnc.desktop.generics
Patch5:         10_usepkgconfig.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(avahi-client) >= 0.6.4
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
Requires:       iproute2

%description
x11vnc allows one to remotely view and interact with real X displays (i.e. a
display corresponding to a physical monitor, keyboard, and mouse) with any VNC
viewer. In this way it plays the role for Unix/X11 that WinVNC plays for
Windows.

For Unix, the VNC implementation includes a virtual X11 server Xvnc (usually
launched via the vncserver command) that is not associated with a real
display, but provides a "fake" one X11 clients (xterm, mozilla, etc.) can
attach to. A remote user then connects to Xvnc via the VNC client vncviewer
from anywhere on the network to view and interact with the whole virtual X11
desktop.

The VNC protocol is in most cases better suited for remote connections with
low bandwidth and high latency than is the X11 protocol. Also, with no state
maintained the viewing-end can crash, be rebooted, or relocated and the
applications and desktop continue running. Not so with X11.

%package frontend
Summary:        Simple GUI Frontend to x11vnc
Group:          System/X11/Utilities
Requires:       %{name} = %{version}-%{release}
Requires:       tcl
Requires:       tk

%description frontend
x11vnc allows one to remotely view and interact with real X displays (i.e. a
display corresponding to a physical monitor, keyboard, and mouse) with any VNC
viewer. In this way it plays the role for Unix/X11 that WinVNC plays for
Windows.

This package adds a simple GUI frontend to run x11vnc.

%prep
%setup -q
%patch1 -p1
# workaround for Factory, as maintaining that patch with fuzz==0 is
# too annoying (it patches files that are modified by other patches):
patch -p1 -i "%{PATCH2}"
%patch3 -p1
%patch4 -p1
%patch5 -p1
mv misc examples

%build
autoreconf -fiv
CFLAGS="%{optflags} -D_REENTRANT -fno-strict-aliasing -fcommon" \
%configure \
    --enable-shared \
    --with-gnu-ld \
    --with-ffmpeg \
    --with-x \
    --with-24bpp \
    --without-tightvnc-filetransfer \
    --with-ssl="%{_usr}" \
    --with-jpeg="%{_usr}" \
    --with-zlib="%{_usr}" \
    %{_target_cpu}-suse-linux

make %{?_smp_mflags}

%install
%make_install
install -m 0755 tkx11vnc "%{buildroot}%{_bindir}/"
install -m 0755 "%{SOURCE2}" "%{buildroot}%{_bindir}/"
install -D -m 0644 "%{SOURCE3}" "%{buildroot}%{_datadir}/pixmaps/x11vnc.png"
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/tkx11vnc.desktop"
for d in tkx11vnc x11vnc; do
    %suse_update_desktop_file -r "$d" System RemoteAccess
done

rm -rf "%{buildroot}%{_includedir}/rfb"

find examples -name 'Makefile*' -exec rm {} \;
find examples -type f -exec chmod 0644 {} \;

%files
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%doc examples
%{_bindir}/Xdummy
%{_bindir}/x11vnc
%{_bindir}/x11vnc_ssh
%{_mandir}/man1/x11vnc.1%{?ext_man}
%{_datadir}/applications/x11vnc.desktop
%{_datadir}/pixmaps/x11vnc.png

%files frontend
%{_bindir}/tkx11vnc
%{_datadir}/applications/tkx11vnc.desktop

%changelog
