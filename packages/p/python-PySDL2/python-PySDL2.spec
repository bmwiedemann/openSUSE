#
# spec file for package python-PySDL2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Can't be properly tested without full desktop system
%bcond_with     test
%if %{with test}
%define         X_display         ":98"
BuildRequires:  %{python_module pytest}
BuildRequires:  SDL2
BuildRequires:  SDL2_ttf
BuildRequires:  xorg-x11-server
%endif
Name:           python-PySDL2
Version:        0.9.7
Release:        0
Summary:        Python SDL2 bindings
License:        SUSE-Public-Domain
URL:            https://github.com/marcusva/py-sdl2
Source:         https://files.pythonhosted.org/packages/source/P/PySDL2/PySDL2-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  SDL2 >= 2.0.5
BuildRequires:  SDL2_ttf >= 2.0.14
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       SDL2 >= 2.0.5
Requires:       SDL2_ttf >= 2.0.14
BuildArch:      noarch
%python_subpackages

%description
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

%prep
%setup -q -n PySDL2-%{version}
sed -i 's/\r$//' AUTHORS.txt COPYING.txt README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

pushd sdl2/test
%python_exec -B -m pytest
popd
%endif

%check
# we do not have audio devices nor joystick in build environment
%pytest -k "not (test_SDL_GetNumAudioDevices or test_SDL_InitJoystick)"

%files %{python_files}
%license COPYING.txt
%doc AUTHORS.txt README.md
%{python_sitelib}/*

%changelog
