#
# spec file for package xf86-video-voodoo
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


Name:           xf86-video-voodoo
Version:        1.2.6
Release:        0
Summary:        Voodoo video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz.sig
Source2:        xf86-video-voodoo.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v0000121Ad*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
ExcludeArch:    s390 s390x
%{?x11_abi_videodrv_req}

%description
voodoo is an Xorg driver for Voodoo 1 and Voodoo 2 series video cards.

On the Voodoo 1 the driver uses a shadow buffer in system memory as the
video adapter has only 3D acceleration. Selected portions of the shadow
framebuffer are copied out to the Voodoo board at the right time.
Because of this, the speed of the driver is very dependent on the CPU.
Processors nowadays are actually rather fast at moving data so we get
very good speed anyway as the shadow framebuffer is in cached RAM.

The Voodoo2 has 16bpp acceleration and the driver provides accelerated
versions of most operations except angled lines and stipples.
Accelerated alpha blending with the Render extension is also supported
as is DGA.

This driver supports 16bpp modes currently. The video hardware supports
image conversion from 24bpp to 16bpp but the hardware is 16bpp only.

The Voodoo 1 series cards can go up to 800x600 resolution while the
Voodoo 2 can reach 1024x768 providing it has at least 2Mb of frame
buffer memory. 1024x768 2D mode does not require two cards configured in
scan-line interleave mode (SLI).

Multihead and Xinerama configurations are supported. SLI configurations
will be treated as multiple video cards.

Limited support for DPMS screen saving is available. The "standby" and
"suspend" modes are just painting the screen black. The "off" mode turns
the Voodoo board off and thus works correctly.

This driver does not support a virtual screen size different from the
display size. This is a hardware limitation. 3D rendering is also not
supported.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc ChangeLog README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.4%{?ext_man}

%changelog
