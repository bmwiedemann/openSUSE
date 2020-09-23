#
# spec file for package mayavi
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


%define         X_display  ":98"
Name:           mayavi
Version:        4.7.2
Release:        0
Summary:        3D visualization of scientific data in Python
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://github.com/enthought/mayavi
Source0:        https://files.pythonhosted.org/packages/source/m/mayavi/mayavi-%{version}.tar.gz
Source1:        mayavi.desktop
Source2:        tvtk_doc.desktop
BuildRequires:  R-base-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRequires:  python3-Pygments
BuildRequires:  python3-Sphinx
BuildRequires:  python3-apptools
BuildRequires:  python3-configobj
BuildRequires:  python3-devel
BuildRequires:  python3-envisage >= 3.0
BuildRequires:  python3-nose
BuildRequires:  python3-numpy-devel >= 1.0.1
BuildRequires:  python3-pyface >= 6.0.0
BuildRequires:  python3-qt5
BuildRequires:  python3-setuptools
BuildRequires:  python3-traits >= 4.6.0
BuildRequires:  python3-traitsui >= 6.0.0
BuildRequires:  python3-vtk >= 5.0
BuildRequires:  update-desktop-files
BuildRequires:  vtk-devel
Requires:       python3-apptools
Requires:       python3-qt5
Requires:       python3-setuptools
Requires:       python3-tvtk = %{version}
Provides:       python3-mayavi = %{version}
Recommends:     %{name}-jupyter
# SECTION test requirements
BuildRequires:  xorg-x11-server
# /SECTION

%description
Mayavi provides interactive visualization of 3-D data. It offers:

 * An (optional) user interface with dialogs to interact with
   all data and objects in the visualization.
 * A scripting interface in Python, including
   one-liners, or an object-oriented programming interface. Mayavi
   integrates with numpy and scipy for 3D plotting and can
   be used in IPython interactively, similarly to Matplotlib.
 * Use of the the VTK toolkit.

Additionally, Mayavi is a reusable tool that can be embedded in
applications in different ways or be combined with the Envisage
application-building framework to assemble domain-specific tools.

It is part of the Enthought Tool Suite (ETS).

%package     -n python3-tvtk
Summary:        A python3-traits enabled version of python3-vtk
Group:          Productivity/Scientific/Other
Requires:       python3-numpy >= 1.0.1
Requires:       python3-pyface >= 6.0.0
Requires:       python3-traits >= 4.6.0
Requires:       python3-traitsui >= 6.0.0
Requires:       python3-vtk >= 5.0
Recommends:     python3-configobj
Recommends:     python3-envisage >= 3.0
Recommends:     python3-wxWidgets >= 2.8

%description -n python3-tvtk
TVTK wraps VTK objects to provide a convenient, Pythonic API, while
supporting Traits attributes and NumPy/SciPy arrays. TVTK is
implemented mostly in pure Python, except for a small extension module.

Developers typically use TVTK to write Mayavi modules, and then use
Mayavi to interact with visualizations or create applications.

It is part of the Enthought Tool Suite (ETS).

%package        doc
Summary:        Documentation for mayavi
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description    doc
Documentation files for the %{name} package.

%package     -n python3-tvtk-doc
Summary:        Documentation for python3-tvtk
Group:          Documentation/HTML
Requires:       python3-tvtk = %{version}

%description -n python3-tvtk-doc
Documentation files for the python3-tvtk package.

%package        jupyter
Summary:        Jupyter notebook backend for mayavi
Group:          Productivity/Scientific/Other
Requires:       %{name} = %{version}
Requires:       jupyter-ipyevents
Requires:       jupyter-ipywidgets
Requires:       jupyter-notebook

%description    jupyter
Interface to allow plotting with mayavi in Jupyter
notebooks.

This package pulls in the dependencies needed to
run mayavi in a Jupyter notebook.

%prep
%setup -q -n mayavi-%{version}
rm -r mayavi.egg-info

# wrong-file-end-of-line-encoding
sed -i 's|\r||' examples/mayavi/data/room_vis.wrl

# spurious-executable-perm
chmod -x mayavi/tests/data/cellsnd.ascii.inp

