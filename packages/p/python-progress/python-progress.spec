#
# spec file for package python-progress
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
Name:           python-progress
Version:        1.6
Release:        0
Summary:        Progress bars for Python
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/verigak/progress/
Source:         https://files.pythonhosted.org/packages/source/p/progress/progress-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Progress bars for Python.

%prep
%setup -q -n progress-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_progress.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/progress
%{python_sitelib}/progress-%{version}*-info

%changelog
