#
# spec file for package python-pymol
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


%bcond_with test
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define oldpython python
%define modname pymol-open-source
Name:           python-pymol
Version:        3.0.0
Release:        0
Summary:        A Molecular Viewer
License:        Python-2.0
Group:          Productivity/Scientific/Chemistry
URL:            https://pymol.org/
Source0:        https://github.com/schrodinger/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-build-date.patch dhall@wustl.edu -- patch eliminates build date
Patch0:         no-build-date.patch
# PATCH-FIX-OPENSUSE no-o3.patch tchvatal@suse.com -- do not add O3 to the code
Patch1:         no-o3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  msgpack-cxx-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  mmtf-cpp-devel
BuildRequires:  netcdf-devel
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  Catch2-2-devel
BuildRequires:  %{python_module Pillow}
## tests need recent biopython not available in Leap
%if 0%{?sle_version} >= 150500 && 0%{?is_opensuse}
%else
BuildRequires:  %{python_module biopython}
%endif
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-numpy
Requires:       python-qt5
Requires:       python-pmw
Requires(post): update-alternatives
Requires(postun):update-alternatives
Obsoletes:      pymol < %{version}
Provides:       pymol = %{version}
%python_subpackages

%description
PyMOL is a molecular graphics system targetted at medium to large
biomolecules like proteins. It can generate molecular graphics
images and animations.

Features include:

* Visualization of molecules, molecular trajectories and surfaces
  of crystallography data or orbitals
* Molecular builder and sculptor
* Internal raytracer and movie generator
* Fully extensible and scriptable via a python interface

The file formats PyMOL can read include PDB, XYZ, CIF, MDL Molfile,
ChemDraw, CCP4 maps, XPLOR maps and Gaussian cube maps.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%python_build %{?with_test:--testing}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pymol
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if %{with test}
## TestExporting.testglTF requires a special executable from Schrodinger
sed -e '/def testglTF(self):/,+7d' -i testing/tests/api/exporting.py
%if 0%{?sle_version} >= 150500 && 0%{?is_opensuse}
## TestSeqalign needs recent biopython not available in Leap
rm testing/tests/api/seqalign.py
## fails on Leap, but freemol is unused anyway
rm testing/tests/system/freemol_.py
## default pytest / python on leap are too old...
sed -e '/--import-mode=importlib/d' -i testing/pytest.ini
%endif
## pymol -ckqy testing/testing.py --run all
PYTHONPATH=%{buildroot}%{python_sitearch} python%{python_version} -m pymol -ckqy testing/testing.py --offline --run all
%endif

%post
%python_install_alternative pymol

%postun
%python_uninstall_alternative pymol

%files %{python_files}
%doc README ChangeLog
%license LICENSE
%python_alternative %{_bindir}/pymol
%{python_sitearch}*

%changelog
