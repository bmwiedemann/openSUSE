#
# spec file for package python-openmesh
#
# Copyright (c) 2023 SUSE LLC
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


%global skip_python36 1
Name:           python-openmesh
Version:        1.2.1
Release:        0
Summary:        A data structure for representing and manipulating polygon meshes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.graphics.rwth-aachen.de:9000/OpenMesh/openmesh-python
Source:         https://files.pythonhosted.org/packages/source/o/openmesh/openmesh-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
# /SECTION
Requires:       python-numpy

%python_subpackages

%description
A halfedge-based data structure for representing and manipulating polygon meshes.

%prep
%setup -q -n openmesh-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd tests
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m unittest
}
popd

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/openmesh-%{version}-py*.egg-info
%{python_sitearch}/openmesh.*so

%changelog
