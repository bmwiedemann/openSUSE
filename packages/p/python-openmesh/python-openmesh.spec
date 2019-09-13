#
# spec file for package python-openmesh
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-openmesh
Version:        1.1.3
Release:        0
License:        BSD-3-Clause
Summary:        A data structure for representing and manipulating polygon meshes
Url:            https://www.graphics.rwth-aachen.de:9000/OpenMesh/openmesh-python
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/o/openmesh/openmesh-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
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
