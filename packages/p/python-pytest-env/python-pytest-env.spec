#
# spec file for package python-pytest-env
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


%{?sle15_python_module_pythons}
Name:           python-pytest-env
Version:        1.1.3
Release:        0
Summary:        Pytest plugin to add environment variables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-env
Source:         https://files.pythonhosted.org/packages/source/p/pytest-env/pytest_env-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.6.0
BuildArch:      noarch
%python_subpackages

%description
A py.test plugin that allows you to add environment variables.

%prep
%setup -q -n pytest_env-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytest_env
%{python_sitelib}/pytest_env-%{version}.dist-info

%changelog
