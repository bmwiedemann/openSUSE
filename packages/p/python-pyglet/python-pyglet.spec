#
# spec file for package python-pyglet
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


%define         X_display         :98
%ifarch %{arm} aarch64 x86_64 %{ix86} ppc64le
%bcond_without  gtk2
%bcond_without  test
# test_worker_refill_multiple_players_refill_multiple failed once on armv7l
%else
# s390x fails without out of memory with gtk and freetype,
# even with 8G memory from _constraints
# ppc has lots of similar problems, especially with gdk
%bcond_with     test
%bcond_with     gtk2
%endif
%define skip_python2 1
%bcond_with     pytest_helpers
Name:           python-pyglet
Version:        2.0.4
Release:        0
Summary:        Windowing and multimedia library
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/pyglet/pyglet
Source0:        https://files.pythonhosted.org/packages/source/p/pyglet/pyglet-%{version}.zip
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       Mesa-dri
Requires:       libxcb-glx0
Requires:       python-Pillow
Requires:       python-future
Requires:       python-pypng
Recommends:     alsa-lib
Recommends:     fontconfig
Recommends:     freetype
Recommends:     libGLU1
Recommends:     libopenal0
BuildArch:      noarch
%if %{with gtk2}
Recommends:     gtk2
%endif
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  Mesa-dri
BuildRequires:  alsa-lib
BuildRequires:  fontconfig
BuildRequires:  freetype
BuildRequires:  gnu-free-fonts
BuildRequires:  libopenal0
BuildRequires:  xorg-x11-server
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-glx)
%if %{with gtk2}
BuildRequires:  gtk2
%endif
%if %{with pytest_helpers}
BuildRequires:  %{python_module pytest-error-for-skips}
BuildRequires:  %{python_module pytest-instafail}
BuildRequires:  %{python_module pytest-timeout}
%endif
# endif test
%endif
%python_subpackages

%description
Pyglet provides an object-oriented programming interface for
developing games and other visually-rich applications.

%prep
%autosetup -p1 -n pyglet-%{version}

# Windows only, and is a vendored module
rm pyglet/font/win32*.py

# De-vendoring pypng-ing results in failures in v1.3.2, as it is using pypng an earlier pypng:
# AttributeError: 'module' object has no attribute 'Writer'
# pyglet 1.4 is using the latest pypng 0.0.19, the same version as python-pypng package
rm pyglet/extlibs/png.py
sed -i 's/import pyglet.extlibs.png as pypng/import png as pypng/' pyglet/image/codecs/png.py

# Files unneccessary for Linux runtimes
rm -r \
  pyglet/gl/lib_agl.py pyglet/gl/lib_wgl.py pyglet/gl/wgl*.py \
  pyglet/*/cocoa.py pyglet/*/quartz.py pyglet/*/win32.py \
  pyglet/image/codecs/quartz.py pyglet/image/codecs/gdiplus.py \
  pyglet/window/cocoa/ pyglet/window/win32/ \
  pyglet/libs/darwin/ pyglet/libs/win32/ \
  pyglet/media/drivers/directsound/ tests/integration/media/test_directsound.py \
  tests/integration/platform/test_win_multicore_clock.py

%if %{without gtk2}
# Disable GdkPixbuf
sed -i 's/^\( *\).*gdkpixbuf2.*/\1pass/' pyglet/image/codecs/__init__.py
%endif

# Allow invocation using unittest discover -vv --start-directory tests/xyz/
# https://bitbucket.org/pyglet/pyglet/issues/231/allow-invocation-using-unittest-discover
sed -i 's/from \.\.\./from tests./' \
  tests/unit/media/test_listener.py \
  tests/integration/image/test_gdkpixbuf2.py \
  tests/interactive/image/test_image.py

# Fails with Arial and FreeSerif, Bitstream Vera Sans and Courier
# https://bitbucket.org/pyglet/pyglet/issues/245/bitstream-vera-sans-bold-and-italic-font
sed -i 's/test_find_font_match_bold/_test_find_font_match_bold/' tests/integration/platform/test_linux_fontconfig.py

