#
# spec file for package python-uuid6
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-uuid6
Version:        2025.0.1
Release:        0
Summary:        New time-based UUID formats which are suited for use as a database key
License:        MIT
URL:            https://github.com/oittaa/uuid6-python
Source:         https://files.pythonhosted.org/packages/source/u/uuid6/uuid6-2025.0.1.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
New time-based UUID formats which are suited for use as a database key

%prep
%autosetup -p1 -n uuid6-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/uuid6
%{python_sitelib}/uuid6-%{version}.dist-info

%changelog