# non-executable-script
sed -i -e '/^#!\//, 1d' integrationtests/mayavi/*.py
sed -i -e '/^#!\//, 1d' mayavi/tests/*.py
sed -i -e '/^#!\//, 1d' mayavi/tests/csv_files/csv_2_py
sed -i -e '/^#!\//, 1d' mayavi/scripts/*.py
sed -i -e '/^#!\//, 1d' tvtk/setup.py

# env-script-interpreter
find . -name \*.py -exec \
    sed -i -e '1s@#!\s*%{_bindir}/env\s*python@#!%{_bindir}/python@' '{}' \;

%build
export LANG=en_US.UTF-8
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

export CFLAGS="%{optflags}"
%python3_build

%install
export LANG=en_US.UTF-8
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%python3_install

# examples and integrationtests are not installed by the build system
# Manually install examples and integrationtests in python3_sitearch
mkdir -p %{buildroot}%{python3_sitearch}/mayavi/examples
cp -R examples/mayavi/* %{buildroot}%{python3_sitearch}/mayavi/examples/
mkdir -p %{buildroot}%{python3_sitearch}/mayavi/integrationtests
cp -R integrationtests/mayavi/* %{buildroot}%{python3_sitearch}/mayavi/integrationtests/
mkdir -p %{buildroot}%{python3_sitearch}/tvtk/examples
cp -R examples/tvtk/* %{buildroot}%{python3_sitearch}/tvtk/examples/

# Remove shebang from .py files in examples and integrationtests
# as they are not supposed to be executed
find %{buildroot}%{python3_sitearch}/{mayavi,tvtk}/examples -name \*.py \
    -exec sed -i -e '/^#!\//, 1d' '{}' \;
%if 0%{?suse_version} > 1320
find %{buildroot}%{python3_sitearch}/mayavi/html/_downloads -name \*.py \
    -exec sed -i -e '/^#!\//, 1d' '{}' \;
%endif

mkdir -p %{buildroot}/%{_mandir}/man1/
mv docs/mayavi2.man %{buildroot}/%{_mandir}/man1/mayavi2.1
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 ./docs/source/mayavi/images/mayavi2-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/mayavi2.png
install -p -m 644 ./docs/source/mayavi/images/mayavi2-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tvtk_doc.png

chmod a+x %{buildroot}%{python3_sitearch}/mayavi/scripts/mayavi2.py
chmod a+x %{buildroot}%{python3_sitearch}/mayavi/tests/runtests.py
chmod a+x %{buildroot}%{python3_sitearch}/tvtk/setup.py

# REMOVE BYTECODES NOT ACCOMPANIED BY SOURCE CODE
rm -fr %{buildroot}%{python3_sitearch}/tvtk/plugins/scene/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/plugins/browser/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/plugins/scene/ui/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/tools/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/pipeline/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/plugins/__init__.py{c,o}
rm -fr %{buildroot}%{python3_sitearch}/tvtk/version.py{c,o}

# script-without-shebang
chmod a-x %{buildroot}%{python3_sitearch}/mayavi/scripts/mayavi2.py
chmod a-x %{buildroot}%{python3_sitearch}/mayavi/tests/csv_files/csv_2_py
chmod a-x %{buildroot}%{python3_sitearch}/mayavi/tests/runtests.py
chmod a-x %{buildroot}%{python3_sitearch}/tvtk/setup.py

# REMOVE UNNEEDED HIDDEN FILE

%suse_update_desktop_file -i mayavi
%suse_update_desktop_file -i tvtk_doc

mkdir -p %{buildroot}%{_docdir}/mayavi/
mkdir -p %{buildroot}%{_docdir}/python3-tvtk/
cp -r docs/build/mayavi/html %{buildroot}%{_docdir}/mayavi/
cp -r docs/build/tvtk/html %{buildroot}%{_docdir}/python3-tvtk/

%fdupes %{buildroot}%{_docdir}/mayavi/
%fdupes %{buildroot}%{_docdir}/python3-tvtk/
%fdupes %{buildroot}%{python3_sitearch}/mayavi/
%fdupes %{buildroot}%{python3_sitearch}/mayavi-%{version}-py*.egg-info
%fdupes %{buildroot}%{python3_sitearch}/tvtk/
%fdupes %{buildroot}%{_datadir}/icons/

sed -i "s|\r||g" %{buildroot}%{_docdir}/python3-tvtk/html/objects.inv
rm -r %{buildroot}%{python3_sitearch}/{tvtk,mayavi}/html/.buildinfo
rm -r %{buildroot}%{_docdir}/{python3-tvtk,mayavi}/html/.buildinfo

python3    -m compileall -d %{python3_sitearch} %{buildroot}%{python3_sitearch}/mayavi/
python3 -O -m compileall -d %{python3_sitearch} %{buildroot}%{python3_sitearch}/mayavi/
python3    -m compileall -d %{python3_sitearch} %{buildroot}%{python3_sitearch}/tvtk/
python3 -O -m compileall -d %{python3_sitearch} %{buildroot}%{python3_sitearch}/tvtk/
%fdupes %{buildroot}%{python3_sitearch}/mayavi/
%fdupes %{buildroot}%{python3_sitearch}/tvtk/

%files
%doc README*.*
%license LICENSE*.txt image_LICENSE*.txt
%{_bindir}/mayavi2
%{_mandir}/man1/mayavi2.1%{?ext_man}
%{_datadir}/applications/mayavi.desktop
%{python3_sitearch}/mayavi/
%{python3_sitearch}/mayavi-%{version}-py*.egg-info
%exclude %{_docdir}/mayavi/html/

%files -n python3-tvtk
%doc README*.*
%license LICENSE*.txt image_LICENSE*.txt
%{_bindir}/tvtk_doc
%{_datadir}/applications/tvtk_doc.desktop
%{_datadir}/icons/hicolor/
%{python3_sitearch}/tvtk/
%exclude %{_docdir}/python3-tvtk/html/

%files doc
%license LICENSE*.txt image_LICENSE*.txt
%{_docdir}/mayavi/html/

%files -n python3-tvtk-doc
%license LICENSE*.txt image_LICENSE*.txt
%{_docdir}/python3-tvtk/html/

%files jupyter
%license LICENSE*.txt image_LICENSE*.txt

%changelog
