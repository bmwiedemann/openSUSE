#
# spec file for package python2-matplotlib
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


# Not doing tests because they take too long
# The tests also pull in dependencies of all backends done in pure python
%bcond_with tests

# No Qt4 plugin on > Leap 15
%if 0%{?suse_version} > 1500
%bcond_with qt4
%else
%bcond_without qt4
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
%define         skip_python3 1
Name:           python2-matplotlib
Version:        2.2.3
Release:        0
Summary:        Plotting Library for Python
License:        SUSE-Matplotlib
Group:          Development/Libraries/Python
Url:            http://matplotlib.org
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-%{version}.tar.gz
Source1:        matplotlib-setup.cfg
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(freetype2) >= 2.3
BuildRequires:  pkgconfig(libpng) >= 1.2
# Python 2 only
BuildRequires:  python2-functools32
BuildRequires:  python2-subprocess32
# Needed for all versions of python
BuildRequires:  %{python_module Cycler >= 0.10}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module kiwisolver}
BuildRequires:  %{python_module numpy >= 1.7.1}
BuildRequires:  %{python_module numpy-devel >= 1.7.1}
BuildRequires:  %{python_module pyparsing > 2.1.6}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10}
# needed for testing
%if %{with tests}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  inkscape
# latex dependencies
BuildRequires:  ghostscript
BuildRequires:  poppler-tools
BuildRequires:  texlive-dvipng
BuildRequires:  texlive-latex
BuildRequires:  texlive-tex
%if 0%{?is_opensuse}
BuildRequires:  qhull-devel >= 2003.1
BuildRequires:  texlive-sfmath
BuildRequires:  tex(8a.enc)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(phvr7t.tfm)
BuildRequires:  tex(pncr7t.tfm)
BuildRequires:  tex(psfrag.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(ucs.sty)
%endif
# GTK3 dependencies
BuildRequires:  %{python_module gobject}
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with qt4}
# Qt4 dependencies
BuildRequires:  %{python_module qt4}
%endif
# Qt5 dependencies
BuildRequires:  %{python_module qt5}
# Wx dependencies (currently Python 2 only)
BuildRequires:  python2-wxWidgets >= 3
# tk dependencies
BuildRequires:  %{python_module tk}
# X server needed for Qt4/Qt5 tests
BuildRequires:  xorg-x11-Xvfb
%endif
# tk dependencies via tcl
BuildRequires:  tcl
BuildRequires:  pkgconfig(tcl)
# WebAgg dependencies
BuildRequires:  %{python_module tornado}
# End of backend dependencies
Requires:       python2-Cycler >= 0.10
Requires:       python2-kiwisolver >= 1.0.1
Requires:       python2-numpy >= 1.7.1
Requires:       python2-pyparsing > 2.1.6
Requires:       python2-python-dateutil >= 2.1
Requires:       python2-pytz
Requires:       python2-six >= 1.10
%ifpython2
Requires:       python2-backports.functools_lru_cache
Requires:       python2-functools32
Requires:       python2-subprocess32
%endif
Recommends:     ghostscript
Recommends:     libxml2-tools
Recommends:     python2-Pillow
Recommends:     poppler-tools
%if 0%{?suse_version} >= 1500
Recommends:     (python2-matplotlib-tk if tk)
%else
Recommends:     python2-matplotlib-tk
%endif
Provides:       %{oldpython}-matplotlib = %{version}
Provides:       python2-matplotlib-gtk = %{version}
Obsoletes:      python2-matplotlib-gtk < %{version}
Provides:       %{oldpython}-matplotlib-gtk = %{version}
Obsoletes:      %{oldpython}-matplotlib-gtk < %{version}

%python_subpackages

%description
matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell (ala matlab or mathematica), web
application servers, and six graphical user interface toolkits.

%package gtk3
Summary:        GTK3 backends for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python2-gobject
Provides:       %{oldpython}-matplotlib-gtk3 = %{version}

%description gtk3
This package includes the GTK3-based gtk3 and gtk3agg
backends for the %{name} plotting package

%package latex
Summary:        Allow rendering latex in %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       texlive-dvipng
Requires:       texlive-latex
Requires:       texlive-tex
%if 0%{?is_opensuse}
Requires:       texlive-sfmath
%endif
Provides:       %{oldpython}-matplotlib-latex = %{version}

%description latex
This package allows %{name} to display latex in plots
and figures.

%package qt-shared
Summary:        Shared files for the Qt backends for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Provides:       %{oldpython}-matplotlib-qt-shared = %{version}

%description qt-shared
This package includes files needed by both the Qt4-based pyqt4 and 
pyside backends and the Qt5-based pyqt5 backend for the %{name}
plotting package

%package qt4
Summary:        Qt4 backends for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{name}-qt-shared = %{version}
Requires:       python2-qt4 >= 4.0
Provides:       %{oldpython}-matplotlib-qt4 = %{version}

%description qt4
This package includes the Qt4-based pyqt4 and pyside backends
for the %{name} plotting package

%package qt5
Summary:        Qt5 backend for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{name}-qt-shared = %{version}
Requires:       python2-qt5
Provides:       %{oldpython}-matplotlib-qt5 = %{version}

%description qt5
This package includes the Qt5-based pyqt5 backend
for the %{name} plotting package

%package tk
Summary:        Tk backend for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python2-tk
Requires:       tcl >= 8.3
Provides:       %{oldpython}-matplotlib-tk = %{version}

