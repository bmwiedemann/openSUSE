#
# spec file for package python-pytest-expect
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


Name:           python-pytest-expect
Version:        1.1.0
Release:        0
Summary:        Py.test plugin to store test expectations and mark tests based on them
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gsnedders/pytest-expect
Source:         https://files.pythonhosted.org/packages/source/p/pytest-expect/pytest-expect-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/gsnedders/pytest-expect/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-six
Requires:       python-u-msgpack-python
BuildArch:      noarch
%python_subpackages

%description
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them
in future. The tests expectations are stored such that they can be
distributed alongside the tests. However, note that test expectations
can only be reliably shared between Python 2 and Python 3 if they only
use ASCII characters in their node ids: this likely isn’t a limitation
if tests are using the normal Python format, as Python 2 only allows
ASCII characters in identifiers.

%prep
%setup -q -n pytest-expect-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_expect
%{python_sitelib}/pytest_expect-%{version}*-info

%changelog
