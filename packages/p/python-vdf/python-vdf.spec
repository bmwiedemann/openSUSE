#
# spec file for package python-vdf
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}

Name:           python-vdf
Version:        4.0
Release:        0
Summary:        Python Parser for VDF Files
License:        MIT
URL:            https://github.com/solsticegamestudios/vdf
Group:          Development/Languages/Python

# Get the source from tar_scm
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

# VDF BuildDeps
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}

# To remove duplicated files
BuildRequires:  fdupes

%python_subpackages

%description
Library for working with Valve's VDF text format

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
find %{buildroot} -type d -name "__pycache__" -exec rm -rf {} +

# Remove 0 length REQUESTED file
find %{buildroot}%{python_sitelib} -name "REQUESTED" -size 0 -delete

# Remove duplicated files
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand rm -f .coverage vdf/*.pyc tests/*.pyc
PYTHONHASHSEED=0 $python -m pytest tests
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/vdf
%{python_sitelib}/vdf-4.0.dist-info

%changelog
