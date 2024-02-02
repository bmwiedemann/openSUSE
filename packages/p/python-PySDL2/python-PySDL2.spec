#
# spec file for package python-PySDL2
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


%define         X_display         ":98"
Name:           python-PySDL2
Version:        0.9.16
Release:        0
Summary:        Python ctypes wrapper around SDL2
License:        SUSE-Public-Domain
URL:            https://github.com/py-sdl/py-sdl2
Source:         https://files.pythonhosted.org/packages/source/P/PySDL2/PySDL2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-tests-SDL_GetError.patch -- based on commit 1c865e3
Patch0:         https://github.com/py-sdl/py-sdl2/commit/1c865e3f751e678f3ad2d8f3fca17a0755fbeaf7.patch#/fix-tests-SDL_GetError.patch
# PATCH-FIX-UPSTREAM fix-test-SDL_hid_enumerate.patch -- based on commit d7c0604
Patch1:         https://github.com/py-sdl/py-sdl2/commit/d7c0604381f6cbefa2c8b51c84b879e2f927e91e.patch#/fix-test-SDL_hid_enumerate.patch
# PATCH-FIX-UPSTREAM fix-partially-resolve-video_test.patch -- based on commit ed28ea6
Patch2:         https://github.com/py-sdl/py-sdl2/commit/ed28ea6305dede1b6ba046e36ddae9ba2016b62e.patch#/fix-partially-resolve-video_test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  SDL2 >= 2.0.22
BuildRequires:  SDL2_gfx >= 1.0.4
BuildRequires:  SDL2_image >= 2.6.0
BuildRequires:  SDL2_mixer >= 2.6.0
BuildRequires:  SDL2_ttf >= 2.20.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest}
BuildRequires:  libmpg123-0
BuildRequires:  xorg-x11-server
# /SECTION
Requires:       SDL2 >= 2.0.22
Requires:       SDL2_gfx >= 1.0.4
Requires:       SDL2_image >= 2.6.0
Requires:       SDL2_mixer >= 2.6.0
Requires:       SDL2_ttf >= 2.20.0
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
find . -name *DS_Store -delete

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export SDL_VIDEODRIVER=dummy
export SDL_AUDIODRIVER=dummy
export SDL_RENDER_DRIVER=software
export PYTHONFAULTHANDLER=1

%pytest -rfEs

%files %{python_files}
%license COPYING.txt
%doc AUTHORS.txt README.md doc/
%{python_sitelib}/sdl2
%{python_sitelib}/PySDL2-%{version}*-info

%changelog
