#
# spec file for package python-PySDL2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         X_display         ":98"
Name:           python-PySDL2
Version:        0.9.11
Release:        0
Summary:        Python ctypes wrapper around SDL2
License:        SUSE-Public-Domain
URL:            https://github.com/py-sdl/py-sdl2
Source:         https://files.pythonhosted.org/packages/source/P/PySDL2/PySDL2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  SDL2 >= 2.0.5
BuildRequires:  SDL2_gfx >= 1.0.3
BuildRequires:  SDL2_image >= 2.0.1
BuildRequires:  SDL2_mixer >= 2.0.1
BuildRequires:  SDL2_ttf >= 2.0.14
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest}
BuildRequires:  xorg-x11-server
# /SECTION
Requires:       SDL2 >= 2.0.5
Requires:       SDL2_gfx >= 1.0.3
Requires:       SDL2_image >= 2.0.1
Requires:       SDL2_mixer >= 2.0.1
Requires:       SDL2_ttf >= 2.0.14
BuildArch:      noarch
%python_subpackages

%description
PySDL2 is a pure Python wrapper around the SDL2, SDL2_mixer, SDL2_image,
SDL2_ttf, and SDL2_gfx libraries. Instead of relying on C code, it uses
the built-in ctypes module to interface with SDL2, and provides simple
Python classes and wrappers for common SDL2 functionality.

%prep
%autosetup -p1 -n PySDL2-%{version}
sed -i 's/\r$//' AUTHORS.txt COPYING.txt README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#############################################
### Launch a virtual framebuffer X server ###
###      (pytest-xvfb is not enough)      ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

export SDL_VIDEODRIVER=dummy
export SDL_AUDIODRIVER=dummy
export SDL_RENDER_DRIVER=software
export PYTHONFAULTHANDLER=1

donttest="pytest_k_dummyprefix"
# color mismatches, test shell variable because this is a noarch package
if [ "$RPM_ARCH" = "ppc64" -o "$RPM_ARCH" = "ppc64le" -o "$RPM_ARCH" = "s390x" ]; then
  donttest="$donttest or sdl2ext"
fi
# Does not recognize big endian byteorder
if [ $(python3 -c "import sys; print(sys.byteorder)") = "big" ]; then
  donttest="$donttest or PixelFormatEnum"
fi
%if 0%{suse_version} < 1550
# Segfault with SDL on Leap
donttest="$donttest or test_SDL_GetPowerInfo"
# python2 env different, pytest arg missing
python2_donttest=" or test_SDL_GetBasePath or test_render_on"
%endif
%pytest -rfEs -k "not ($donttest ${$python_donttest})"

%files %{python_files}
%license COPYING.txt
%doc AUTHORS.txt README.md
%{python_sitelib}/sdl2
%{python_sitelib}/PySDL2-%{version}*-info

%changelog
