#
# spec file for package python-pytest-echo
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


Name:           python-pytest-echo
Version:        2.0.1
Release:        0
Summary:        Pytest plugin for echoing build environment attributes
License:        MIT
URL:            https://github.com/pytest-dev/pytest-echo
Source:         https://files.pythonhosted.org/packages/source/p/pytest-echo/pytest_echo-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 8.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3}
# /SECTION
%python_subpackages

%description
pytest plugin with mechanisms for echoing environment variables,
package version and generic attributes.

%prep
%setup -q -n pytest_echo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/pytest_echo
%{python_sitelib}/pytest_echo-%{version}.dist-info

%changelog
