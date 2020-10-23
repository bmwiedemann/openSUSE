#
# spec file for package python-matplotlib
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
%define         skip_python2 1
# Not doing tests because they take too long
# The tests also pull in dependencies of all backends done in pure python
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
Version:        3.3.0
Release:        0
Summary:        Plotting Library for Python
License:        SUSE-Matplotlib
URL:            https://matplotlib.org
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-%{version}.tar.gz
Source1:        matplotlib-setup.cfg
# Remove after next update
Source2:        https://github.com/matplotlib/matplotlib/raw/b9470957c7f440084915a0b6573af3ee2235b941/lib/matplotlib/tests/baseline_images/test_axes/transparent_markers.pdf
# Bundled version of freetype for testing purposes only
Source99:       https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz
Patch0:         no-builddir-freetype.patch
BuildRequires:  %{python_module Cycler >= 0.10}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module kiwisolver >= 1.0.1}
BuildRequires:  %{python_module numpy >= 1.7.1}
BuildRequires:  %{python_module numpy-devel >= 1.7.1}
BuildRequires:  %{python_module pyparsing > 2.2.1}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  qhull-devel >= 2003.1
Requires:       python-Cycler >= 0.10
Requires:       python-Pillow >= 6.2
Requires:       python-kiwisolver >= 1.0.1
Requires:       python-numpy >= 1.7.1
Requires:       python-pyparsing > 2.2.1
Requires:       python-python-dateutil >= 2.7
Requires:       python-pytz
Recommends:     ghostscript
Recommends:     libxml2-tools
Recommends:     poppler-tools
Provides:       python-matplotlib-gtk = %{version}
Obsoletes:      python-matplotlib-gtk < %{version}
# SECTION WebAgg dependencies
BuildRequires:  %{python_module tornado}
# /SECTION
# SECTION tk dependencies via tcl
BuildRequires:  tcl
BuildRequires:  pkgconfig(freetype2) >= 2.3
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(tcl)
# /SECTION
%if %{with test}
BuildRequires:  %{python_module Pillow >= 6.2}
BuildRequires:  %{python_module matplotlib-cairo = %{version}}
BuildRequires:  %{python_module matplotlib-gtk3 = %{version}}
BuildRequires:  %{python_module matplotlib-qt5 = %{version}}
BuildRequires:  %{python_module matplotlib-testdata = %{version}}
BuildRequires:  %{python_module matplotlib-tk = %{version}}
BuildRequires:  %{python_module matplotlib-web = %{version}}
BuildRequires:  %{python_module matplotlib-wx = %{version}}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7}
# SECTION cairo dependencies
BuildRequires:  %{python_module cairo}
# /SECTION
# SECTION GTK3 dependencies
BuildRequires:  %{python_module gobject-Gdk}
# /SECTION
# SECTION Qt5 dependencies
BuildRequires:  %{python_module qt5}
BuildRequires:  pkgconfig(gtk+-3.0)
# /SECTION
# SECTION tk dependencies
BuildRequires:  %{python_module tk}
# /SECTION
# SECTION Wx dependencies
BuildRequires:  %{python_module wxPython >= 4}
# /SECTION
# SECTION latex dependencies
BuildRequires:  ghostscript
BuildRequires:  inkscape
BuildRequires:  poppler-tools
BuildRequires:  texlive-dvipng
BuildRequires:  texlive-latex
BuildRequires:  texlive-sfmath
BuildRequires:  texlive-tex
BuildRequires:  tex(8a.enc)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(phvr7t.tfm)
BuildRequires:  tex(pncr7t.tfm)
BuildRequires:  tex(psfrag.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(ucs.sty)
# /SECTION
%endif
Recommends:     (python-matplotlib-tk if tk)
%python_subpackages

%description
matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell (ala matlab or mathematica), web
application servers, and six graphical user interface toolkits.

%package        cairo
Summary:        Cairo backend for %{name}
License:        SUSE-Matplotlib
Requires:       %{name} = %{version}
Requires:       python-cairo

%description    cairo
This package includes the non-interactive Cairo-based backend
for the %{name} plotting package

%package        gtk3
Summary:        GTK3 backends for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       %{name}-cairo = %{version}
Requires:       python-gobject-Gdk

%description    gtk3
This package includes the GTK3-based gtk3, gtk3agg, and
gtk3cairo backends for the %{name} plotting package

%package        latex
Summary:        Allow rendering latex in %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       texlive-dvipng
Requires:       texlive-latex
Requires:       texlive-sfmath
Requires:       texlive-tex

%description    latex
This package allows %{name} to display latex in plots
and figures.

%package        qt5
Summary:        Qt5 backend for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       python-qt5
Provides:       %{name}-qt-shared = %{version}
Obsoletes:      %{name}-qt-shared < %{version}

%description    qt5
This package includes the Qt5-based pyqt5 backend
for the %{name} plotting package

%package        testdata
Summary:        Test data for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}

