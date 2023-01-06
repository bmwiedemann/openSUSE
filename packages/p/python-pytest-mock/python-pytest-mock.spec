#
# spec file for package python-pytest-mock
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


%define skip_python2 1
Name:           python-pytest-mock
Version:        3.10.0
Release:        0
Summary:        Thin-wrapper around the mock package for easier use with pytest
License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mock/pytest-mock-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 5}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools >= 36}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
This plugin installs a ``mocker`` fixture which is a thin-wrapper around the patching API
provided by the `mock` package, but with the benefit of not having to worry about undoing
patches at the end of a test

%prep
%autosetup -p1 -n pytest-mock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --assert=plain

%files %{python_files}
%doc CHANGELOG.rst
%license LICENSE
%{python_sitelib}/pytest_mock
%{python_sitelib}/pytest_mock-%{version}*-info

%changelog
