#
# spec file for package python-vcrpy
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-vcrpy
Version:        4.0.2
Release:        0
Summary:        Python module to mock and replay HTTP interactions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kevin1024/vcrpy
Source:         https://files.pythonhosted.org/packages/source/v/vcrpy/vcrpy-%{version}.tar.gz
# Enable Python 2 again. Drop as soon as Python 2 will be dropped from Factory.
Patch0:         0001-Revert-v4.0.x-Remove-legacy-python-and-add-python3.8.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5}
BuildRequires:  %{python_module wrapt}
BuildRequires:  fdupes
BuildRequires:  python-contextlib2
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
BuildRequires:  python3-yarl
Requires:       python-PyYAML
Requires:       python-six >= 1.5
Requires:       python-wrapt
BuildArch:      noarch
%ifpython2
Requires:       python-contextlib2
Requires:       python-mock
%endif
%ifpython3
Requires:       python-yarl
%endif
%python_subpackages

%description
This module records a test suite's HTTP interactions and replays them during future
test runs for deterministic tests.

This is a Python version of Ruby's VCR library.

%prep
%setup -q -n vcrpy-%{version}
%patch0 -p1
# online integration tests
rm -r tests/integration

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/vcr

%check
# Skip TestVCRConnection.testing_connect. Attempts
# a real connection.
export LANG=en_US.UTF-8
%pytest -k "not testing_connect"

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
