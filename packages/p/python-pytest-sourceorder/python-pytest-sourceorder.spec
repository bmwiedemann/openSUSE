#
# spec file for package python-pytest-sourceorder
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-pytest-sourceorder
Version:        0.6.0
Release:        0
Summary:        Test-ordering plugin for pytest
License:        GPL-3.0-or-later
URL:            https://pagure.io/python-pytest-sourceorder
Source:         pytest-sourceorder-%{version}.tar.gz
# PATCH-FIX-OPENSUSE https://pagure.io/python-pytest-sourceorder/issue/3
Patch0:         remove-yield-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Test-ordering plugin for pytest

When installed, test classes marked @pytest_sourceorder.ordered
will have tests run in the order of their definition.

Methods are ordered by line nuber of their definition, so
spreading them between multiple files or otherwise defining them
outside of their class might cause the plugin to order them
wrong.

When inheriting from an ordered test class, the superclass’
methods will be run first (even if overridden), followed by the
ones from subclasses. You generally do not want to apply an
additional @ordered decorator to the subclasses – doing so will
reset the inheritance-based ordering.

%prep
%autosetup -p1 -n pytest-sourceorder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING
%{python_sitelib}/pytest_sourceorder.py
%{python_sitelib}/pytest_sourceorder-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/pytest_sourceorder.*.pyc

%changelog
