#
# spec file for package ueberzugpp
#
# Copyright (c) 2024 SUSE LLC
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


%define short_name ueberzug
Name:           ueberzugpp
Version:        2.9.6+git20240609.7051b04
Release:        0
Summary:        Utility to render images in terminals
License:        GPL-3.0
URL:            https://github.com/jstkdng/%{name}
Source:         https://github.com/jstkdng/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(vips)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb-image)

%description
Überzug++ is a C++ command line utility which allows to draw images
on terminals by using child windows or using sixel on supported
terminals. (This is a drop-in replacement for the now defunct
ueberzug project.)

Advantages over w3mimgdisplay and ueberzug:

- support for wayland (sway only)
- no race conditions as a new window is created to display images
- "expose" events will be processed, so that images will be
  redrawn when switching workspaces
- tmux support on X11
- terminals without the WINDOWID environment variable are supported
- chars are used as position and size unit
- A lot of image formats are supported (through opencv and libvips)
- GIF and animated WEBP support on X11 and Sixel
- Resized images are cached for faster viewing

%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_SKIP_RPATH=YES -DCMAKE_BUILD_TYPE=release -DENABLE_WLROOTS=ON
%cmake_build

%install
%cmake_install
rm -v %{buildroot}%{_mandir}/man1/ueberzug.1
ln -s %{_mandir}/man1/ueberzugpp.1 %{buildroot}%{_mandir}/man1/ueberzug.1

%files
%{_bindir}/%{short_name}
%{_bindir}/%{short_name}pp
%license LICENSE
%doc README.md
%{_mandir}/man1/%{short_name}.1%{?ext_man}
%{_mandir}/man1/%{short_name}pp.1%{?ext_man}

%changelog

