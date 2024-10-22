#
# spec file for package python-pytest-pyramid-server
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-pytest-pyramid-server
Version:        1.8.0
Release:        0
Summary:        Pyramid server fixture for py.test
License:        MIT
URL:            https://github.com/man-group/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-pyramid-server/pytest-pyramid-server-%{version}.tar.gz
# https://github.com/man-group/pytest-plugins/issues/209
Patch0:         python-pytest-pyramid-server-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyramid
Requires:       python-pytest
Requires:       python-pytest-server-fixtures
Requires:       python-waitress
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyramid-debugtoolbar}
BuildRequires:  %{python_module pyramid}
BuildRequires:  %{python_module pytest-server-fixtures}
BuildRequires:  %{python_module waitress}
# /SECTION
%python_subpackages

%description
Pyramid server fixture for py.test.

%prep
%autosetup -p1 -n pytest-pyramid-server-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_pyramid_server.py
%{python_sitelib}/pyramid_server_test.py
%pycache_only %{python_sitelib}/__pycache__/pytest_pyramid_server*.pyc
%pycache_only %{python_sitelib}/__pycache__/pyramid_server_test*.pyc
%{python_sitelib}/pytest_pyramid_server-%{version}.dist-info

%changelog