# Tests rely on Arial font, however webcore-fonts is not OSS, and fetchmsttfonts
# only includes the script.  Use gnu-free-fonts instead.
# https://bitbucket.org/pyglet/pyglet/issues/230/use-a-free-er-font-in-test-suite
sed -i 's/arial/freeserif/g;s/Arial/FreeSerif/g' \
  tests/unit/test_text.py \
  tests/integration/platform/test_linux_fontconfig.py \
  tests/integration/font/*.py \

## Unit tests

# Convert to a mark, so it can be deselected, bypassing error-for-skips
sed -i "s/@unittest.skip('Requires changes to events from fork by Leif')/@pytest.mark.leif_fork/" tests/unit/test_events.py
sed -i 's/import unittest/import unittest, pytest/' tests/unit/test_events.py

## Integration tests

# Test fails on all platforms
#sed -i 's/test_unreferenced_cleanup/_test_unreferenced_cleanup/' tests/integration/media/test_player.py

# test_driver: AssertionError: Cannot load audio driver for your platform
# test_openal: OpenALException: OpenAL Exception [40965: Out of Memory]: Failed to open device.
# Similar for pulse, and hang in player
rm -f tests/integration/media/test_driver.py \
  tests/integration/media/test_player.py \
  tests/integration/media/test_openal.py \
  tests/integration/media/test_pulse.py

# test_immediate_drawing*, test_immediate_drawing and multitexture fails
# except on Tumbleweed
rm -f tests/integration/graphics/test_retained_drawing*.py \
  tests/integration/graphics/test_immediate_drawing*.py \
  tests/integration/graphics/test_multitexture.py

## Interactive tests

# Fix missing interactive_test_base
# See https://bitbucket.org/pyglet/pyglet/issues/234/interactive_test_base-is-missing
sed -i '/interactive_test_base/d' tests/interactive/__init__.py
rm tests/base/test_interactive_test_base.py

# Final tidy up

# Convert to unix line endings
find pyglet -name "*.py" -exec dos2unix "{}" "+"

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{python_expand pkgdocdir=%{_docdir}/$(cat _current_flavor)-pyglet
mkdir -p %{buildroot}$pkgdocdir
cp -Lr examples/ %{buildroot}$pkgdocdir/
find %{buildroot}$pkgdocdir/examples/ -name "*.py" -exec sed -i "s|^#!%{_bindir}/python$|#!%{__$python}|" {} \;
find %{buildroot}$pkgdocdir/examples/ -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" {} \;

%fdupes %{buildroot}$pkgdocdir/examples/
}

%if %{with test}
%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb +iglx %{X_display} -screen 0 1600x1200x16 &
trap "kill $! || true" EXIT
sleep 5

# This is to allow use of pytest-error-for-skips and pytest-instafail,
# used to see problems even when tests hang.
# test_multiple_start_stop is occasional failures on most platforms
# test_pause_resume is occasional failures on aarch64
pytest_k_list="test_openal or test_pulse or test_arb or \
  test_multitexture or test_clock or test_get_animation_no_video or \
  leif_fork or test_load_privatefont or test_load_privatefont_from_list or test_directsound_listener or \
  test_gdiplus_loading or test_quartz_loading or test_quicktime_loading or test_multiple_start_stop or test_pause_resume"
# Disable beause broken in python 3.11, gh#pyglet/pyglet#606
pytest_k_list+=" or test_push_handlers_instance"

%if %{without gtk2}
pytest_k_list="$pytest_k_list or test_gdkpixbuf2 or test_gdkpixbuf2_loading"
%endif

%if %{with pytest_helpers}
pytest_addopts="--instafail --error-for-skips --timeout=30 "
%endif

pytest_addopts="$pytest_addopts tests/unit tests/integration"
pytest_image_loading="test_resource_image_loading"

%{python_expand  #
# These are only problematic on Python 2, and are restored after Python 2 tests
# https://bitbucket.org/pyglet/pyglet/issues/223/clock-test-failures
if [ $python = python2 ]; then
  mv tests/unit/test_clock.py tests/unit/.test_clock.py
fi

$python -m pytest $pytest_addopts -k "not ($pytest_k_list or $pytest_image_loading)"
# Run test_resource_image_loading tests in a second steps, this fails
# if run with the other tests, possible because a test not cleaning
# correctly
$python -m pytest $pytest_addopts -k "$pytest_image_loading"

if [ -x tests/unit/.test_clock.py ]; then
  mv tests/unit/.test_clock.py tests/unit/test_clock.py
fi
}

# endif test
%endif

%files %{python_files}
%license LICENSE
%doc README.md RELEASE_NOTES examples
%{python_sitelib}/pyglet
%{python_sitelib}/pyglet-%{version}-py*.egg-info

%changelog
