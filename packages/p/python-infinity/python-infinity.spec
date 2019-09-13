#
# spec file for package python-infinity
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-infinity
Version:        1.4
Release:        0
Summary:        All-in-one infinity value for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/kvesteri/infinity
Source:         https://files.pythonhosted.org/packages/source/i/infinity/infinity-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module flake8 >= 2.4.0}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pytest >= 2.2.3}
BuildRequires:  %{python_module six >= 1.4.1}
%endif
BuildArch:      noarch

%python_subpackages

%description
All-in-one infinity value for Python. Can be compared to any object.

%prep
%setup -q -n infinity-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec test_infinity.py
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
