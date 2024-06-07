#
# spec file for package python-matplotlib
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# Run on 64bit intel and arm only, on others there are >100 test failures
ExclusiveArch:  x86_64 aarch64
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_with ringdisabled
%{?sle15_python_module_pythons}
Name:           python-matplotlib%{psuffix}
Version:        3.9.0
Release:        0
Summary:        Plotting Library for Python
License:        SUSE-Matplotlib
URL:            https://matplotlib.org
# SourceRepository: https://github.com/matplotlib/matplotlib
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-%{version}.tar.gz
# Use fixed versions of freetype and qhull for imagecomparison tests to succeed. See lib/matplotlib/__init__.py:_init_tests() and the meson .wrap files in subprojects/
Source98:       https://github.com/qhull/qhull/archive/v8.0.2/qhull-8.0.2.tar.gz#/qhull-8.0.2.tgz
Source99:       https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz
Source100:      python-matplotlib.rpmlintrc
# PATCH-FEATURE-OPENSUSE matplotlib-meson-options-opensuse.patch code@bnavigator.de -- Custom build options for meson-python
Patch0:         matplotlib-meson-options-opensuse.patch
Recommends:     ghostscript
Recommends:     libxml2-tools
Recommends:     poppler-tools
Recommends:     python-certifi
Recommends:     (%{python_flavor}-matplotlib-tk if tk)
Provides:       python-matplotlib-gtk = %{version}
Obsoletes:      python-matplotlib-gtk < %{version}
# SECTION build
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module meson-python >= 0.13.1}
BuildRequires:  %{python_module numpy-devel >= 1.25 with %python-numpy-devel < 2.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel >= 2.6}
BuildRequires:  %{python_module setuptools_scm >= 7}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  qhull-devel >= 2003.1
# /SECTION
# SECTION tk dependencies via tcl
BuildRequires:  tcl
BuildRequires:  pkgconfig(freetype2) >= 2.3
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(tcl)
# /SECTION
# SECTION runtime
Requires:       python-Cycler >= 0.10
Requires:       python-FontTools >= 4.22.0
Requires:       python-Pillow >= 8
Requires:       python-contourpy >= 1.0.1
Requires:       python-kiwisolver >= 1.3.1
Requires:       python-numpy >= 1.23
Requires:       python-packaging >= 20.0
Requires:       python-pyparsing > 2.3.1
Requires:       python-python-dateutil >= 2.7
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-resources >= 3.2.0
%endif
# /SECTION
# SECTION test
%if %{with test}
BuildRequires:  %{python_module matplotlib = %{version}}
BuildRequires:  %{python_module matplotlib-cairo = %{version}}
BuildRequires:  %{python_module matplotlib-gtk3 = %{version}}
BuildRequires:  %{python_module matplotlib-gtk4 = %{version}}
BuildRequires:  %{python_module matplotlib-qt5 = %{version}}
BuildRequires:  %{python_module matplotlib-testdata = %{version}}
BuildRequires:  %{python_module matplotlib-tk = %{version}}
BuildRequires:  %{python_module matplotlib-web = %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module matplotlib-nbagg = %{version} if %python-base >= 3.10}
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module matplotlib-wx = %{version}}
%endif
# SECTION latex test dependencies
BuildRequires:  %{python_module matplotlib-latex = %{version}}
BuildRequires:  Mesa-dri
BuildRequires:  ghostscript
BuildRequires:  inkscape
BuildRequires:  poppler-tools
# /SECTION latex
# SECTION cairo backend options
BuildRequires:  %{python_module cairo >= 1.14.0}
BuildRequires:  %{python_module cairocffi >= 0.8}
# /SECTION cairo
# SECTION nbagg backend tests
%if %{without ringdisabled} && 0%{?suse_version} > 1500
BuildRequires:  %{python_module nbconvert if %python-base >= 3.10}
BuildRequires:  %{python_module nbformat if %python-base >= 3.10}
%endif
# /SECTION nbagg
# SECTION qt backends: Only test PyQt5 in Minimal-X
BuildRequires:  %{python_module qt5}
%if %{without ringdisabled}
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module PyQt6}
BuildRequires:  python3-pyside2
BuildRequires:  python3-pyside6
%endif
%endif
# /SECTION qt
# /SECTION test
%endif
%python_subpackages

