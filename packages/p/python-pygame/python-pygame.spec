#
# spec file for package python-pygame
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


%define skip_python36 1
Name:           python-pygame
Version:        2.1.2
Release:        0
Summary:        A Python Module for Interfacing with the SDL Multimedia Library
License:        LGPL-2.1-or-later
URL:            https://github.com/pygame/pygame
Source0:        https://files.pythonhosted.org/packages/source/p/pygame/pygame-%{version}.tar.gz
# PATCH-FIX-UPSTREAM adjust-surface-mask.patch gh#pygame/pygame#3577
Patch0:         adjust-surface-mask.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bitstream-vera-fonts
BuildRequires:  fdupes
BuildRequires:  fontconfig
BuildRequires:  libtiff-devel
BuildRequires:  libudev-devel
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
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
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
%autosetup -p1 -n pygame-%{version}

sed -i 's/\r$//' docs/reST/ref/code_examples/draw_module_example.py
sed -i 's/\r$//' docs/reST/ref/code_examples/joystick_calls.py
sed -i 's/\r$//' docs/licenses/LICENSE*.txt
# Fix wrong-script-interpreter
find examples -name '*.py' -exec sed -i "s|^#!.*env python.*$|#!%{_bindir}/python3|" {} \;
chmod a+x examples/*.py
chmod a-x docs/licenses/LICENSE.sdl_gfx.txt

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export PORTMIDI_INC_PORTTIME=1
%python_build

%install
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_install
%{python_expand pushd %{buildroot}%{$python_sitearch}
sed -i "s|^#!.*env python.*$|#!%{_bindir}/$python|" pygame/tests/test_utils/png.py
chmod a+x pygame/tests/test_utils/png.py
chmod a+x pygame/examples/*.py
chmod a-x pygame/examples/__init__.py
popd
}
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# install docs and examples for doc package and deduplicate
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r examples docs %{buildroot}%{_docdir}/%{name}-doc/
rm %{buildroot}%{_docdir}/%{name}-doc/examples/.editorconfig
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%check
export SDL_VIDEODRIVER=dummy
export SDL_AUDIODRIVER=disk
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m pygame.tests.__main__ -v --exclude opengl --time_out 300
}

%files %{python_files}
%doc README.rst
%license docs/LGPL.txt
%{python_sitearch}/pygame/
%{python_sitearch}/pygame-%{version}*-info

%files %{python_files devel}
%license docs/LGPL.txt
%{python_sysconfig_var INCLUDEPY}/pygame/

%files -n %{name}-doc
%doc %{_docdir}/%{name}-doc/

%changelog
