#
# spec file for package python-pymol
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
%define oldpython python
%define modname pymol-open-source
%define test_version 0.0+git.1613482680.a99b9c6
Name:           python-pymol
Version:        2.4.0
Release:        0
Summary:        A Molecular Viewer
License:        Python-2.0
Group:          Productivity/Scientific/Chemistry
URL:            https://pymol.org/2/
Source0:        https://github.com/schrodinger/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
Source1:        pymol-testing-%{test_version}.tar.xz
# PATCH-FIX-OPENSUSE no-build-date.patch dhall@wustl.edu -- patch eliminates build date
Patch0:         no-build-date.patch
# PATCH-FIX-OPENSUSE no-o3.patch tchvatal@suse.com -- do not add O3 to the code
Patch1:         no-o3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  Catch2-devel
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libmsgpack-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  mmtf-cpp-devel
BuildRequires:  netcdf-devel
BuildRequires:  python-rpm-macros
# It needed itself for testing.
%if %{with test}
BuildRequires:  %{python_module pymol}
%endif
Requires:       python-numpy
Requires:       python-qt5
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
sed -i "1d" modules/pmg_tk/startup/apbs_tools.py # Remove she-bang line
chmod -x test/cyg test/run test/show
%if %{with test}
# Unpack data for pymol-testing
tar -xvf %{SOURCE1} -C %{_builddir}/%{modname}-%{version}
# Use this to enable testing.
sed -i 's/testing = False/testing = True/g' setup.py
%endif

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
# Use --testing to enable testing.
%python_build %{?with_test:--testing}%{!?with_test:}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pymol
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative pymol

%postun
%python_uninstall_alternative pymol

%check
# Use this to enable testing.
# I think it use pymol itself to run test, I could not get pymol to run.
%if %{with test}
pymol -ckqy pymol-testing-%{test_version}/testing.py --run all
%endif

%files %{python_files}
%doc README ChangeLog
%license LICENSE
%python_alternative %{_bindir}/pymol
%{python_sitearch}*

%changelog