%description
matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell (ala matlab or mathematica), web
application servers, and six graphical user interface toolkits.

%package        cairo
Summary:        Cairo backend for %{name}
Requires:       %{name} = %{version}
Requires:       (python-cairo or python-cairocffi)

%description    cairo
This package includes the non-interactive Cairo-based backend
for the %{name} plotting package

%package        gtk3
Summary:        GTK3 backends for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-gtk-common = %{version}

%description    gtk3
This package includes the GTK3-based gtk3, gtk3agg, and
gtk3cairo backends for the %{name} plotting package

%package        gtk4
Summary:        GTK4 backends for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-gtk-common = %{version}

%description    gtk4
This package includes the GTK4-based gtk4, gtk4agg, and
gtk4cairo backends for the %{name} plotting package

%package        gtk-common
Summary:        Code common for GTK3 and GTK4 backends for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-cairo = %{version}
Requires:       gdk-pixbuf-loader-rsvg
Requires:       python-gobject-Gdk
Requires:       python-gobject-cairo

%description    gtk-common
This package provides code common for the GTK3 and GTK4 backends
for the %{name} plotting package

%package        nbagg
Summary:        Jupyter nbagg backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-ipykernel

%description    nbagg
This package includes the Jupyter notebook backend
for the %{name} plotting package

