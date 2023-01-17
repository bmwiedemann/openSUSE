#
# spec file for package python-pytest-isort
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


Name:           python-pytest-isort
Version:        3.1.0
Release:        0
Summary:        Pytest plugin to check import ordering using isort
License:        MIT
URL:            https://github.com/stephrdev/pytest-isort/
Source:         https://github.com/stephrdev/pytest-isort/archive/refs/tags/%{version}.tar.gz#/pytest-isort-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module isort >= 4.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  %{python_module pytest >= 6.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-isort >= 4.0
Requires:       python-pytest >= 5.0
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
BuildArch:      noarch
%python_subpackages

%description
This is a pytest plugin to check import ordering using isort.

%prep
%setup -q -n pytest-isort-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
rm %{buildroot}%{$python_sitelib}/LICENSE.rst
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_isort
%{python_sitelib}/pytest_isort-%{version}*-info

%changelog