%description    testdata
This package includes the test baseline data
for the %{name} plotting package

%package        tk
Summary:        Tk backend for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       python-tk
Requires:       tcl >= 8.3

%description    tk
This package includes the Tk-based tkagg backend
for the %{name} plotting package

%package        web
Summary:        Web backend for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       python-tornado

%description    web
This package includes the browser-based webagg backend
for the %{name} plotting package

%package        wx
Summary:        WxWidgets backend for %{name}
License:        BSD-2-Clause
Requires:       %{name} = %{version}
Requires:       python-wxPython >= 4

%description    wx
This package includes the wxWidgets-based wxagg backend
for %{name} plotting package

%prep
%setup -q -n matplotlib-%{version} -a99
chmod -x lib/matplotlib/mpl-data/images/*.svg
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/env python||" {} \;
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/python||" {} \;
cp %{SOURCE1} setup.cfg
%patch0 -p1

# Fix test with ghostscript 9.53
cp %{SOURCE2} lib/matplotlib/tests/baseline_images/test_axes/transparent_markers.pdf

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
%fdupes %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
sed -i -e "s/install matplotlib from source/install the ${python_flavor}-matplotlib-testdata package/" \
    %{buildroot}%{$python_sitearch}/matplotlib/tests/__init__.py
}
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
%pytest_arch --pyargs matplotlib.tests --pyargs mpl_toolkits.tests -n auto -k "not ( ${skip_tests:4} )"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%doc examples/
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/
%{python_sitearch}/matplotlib-%{version}-py*.egg-info
%{python_sitearch}/matplotlib-%{version}-py*-nspkg.pth
%{python_sitearch}/mpl_toolkits
%{python_sitearch}/pylab.py*
%pycache_only %{python_sitearch}/__pycache__/pylab.*
%exclude %{python_sitearch}/matplotlib/backends/backend_cairo.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3cairo.*
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
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_cairo.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3cairo.*.py*
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
%license doc/users/license.rst

%files %{python_files cairo}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_cairo.*.py*

%files %{python_files gtk3}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_gtk3.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3agg.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3cairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3cairo.*.py*

%files %{python_files qt5}
%license LICENSE/
%license doc/users/license.rst
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
%license doc/users/license.rst
%{python_sitearch}/matplotlib/tests/baseline_images
%{python_sitearch}/matplotlib/tests/tinypages
%{python_sitearch}/mpl_toolkits/tests/baseline_images
%exclude %{python_sitearch}/matplotlib/tests/tinypages/.gitignore
%exclude %{python_sitearch}/matplotlib/tests/tinypages/_static/.gitignore

%files %{python_files tk}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/backend_tkcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkcairo.*.py*

%files %{python_files web}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_webagg.py*
%{python_sitearch}/matplotlib/backends/backend_webagg_core.py*
%{python_sitearch}/matplotlib/backends/web_backend/
%exclude %{python_sitearch}/matplotlib/backends/web_backend/.*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*.py*

%files %{python_files wx}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_wx.py*
%{python_sitearch}/matplotlib/backends/backend_wxagg.py*
%{python_sitearch}/matplotlib/backends/backend_wxcairo.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wx.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_wxcairo.*.py*
%endif

%changelog
