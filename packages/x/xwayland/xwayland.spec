#
# spec file for package xwayland
#
# Copyright (c) 2021 SUSE LLC
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


%define have_wayland_eglstream 0

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           xwayland
Version:        21.1.1
Release:        0
URL:            http://xorg.freedesktop.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        X
# Source URL: https://xorg.freedesktop.org/archive/individual/xserver/
License:        MIT
Group:          System/X11/Servers/XF86_4
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sig
BuildRequires:  meson
BuildRequires:  ninja
#BuildRequires:  bison
#BuildRequires:  flex
#BuildRequires:  libtool
BuildRequires:  pkgconfig
#BuildRequires:  systemd-rpm-macros
BuildRequires:  rendercheck
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto)
#BuildRequires:  pkgconfig(dbus-1)
#BuildRequires:  pkgconfig(dmx)
BuildRequires:  pkgconfig(dri)
#BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(dri3proto)
#BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
%if 0%{?have_wayland_eglstream} == 1
BuildRequires:  pkgconfig(wayland-eglstream-protocols)
%endif
BuildRequires:  pkgconfig(fixesproto)
#BuildRequires:  pkgconfig(fontconfig)
#BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontutil)
#BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
#BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libdrm)
#BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openssl)
#BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
#BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(videoproto)
#BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xinput)
#BuildRequires:  pkgconfig(xaw7)
#BuildRequires:  pkgconfig(xcb-aux)
#BuildRequires:  pkgconfig(xcb-icccm)
#BuildRequires:  pkgconfig(xcb-image)
#BuildRequires:  pkgconfig(xcb-keysyms)
#BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xdmcp)
#BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
#BuildRequires:  pkgconfig(xf86dgaproto)
#BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
#BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfont2)
#BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  pkgconfig(xkbfile)
#BuildRequires:  pkgconfig(xmu)
#BuildRequires:  pkgconfig(xorg-macros)
#BuildRequires:  pkgconfig(xp)
#BuildRequires:  pkgconfig(xpm)
#BuildRequires:  pkgconfig(xprintutil)
BuildRequires:  pkgconfig(xproto)
#BuildRequires:  pkgconfig(xrender)
#BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xshmfence)
#BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans)
#BuildRequires:  pkgconfig(xtst)
#BuildRequires:  pkgconfig(xv)

#BuildRequires:  pkgconfig(libudev)


%ifnarch s390 s390x
Requires(pre):  %fillup_prereq
%endif
Requires:       pkgconfig
Requires:       xkbcomp
#Recommends:     xorg-x11-fonts-core
%ifnarch s390 s390x
Requires:       libpixman-1-0
%endif
#Requires:       Mesa
#Requires:       xkeyboard-config
Obsoletes:      xorg-x11-server-wayland < %{version}
Provides:       xorg-x11-server-wayland = %{version}


%description
This package contains the Xwayland Server.

%package %{name}
Summary:        Xwayland Xserver
Group:          System/X11/Servers/XF86_4
Requires:       xkbcomp
Requires:       xkeyboard-config
Recommends:     xorg-x11-fonts-core

%description %{name}
This package contains the Xserver running on the Wayland Display Server.

%package devel
Summary:        Development files for Xwayland
Group:          System/Libraries
Requires:       meson
Requires:       c_compiler
Requires:       %{name}
#Requires:       pkgconfig(fontconfig)
#Requires:       pkgconfig(fontenc)
#Requires:       pkgconfig(freetype2)
#Requires:       pkgconfig(ice)
Requires:       pkgconfig(libdrm)
#Requires:       pkgconfig(libevdev)
#Requires:       pkgconfig(libudev)
#Requires:       pkgconfig(mtdev)
#Requires:       pkgconfig(sm)
#Requires:       pkgconfig(x11)
Requires:       pkgconfig(xau)
Requires:       pkgconfig(xdmcp)
#Requires:       pkgconfig(xext)
#Requires:       pkgconfig(xfixes)
Requires:       pkgconfig(xkbfile)
#Requires:       pkgconfig(xmu)
#Requires:       pkgconfig(xorg-macros)
#Requires:       pkgconfig(xp)
#Requires:       pkgconfig(xpm)
#Requires:       pkgconfig(xprintutil)
#Requires:       pkgconfig(xrender)
#Requires:       pkgconfig(xt)
Requires:       pkgconfig(xtrans)
Requires:       pkgconfig(xv)


%description devel
This package contains the Xwayland Server development files.

%prep
%setup -q -n %{name}-%{version}

%build
%define _lto_cflags %{nil}

#option('builder_addr', type: 'string', description: 'Builder address', value: 'xorg@lists.freedesktop.org')
#option('builder_string', type: 'string', description: 'Additional builder string')

#option('xkb_default_rules', type: 'string', value: 'evdev')
#option('xkb_default_model', type: 'string', value: 'pc105')
#option('xkb_default_layout', type: 'string', value: 'us')
#option('xkb_default_variant', type: 'string')
#option('xkb_default_options', type: 'string')

%{meson} \
   -Dglamor=true \
%if 0%{?have_wayland_eglstream} == 1
   -Dxwayland_eglstream=true \
%endif
   -Dxvfb=true \
   -Dglx=true \
   -Dxdmcp=true \
   -Dxdm-auth-1=true \
   -Dsecure-rpc=true \
   -Dipv6=true \
   -Dinput_thread=true \
   -Dvendor_name="SUSE LINUX" \
   -Dvendor_name_short="openSUSE" \
   -Dvendor_web="https://www.opensuse.org" \
   -Dlisten_tcp=false \
   -Dlisten_unix=true \
   -Dlisten_local=true \
   -Ddpms=true \
   -Dxf86bigfont=true \
   -Dscreensaver=true \
   -Dxres=true \
   -Dxace=true \
   -Dxselinux=false \
   -Dxinerama=true \
   -Dxcsecurity=true \
   -Dxv=true \
   -Dmitshm=true \
   -Dsha1=libcrypto \
   -Ddri3=true \
   -Dxwayland-path="%{_bindir}" \
   -Ddtrace=false \
   -Dlibunwind=false \
   -Dxkb_dir="/usr/share/X11/xkb" \
   -Dxkb_output_dir="/var/lib/xkb/compiled" \
   -Ddefault_font_path="/usr/share/fonts/misc:unscaled,\
/usr/share/fonts/Type1/,/usr/share/fonts/100dpi:unscaled,\
/usr/share/fonts/75dpi:unscaled,/usr/share/fonts/ghostscript/,\
/usr/share/fonts/cyrillic:unscaled,\
/usr/share/fonts/misc/sgi:unscaled,\
/usr/share/fonts/truetype/,built-ins" \
   %{nil}

%{meson_build}

%install
%{meson_install}
# Let xorg-x11-server provide the Xserver manual
rm -f %{buildroot}%{_mandir}/man1/Xserver.1
# Provided by xorg-x11-server
rm -f %{buildroot}%{_libdir}/xorg/protocol.txt

%files
%{_bindir}/Xwayland

%files devel
%defattr(-,root,root)
%ifnarch s390 s390x
%{_libdir}/pkgconfig/*.pc
%endif
%dir %{_libdir}/xorg
%{_mandir}/man1/Xwayland.1.gz

%changelog
