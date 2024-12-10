#
# spec file for package python-pytest-datafiles
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


Name:           python-pytest-datafiles
Version:        3.0.0
Release:        0
Summary:        Plugin for pytest to create data files
License:        MIT
URL:            https://github.com/omarkohl/pytest-datafiles
Source:         https://github.com/omarkohl/pytest-datafiles/archive/refs/tags/%{version}.tar.gz#/pytest-datafiles-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.6
BuildArch:      noarch
%python_subpackages

%description
pytest plugin to create a 'tmp_path' containing predefined files/directories.

%prep
%autosetup -p1 -n pytest-datafiles-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/pytest_datafiles.py
%pycache_only %{python_sitelib}/__pycache__/pytest_datafiles*.pyc
%{python_sitelib}/pytest_datafiles-%{version}.dist-info

%changelog
