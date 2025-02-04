#
# spec file for package python-pytest-profiling
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


Name:           python-pytest-profiling
Version:        1.8.1
Release:        0
Summary:        Profiling plugin for pytest
License:        MIT
URL:            https://github.com/man-group/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-profiling/pytest-profiling-%{version}.tar.gz
# https://github.com/man-group/pytest-plugins/issues/209
Patch0:         python-pytest-profiling-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gprof2dot
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gprof2dot}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Profiling plugin for pytest

%prep
%autosetup -p1 -n pytest-profiling-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# integration tests omit as they try to use the system image instead of buildroot
%pytest -k 'not test_profile_integration'

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_profiling.py
%pycache_only %{python_sitelib}/__pycache__/pytest_profiling*.pyc
%{python_sitelib}/pytest_profiling-%{version}.dist-info

%changelog
