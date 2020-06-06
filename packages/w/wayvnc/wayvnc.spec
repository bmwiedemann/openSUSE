#
# spec file for package wayvnc
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.1.2
Release:        0
Summary:        A VNC server for wlroots based Wayland compositors
License:        ISC
Group:          System/GUI/Other
URL:            https://github.com/any1/wayvnc
Source0:        https://github.com/any1/wayvnc/archive/v%{version}.tar.gz
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  gegl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  libuv-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  meson
BuildRequires:  neatvnc-devel
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel

%description
This is a VNC server for wlroots based Wayland compositors.
It attaches to a running Wayland session, creates virtual input devices and exposes a single display via the RFB protocol.
The Wayland session may be a headless one, so it is also possible to run wayvnc without a physical display attached.

%prep
%setup -q

%build
%meson

%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayvnc
%dir %{_datadir}/wayvnc/
%{_datadir}/wayvnc/shaders/

%changelog
