#
# spec file for package kitty
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


# sphinx_copybutton not in Factory
%bcond_with docs
Name:           kitty
Version:        0.35.2
Release:        0
Summary:        A GPU-based terminal emulator
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://github.com/kovidgoyal/kitty
Source:         https://github.com/kovidgoyal/kitty/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        kitty-rpmlintrc
Patch0:         buildmode-and-skip_docs.diff
BuildRequires:  ImageMagick-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  go >= 1.22
BuildRequires:  harfbuzz-devel >= 1.5.0
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  librsync-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  terminfo
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(simde)
# Python requirements for Factory and Leap
%if 0%{?suse_version} > 1500
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-sphinxext-opengraph
%else
# Leap still provides python3.6 kitty requires at least 3.7
%if 0%{?sle_version} > 150400
BuildRequires:  python311-devel
%else
%if 0%{?sle_version} > 150300
BuildRequires:  python310-devel
%else
BuildRequires:  python39-devel
%endif
%endif
%endif
# Optional documentation requirements
%if %{with docs}
BuildRequires:  python3-Sphinx >= 1.7
BuildRequires:  python3-importlib-resources
BuildRequires:  python3-readthedocs-sphinx-ext
BuildRequires:  python3-sphinx-inline-tabs
BuildRequires:  python3-sphinxcontrib-copybutton
%endif
Recommends:     %{name}-shell-integration
Recommends:     %{name}-terminfo
Recommends:     python3-importlib_resources

%description
A terminal emulator that uses OpenGL for rendering.
Supports terminal features like: graphics, Unicode,
true-color, OpenType ligatures, mouse protocol, focus tracking,
bracketed paste and so on, and which can be controlled by scripts.

%package terminfo
Summary:        The terminfo file for the Kitty terminal
BuildArch:      noarch

%description terminfo
Provides 'xterm-kitty' terminfo file(s) for the Kitty terminal; this package can be installed on its own to provide file(s) instead of the full kitty package on remote systems.

%package shell-integration
Summary:        The shell-integation file(s) for the Kitty terminal

%description shell-integration
shell-integration [bash,fish,zsh] file(s) for the Kitty terminal; this package can be installed on its own to provide file(s) instead of the full kitty package on remote systems.

%prep
%autosetup -p0 -a 1

%if 0%{?suse_version} > 1500
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python@' {} +
%else
%if 0%{?sle_version} > 150400
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3.11@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python3.11@' {} +
%else
%if 0%{?sle_version} > 150300
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3.10@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python3.10@' {} +
%else
find . -type f -exec sed -i 's@#!/usr/bin/env python3$@#!%{_bindir}/python3.9@' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python$@#!%{_bindir}/python3.9@' {} +
%endif
%endif
%endif

%build

%install
# yes they have a makefile, no they dont use it properly
# no they dont have a make install
# we used to have this in the build section but since rpm 4.16 buildroot is cleaned
#
# See: https://build.opensuse.org/request/show/1096854
# Set -Wno-error=switch flag to prevent compiler crashes
#export CFLAGS="${CFLAGS:-%%optflags} -Wno-error=switch"
#export CXXFLAGS="${CXXFLAGS:-%%optflags} -Wno-error=switch"
#
### This might have been fixed as part of #gh/kovidgoyal/kitty/7026
#%%ifarch i586
#export CFLAGS="${CFLAGS:-%%optflags} -fcf-protection=none"
#%%endif
#####
%if 0%{?suse_version} > 1500
python3 \
%else
%if 0%{?sle_version} > 150400
python3.11 -B \
%else
%if 0%{?sle_version} > 150300
python3.10 -B \
%else
python3.9 -B \
%endif
%endif
%endif
setup.py \
  --verbose \
  linux-package \
  --prefix %{buildroot}%{_prefix} \
  --libdir-name %{_lib} \
  --extra-include-dirs %{_prefix}/include/libxkbcommon

%fdupes %{buildroot}%{_libdir}/%{name}

%files
%license LICENSE
%doc CHANGELOG.rst README.asciidoc
%{_bindir}/%{name}
%{_bindir}/kitten
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/shell-integration
%{_datadir}/applications/%{name}{,-open}.desktop
%{_datadir}/icons/hicolor/
%if %{with docs}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/doc/%{name}
%{_mandir}/man5/kitty.conf.5%{?ext_man}
%endif

%files terminfo
%license LICENSE
%doc CHANGELOG.rst README.asciidoc
%{_datadir}/terminfo/x/xterm-%{name}

%files shell-integration
%license LICENSE
%doc CHANGELOG.rst README.asciidoc
%{_libdir}/%{name}/shell-integration

%changelog
