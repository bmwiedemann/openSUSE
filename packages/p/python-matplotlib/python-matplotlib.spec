#
# spec file
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


%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
# NEP 29: Numpy 1.20 dropped Python 3.6. No python36-numpy in TW anymore.
%define         skip_python36 1
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
Name:           python-matplotlib%{psuffix}
Version:        3.5.3
Release:        0
Summary:        Plotting Library for Python
License:        SUSE-Matplotlib
URL:            https://matplotlib.org
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-%{version}.tar.gz
Source1:        matplotlib-mplsetup.cfg
# Bundled version of freetype and qhull for testing purposes only
Source98:       http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz
Source99:       https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz
# PATCH-FIX-UPSTREAM fix-tests-pytest72.patch gh#matplotlib/matplotlib#24173
Patch1:         fix-tests-pytest72.patch
BuildRequires:  %{python_module Cycler >= 0.10}
BuildRequires:  %{python_module FontTools >= 4.22.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module kiwisolver >= 1.0.1}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module numpy-devel >= 1.16}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing > 2.2.1}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  qhull-devel >= 2003.1
Requires:       python-Cycler >= 0.10
Requires:       python-FontTools >= 4.22.0
Requires:       python-Pillow >= 6.2
Requires:       python-kiwisolver >= 1.0.1
Requires:       python-numpy >= 1.17
Requires:       python-packaging >= 20.0
Requires:       python-pyparsing > 2.2.1
Requires:       python-python-dateutil >= 2.7
Requires:       python-pytz
Recommends:     ghostscript
Recommends:     libxml2-tools
Recommends:     poppler-tools
Recommends:     python-certifi
Recommends:     (%{python_flavor}-matplotlib-tk if tk)
Provides:       python-matplotlib-gtk = %{version}
Obsoletes:      python-matplotlib-gtk < %{version}
# SECTION tk dependencies via tcl
BuildRequires:  tcl
BuildRequires:  pkgconfig(freetype2) >= 2.3
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(tcl)
# /SECTION
%if %{with test}
BuildRequires:  %{python_module matplotlib = %{version}}
BuildRequires:  %{python_module matplotlib-cairo = %{version}}
BuildRequires:  %{python_module matplotlib-gtk3 = %{version}}
BuildRequires:  %{python_module matplotlib-gtk4 = %{version}}
BuildRequires:  %{python_module matplotlib-qt5 = %{version}}
BuildRequires:  %{python_module matplotlib-testdata = %{version}}
BuildRequires:  %{python_module matplotlib-tk = %{version}}
BuildRequires:  %{python_module matplotlib-web = %{version}}
BuildRequires:  %{python_module matplotlib-wx = %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
# SECTION latex test dependencies
BuildRequires:  %{python_module matplotlib-latex = %{version}}
BuildRequires:  ghostscript
BuildRequires:  inkscape
BuildRequires:  poppler-tools
# /SECTION
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
Requires:       python-cairo

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
Summary:        code common for GTK3 and GTK4 backends for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-cairo = %{version}
Requires:       gdk-pixbuf-loader-rsvg
Requires:       python-gobject-Gdk
Requires:       python-gobject-cairo

%description    gtk-common
This package provides code common for the GTK3 and GTK4 backends
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

%description    latex
This package allows %{name} to display latex in plots
and figures.

%package        qt5
Summary:        Qt5 backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-qt5
Provides:       %{name}-qt-shared = %{version}
Obsoletes:      %{name}-qt-shared < %{version}

%description    qt5
This package includes the Qt5-based pyqt5 backend
for the %{name} plotting package

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
Requires:       tcl >= 8.3

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

%package        wx
Summary:        WxWidgets backend for %{name}
Requires:       %{name} = %{version}
Requires:       python-wxPython >= 4

%description    wx
This package includes the wxWidgets-based wxagg backend
for %{name} plotting package

%prep
%autosetup -p1 -n matplotlib-%{version}
#copy freetype to the right location, so that matplotlib will not try to download it
mkdir -p ~/.cache/matplotlib/
SHA=($(sha256sum %{SOURCE98}))
cp %{SOURCE98} ~/.cache/matplotlib/${SHA}
SHA=($(sha256sum %{SOURCE99}))
cp %{SOURCE99} ~/.cache/matplotlib/${SHA}

chmod -x lib/matplotlib/mpl-data/images/*.svg
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/env python||" {} \;
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/python||" {} \;
cp %{SOURCE1} mplsetup.cfg
# The setup procedure wants certifi to download packages over https. Not applicable here.
sed -i '/"certifi>=.*"/ d' setup.py
# To make it work with setuptools_scm >= 7
# https://discourse.matplotlib.org/t/matplotlib-announce-amm-matplotlib-3-5-3/23046
sed -i 's/setuptools_scm>=4,<7/setuptools_scm>=4/' setup.py
sed -i '/"setuptools_scm_git_archive"/ d' setup.py

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%{python_expand sed -i -e "s/install matplotlib from source/install the $python-matplotlib-testdata package/" \
                      %{buildroot}%{$python_sitearch}/matplotlib/tests/__init__.py
}
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# fails to detect alternative backend within xvfb
skip_tests+=" or test_backend_fallback_headful"
# test_usetex.py::test_usetex[png] - no tex text -- do not skip test_empty[png] and test_unicode_minus[png]
skip_tests+=" or (test_usetex and png and not empty and not unicode)"
# output slightly differs: text moves a bit
skip_tests+=" or test_pdflatex"
# we do not ship the qt4 backend
skip_tests+=" or (test_correct_key and Qt4Agg)"
skip_tests+=" or (test_fig_close and Qt4Agg)"
# timing tests on obs can fail unpredictably
skip_tests+=" or test_invisible_Line_rendering"
# too much memory consumption on obs parallel workers
skip_tests+=" or (test_agg and chunksize) or test_throw_rendering_complexity_exceeded"
# testing interactive backend leaks inside obs is flaky
skip_tests+=" or (test_backends_interactive and test_figure_leak_20490)"
# flaky signal termination tests inside obs
skip_tests+=" or _sigint"
%ifnarch x86_64
# image comparison failures due to precisions dicrepancies to the x86 produced references
skip_tests+=" or png or svg or pdf"
%endif
%{pytest_arch --pyargs matplotlib.tests \
              --pyargs mpl_toolkits.tests \
              -n auto \
              -m "not network" \
              -k "not ( ${skip_tests:4} or test_backend )"
}
# backend tests landing in the wrong xdist process may fail with an error. Test them without xdist.
%pytest_arch --pyargs matplotlib.tests -k "test_backend and not ( ${skip_tests:4} )"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%doc examples/
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/
%{python_sitearch}/matplotlib-%{version}-py*.egg-info
%{python_sitearch}/matplotlib-%{version}-py*-nspkg.pth
%{python_sitearch}/mpl_toolkits
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
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4agg.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4cairo.py*
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
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4cairo.*.py*
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
%exclude %{python_sitearch}/matplotlib/tests/tinypages
%exclude %{python_sitearch}/mpl_toolkits/tests/baseline_images

# Dummy package to pull in latex dependencies.
%files %{python_files latex}
%license LICENSE/
%license doc/users/project/license.rst

%files %{python_files cairo}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/backend_cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_cairo.*.py*

%files %{python_files gtk3}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/backend_gtk3.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3agg.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3cairo.*.py*

%files %{python_files gtk4}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/backend_gtk4.py*
%{python_sitearch}/matplotlib/backends/backend_gtk4agg.py*
%{python_sitearch}/matplotlib/backends/backend_gtk4cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk4cairo.*.py*

%files %{python_files gtk-common}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/_backend_gtk.py
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/_backend_gtk.*.py*

%files %{python_files qt5}
%license LICENSE/
%license doc/users/project/license.rst
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
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/tests/baseline_images
%{python_sitearch}/matplotlib/tests/tinypages
%{python_sitearch}/mpl_toolkits/tests/baseline_images
%exclude %{python_sitearch}/matplotlib/tests/tinypages/.gitignore
%exclude %{python_sitearch}/matplotlib/tests/tinypages/_static/.gitignore

%files %{python_files tk}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/_backend_tk.py*
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/backend_tkcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/_backend_tk.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkcairo.*.py*

%files %{python_files web}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/backend_webagg.py*
%{python_sitearch}/matplotlib/backends/backend_webagg_core.py*
%{python_sitearch}/matplotlib/backends/web_backend/
%exclude %{python_sitearch}/matplotlib/backends/web_backend/.*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*.py*

%files %{python_files wx}
%license LICENSE/
%license doc/users/project/license.rst
%{python_sitearch}/matplotlib/backends/backend_wx.py*
%{python_sitearch}/matplotlib/backends/backend_wxagg.py*
%{python_sitearch}/matplotlib/backends/backend_wxcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wx.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxcairo.*.py*
%endif

%changelog
