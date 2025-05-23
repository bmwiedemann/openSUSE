#
# spec file for package python-pytest-tornado
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
Name:           python-pytest-tornado
Version:        0.8.1
Release:        0
Summary:        A py.test plugin for tornado applications
License:        Apache-2.0
URL:            https://github.com/eugeniy/pytest-tornado
Source:         https://github.com/eugeniy/pytest-tornado/archive/v%{version}.tar.gz#/pytest-tornado-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-pytest
Requires:       python-tornado >= 4.1
BuildArch:      noarch
%python_subpackages

%description
A py.test_ plugin providing fixtures and markers to simplify testing
of asynchronous tornado applications.

%prep
%setup -q -n pytest-tornado-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_tornado
%{python_sitelib}/pytest_tornado-%{version}.dist-info

%changelog
