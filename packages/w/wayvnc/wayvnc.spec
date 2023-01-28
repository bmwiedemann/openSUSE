#
# spec file for package wayvnc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           wayvnc
Version:        0.6.2
Release:        0
Summary:        A VNC server for wlroots based Wayland compositors
License:        ISC
Group:          System/GUI/Other
URL:            https://github.com/any1/wayvnc
Source0:        https://github.com/any1/wayvnc/archive/v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  neatvnc-devel >= 0.6.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(gegl-sc-0.4)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glx)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libdrm_nouveau)
BuildRequires:  pkgconfig(libdrm_radeon)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
This is a VNC server for wlroots based Wayland compositors.
It attaches to a running Wayland session, creates virtual input devices and exposes a single display via the RFB protocol.
The Wayland session may be a headless one, so it is also possible to run wayvnc without a physical display attached.

%prep
%setup -q
find . -type f \( -name '*.c' -o -name '*.h' \) -exec sed -i "s|wayland-client.h|wayland/wayland-client.h|g" {} +

%build
%meson

%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayvnc
%{_bindir}/wayvncctl
%{_mandir}/man1/wayvnc.1%{?ext_man}
%{_mandir}/man1/wayvncctl.1%{?ext_man}

%changelog
