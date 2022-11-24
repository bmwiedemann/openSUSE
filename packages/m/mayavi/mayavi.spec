#
# spec file for package mayavi
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


# vtk only for python3 flavor
%define         pythons python3
Name:           mayavi
Version:        4.8.1
Release:        0
Summary:        3D visualization of scientific data in Python
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://github.com/enthought/mayavi
Source0:        https://files.pythonhosted.org/packages/source/m/mayavi/mayavi-%{version}.tar.gz
Source1:        mayavi.desktop
Source2:        tvtk_doc.desktop
Source99:       mayavi-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Pygments
BuildRequires:  python3-apptools
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-envisage
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-pyface >= 6.1.1
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-traits >= 6.0.0
BuildRequires:  python3-traitsui >= 7.0.0
BuildRequires:  python3-vtk
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
BuildRequires:  vtk-devel
# see mayavi/__init__.py
Requires:       python3-Pygments
Requires:       python3-apptools
Requires:       python3-envisage
Requires:       python3-packaging
Requires:       python3-pyface >= 6.1.1
Requires:       python3-traits >= 6.0.0
Requires:       python3-traitsui >= 7.0.0
Requires:       python3-vtk
Recommends:     python3-qt5
Provides:       python3-tvtk = %{version}
Obsoletes:      python3-tvtk < 4.8.1
Provides:       python3-mayavi = %{version}
Recommends:     %{name}-jupyter

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

%package        jupyter
Summary:        Jupyter notebook backend for mayavi
Group:          Productivity/Scientific/Other
Requires:       %{name} = %{version}
Requires:       jupyter-ipyevents
Requires:       jupyter-ipywidgets
Requires:       jupyter-notebook
BuildArch:      noarch

%description    jupyter
Interface to allow plotting with mayavi in Jupyter
notebooks.

This package pulls in the dependencies needed to
run mayavi in a Jupyter notebook.

%prep
%setup -q -n mayavi-%{version}

# wrong-file-end-of-line-encoding
sed -i 's|\r||' examples/mayavi/data/room_vis.wrl

# spurious-executable-perm
chmod -x mayavi/tests/data/cellsnd.ascii.inp

# non-executable-script
sed -i -e '/^#!\//, 1d' integrationtests/mayavi/*.py
sed -i -e '/^#!\//, 1d' mayavi/tests/*.py
sed -i -e '/^#!\//, 1d' mayavi/scripts/*.py
sed -i -e '/^#!\//, 1d' tvtk/setup.py

# env-script-interpreter
find . -name \*py -exec \
    sed -i -e '1s@#!\s*%{_bindir}/env\s*python@#!%{__python3}@' '{}' \;

%build
export CFLAGS="%{optflags}"
%python3_pyproject_wheel

%install
%python3_pyproject_install

mkdir -p %{buildroot}/%{_mandir}/man1/
mv docs/mayavi2.man %{buildroot}/%{_mandir}/man1/mayavi2.1
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 ./docs/source/mayavi/images/mayavi2-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/mayavi2.png
install -p -m 644 ./docs/source/mayavi/images/mayavi2-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tvtk_doc.png

%suse_update_desktop_file -i mayavi
%suse_update_desktop_file -i tvtk_doc

%fdupes %{buildroot}%{python3_sitearch}
%fdupes %{buildroot}%{_datadir}/icons

%ifnarch %ix86 %arm32
%check
# see .gitub/workflows/headless-tests.yml
export ETS_TOOLKIT=null
%pytest_arch -v --pyargs tvtk
# no vtkAMRVolumeMapper (?)
donttest="(TestMlabModules and test_volume)"
donttest="$donttest or test_volume_works_with_probe"
%pytest_arch -v --pyargs mayavi  -k "not ($donttest)"
%endif

%files
%doc README*.*
%license LICENSE*.txt image_LICENSE*.txt
%{_bindir}/mayavi2
%{_bindir}/tvtk_doc
%{_mandir}/man1/mayavi2.1%{?ext_man}
%{_datadir}/applications/mayavi.desktop
%{_datadir}/applications/tvtk_doc.desktop
%{_datadir}/icons/hicolor/
%{python3_sitearch}/mayavi/
%{python3_sitearch}/mayavi-%{version}*-info
%{python3_sitearch}/tvtk/

%files jupyter
%license LICENSE*.txt image_LICENSE*.txt

%changelog
