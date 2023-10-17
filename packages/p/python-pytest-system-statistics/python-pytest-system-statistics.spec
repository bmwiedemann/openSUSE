#
# spec file for package python-pytest-system-statistics
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


Name:           python-pytest-system-statistics
Version:        1.0.2
Release:        0
Summary:        Pytest plugin to track and report system usage statistics
License:        Apache-2.0
URL:            https://github.com/saltstack/pytest-system-statistics
Source:         https://files.pythonhosted.org/packages/source/p/pytest-system-statistics/pytest-system-statistics-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools >= 50.3.2}
BuildRequires:  %{python_module setuptools-declarative-requirements}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module psutil >= 5.0.0}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-skip-markers}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 19.2.0
Requires:       python-psutil >= 5.0.0
Requires:       python-pytest >= 6.0.0
Requires:       python-pytest-skip-markers
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Pytest plugin to track and report system usage statistics

%prep
%setup -q -n pytest-system-statistics-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytestsysstats
%{python_sitelib}/pytest_system_statistics-%{version}*-info

%changelog
