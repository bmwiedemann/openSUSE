#
# spec file for package python-vcrpy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.0.1
Release:        0
Summary:        Python module to mock and replay HTTP interactions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kevin1024/vcrpy
Source:         https://files.pythonhosted.org/packages/source/v/vcrpy/vcrpy-%{version}.tar.gz
Patch0:         python-vcrpy-fix-tunnel-uri-generation.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5}
BuildRequires:  %{python_module wrapt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-contextlib2
BuildRequires:  python2-mock
BuildRequires:  python3-yarl
Requires:       python-PyYAML
Requires:       python-six >= 1.5
Requires:       python-wrapt
BuildArch:      noarch
%ifpython2
Requires:       python2-contextlib2
Requires:       python2-mock
%endif
%ifpython3
Requires:       python3-yarl
%endif
%python_subpackages

%description
This module records a test suite's HTTP interactions and replays them during future
test runs for deterministic tests.

This is a Python version of Ruby's VCR library.

%prep
%setup -q -n vcrpy-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/vcr

%check
# Skip TestVCRConnection.testing_connect. Attempts
# a real connection.
# This just doesn't work gh#kevin1024/vcrpy#427
# %%python_exec -m pytest -k "not testing_connect" tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