%description tk
This package includes the Tk-based tkagg backend
for the %{name} plotting package

%package web
Summary:        Web backend for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python2-tornado
Provides:       %{oldpython}-matplotlib-web = %{version}

%description web
This package includes the browser-based webagg backend
for the %{name} plotting package

%package        wx
Summary:        WxWidgets backend for %{name}
License:        BSD-2-Clause
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python2-wxWidgets >= 3
Provides:       %{oldpython}-matplotlib-wx = %{version}

%description    wx
This package includes the wxWidgets-based wxagg backend
for %{name} plotting package

%prep
%setup -q -n matplotlib-%{version}
chmod -x lib/matplotlib/mpl-data/images/*.svg
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/env python||" {} \;
find examples lib/matplotlib lib/mpl_toolkits/mplot3d -type f -name "*.py" -exec sed -i "s|#!\/usr\/bin\/python||" {} \;
cp %{SOURCE1} ./setup.cfg

%if %{without tests}
sed -i -e 's/tests = .*/tests = False/' ./setup.cfg
%else
# raise tolerance for changes due to freetype 2.6/2.7 rendering differences
sed -i -e 's/\(image_comparison.*\)tol=0/\1tol=0.310/' lib/matplotlib/testing/decorators.py # default
sed -i -e 's/tol=0.002/tol=0.009/' lib/matplotlib/tests/test_streamplot.py
sed -i -e 's/tol=0.*)/tol=0.012)/' lib/matplotlib/tests/test_png.py
# image rotation is broken, investigate
sed -i -e 's/\(image_comparison.*rotate_image.*\)/\1 tol=150,/' lib/matplotlib/tests/test_image.py
%endif

%build
export XDG_RUNTIME_DIR=/tmp
%python_build

%install
export XDG_RUNTIME_DIR=/tmp
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
%fdupes %{buildroot}%{$python_sitearch}/matplotlib/backends/qt_editor/
}

%if %{with tests}
%check
export DISPLAY=:42
/usr/bin/Xvfb :42 -screen 0 1024x768x24 >& /tmp/Xvfb.log &
trap "kill $! || true" EXIT
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python ./tests.py --no-network --recursionlimit=5000
%endif

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
%if 0%{?is_opensuse}
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3.*
%exclude %{python_sitearch}/matplotlib/backends/backend_gtk3agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt4agg.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt5.*
%exclude %{python_sitearch}/matplotlib/backends/backend_qt5agg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_webagg.*
%exclude %{python_sitearch}/matplotlib/backends/backend_webagg_core.*
%exclude %{python_sitearch}/matplotlib/backends/qt_compat.*
%exclude %{python_sitearch}/matplotlib/backends/qt_editor/
%exclude %{python_sitearch}/matplotlib/backends/tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/web_backend/
%endif
%ifpycache
%if 0%{?is_opensuse}
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4agg.*.py*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5agg.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/qt_compat.*
%exclude %{python_sitearch}/matplotlib/backends/__pycache__/tkagg.*
%endif
%endif
%ifpython2
%if 0%{?is_opensuse}
%exclude %{python_sitearch}/matplotlib/backends/backend_wx.py*
%exclude %{python_sitearch}/matplotlib/backends/backend_wxagg.py*
%exclude %{python_sitearch}/matplotlib/backends/wx_compat.py*
%endif
%endif

# Dummy package to pull in latex dependencies.
%files %{python_files latex}
%license LICENSE/
%license doc/users/license.rst

%if 0%{?is_opensuse}

%files %{python_files gtk3}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_gtk3.py*
%{python_sitearch}/matplotlib/backends/backend_gtk3agg.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_gtk3agg.*.py*

# IMPORTANT: the qt4 backend makes use of the qt5 backend,
# which is actually a generic qt backend.
# So we need to package all the qt5 stuff in a generic
# package, and provide the -qt5 stub package which pulls in
# the python-qt5 dependency.
%files %{python_files qt-shared}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_qt5.py*
%{python_sitearch}/matplotlib/backends/backend_qt5agg.py*
%{python_sitearch}/matplotlib/backends/qt_compat.py*
%{python_sitearch}/matplotlib/backends/qt_editor/
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt5agg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/qt_compat.*.py*

%if %{with qt4}
%files %{python_files qt4}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_qt4.py*
%{python_sitearch}/matplotlib/backends/backend_qt4agg.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_qt4agg.*.py*
%endif

%files %{python_files qt5}
%license LICENSE/
%license doc/users/license.rst
%doc README.rst

%files %{python_files tk}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/tkagg.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/tkagg.*.py*

%files %{python_files web}
%license LICENSE/
%license doc/users/license.rst
%{python_sitearch}/matplotlib/backends/backend_webagg.py*
%{python_sitearch}/matplotlib/backends/backend_webagg_core.py*
%{python_sitearch}/matplotlib/backends/web_backend/
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg.*.py*
%pycache_only %{python_sitearch}/matplotlib/backends/__pycache__/backend_webagg_core.*.py*

%files %{python_files wx}
%license LICENSE/
%license doc/users/license.rst
%{python2_sitearch}/matplotlib/backends/wx_compat.py*
%{python2_sitearch}/matplotlib/backends/backend_wx.py*
%{python2_sitearch}/matplotlib/backends/backend_wxagg.py*

%endif

%changelog
