#
# spec file for package kitty
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


Name:           kitty
Version:        0.20.3
Release:        0
Summary:        A GPU-based terminal emulator
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://github.com/kovidgoyal/kitty
Source:         https://github.com/kovidgoyal/kitty/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         kitty-no-docs.patch
BuildRequires:  ImageMagick-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  harfbuzz-devel >= 1.5.0
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
# for 'tic'
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.5
BuildRequires:  terminfo
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dbus-1)
%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550
BuildRequires:  python3-Sphinx >= 1.7
%endif

%description
A terminal emulator that uses OpenGL for rendering.
Supports terminal features like: graphics, Unicode,
true-color, OpenType ligatures, mouse protocol, focus tracking,
bracketed paste and so on, and which can be controlled by scripts.

%prep
%setup -q
%if 0%{?sle_version} <= 150100 && ! (0%{?suse_version} >= 1550)
%patch0 -p1
%endif

find . -type f -exec sed -i 's@#!%{_bindir}/env python3$@#!%{_bindir}/python3@' {} +
find . -type f -exec sed -i 's@#!%{_bindir}/env python$@#!%{_bindir}/python@' {} +

%install
# yes they have a makefile, no they dont use it properly
# no they dont have a make install
# we used to have this in the build section but since rpm 4.16 buildroot is cleaned
python3 setup.py --verbose linux-package --prefix %{buildroot}%{_prefix}

%fdupes %{buildroot}%{_prefix}/lib

%files
%license LICENSE
%doc CHANGELOG.rst README.asciidoc
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/256x256/
%{_datadir}/icons/hicolor/256x256/apps/
%{_datadir}/terminfo/x/xterm-%{name}
%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/doc/%{name}
%{_mandir}/man5/kitty.conf.5%{?ext_man}
%endif

%changelog
