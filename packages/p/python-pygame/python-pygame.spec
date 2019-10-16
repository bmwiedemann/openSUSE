#
# spec file for package python-pygame
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pygame
Version:        1.9.6
Release:        0
Summary:        A Python Module for Interfacing with the SDL Multimedia Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
Url:            https://github.com/pygame/pygame
Source0:        https://files.pythonhosted.org/packages/source/p/pygame/pygame-%{version}.tar.gz
# Do not test mp3 format; whe have that support disabled in SDL1
Patch0:         python-pygame-test-no-mp3.patch
Patch1:         python-pygame-python38-import.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  fontconfig
BuildRequires:  libtiff-devel
BuildRequires:  libv4l-devel >= 0.8.4
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-fonts-100dpi
BuildRequires:  xorg-x11-fonts-75dpi
BuildRequires:  xorg-x11-fonts-core
BuildRequires:  xorg-x11-fonts-cyrillic
BuildRequires:  config(fluid-soundfont-gm)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(x11)
Requires:       fontconfig
Requires:       python-numpy
%ifpython2
Provides:       pygame = %{version}
Obsoletes:      pygame < %{version}
%endif
%python_subpackages

%description
Pygame is a Python wrapper module for the SDL multimedia library. It
contains Python functions and classes that allow you to use SDL's
support for playing CD-ROMs, audio and video output, and keyboard,
mouse and joystick input. Pygame also includes support for the
Numerical Python extension. Pygame is the successor to the pySDL
wrapper project, written by Mark Baker.

%package devel
Summary:        Pygame development package
Group:          Development/Libraries/Python
Requires:       python-pygame = %{version}

%description devel
This package contains the header files for developers of Pygame.

%package -n %{name}-doc
Summary:        Pygame documentation and example programs
Group:          Documentation/Other
Provides:       pygame-doc = %{version}
Obsoletes:      pygame-doc < %{version}
Provides:       %{python_module pygame-doc = %{version}}

%description -n %{name}-doc
This package contains documentation and example programs for Pygame.

%prep
%setup -q -n pygame-%{version}
%autopatch -p1
sed -i 's/\r$//' docs/reST/ref/code_examples/draw_module_example.py
sed -i 's/\r$//' docs/reST/ref/code_examples/joystick_calls.py
# Fix wrong-script-interpreter
find examples -name '*.py' -exec sed -i "s|^#!%{_bindir}/env python$|#!%{_bindir}/python3|" {} \;
find examples -name '*.py' -exec sed -i "s|^#! %{_bindir}/env python$|#!%{_bindir}/python3|" {} \;
chmod a+x examples/*.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_install
%{python_expand pushd %{buildroot}%{$python_sitearch}
sed -i "s|^#!%{_bindir}/env python$|#!%{_bindir}/python3|" pygame/tests/test_utils/png.py
chmod a+x pygame/tests/test_utils/png.py
chmod a+x pygame/examples/macosx/aliens_app_example/aliens.py
chmod a+x pygame/examples/*.py
chmod a-x pygame/examples/__init__.py
chmod a-x pygame/examples/prevent_display_stretching.py
chmod a-x pygame/examples/freetype_misc.py
$python -m compileall -d %{$python_sitearch} pygame/tests/test_utils/
$python -O -m compileall -d %{$python_sitearch} pygame/tests/test_utils/
%fdupes %{buildroot}%{$python_sitearch}
popd
}
%fdupes docs
%fdupes examples

%check
export SDL_VIDEODRIVER=dummy
export SDL_AUDIODRIVER=disk
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m pygame.tests.__main__ --exclude opengl --time_out 300
}

%files %{python_files}
%doc README.rst
%license docs/LGPL
%{python_sitearch}/pygame/
%{python_sitearch}/pygame-%{version}-py*.egg-info

%files %{python_files devel}
%license docs/LGPL
%{python_sysconfig_var INCLUDEPY}/pygame/

%files -n %{name}-doc
%doc docs/
%doc examples/

%changelog
