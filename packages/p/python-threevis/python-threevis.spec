#
# spec file for package python-threevis
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-threevis
Version:        0.1.0.post25
Release:        0
Summary:        Plugin for visualizing meshes, point clouds, and other geometry in a Jupyter Notebook
License:        BSD-3-Clause
URL:            https://graphics.rwth-aachen.de:9000/threevis/threevis
Source:         https://files.pythonhosted.org/packages/source/t/threevis/threevis-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module openmesh}
BuildRequires:  %{python_module pythreejs >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy
Requires:       python-openmesh
Requires:       python-pythreejs >= 1.0.0
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-threevis = %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
A plugin for visualizing meshes, point clouds, and other geometry in
a Jupyter Notebook.

%prep
%setup -q -n threevis-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B -m unittest
}
popd

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
