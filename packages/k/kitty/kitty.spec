#
# spec file for package kitty
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


# sphinx_copybutton not in Factory
%bcond_with docs
Name:           kitty
Version:        0.27.1
Release:        0
Summary:        A GPU-based terminal emulator
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://github.com/kovidgoyal/kitty
Source:         https://github.com/kovidgoyal/kitty/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE optional-disable-docs.patch -- Optionally disable building documentation files
Patch0:         optional-disable-docs.patch
# PATCH-FIX-OPENSUSE fix-librsync-leap.patch -- Fix for Leap, as librsync header is missing the stdio.h header for FILE*
Patch1:         fix-librsync-leap.patch
BuildRequires:  ImageMagick-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  go >= 1.20
BuildRequires:  harfbuzz-devel >= 1.5.0
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  librsync-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  openssl-devel
# for 'tic'
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  terminfo
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dbus-1)
# Python requirements for Factory and Leap
%if 0%{?suse_version} > 1500
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-sphinxext-opengraph
%else
# Leap still provides python3.6 kitty requires at least 3.7
BuildRequires:  python39-devel
%endif
# Optional documentation requirements
%if %{with docs}
BuildRequires:  python3-Sphinx >= 1.7
BuildRequires:  python3-importlib-resources
BuildRequires:  python3-readthedocs-sphinx-ext
BuildRequires:  python3-sphinx-inline-tabs
BuildRequires:  python3-sphinxcontrib-copybutton
%endif

%description
A terminal emulator that uses OpenGL for rendering.
Supports terminal features like: graphics, Unicode,
true-color, OpenType ligatures, mouse protocol, focus tracking,
bracketed paste and so on, and which can be controlled by scripts.

%prep
%autosetup -p1 -a 1

%if 0%{?suse_version} > 1500
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python@' {} +
%else
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3.9@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python3.9@' {} +
%endif

%install
# yes they have a makefile, no they dont use it properly
# no they dont have a make install
# we used to have this in the build section but since rpm 4.16 buildroot is cleaned
%if 0%{?suse_version} > 1500
python3 \
%else
python3.9 -B \
%endif
  setup.py --verbose \
%if !%{with docs}
    --no-docs \
%endif
    linux-package \
    --prefix %{buildroot}%{_prefix} \
    --libdir-name %{_lib}

%fdupes %{buildroot}%{_libdir}/%{name}

%files
%license LICENSE
%doc CHANGELOG.rst README.asciidoc
%{_bindir}/%{name}
%{_bindir}/kitten
%{_libdir}/%{name}
%{_datadir}/applications/%{name}{,-open}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/terminfo/x/xterm-%{name}
%if %{with docs}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/doc/%{name}
%{_mandir}/man5/kitty.conf.5%{?ext_man}
%endif

%changelog
