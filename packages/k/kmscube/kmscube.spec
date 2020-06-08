#
# spec file for package kmscube
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Guillaume GARDET <guillaume@opensuse.org>
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


Name:           kmscube
Version:        0.0.0.git1585705428.4660a7d
Release:        0
Summary:        Demo for bare metal graphics
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/bastibl/kmscube.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  meson >= 0.47
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gstreamer-devel >= 1.6.0
BuildRequires:  gstreamer-plugins-base-devel >= 1.6.0
BuildRequires:  libdrm-devel >= 2.4.71
BuildRequires:  libgbm-devel >= 13.0
BuildRequires:  make
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(x11)

%description
kmscube is a little demonstration program for how to drive bare metal graphics
without a compositor like X11, wayland or similar, using DRM/KMS (kernel mode
setting), GBM (graphics buffer manager) and EGL for rendering content using
OpenGL or OpenGL ES.

%prep
%setup -q
# Fix libpng detection
sed -i -e "s/'libpng'/'libpng16'/" meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_bindir}/*

%changelog
