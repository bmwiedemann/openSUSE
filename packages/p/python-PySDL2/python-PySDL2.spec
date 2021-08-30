#
# spec file for package python-PySDL2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         X_display         ":98"
Name:           python-PySDL2
Version:        0.9.8
Release:        0
Summary:        Python SDL2 bindings
License:        SUSE-Public-Domain
URL:            https://github.com/marcusva/py-sdl2
Source:         https://files.pythonhosted.org/packages/source/P/PySDL2/PySDL2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM PySDL2-pr193-skipnumpy.patch -- gh#marcusva/py-sdl2#193
Patch0:         https://github.com/marcusva/py-sdl2/pull/193.patch#/PySDL2-pr193-skipnumpy.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  SDL2 >= 2.0.5
BuildRequires:  SDL2_gfx >= 1.0.3
BuildRequires:  SDL2_image >= 2.0.1
BuildRequires:  SDL2_mixer >= 2.0.1
BuildRequires:  SDL2_ttf >= 2.0.14
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pytest}
BuildRequires:  xorg-x11-server
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
Requires:       SDL2 >= 2.0.5
Requires:       SDL2_gfx >= 1.0.3
Requires:       SDL2_image >= 2.0.1
Requires:       SDL2_mixer >= 2.0.1
Requires:       SDL2_ttf >= 2.0.14
BuildArch:      noarch
%python_subpackages

%description
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

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

pushd sdl2/test
# these segfault when not tested separately
testextra="SpriteFactory or SDL2EXTSprite or test_SDL_GL"
# we do not have audio devices in build environment
donttest+=" or test_Mix_OpenAudio or test_SDL_GetNumAudioDevices or TestSDLMixer"
# we get border size 0 in build "desktop" environment
donttest+=" or test_SDL_GetWindowsBordersSize"
# flaky segfaults
donttest+=" or (TestSDL2ExtWindow and (test_Window_position or test_Window_size))"
# test suite assumes SDL devel version from mercurial (hg) checkout
donttest+=" or test_SDL_GetRevision"
# python2 env on Leap different, pytest arg missing
python2_donttest="or test_SDL_GetBasePath or test_BitmapFont_render_on"
%pytest -rfEs -k "not (${testextra} ${donttest} ${$python_donttest})"
%pytest -rfEs -k "${testextra}"
popd

%files %{python_files}
%license COPYING.txt
%doc AUTHORS.txt README.md
%{python_sitelib}/sdl2
%{python_sitelib}/PySDL2-%{version}*-info

%changelog