%package        latex
Summary:        Allow rendering latex in %{name}
Requires:       %{name} = %{version}
# grep usepackage lib/matplotlib/texmanager.py lib/matplotlib/backends/backend_pgf.py
# https://github.com/search?q=usepackage+repo%3Amatplotlib%2Fmatplotlib+path%3Alib&type=Code
Requires:       texlive-dvipng
Requires:       texlive-dvips
Requires:       texlive-geometry
Requires:       texlive-graphics
Requires:       texlive-helvetic
Requires:       texlive-latex
Requires:       texlive-pgf
Requires:       texlive-sfmath
Requires:       texlive-tex
Requires:       texlive-txfonts
Requires:       texlive-xcolor
Requires:       texlive-xetex
Requires:       tex(avant.sty)
Requires:       tex(chancery.sty)
Requires:       tex(charter.sty)
Requires:       tex(courier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(helvet.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(pncr.tfm)
Requires:       tex(psfrag.sty)
Requires:       tex(type1cm.sty)
Requires:       tex(type1ec.sty)
Requires:       tex(ucs.sty)
Requires:       tex(underscore.sty)
BuildArch:      noarch

%description    latex
This package allows %{name} to display latex in plots
and figures.

%package        qt
Summary:        Qt backend for %{name}
Requires:       %{name} = %{version}
Requires:       (python-qt5 or python-PyQt6 >= 6.1 or python-pyside2 or python-pyside6)
Provides:       %{name}-qt-shared = %{version}
Provides:       %{name}-qt5 = %{version}
Obsoletes:      %{name}-qt-shared < %{version}
# Renamed at upgrade from MPL 3.6.3 to 3.8.2
Obsoletes:      %{name}-qt5 < 3.8.2

%description    qt
This package includes the Qt-based backend
for the %{name} plotting package
PyQt5, PyQt6, Pyside2 or Pyside 6 may be used

%package        testdata
Summary:        Test data for %{name}
Requires:       %{name} = %{version}

%description    testdata
This package includes the test baseline data
for the %{name} plotting package

%package        tk
Summary:        Tk backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-Pillow-tk
Requires:       python-tk
Requires:       tcl >= 8.5

%description    tk
This package includes the Tk-based tkagg backend
for the %{name} plotting package

%package        web
Summary:        Web backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-tornado

%description    web
This package includes the browser-based webagg backend
for the %{name} plotting package

%if 0%{?suse_version} > 1500
%package        wx
Summary:        WxWidgets backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-wxPython >= 4

%description    wx
This package includes the wxWidgets-based wxagg backend
for %{name} plotting package
%endif

%prep
%autosetup -p1 -n matplotlib-%{version}
# Copy freetype and qhull to the right location, so that matplotlib will not try to download it
mkdir subprojects/packagecache
cp %{SOURCE98} %{SOURCE99} subprojects/packagecache/
chmod -x lib/matplotlib/mpl-data/images/*.svg
find lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "1{/#!.*python/ d}" {} \;
%{python_expand # use the last python in the buildset as generator (only the pythons in the buildset have setuptools_scm installed)
myprimarypython=%{__$python}
}
sed -i "s|find_program('python3')|'$myprimarypython'|" meson.build
find tools -type f -name "*.py" -exec sed -i "1{s|^#!.*python\S*|#!$myprimarypython|}" {} \;

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%{python_expand sed -i -e "s/install matplotlib from source/install the $python-matplotlib-testdata package/" \
                      %{buildroot}%{$python_sitearch}/matplotlib/tests/__init__.py
}
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# force 'swrast' ("llvmpipe") Mesa/OpenGL driver to be used by
# setting and exporting LIBGL_ALWAYS_SOFTWARE=1 to get rid of
# issues when Mesa is trying to load 'zink' driver (messages are
# just warnings, but seem to be fatal for the tests here) (boo#1219095)
export LIBGL_ALWAYS_SOFTWARE=1
# fails to detect alternative backend within xvfb
skip_tests+=" or test_backend_fallback_headful"
# test_usetex.py::test_usetex[png] - no tex text -- do not skip test_empty[png] and test_unicode_minus[png]
skip_tests+=" or (test_usetex and png and not empty and not unicode)"
# output slightly differs: text moves a bit
skip_tests+=" or test_pdflatex"
# timing tests on obs can fail unpredictably
skip_tests+=" or test_invisible_Line_rendering"
# too much memory consumption on obs parallel workers
skip_tests+=" or (test_agg and chunksize) or test_throw_rendering_complexity_exceeded"
# testing interactive backend leaks inside obs is flaky
skip_tests+=" or (test_backends_interactive and test_figure_leak_20490)"
# flaky signal termination tests inside obs
skip_tests+=" or _sigint"
# test finds extra system fonts not found by the mpl fontmanager
skip_tests+=" or test_get_font_names"
# different default font
skip_tests+=" or test_bold_font_output_with_none_fonttype"
# different position values on python311 (different version in a dependency or different font?)
skip_tests+=" or test_compressed1"
%ifnarch x86_64
# image comparison failures due to precisions dicrepancies to the x86 produced references
skip_tests+=" or png or svg or pdf"
%endif
# backend tests landing in the wrong xdist process may fail with an error. Test them without xdist.
no_xdist="test_backend or test_span_selector_animated_artists_callback"
%{python_expand # see https://matplotlib.org/devdocs/devel/testing.html#testing
# if one of the pyargs modules is not present, the xargs collection looks empty
$python -m pytest --pyargs matplotlib.tests \
                           mpl_toolkits.axes_grid1.tests \
                           mpl_toolkits.axisartist.tests \
                           mpl_toolkits.mplot3d.tests \
                  -n auto \
                  -m "not network" \
                  -vv -rsfE \
                  -k "not (${no_xdist} ${skip_tests})"
$python -m pytest --pyargs matplotlib.tests \
                  -vv -rsfE \
                  -k "(${no_xdist}) and not (${skip_tests:4})"
}
%endif

%if %{without test}
%files %{python_files}
%doc README.md
%license LICENSE/
%{python_sitearch}/matplotlib
%{python_sitearch}/matplotlib-%{version}.dist-info
%dir %{python_sitearch}/mpl_toolkits
%{python_sitearch}/mpl_toolkits/axes_grid1
%{python_sitearch}/mpl_toolkits/axisartist
%{python_sitearch}/mpl_toolkits/mplot3d
%{python_sitearch}/pylab.py*
%pycache_only %{python_sitearch}/__pycache__/pylab.*
%exclude %{python_sitearch}/matplotlib/backends/_backend_tk.py
%exclude %{python_sitearch}/matplotlib/backends/_backend_gtk.py
%exclude %{python_sitearch}/matplotlib/backends/backend_cairo.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3cairo.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk4.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk4agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk4cairo.*
%exclude %{python_sitearch}/matplotlib/backends/backend_nbagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt5.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt5agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt5cairo.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_tkcairo.*
%exclude %{python_sitearch}/matplotlib/backends/backend_webagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_webagg_core.*
%exclude %{python_sitearch}/matplotlib/backends/backend_wx.*
%exclude %{python_sitearch}/matplotlib/backends/backend_wxagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_wxcairo.*
%exclude %{python_sitearch}/matplotlib/backends/qt_compat.*
%exclude %{python_sitearch}/matplotlib/backends/qt_editor/
%exclude %{python_sitearch}/matplotlib/backends/web_backend/
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/_backend_tk.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/_backend_gtk.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_cairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3cairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4cairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_nbagg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5cairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkcairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_wx.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxagg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxcairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/qt_compat.*.py*
%exclude %{python_sitearch}/matplotlib/tests/baseline_images
%exclude %{python_sitearch}/mpl_toolkits/axes_grid1/tests/baseline_images
%exclude %{python_sitearch}/mpl_toolkits/axisartist/tests/baseline_images
%exclude %{python_sitearch}/mpl_toolkits/mplot3d/tests/baseline_images
%exclude %{python_sitearch}/matplotlib/tests/tinypages

# Dummy package to pull in latex dependencies.
%files %{python_files latex}
%license LICENSE/

%files %{python_files cairo}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_cairo.*.py*

%files %{python_files gtk3}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_gtk3.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3agg.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3cairo.*.py*

%files %{python_files gtk4}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_gtk4.py*
%{python_sitearch}/matplotlib/backends/backend_gtk4agg.py*
%{python_sitearch}/matplotlib/backends/backend_gtk4cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4cairo.*.py*

%files %{python_files gtk-common}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/_backend_gtk.py
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/_backend_gtk.*.py*

%if 0%{?suse_version} > 1500 && 0%{?python_version_nodots} >= 310
%files %{python_files nbagg}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_nbagg.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_nbagg.*.py*
%endif

%files %{python_files qt}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_qt5.py*
%{python_sitearch}/matplotlib/backends/backend_qt5agg.py*
%{python_sitearch}/matplotlib/backends/backend_qt5cairo.py*
%{python_sitearch}/matplotlib/backends/qt_compat.py*
%{python_sitearch}/matplotlib/backends/qt_editor/
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5cairo.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/qt_compat.*.py*

%files %{python_files testdata}
%license LICENSE/
%{python_sitearch}/matplotlib/tests/baseline_images
%{python_sitearch}/mpl_toolkits/axes_grid1/tests/baseline_images
%{python_sitearch}/mpl_toolkits/axisartist/tests/baseline_images
%{python_sitearch}/mpl_toolkits/mplot3d/tests/baseline_images
%{python_sitearch}/matplotlib/tests/tinypages
%exclude %{python_sitearch}/matplotlib/tests/tinypages/.gitignore
%exclude %{python_sitearch}/matplotlib/tests/tinypages/_static/.gitignore

%files %{python_files tk}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/_backend_tk.py*
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/backend_tkcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/_backend_tk.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkcairo.*.py*

%files %{python_files web}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_webagg.py*
%{python_sitearch}/matplotlib/backends/backend_webagg_core.py*
%{python_sitearch}/matplotlib/backends/web_backend/
%exclude %{python_sitearch}/matplotlib/backends/web_backend/.*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*.py*

%if 0%{?suse_version} > 1500
%files %{python_files wx}
%license LICENSE/
%{python_sitearch}/matplotlib/backends/backend_wx.py*
%{python_sitearch}/matplotlib/backends/backend_wxagg.py*
%{python_sitearch}/matplotlib/backends/backend_wxcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wx.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxcairo.*.py*
%endif
%endif

%changelog
