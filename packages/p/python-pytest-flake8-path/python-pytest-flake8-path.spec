#
# spec file for package python-pytest-flake8-path
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


Name:           python-pytest-flake8-path
Version:        1.3.0
Release:        0
Summary:        A pytest fixture for testing flake8 plugins
License:        MIT
URL:            https://github.com/adamchainz/pytest-flake8-path
Source:         https://github.com/adamchainz/pytest-flake8-path/archive/%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
A pytest fixture for testing flake8 plugins.

%prep
%autosetup -p1 -n pytest-flake8-path-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_flake8_path
%{python_sitelib}/pytest_flake8_path-%{version}*-info

%changelog
