#
# spec file for package python-enable
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
%define         oldpython python
%define         X_display         ":98"
Name:           python-enable
Version:        4.8.0
Release:        0
Summary:        Low-level drawing and interaction
License:        BSD-3-Clause AND EPL-1.0 AND GPL-1.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND SUSE-Public-Domain
Group:          Development/Languages/Python
Url:            https://github.com/enthought/enable/
Source:         https://files.pythonhosted.org/packages/source/e/enable/enable-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  Mesa-devel
BuildRequires:  bitstream-vera-fonts
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-server
BuildRequires:  font(adobehelvetica)
BuildRequires:  pkgconfig(glu)
%if %{with test}
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyPDF2}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module apptools >= 4.3.0}
BuildRequires:  %{python_module cairo}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module kiwisolver}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyface}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module reportlab >= 3.1}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module traitsui}
BuildRequires:  %{python_module traits}
BuildRequires:  python-wxWidgets
%endif
Requires:       python-kiva = %{version}

%python_subpackages

%description
The Enable package is a multi-platform object drawing library built on top of
Kiva. The core of Enable is a container/component model for drawing and event
notification. The core concepts of Enable are:

- Component
- Container
- Events (mouse, drag, and key events)

Enable provides a high-level interface for creating GUI objects, while
enabling a high level of control over user interaction. Enable is a supporting
technology for the Chaco and BlockCanvas projects.

Part of the Enthought Tool Suite (ETS).

%package kiva
Summary:        DisplayPDF vector drawing engine for Python
Group:          Development/Libraries/Python
Requires:       bitstream-vera-fonts
Requires:       python-Cython
Requires:       python-FontTools
Requires:       python-apptools >= 4.3.0
Requires:       python-numpy
Requires:       python-pyface
Requires:       python-reportlab
Requires:       python-setuptools
Requires:       python-six
Requires:       python-traits
Requires:       python-traitsui
Requires:       xorg-x11-fonts
Requires:       font(adobehelvetica)
Recommends:     python-Pillow
Recommends:     python-cairo
Recommends:     python-kiwisolver
Recommends:     python-pygarrayimage
Recommends:     python-pyglet >= 1.1.4
Recommends:     python-pyparsing
Recommends:     python-qt5
Recommends:     python-reportlab >= 3.1
Recommends:     python-tk
Provides:       python-kiva = %{version}
Obsoletes:      python-kiva < %{version}
%ifpython2
Provides:       %{oldpython}-kiva = %{version}
Obsoletes:      %{oldpython}-kiva < %{version}
%endif

%description kiva
Kiva is a multi-platform DisplayPDF vector drawing engine that supports
multiple output backends, including Windows, GTK, and Macintosh native
windowing systems, a variety of raster image formats, PDF, and Postscript.

DisplayPDF is more of a convention than an actual specification. It is a
path-based drawing API based on a subset of the Adobe PDF specification.
Besides basic vector drawing concepts such as paths, rects, line sytles, and
the graphics state stack, it also supports pattern fills, antialiasing, and
transparency. Perhaps the most popular implementation of DisplayPDF is
Apple's Quartz 2-D graphics API in Mac OS X.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n enable-%{version}
sed -i -e '/^#!\//, 1d' enable/savage/compliance/*.py
sed -i -e '/^#!\//, 1d' kiva/setup.py
sed -i -e '/^#!\//, 1d' kiva/*/setup.py
sed -i -e '/^#!\//, 1d' kiva/tests/agg/clean.py
chmod a-x kiva/agg/tests/gcmemtest.py
chmod a-x kiva/tests/agg/clean.py

%build
# regenerate cython sources
cython-%{python3_version} --cplus kiva/*.pyx
cython-%{python3_version} --cplus kiva/quartz/*.pyx

export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/enable/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/enable/
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/kiva/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/kiva/tests/
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/kiva/agg/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/kiva/agg/tests/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} -screen 0 1600x1200x24 >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

mkdir tester
pushd tester
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -m nose -v --no-byte-compile kiva.tests
$python -B -m nose -v --no-byte-compile enable.tests
}
popd
rm -r tester
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt image_LICENSE.txt image_LICENSE_CP.txt image_LICENSE_Eclipse.txt image_LICENSE_Nuvola.txt image_LICENSE_OOo.txt
%{python_sitearch}/enable/
%{python_sitearch}/enable-%{version}-py*.egg-info

%files %{python_files kiva}
%defattr(-,root,root)
%doc README.rst
%{python_sitearch}/kiva/

%changelog
