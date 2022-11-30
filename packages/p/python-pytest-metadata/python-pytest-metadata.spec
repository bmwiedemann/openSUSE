#
# spec file for package python-pytest-metadata
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


Name:           python-pytest-metadata
Version:        2.0.4
Release:        0
Summary:        Pytest plugin for test session metadata
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-metadata
Source:         https://files.pythonhosted.org/packages/source/p/pytest-metadata/pytest_metadata-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.0.0}
# /SECTION
%python_subpackages

%description
Pytest plugin for test session metadata.

%prep
%setup -q -n pytest_metadata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_metadata
%{python_sitelib}/pytest_metadata-%{version}*-info

%changelog
