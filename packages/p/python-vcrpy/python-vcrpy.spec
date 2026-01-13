#
# spec file for package python-vcrpy
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-vcrpy
Version:        8.1.1
Release:        0
Summary:        Python module to mock and replay HTTP interactions
License:        MIT
URL:            https://github.com/kevin1024/vcrpy
Source:         https://files.pythonhosted.org/packages/source/v/vcrpy/vcrpy-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wrapt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-wrapt
BuildArch:      noarch
%python_subpackages

%description
This module records a test suite's HTTP interactions and replays them during future
test runs for deterministic tests.

This is a Python version of Ruby's VCR library.

%prep
%autosetup -p1 -n vcrpy-%{version}
# online integration tests
rm -r tests/integration

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/vcr

%check
# Skip online tests
export LANG=en_US.UTF-8
%pytest -k "not (testing_connect or test_get_vcr_with_matcher or test_testcase_playback)"

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/vcr
%{python_sitelib}/vcrpy-%{version}.dist-info

%changelog
