#
# spec file for package python-pyglet
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define         X_display         :98
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%bcond_with     pytest_helpers

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

# Set _version to 1.4 for 1.4.0betas and hg default
%define _version 1.3.2
Name:           python-pyglet
Version:        1.3.2
Release:        0
Summary:        Windowing and multimedia library
# 1.3.2 contains a vendored old pypng
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/pyglet/pyglet
Source0:        https://files.pythonhosted.org/packages/source/p/pyglet/pyglet-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE pyglet-1.2.4-fix-image-import.patch -- fix "import Image"
Patch0:         pyglet-1.2.4-fix-image-import.patch
%if "%{_version}" == "1.3.2"
Patch1:         pypng-license.patch
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       Mesa-dri
Requires:       config(Mesa)
Requires:       python-Pillow
Requires:       python-future
Requires:       libxcb-glx0
%if "%{_version}" == "1.4"
Requires:       python-pypng
%endif
Recommends:     alsa-lib
Recommends:     fontconfig
Recommends:     freetype
Recommends:     libGLU1
Recommends:     libopenal0
%if %{with gtk2}
Recommends:     gtk2
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  Mesa-dri
BuildRequires:  alsa-lib
BuildRequires:  fontconfig
BuildRequires:  freetype
BuildRequires:  gnu-free-fonts
BuildRequires:  libopenal0
BuildRequires:  xorg-x11-server
BuildRequires:  config(Mesa)
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
%setup -q -n pyglet-%{version}
%patch0
%if "%{_version}" == "1.3.2"
%patch1 -p1
%endif

# Can't be used for commercial purposes
rm -r examples/noisy/

# Not needed, and interferes with test discovery
rm -r pyglet/extlibs/future/
rm -r tests/extlibs/future/ tests/extlibs/mock.py

# Windows only, and is a vendored module
rm pyglet/font/win32*.py examples/font_comparison.py

%if "%{_version}" == "1.4"
# De-vendoring pypng-ing results in failures in v1.3.2, as it is using pypng an earlier pypng:
# AttributeError: 'module' object has no attribute 'Writer'
# pyglet 1.4 is using the latest pypng 0.0.19, the same version as python-pypng package
rm pyglet/extlibs/png.py
sed -i 's/import pyglet.extlibs.png as pypng/import png as pypng/' pyglet/image/codecs/png.py
%endif

# Files unneccessary for Linux runtimes
rm -r \
%if "%{_version}" == "1.3.2"
  pyglet/*/carbon.py pyglet/input/carbon_*.py pyglet/window/carbon/ pyglet/image/codecs/quicktime.py tests/unit/test_osx.py \
%endif
  pyglet/gl/lib_agl.py pyglet/gl/lib_wgl.py pyglet/gl/wgl*.py \
  pyglet/*/cocoa.py pyglet/*/quartz.py pyglet/*/win32.py \
  pyglet/input/darwin_hid.py pyglet/input/directinput.py pyglet/input/wintab.py \
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
%if "%{_version}" == "1.3.2"
  tests/interactive/window/test_window_multisample.py \
%endif
%if "%{_version}" == "1.4"
  tests/unit/media/test_listener.py \
%endif
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
  tests/interactive/font/*.py

## Unit tests

# Convert to a mark, so it can be deselected, bypassing error-for-skips
sed -i "s/@unittest.skip('Requires changes to events from fork by Leif')/@pytest.mark.leif_fork/" tests/unit/test_events.py
sed -i 's/import unittest/import unittest, pytest/' tests/unit/test_events.py

%if "%{_version}" == "1.3.2"
# https://bitbucket.org/pyglet/pyglet/issues/224/mediatest_playerplayertestcasetest_delete
sed -i 's/test_delete/_test_delete/' tests/unit/media/test_player.py
%endif

# https://bitbucket.org/pyglet/pyglet/issues/223/clock-test-failures
# Occasional errors on all platforms, and test_clock.py fails on Python 2 only
rm tests/unit/test_clock_fps.py

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
sed -i '/interactive_test_base/d' tests/run.py tests/interactive/__init__.py
rm tests/base/test_interactive_test_base.py

# Final tidy up

# Only useful to creates Windows or MacOS apps
rm examples/astraea/setup.py

# Convert to unix line endings
find pyglet -name "*.py" -exec dos2unix "{}" "+"

chmod a+x examples/synthesizer.py examples/soundspace/soundspace.py examples/game/version*/asteroid.py

dos2unix examples/opengl_3.py examples/tablet.py

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
pytest_k_list="test_openal or test_pulse or test_arb or \
  test_multitexture or test_clock or test_get_animation_no_video or \
  leif_fork or test_load_privatefont or test_load_privatefont_from_list or test_directsound_listener or \
  test_gdiplus_loading or test_quartz_loading or test_quicktime_loading or test_multiple_start_stop"

%if %{without gtk2}
pytest_k_list="$pytest_k_list or test_gdkpixbuf2 or test_gdkpixbuf2_loading"
%endif

%if %{with pytest_helpers}
pytest_addopts="--instafail --error-for-skips --timeout=30 "
%endif

pytest_addopts="$pytest_addopts tests/unit tests/integration"

%{python_expand  #
# These are only problematic on Python 2, and are restored after Python 2 tests
# https://bitbucket.org/pyglet/pyglet/issues/223/clock-test-failures
if [ $python = python2 ]; then
  mv tests/unit/test_clock.py tests/unit/.test_clock.py
fi

$python -m pytest $pytest_addopts -k "not ($pytest_k_list)"

if [ -x tests/unit/.test_clock.py ]; then
  mv tests/unit/.test_clock.py tests/unit/test_clock.py
fi
}

# endif test
%endif

%files %{python_files}
%license LICENSE
%if "%{_version}" == "1.3.2"
%license LICENSE.pypng
%endif
%doc NOTICE README RELEASE_NOTES
%ifpython2
%{_defaultdocdir}/python{,2}-pyglet/examples/
%endif
%ifpython3
%{_defaultdocdir}/python3-pyglet/examples/
%endif
%{python_sitelib}/pyglet
%{python_sitelib}/pyglet-%{version}-py*.egg-info

%changelog
