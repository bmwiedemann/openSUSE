#
# spec file for package python-infinity
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


%bcond_without  test
Name:           python-infinity
Version:        1.5
Release:        0
Summary:        All-in-one infinity value for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/kvesteri/infinity
Source:         https://files.pythonhosted.org/packages/source/i/infinity/infinity-%{version}.tar.gz
# https://github.com/kvesteri/infinity/issues/7
Patch0:         python-infinity-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module flake8 >= 2.4.0}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pytest >= 2.2.3}
%endif
BuildArch:      noarch

%python_subpackages

%description
All-in-one infinity value for Python. Can be compared to any object.

%prep
%autosetup -p1 -n infinity-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/__pycache__/infinity*.pyc
%{python_sitelib}/infinity.py
%{python_sitelib}/infinity-%{version}*-info

%changelog
